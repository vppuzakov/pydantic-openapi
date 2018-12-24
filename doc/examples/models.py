from datetime import datetime
from enum import Enum

from pydantic import BaseModel

from doc.examples.user import User

__all__ = ['Email', 'Customer']


class Email(BaseModel):
    is_primary: bool = True
    email: str


class CustomerCategory(str, Enum):
    vip = "vip"
    common = "common"


class Customer(BaseModel):
    user: User
    category: CustomerCategory
    created: datetime
