from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional, Union, Any, Dict


@dataclass
class OpenApiDTO:

    title: str
    type: str
    format: Optional[str] = None
    properties: Optional[List[Union[str, OpenApiDTO]]] = None
    required: Optional[List[str]] = None
    definitions: Optional[Dict[str, OpenApiDTO]] = None


class OpenApiModel:

    def __init__(self, dto: OpenApiDTO, path: str, properties: List[Property]) -> None:
        self._dto = dto
        self._path = path
        self._properties = properties

    @property
    def dto(self) -> OpenApiDTO:
        return self._dto

    @property
    def path(self) -> str:
        return self._path

    @property
    def properties(self) -> List[Property]:
        return self._properties


from .properties import Property
