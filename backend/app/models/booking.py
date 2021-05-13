import datetime
import random
from models.base import Base
from sqlalchemy import Column, Integer, String, DateTime, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class Booking(Base):
    __tablename__ = 'booking'

    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    phone_no = Column(String(15))
    passcode = Column(String(20), nullable=False, default=''.join(random.choice('0123456789ABCDEF') for i in range(6)))
    trailhead_id = Column(Integer, ForeignKey('trailhead.id'))
    date = Column(Date, nullable=False)
    am_or_pm = Column(Boolean, nullable=False) # 1 = AM, 0 = PM
    booking_type = Column(String, nullable=False ) # ["VEHICLE, PERSON"]
    num_of_persons = Column(Integer) # required if booking_type = PERSON
    vehicle_licence_plate = Column(String(12)) # required if booking_type = VEHICLE
    application_datetime = Column(DateTime, nullable=False, default=datetime.datetime.now())
    

    trailhead = relationship("Trailhead")


    def __repr__(self):
        return '<Booking %r>' % self.id

    @classmethod
    def get_booking_by_email_and_date(cls, email, date):
        return cls.query.filter(email=email, date=date).one_or_none()

    @classmethod
    def get_booking_by_id(cls, id):
        return cls.query.filter(id=id).one_or_none()

    @classmethod
    def get_all_bookings(cls):
        return cls.query.all()

    @classmethod
    def get_bookings_trailhead_date(cls, date:datetime.date, trailhead_id:int):
        return cls.query.filter(date=date, trailhead_id=trailhead_id).all()
