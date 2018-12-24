import copy
import json
from typing import Type, List, Union

from pydantic import BaseModel

from src.models.object_type import ObjectTypes
from src.models.openapi_model import OpenApiDTO, OpenApiModel
from src.models.properties import Property


class Crawler:

    @staticmethod
    def crawl(model: Type[BaseModel]) -> OpenApiModel:
        print(json.dumps(json.loads(model.schema_json()), indent=2))
        dto = OpenApiDTO(**json.loads(model.schema_json()))
        return Crawler._to_model(dto, model)

    @staticmethod
    def _to_model(dto: OpenApiDTO, model: Type[BaseModel]) -> OpenApiModel:
        properties: List[Union[str, Property]] = []
        for prop in dto.properties:
            if isinstance(prop, BaseModel) and prop.model.type == ObjectTypes.OBJECT:
                extended_prop = Property(prop.schema()['title'], Crawler._to_model(prop.model, model))
                properties.append(extended_prop)
            else:
                properties.append(prop)

        return OpenApiModel(dto, model.__module__, properties)
