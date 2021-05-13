import datetime
from models.base import Base
from sqlalchemy import Column, Integer, String, DateTime, Date, Boolean, ForeignKey


class Booking(Base):
    __tablename__ = 'booking'

    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    phone_no = Column(String(15))
    passcode = Column(String(20), nullable=False)
    trailhead_id = Column(Integer, ForeignKey('trailheadid'))
    date = Column(Date, nullable=False)
    am_or_pm = Column(Boolean, nullable=False) # 0 = AM, 1 = PM
    booking_type = Column(String, nullable=False ) # ["VEHICLE, PERSON"]
    num_of_persons = Column(Integer) # required if booking_type = PERSON
    vehicle_licence_plate = Column(String(12)) # required if booking_type = VEHICLE
    application_datetime = Column(DateTime, nullable=False, default=datetime.datetime.now())

    def __repr__(self):
        return '<Booking %r>' % self.id

    @classmethod
    def get_booking_by_email_and_date(cls, email, date):
        return cls.filter(email=email, date=date).one_or_none()

    @classmethod
    def get_booking_by_id(cls, id):
        return cls.filter(id=id).one_or_none()

    @classmethod
    def get_all_bookings(cls):
        return cls.all()
