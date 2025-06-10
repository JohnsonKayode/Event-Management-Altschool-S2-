from pydantic import BaseModel
from typing import Annotated, Union, Optional


class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True 

class Create_user(BaseModel):
    id: int
    name: str
    email: str

class Update_user(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None

