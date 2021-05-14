import random, datetime

from typing import List

from models.trailhead import Trailhead
from models.booking import Booking
from models.booking_states import BookingState

class LotteryPool(object):

    _all_bookings: List[Booking] = []

    def __init__(self, date: datetime.date, th: Trailhead, am_or_pm:bool, db):
        self.date = date
        self.trailhead = th
        self.am_or_pm = am_or_pm
        self.db_session = db

    def get_allocated_bookings(self): 
        return [b for b in self.get_all_bookings() if b.state != "WAITING"]

    def get_current_allocation(self):
        return len(self.get_allocated_bookings()) if self.trailhead.capacity_type == "Vehicle" else sum([b.num_of_persons for b in self.get_allocated_bookings()])


    def get_total_interest(self):   
        return len(self.get_all_bookings()) if self.trailhead.capacity_type == "Vehicle" else sum([b.num_of_persons for b in self.get_all_bookings()])

    def get_max_allocation(self):
        return self.trailhead.am_capacity if self.am_or_pm else self.trailhead.pm_capacity

    def _all_booking_query(self):
        return self.db_session.query(Booking).filter(
                    Booking.trailhead_id==self.trailhead.id,
                    Booking.date== self.date,
                    Booking.booking_type==self.trailhead.capacity_type, 
                    Booking.am_or_pm==self.am_or_pm)

    def get_all_bookings(self):
        if not self._all_bookings:
            self._all_bookings = self._all_booking_query().all()
        return self._all_bookings

    def lottery_pool(self):
        return self._all_booking_query().filter_by(state="WAITING").all()



def runLottery(l: LotteryPool, db) -> List[Booking]:

    all_bookings: List[Booking] = l.get_all_bookings()
    total_interest: int = l.get_total_interest()
    max_allocation: int = l.get_max_allocation()
    allocated_bookings: List[Booking] = l.get_allocated_bookings()
    current_allocation: int = l.get_current_allocation()

    new_winners: List[Booking] = []
    
    print('Total Reservations: {}'.format(len(all_bookings)))
    print("Active Reservations {}".format(len(allocated_bookings)))
    print('Trailhead Capacity: {}'.format(max_allocation))
    print('Allocation Request: {}'.format(total_interest))

    while current_allocation < max_allocation:
        winner: Booking = random.choice(all_bookings)
        if l.trailhead.capacity_type == 'Trail':
            current_allocation +=  winner.num_of_persons
        else: #Vehicles allocation is one per booking
            current_allocation += 1
        print("WINNER " + str(winner))
        winner.state="PASS OFFERED"
        new_winners.append(winner)
        all_bookings.remove(winner)
    
    print('Final Allocation: {}'.format(current_allocation))
       
    db.bulk_save_objects(new_winners)
    db.commit()
    for b in new_winners:   
        b.send_offer_email()
    pass

