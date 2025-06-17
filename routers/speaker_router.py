from fastapi import APIRouter, HTTPException, status
from uuid import UUID
from database import speaker_db
from schemas.speaker_schema import Create_speaker, Update_speaker


speaker_router = APIRouter()


@speaker_router.get("/speaker", status_code=status.HTTP_200_OK)
def get_all_speakers():
    return speaker_db


@speaker_router.post("/speaker", status_code=status.HTTP_201_CREATED)
def create_speaker(created_speaker: Create_speaker):
    id = created_speaker.id = str(UUID(int=len(speaker_db) + 1))
    # id = created_speaker.id = len(speaker_db) + 1
    details = created_speaker.model_dump()
    speaker_db.update({id: details})
    return {
        'Message': 'Speaker successfully Created' ,
        'Details': details}


@speaker_router.put("/speaker/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_speaker(id: int, update_a_speaker_details: Update_speaker):
    if id in speaker_db:
        details = speaker_db[id] = update_a_speaker_details.model_dump()
        return {
            'Message': 'Details Updated sucessfully',
            "details" : details
        }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Speaker not found")



@speaker_router.delete("/speaker/{id}", status_code=status.HTTP_204_NO_CONTENT)
def del_speaker(id: int):
    if id in speaker_db:
       del_speaker = speaker_db.pop(id)
       return {
           'message' : "Speaker Deleted ssucessfully", 
           'detailss' : del_speaker
       }
    return f"speaker not found", status.HTTP_404_NOT_FOUND