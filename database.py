import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



SQLALCHEMY_DATABASE_URL = "postgresql://postgres:123456789@localhost:9090/main_duplicate"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# print(SessionLocal)
# print("\n 'Database session initialized' \n")

Base = declarative_base()

# db = SessionLocal()
# db.execute(text("CREATE DATABASE main_duplicate"))
# db.close()

user_db = {}

# dictionnary databasee for speaker

speaker_db = {
    1: {
        "id": '1',
        'name': 'Johnson Kayode',
        'topic': 'Future of AI'
    },

    2: {
        "id": '2',
        'name': 'Eyimofe Johnson',
        'topic': 'Pepper Mentol: Using AI'
    },
    
    3: {
        "id": '3',
        'name': 'Prudence Ralph',
        'topic': 'Product management: Using AI'
    }
}

# dictionnary databasee for eevent

event_db = {}

# dictionnary databasee for registered user

registration_db = {}