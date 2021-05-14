from datetime import date

from fastapi import APIRouter, HTTPException

from .resource_models import Booking_Model

from models.booking import Booking
from data_gen import _genBooking
 
router = APIRouter(
    prefix="/booking",
    tags=["booking"],
)


@router.post("/")
async def create_booking(booking: Booking_Model):
    booking = Booking.get_booking_by_email_and_date(booking.email, booking.date)
    if booking:
        raise HTTPException(status_code=400,
                            detail="A booking for this date and email already exists.")
    new_booking = Booking.create(booking)
    new_booking.save()

    return booking


@router.get("/{booking_id}")
async def get_booking(booking_id: int):
    booking = Booking.get_by_id(booking_id)
    if not booking:
        raise HTTPException(status_code=404, detail='No booking found for that ID.')
    return booking


@router.get("/")
async def get_all_bookings():
    booking = Booking.get_all_bookings()
    return booking if booking else []



@router.post("/random")
async def gen_bookings():
    b: Booking = Booking(
        email="help@gmail.com",
        phone_no="111-111-1111",
        passcode="123456",
        trailhead_id=1,
        date=date.today(),
        am_or_pm=False,
        booking_type="PERSON", 
        )
    b.save()
    return b