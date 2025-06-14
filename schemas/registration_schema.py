from pydantic import BaseModel
from typing import  Annotated, Union


class Registration(BaseModel):
    id: int
    user_id: int
    event_id: int
    registration_date: Annotated[Union[int, str], "date format or timestamp"] = 0
    attended: bool = False


id: Unique identifier
user_id: ID of the registering user
event_id: ID of the event
registration_date: When the user registered
attended: Whether the user attended (default: False)

