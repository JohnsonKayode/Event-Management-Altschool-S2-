from pydantic import BaseModel
from typing import Annotated, Union, Optional

class Event(BaseModel):
    id: int
    title: str
    location: str
    date: Annotated[Union[str, int], "Date can be a string or an integer"] = 0
    is_open: bool = True

class Update_Event(BaseModel):
    title: Optional[str] = None
    location: Optional[str] = None
    date: Optional[Annotated[Union[str, int], "Date can be a string or an integer"]] = 0
    is_open: bool = True