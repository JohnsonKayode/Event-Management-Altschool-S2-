from pydantic import BaseModel
from typing import Annotated, Union, Optional

class Speaker(BaseModel):
    id: int
    user_id: int
    event_id: int
    registration_date: int
    attended: bool = False


class Create_speaker(BaseModel):
    id: int
    name: str
    topic: str


class Update_speaker(BaseModel):
    name: Optional[str] = None
    topic: Optional[str] = None
