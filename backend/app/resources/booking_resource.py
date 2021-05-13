from fastapi import APIRouter, HTTPException

from .resource_models import Booking

from ..models.booking import Booking_Model

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


@router.get("/users/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}