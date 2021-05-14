import random, datetime

from typing import List

from models.trailhead import Trailhead
from models.booking import Booking
from models.booking_states import BookingState

class LotteryPool(object):
    def __init__(self, date: datetime.date, trailhead: Trailhead, booking_type: str, am_or_pm:bool):
        self.date = date
        self.trailhead = trailhead
        self.booking_type = booking_type
        self.am_or_pm = am_or_pm

    def get_total_interest(self):   
        return Booking.query.filter(date=self.date, trailhead_id=self.trailhead.id, booking_type=self.booking_type, am_or_pm=self.am_or_pm).all()
        
    def get_max_allocation(self):
        return self.trailhead.am_capacity if self.am_or_pm else self.trailhead.pm_capacity

    def _all_booking_query(self):
        return Booking.query.filter(date=self.date, trailhead_id=self.trailhead.id, booking_type=self.booking_type, am_or_pm=self.am_or_pm)

    def all_bookings(self):
        return self._all_booking_query.all()

    def lottery_pool(self):
        return self._all_booking_query.filter_by(state="WAITING").all()



def runLottery(l: LotteryPool) -> List[Booking]:
    assert type in ["VEHICLE","PERSON"]

    all_bookings = l.all_bookings()
    total_interest = l.get_total_interest()
    max_allocation = l.get_max_allocation()

    pass

