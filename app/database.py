from typing import Annotated

from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker
from dotenv import load_dotenv
import os


load_dotenv()
DB_URL:str =  os.getenv("DB_URL", "")
print("DB_URL", DB_URL)
engine = create_engine(DB_URL)

session = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()



DbSession = Annotated[Session, Depends(get_db)]