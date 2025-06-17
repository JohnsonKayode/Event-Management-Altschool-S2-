from fastapi import FastAPI, APIRouter, HTTPException, status
from uuid import UUID
from database import user_db, registration_db, event_db, speaker_db
from schemas.registration_schema import Registration, Attendance


# So the first eendpoint should take in user ID as a query parameter to check for user status beefore reegistering

registration_router = APIRouter()


@registration_router.get("/registration", status_code=status.HTTP_200_OK)
def get_all_registered_user():
    return registration_db

@registration_router.post("/registration/{user_id}", status_code=status.HTTP_201_CREATED)
async def register_user_for_event(user_id: UUID, registration: Registration):

    # registration_id = registration.id = len(registration_db) + 1
    registration_id = registration.id = str(UUID(int=len(registration_db) + 1))

    # check if user exissts
    user = user_db.get(user_id)
    if not user or user == 0:
        raise HTTPException(status_code=404, detail="User not found")
    
    # check if user is active
    user_status = user.get("is_active")
    if user_status == False:
        raise HTTPException(status_code=404, detail="User is not active")
    
    # check if the event exixts in the event db
    get_event = event_db.get(registration.event_id)
    if not get_event:
        raise HTTPException(status_code=404, detail="Event not found")
    
    # check if event is open
    event_status = get_event.get("is_open")
    if not event_status:
        raise HTTPException(status_code=404, detail="Event is closed")
    
    #  event id for a user in regisstration db ssshould not be the same
    for key, value in registration_db.items():
        if value["user_id"] == user_id and value["event_id"] == registration.event_id:
            raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED, detail="You cannor registerr for the same event Twice. Kindly register for another event")

    
    details = registration.model_dump()
    registration_db.update({registration_id: details})
    return {
        "messsage" : "User Successfully registered for event",
        "details" : details
    }


# @registration_router.post("/register")
# async def register(register:Registration):
#     id = register.id = len(registration_db) + 1
#     details = register.model_dump()
#     registration_db.update({id: details})
#     return {
#         'message' : "this works",
#         "detailss" : details
#     }

@registration_router.put("/registration/{user_id}/attendance", status_code=status.HTTP_200_OK)
async def update_attendance(user_id: UUID):
    user = registration_db.get(user_id)
    if not user or user == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This user has not registered for any event")

    user["attended"] = True
    registration_db[user_id] = user
    return {
        'message': 'User attendance successfully updated',
        'user': user
    }

@registration_router.get("/registration/{user_id}", status_code=status.HTTP_202_ACCEPTED)
async def get_user_info(user_id: UUID):
    user = registration_db[user_id]
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return user