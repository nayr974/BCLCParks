import random, datetime

from typing import List

from models.trailhead import Trailhead
from models.booking import Booking
from models.booking_states import BookingState

class LotteryPool(object):
    def __init__(self, date: datetime.date, th: Trailhead, am_or_pm:bool, db):
        self.date = date
        self.trailhead = th
        self.am_or_pm = am_or_pm
        self.db_session = db

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



def runLottery(l: LotteryPool, db) -> List[Booking]:

    all_bookings: List[Booking] = l.all_bookings()
    total_interest: int = len(all_bookings) if l.trailhead.capacity_type == "Vehicle" else sum([b.num_of_persons for b in all_bookings])
    max_allocation: int = l.get_max_allocation()

    allocated_bookings: List[Booking] = [b for b in all_bookings if b.state != "WAITING"]

    current_allocation: int = len(allocated_bookings) if l.trailhead.capacity_type == "Vehicle" else sum([b.num_of_persons for b in allocated_bookings])

    print('Total Reservations: {}'.format(len(all_bookings)))
    print('Trailhead Capacity: {}'.format(max_allocation))
    print('Allocation Request: {}'.format(total_interest))
    print('Current Allocation: {}'.format(current_allocation))

    while current_allocation < max_allocation:
        winner: Booking = random.choice(all_bookings)
        if l.trailhead.capacity_type == 'Trail':
            current_allocation +=  winner.num_of_persons
        else: #Vehicles allocation is one per booking
            current_allocation += 1
        winner.state = "PASS OFFERED"
        winner.send_offer_email()
        print("WINNER: {}",winner) 
        db.add(winner)
        db.commit()
    
    print("FULLY ALLOCATED")
    pass

