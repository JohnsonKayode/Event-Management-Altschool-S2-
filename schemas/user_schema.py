from pydantic import BaseModel
from typing import Annotated, Union


class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True 




