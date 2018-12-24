from uuid import UUID

from pydantic import BaseModel


class Photo(BaseModel):
    uid: UUID
    title: str
