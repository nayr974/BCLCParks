from datetime import date
from pydantic import BaseModel
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from data_gen import genBookings
from managers.lottery import LotteryPool, runLottery
from models.trailhead import Trailhead

from .resource_models import *
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
async def gen_bookings(db: Session = Depends(get_db)):
    b = genBookings(db)
    return b


@router.post("/run-lottery")
async def run_lottery(body: RunLotteryRequest, db: Session = Depends(get_db)): 
    print(body.__dict__)
    th = Trailhead.get_trialhead_by_id(db, body.trailhead_id)
    lp = LotteryPool(date=body.date, am_or_pm=body.am_or_pm, th=th, db=db)    

    runLottery(lp,db)