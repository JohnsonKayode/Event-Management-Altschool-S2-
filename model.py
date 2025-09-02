from sqlalchemy import Column, Integer, String, Boolean
from database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=False, nullable=False)
    is_active = Column(Boolean, default=True)