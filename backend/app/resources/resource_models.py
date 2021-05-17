from pydantic import BaseModel
from typing import Optional, List
from datetime import date

from models.model_enums import BookingState

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

class Booking_ModelPatch(BaseModel):
    email: Optional[str]
    phone_no: Optional[str]
    passcode: Optional[str]
    num_of_persons: Optional[int]
    vehicle_licence_plate: Optional[str]
    state: Optional[BookingState]

class Trailhead_Model(BaseModel):
    id: int
    park_name: str
    trailhead_name: str
    am_capacity: int
    pm_capacity: int


class RunLotteryRequest(BaseModel):
    date: date
    am_or_pm: bool
    trailhead_id: int


class TrailheadReservationsRequest(BaseModel):
    date: date
    am_or_pm: bool

class TrailheadReservationsResponse(BaseModel):
    total_bookings: int
    total_interest: int
    num_allocated_bookings: int
    allocated_capacity: int
    trailhead_capacity: int
    allocated_bookings: List[Booking_Model]