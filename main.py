from fastapi import FastAPI


app = FastAPI()

# app.include_router(routername) This is to import routers into the main file


@app.get("/")
def home():
    return f"welcome to the home page of the Events"