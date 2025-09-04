from sqlalchemy import Column, Integer, String, Boolean
from database import Base


class UserT(Base):

    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=False, nullable=False)
    is_active = Column(Boolean, default=True)


class EventT(Base):
    
    __tablename__ = "event"
    
    id = Column(String, primary_key=True, index=True)
    title = Column(String, nullable=False)
    location = Column(String, nullable=False)
    date = Column(String, nullable=False)
    is_open = Column(Boolean, default=True)
