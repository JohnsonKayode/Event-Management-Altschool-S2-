from pydantic import BaseModel
from typing import Annotated, Union, Optional
from uuid import UUID


class UserBase(BaseModel):
    name: str
    email: str
    is_active: bool = True 

class User(UserBase):
    id: UUID

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    name: str = None
    email: str = None

class UserStatusUpdate(BaseModel):
    is_active: bool