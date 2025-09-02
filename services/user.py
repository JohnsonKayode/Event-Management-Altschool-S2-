import uuid
from schemas.user_schema import UserCreate, UserUpdate, User, UserStatusUpdate, UserBase
from database import user_db
from uuid import UUID
from model import User
from sqlalchemy.orm import Session
from fastapi import status

class UserServices:
    @staticmethod
    def get_all_users(user_db: Session):
        user  = user_db.query(User).all()
        return user
    
    @staticmethod
    def get_user_by_id(user_db: Session, user_id: UUID):
        user = user_db.query(User).filter(User.id == str(user_id)).first()
        if user:
            return user
        return f"User not found", status.HTTP_404_NOT_FOUND

    @staticmethod
    def create_user(user_db: Session, createUser: UserCreate):
        user = User(id=str(uuid.uuid4()), **createUser.model_dump())
        user_db.add(user)
        user_db.commit()
        user_db.refresh(user)
        return {
            'message': 'User Created Successfully',
            'details': user
        }

    @staticmethod
    def update_user(user_db: Session, user_id: UUID, updateUser: UserUpdate):
        user = UserServices.get_user_by_id(user_db, user_id)
        if user:
            for key, value in updateUser.model_dump().items():
                if value is not None:
                    setattr(user, key, value)
            user_db.commit()
            user_db.refresh(user)
            return {
                'message': 'user updated successfully',
                'details' : user
            }
        return f"User not found", status.HTTP_404_NOT_FOUND
    

    @staticmethod
    def update_user_status(user_db: Session, user_id: UUID, updateStatus: UserStatusUpdate):
        user = user_db.query(User).filter(User.id == str(user_id)).first()
        if user:
            user.is_active = updateStatus.is_active
            user_db.commit()
            user_db.refresh(user)
            return {
                'message': 'Status updated successfully',
                'details': user
            }
        return f"User Id not found", status.HTTP_404_NOT_FOUND
    

    @staticmethod
    def delete_user(user_db: Session, user_id:UUID):
        user = user_db.query(User).filter(User.id == str(user_id)).first()
        if user:
            user_db.delete(user)
            user_db.commit()
            return {
                'message': 'user deleted successfully',
                'details': user
            }
        return f"This user does not exist, enter a valid user ID", status.HTTP_404_NOT_FOUND
    

user_services = UserServices()