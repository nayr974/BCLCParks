import datetime
from ..extensions import db


class Booking(db.Model):
    __tablename__ = 'booking'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_no = db.Column(db.String(15))
    passcode = db.Column(db.String(20), nullable=False)
    trailhead_id = db.Column(db.Integer, db.ForeignKey('trailhead.id'))
    date = db.Column(db.Date, nullable=False)
    am_or_pm = db.Column(db.Boolean, nullable=False)  # 0 = AM, 1 = PM
    booking_type = db.Column(db.String, nullable=False)  # ["VEHICLE, PERSON"]
    num_of_persons = db.Column(db.Integer)  # required if booking_type = PERSON
    vehicle_licence_plate = db.Column(db.String(12))  # required if booking_type = VEHICLE
    application_datetime = db.Column(db.Datetime, nullable=False, default=datetime.datetime.now())

    def __repr__(self):
        return '<Booking %r>' % self.id

    @classmethod
    def get_booking_by_email_and_date(email, date):
        return cls.filter(email=email, date=date).first()
