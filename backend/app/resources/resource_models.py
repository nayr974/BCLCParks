from pydantic import BaseModel
from typing import Optional
from datetime import date


class Booking_Model(BaseModel):
    id: int
    email: str
    phone_no: str
    passcode: str
    trailhead_id: int
    date: date
    am_or_pm: bool
    booking_type: str
    num_of_persons: int
    vehicle_licence_plate: str
    application_datetime: date


class Trailhead_Model(BaseModel):
    id: int
    park_name: str
    trailhead_name: str
    am_capacity: int
    pm_capacity: int
