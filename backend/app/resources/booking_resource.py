from datetime import date

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from data_gen import genBookings

from .resource_models import Booking_Model
from models.booking import Booking
from database import get_db
 
router = APIRouter(
    prefix="/booking",
    tags=["booking"],
)


@router.post("/")
async def create_booking(booking: Booking_Model, db: Session = Depends(get_db)):
    booking = Booking.get_booking_by_email_and_date(db, booking.email, booking.date, booking.trailhead_id)
    if booking:
        raise HTTPException(status_code=400,
                            detail="A booking for this date and email already exists.")
    new_booking = Booking.create(booking)
    new_booking.save()

    return booking


@router.get("/{booking_id}")
async def get_booking(booking_id: int, db: Session = Depends(get_db)):
    booking = Booking.get_by_id(db, booking_id)
    if not booking:
        raise HTTPException(status_code=404, detail='No booking found for that ID.')
    return booking


@router.get("/")
async def get_all_bookings(db: Session = Depends(get_db)):
    booking = Booking.get_all_bookings(db)
    return booking if booking else []



@router.post("/random")
async def gen_bookings():
    b = genBookings()
    b.save()
    return b