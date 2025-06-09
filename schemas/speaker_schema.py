from pydantic import BaseModel
from typing import Annotated, Union

class Speaker(BaseModel):
    id: int
    user_id: int
    event_id: int
    registration_date: int
    attended: bool = False