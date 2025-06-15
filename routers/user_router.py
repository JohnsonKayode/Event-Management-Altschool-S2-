from fastapi import FastAPI, HTTPException, status, APIRouter
from schemas.user_schema import Create_user, Update_user, User
from database import user_db


user_router = APIRouter()

@user_router.get("/user")
def get_all_users():
    return user_db

@user_router.post("/user", status_code= status.HTTP_201_CREATED)
def create_user(createUser: User):
    id = createUser.id = len(user_db) + 1
    details = createUser.model_dump()
    user_db.update({id: details})
    return {
        'message': 'User Created Successfully',
        'details': details
    }


@user_router.put("/user/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_user(id: int, updateUser: Update_user):
    if id in user_db:
        details = user_db[id] = updateUser.model_dump()
        return {
            'message': 'user updated successfully',
            'details' : details
        }
    return f"User not found", status.HTTP_404_NOT_FOUND


@user_router.put("/User/{id}/status", status_code=status.HTTP_202_ACCEPTED)
def update_user_status(id: int, updateStatus:User):
    if id in user_db:
        details = user_status = user_db[id]
        user_status["is_active"] = updateStatus.is_active
        return {
            'message': 'Status updated sucessfullly',
            'details': details
        }
    return f"User Id not found", status.HTTP_404_NOT_FOUND


@user_router.delete("/user/{id}")
def delete_user(id:int):
    if id in user_db:
        details = user_db.pop(id)
        return {
            'message': 'user deleted successfully',
            'details': details
        }
    return f"This user does not exist, enter a valid user ID", status.HTTP_404_NOT_FOUND