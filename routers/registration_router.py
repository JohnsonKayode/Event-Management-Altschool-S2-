from fastapi import FastAPI, APIRouter, HTTPException, status
from database import user_db, registration_db, event_db, speaker_db
from schemas.registration_schema import Registration


# So the first eendpoint should take in user ID as a query parameter to check for user status beefore reegistering

registration_router = APIRouter()


@registration_router.get("/registration")
def get_all_registered_user():
    return registration_db

@registration_router.post("/registration/{user_id}")
async def register_user_for_event(user_id: int, registration: Registration):

    registration_id = registration.id = len(registration_db) + 1

    # check if user exissts
    user = dict(user_db.get(user_id))
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # check if user is active
    user_status = user.get("is_active")
    if user_status == False:
        raise HTTPException(status_code=404, detail="User is not active")
    
    # check if the event exixts in the event db
    get_event = dict(event_db.get(registration.event_id))
    if not get_event:
        raise HTTPException(status_code=404, detail="Event not found")
    
    # check if event is open
    event_status = get_event.get("is_open")
    if not event_status:
        raise HTTPException(status_code=404, detail="Event is closed")
    
    #  event id for a user in regisstration db ssshould not be the same
    for key, value in registration_db.items():
        if key["user_id"] == user_id and value["event_id"] == registration.event_id:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    
    details = registration.model_dump()
    registration_db.update({registration_id: details})
    return {
        "messsage" : "User Successfully registered for event",
        "details" : details
    }


@registration_router.post("/register")
async def register(register:Registration):
    id = register.id = len(registration_db) + 1
    details = register.model_dump()
    registration_db.update(details)
    return {
        'message' : "this works",
        "detailss" : details
    }