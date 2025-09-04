import uuid
from schemas.event_schema import EventCreate, UpdateEvent, EventStatusUpdate, Event, EventBase
from database import Base, SessionLocal, engine
from uuid import UUID
from model import EventT
from sqlalchemy.orm import Session
from fastapi import status

class EventServices:
    @staticmethod
    def get_all_event(event_db: Session):
        event  = event_db.query(EventT).all()
        return event
    
    @staticmethod
    def get_event_by_id(event_db: Session, event_id: UUID):
        event = event_db.query(EventT).filter(EventT.id == str(event_id)).first()
        if event:
            return event
        return f"Event not found", status.HTTP_404_NOT_FOUND

    @staticmethod
    def create_event(event_db: Session, createEvent: EventCreate):
        event = EventT(id=str(uuid.uuid4()), **createEvent.model_dump())
        event_db.add(event)
        event_db.commit()
        event_db.refresh(event)
        return {
            'message': 'Event Created Successfully',
            'details': event
        }

    @staticmethod
    def update_event(event_db: Session, event_id: UUID, updateEvent: UpdateEvent):
        event = EventServices.get_event_by_id(event_db, event_id)
        if event:
            for key, value in updateEvent.model_dump().items():
                if value is not None:
                    setattr(event, key, value)
            event_db.commit()
            event_db.refresh(event)
            return {
                'message': 'Event updated successfully',
                'details' : event
            }
        return f"Event not found", status.HTTP_404_NOT_FOUND
    

    @staticmethod
    def update_event_status(event_db: Session, event_id: UUID, updateStatus: EventStatusUpdate):
        event = event_db.query(EventT).filter(EventT.id == str(event_id)).first()
        if event:
            event.is_open = updateStatus.is_open
            event_db.commit()
            event_db.refresh(event)
            return {
                'message': 'Status updated successfully',
                'details': event
            }
        return f"Event Id not found", status.HTTP_404_NOT_FOUND
    

    @staticmethod
    def delete_event(event_db: Session, event_id: UUID):
        event = event_db.query(EventT).filter(EventT.id == str(event_id)).first()
        if event:
            event_db.delete(event)
            event_db.commit()
            return {
                'message': 'event deleted successfully',
                'details': event
            }
        return f"This event does not exist, enter a valid event ID", status.HTTP_404_NOT_FOUND
    

event_services = EventServices()