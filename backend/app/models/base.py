from database import SessionLocal
from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

from database import get_db


class MyBaseModel(object):
    def save(self, db: Session = Depends(get_db)):
        db=next(get_db())
        print(db)
        db.add(self)
        db.commit()

Base = declarative_base(cls=MyBaseModel)