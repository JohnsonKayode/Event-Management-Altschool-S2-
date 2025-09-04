from pydantic import BaseModel
from typing import Annotated, Union, Optional
from uuid import UUID


class EventBase(BaseModel):
    title: str
    location: str
    date: str
    is_open: bool = True

class Event(EventBase):
    id: UUID

class EventCreate(EventBase):
    pass

class UpdateEvent(BaseModel):
    title: str = None
    location: str = None
    date: str = None

class EventStatusUpdate(BaseModel):
    is_open: bool