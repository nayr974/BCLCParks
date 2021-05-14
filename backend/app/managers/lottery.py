import random, datetime

from typing import List

from models.trailhead import Trailhead
from models.booking import Booking
from models.booking_states import BookingState

class LotteryPool(object):
    def __init__(self, date: datetime.date, th: Trailhead, am_or_pm:bool, sess):
        self.date = date
        self.trailhead = th
        self.am_or_pm = am_or_pm
        self.db_session = sess

    def get_total_interest(self):   
        return self.db_session.query(Booking).filter(
                    Booking.date==self.date, 
                    Booking.trailhead_id==self.trailhead.id,
                    Booking.booking_type==self.trailhead.capacity_type, 
                    Booking.am_or_pm==self.am_or_pm).all()
        
    def get_max_allocation(self):
        return self.trailhead.am_capacity if self.am_or_pm else self.trailhead.pm_capacity

    def _all_booking_query(self):
        return self.db_session.query(Booking).filter(
                    Booking.trailhead_id==self.trailhead.id,
                    Booking.date== self.date,
                    Booking.booking_type==self.trailhead.capacity_type, 
                    Booking.am_or_pm==self.am_or_pm)

    def all_bookings(self):
        return self._all_booking_query().all()

    def lottery_pool(self):
        return self._all_booking_query().filter_by(state="WAITING").all()



def runLottery(l: LotteryPool) -> List[Booking]:

    all_bookings: List[Booking] = l.all_bookings()
    total_interest: int = len(all_bookings) if l.trailhead.capacity_type == "Vehicle" else sum([b.num_of_persons for b in all_bookings])
    max_allocation: int = l.get_max_allocation()

    print(len(all_bookings))
    print(max_allocation)
    print(total_interest)

    pass

