from pydantic import BaseModel
from typing import  Annotated, Union, Optional

class Registration(BaseModel):
    id: int
    user_id: int
    event_id: int
    registration_date: Annotated[Union[str, int], "date format or timestamp"] = 0
    attended: bool = False

class Attendance(BaseModel):
    attended: bool = False
    