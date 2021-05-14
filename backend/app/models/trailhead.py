from datetime import date
from sqlalchemy import Column, Integer, String, DateTime, Date, Boolean, ForeignKey

from models.base import Base


class Trailhead(Base):
    __tablename__ = "trailhead"

    id = Column(Integer, primary_key=True)
    park_name = Column(String(80), nullable=False)
    trailhead_name = Column(String(80), nullable=False)
    capacity_type = Column(String(32), nullable=False)
    am_capacity = Column(Integer, nullable=False)
    pm_capacity = Column(Integer, nullable=False)

    def __repr__(self):
        return '<Trailhead {},{},{},{}>'.format(self.park_name, self.trailhead_name, self.am_capacity, self.pm_capacity)

    @classmethod
    def get_trialhead_by_id(cls, db, id):
        return db.query(cls).filter(id=id).one_or_none()

    @classmethod
    def get_all_trailheads_by_park_name(cls, db, park_name):
        return db.query(cls).filter(park_name=park_name).all()

    @classmethod
    def get_all_trailheads(cls, db):
        return db.query(cls).all()
