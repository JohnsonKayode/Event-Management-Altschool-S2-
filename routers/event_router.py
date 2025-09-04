from fastapi import APIRouter, status, Depends
from uuid import UUID
from database import SessionLocal, Base, engine
from sqlalchemy.orm import Session
from schemas.event_schema import EventCreate, UpdateEvent, EventStatusUpdate, EventBase
from services.event import event_services

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base.metadata.create_all(bind=engine)
print("Tables created successfully!")

event_router = APIRouter()

@event_router.get("/event", status_code=status.HTTP_202_ACCEPTED)
def get_all_event(event_db: Session = Depends(get_db)):
    event = event_services.get_all_event(event_db)
    return event

@event_router.get("/event/{event_id}", status_code=status.HTTP_200_OK)
def get_event_by_id(event_id: UUID, event_db: Session = Depends(get_db)):
    event = event_services.get_event_by_id(event_db, event_id)
    return event

@event_router.post("/event", status_code=status.HTTP_201_CREATED)
def create_event(createEvent: EventCreate, event_db: Session = Depends(get_db)):
    details = event_services.create_event(event_db, createEvent)
    return details

@event_router.patch("/event/{event_id}", status_code=status.HTTP_202_ACCEPTED)
def update_event(event_id: UUID, updateEvent: UpdateEvent, event_db: Session = Depends(get_db)):
    event = event_services.update_event(event_db, event_id, updateEvent)
    return event

@event_router.patch("/event/{event_id}/status", status_code=status.HTTP_200_OK)
def update_event_status(event_id: UUID, updateStatus: EventStatusUpdate, event_db : Session = Depends(get_db)):
    details = event_services.update_event_status(event_db, event_id, updateStatus)
    return {
        "message" : "Status updated Successfully",
        'details' : details
    }


@event_router.delete("/event/{event_id}", status_code=status.HTTP_200_OK)
def delete_event(event_id:UUID, event_db: Session = Depends(get_db)):
    details = event_services.delete_event(event_db, event_id)
    return details