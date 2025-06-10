from fastapi import FastAPI
from routers.speaker_router import speaker_router


app = FastAPI()

app.include_router(speaker_router) 
# This is to import routers into the main file


@app.get("/")
def home():
    return f"welcome to the home page of the Events"