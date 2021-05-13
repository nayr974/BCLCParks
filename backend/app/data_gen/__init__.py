import random

from typing import Any, List
from datetime import date

from models.trailhead import Trailhead
from models.booking import Booking
from managers.lottery import LotteryPool

from .booking_factory import BookingFactory

def _genBooking(date: date, am_or_pm: bool, booking_type: str):
    b = BookingFactory(
        date=date,
        am_or_pm=am_or_pm,
        booking_type=booking_type,
    )
    return b


def genBookings(): 
    l = LotteryPool(date.today()
                ,Trailhead.query.first()
                ,random.choice(["VEHICLE","PERSON"])
                ,random.choice([True, False]))

    pass


def gen_bookings_for_lottery_pool(l: LotteryPool) -> List[Any]:
    interest_output = l.get_max_allocation * 3
    generated_interest = 0
    while generated_interest < interest_output: 
        _genBooking(l.date, l.am_or_pm,l.booking_type, l.trailhead)

    pass
