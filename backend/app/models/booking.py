import datetime
import random

from sqlalchemy import Column, Integer, String, DateTime, Date, Boolean, ForeignKey, Enum
from sqlalchemy.orm import relationship

from models.base import Base
from models.model_enums import BookingState


    

class Booking(Base):
    __tablename__ = 'booking'

    id = Column(Integer, primary_key=True)
    email = Column(String(120), nullable=False)
    phone_no = Column(String(15))
    passcode = Column(String(20), nullable=False, default=''.join(random.choice('0123456789ABCDEF') for i in range(6)))
    trailhead_id = Column(Integer, ForeignKey('trailhead.id'))
    date = Column(Date, nullable=False)
    am_or_pm = Column(Boolean, nullable=False) # 1 = AM, 0 = PM
    booking_type = Column(String, nullable=False ) # ["VEHICLE, PERSON"]
    num_of_persons = Column(Integer) # required if booking_type = PERSON
    vehicle_licence_plate = Column(String(12)) # required if booking_type = VEHICLE
    application_datetime = Column(DateTime, nullable=False, default=datetime.datetime.now())
    state = Column(Enum(BookingState, values_callable=lambda obj: [e.value for e in obj]))

    trailhead = relationship("Trailhead")


    def __repr__(self):
        return '<Booking %r>' % self.id

    @classmethod
    def get_booking_by_email_and_date(cls, db, email, date, trailhead_id):
        return db.query(cls).filter(email=email, date=date, trailhead_id=trailhead_id).one_or_none()

    @classmethod
    def get_booking_by_id(cls, db, id):
        return db.query(cls).filter(id=id).one_or_none()

    @classmethod
    def get_all_bookings(cls):
        return db.query(cls).all()

    @classmethod
    def get_bookings_trailhead_date(cls, db, date:datetime.date, trailhead_id:int):
        return db.query(cls).filter(date=date, trailhead_id=trailhead_id).all()
