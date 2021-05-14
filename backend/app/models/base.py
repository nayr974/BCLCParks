from database import SessionLocal
from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

from database import get_db


class MyBaseModel(object):
    def save(self):
        #fetch new session ideally we get the same one. 
        db=next(get_db())
        db.add(self)
        db.commit()

Base = declarative_base(cls=MyBaseModel)