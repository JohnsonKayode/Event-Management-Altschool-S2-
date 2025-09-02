from fastapi import status, APIRouter, Depends
from schemas.user_schema import UserCreate, UserUpdate, UserStatusUpdate 
from database import SessionLocal, Base, engine
from sqlalchemy.orm import Session
from uuid import UUID
from services.user import user_services

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base.metadata.create_all(bind=engine)

user_router = APIRouter()

@user_router.get("/user", status_code=status.HTTP_202_ACCEPTED)
def get_all_users(user_db: Session = Depends(get_db)):
    users = user_services.get_all_users(user_db)
    return users

@user_router.get("/user/{user_id}", status_code=status.HTTP_200_OK)
def get_user_by_id(user_id: UUID, user_db: Session = Depends(get_db)):
    user = user_services.get_user_by_id(user_db, user_id)
    return user

@user_router.post("/user", status_code= status.HTTP_201_CREATED)
def create_user(createUser: UserCreate, user_db: Session = Depends(get_db)):
    users = user_services.create_user(user_db, createUser)
    return users

@user_router.patch("/user/{user_id}", status_code=status.HTTP_202_ACCEPTED)
def update_user(user_id: UUID, updateUser: UserUpdate, user_db: Session = Depends(get_db)):
    user = user_services.update_user(user_db, user_id, updateUser)
    return user

@user_router.patch("/user/{user_id}/status", status_code=status.HTTP_202_ACCEPTED)
def update_user_status(user_id: UUID, updateStatus: UserStatusUpdate, user_db: Session = Depends(get_db)):
    user = user_services.update_user_status(user_db, user_id, updateStatus)
    return user

@user_router.delete("/user/{user_id}", status_code=status.HTTP_200_OK)
def delete_user(user_id: UUID, user_db: Session = Depends(get_db)):
    user = user_services.delete_user(user_db, user_id)
    return user