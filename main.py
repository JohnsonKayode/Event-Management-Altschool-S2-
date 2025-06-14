from fastapi import FastAPI
from routers.speaker_router import speaker_router
from routers.user_router import user_router
from routers.event_router import event_router
from routers.registration_router import registration_router


app = FastAPI()

app.include_router(speaker_router) 
app.include_router(user_router) 
app.include_router(event_router)
app.include_router(registration_router)
# This is to import routers into the main file


@app.get("/")
def home():
    return f"welcome to the home page of the Events"