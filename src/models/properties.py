from __future__ import annotations

from attr import attrs


class Property:

    def __init__(self, title: str, model: OpenApiModel) -> None:
        self._title = title
        self._model = model

    @property
    def title(self) -> str:
        return self._title

    @property
    def model(self) -> OpenApiModel:
        return self._model


from .openapi_model import OpenApiDTO, OpenApiModel
