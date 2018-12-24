from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from doc.examples.photo import Photo


class User(BaseModel):
    username: str
    uid: UUID
    name: Optional[str]
    photo: Optional[Photo]
