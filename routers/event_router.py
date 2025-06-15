from fastapi import HTTPException, FastAPI, APIRouter, status
from database import event_db, user_db, registration_db, speaker_db
from schemas.event_schema import Event, Update_Event


event_router = APIRouter()

@event_router.get("/event", status_code=status.HTTP_202_ACCEPTED)
def get_all_event():
    return event_db

@event_router.post("/event", status_code=status.HTTP_201_CREATED)
def create_event(createEvent: Event):
    id = createEvent.id = len(event_db) + 1
    details = createEvent.model_dump()
    event_db.update({id: details})
    return {
        'message': 'Event Created Successfully',
        'details': details
    }

@event_router.put("/event/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_event(id: int, updateEvent: Update_Event):
    if id in event_db:
        existing_event = event_db.get(id)  # Get the current event details
        # updateEvent.model_dump(exclude_unset=True)
        if updateEvent.title is not None:
            existing_event["title"] = updateEvent.title
        if updateEvent.location is not None:
            existing_event["location"] = updateEvent.location
        if updateEvent.date is not None:
            existing_event["date"] = updateEvent.date
        if updateEvent.is_open is not None:
            existing_event["is_open"] = updateEvent.is_open

        event_db.update(updateEvent)

        # updated_data = updateEvent.model_dump()  # Only include fields provided in the request
        # existing_event.update(updated_data)  # Update only the provided fields
        # event_db[id]= existing_event  # Save the updated event back to the database
        return {
            'message': 'Event updated successfully',
            'details': existing_event
        }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not found")


@event_router.put("/event/{id}/status", status_code=status.HTTP_200_OK)
async def update_event_status(id: int, updateStatus: Update_Event):
    if id in event_db:
        details = event_db[id] 
        details["is_open"] = updateStatus.is_open
        return {
            "message" : "Status updated Successfully",
            'details' : details
        }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@event_router.delete("/event", status_code=status.HTTP_204_NO_CONTENT)
def delete_event(id:int):
    if id in event_db:
        details = event_db.pop(id)
        return {
            "message": 'Successfully deleted event',
            'details' : details
        }
    return f"This event does not eexist", status.HTTP_404_NOT_FOUND