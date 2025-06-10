from fastapi import APIRouter, HTTPException, status
from database import speaker_db
from schemas.speaker_schema import Create_speaker


speaker_router = APIRouter()


@speaker_router.get("/speaker")
def get_all_speakers():
    return speaker_db


@speaker_router.post("/speaker")
def create_speaker(created_speaker: Create_speaker):
    id = created_speaker.id = len(speaker_db) + 1
    details = created_speaker.model_dump()
    speaker_db.update({id: details})
    return {
        'Message': 'Speaker successfully Created' ,
        'Details': details}

