from uuid import UUID
from database import event_db
from schemas.event_schema import Event, Update_Event
from fastapi import HTTPException, status


class EventServices:

    @staticmethod
    def create_event(createEvent: Event):
        id = createEvent.id = id=str(UUID(int=len(event_db) + 1))
        details = createEvent.model_dump()
        event_db.update({id: details})
        return {
            'message': 'Event Created Successfully',
            'details': details
        }


    @staticmethod
    def update_event_by_id(id: UUID, updateEvent: Update_Event):
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

            return {
                'message': 'Event updated successfully',
                'details': existing_event
            }
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not found")


    @staticmethod
    def UpdateStatus(id: UUID, updateStatus: Update_Event):
        if id in event_db:
            details = event_db[id] 
            details["is_open"] = updateStatus.is_open
            return {
                "message" : "Status updated Successfully",
                'details' : details
            }
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    


    # @staticmethod
    # def deleteEveentt


eventService = EventServices()