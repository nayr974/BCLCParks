import random

from typing import Any, List
from datetime import date

from models.trailhead import Trailhead
from models.booking import Booking
from managers.lottery import LotteryPool

from .booking_factory import BookingFactory

def _genBooking(db, date: date, am_or_pm: bool, th: Trailhead, batch_size = 1, ):
    b = BookingFactory.create_batch(size=batch_size,
        date=date,
        am_or_pm=am_or_pm,
        trailhead_id = th.id)
    db.bulk_save_objects(b)
    db.commit()
    return b


def genBookings(db): 
    l = LotteryPool(date=date.today(),
                th=db.query(Trailhead).first(),
                am_or_pm=random.choice([True, False]),
                db=db)

    gen_bookings_for_lottery_pool(l, db)
    
    return


def gen_bookings_for_lottery_pool(l: LotteryPool, db) -> List[Any]:
    interest_output = l.get_max_allocation() * 3
    generated_interest = 0
    print(l.__dict__)
    while generated_interest < interest_output: 
        print('GENERATING MORE {} < {} ', generated_interest, interest_output)
        bookings = _genBooking(db, l.date, l.am_or_pm, l.trailhead, interest_output//8)
        generated_interest += sum([b.num_of_persons for b in bookings])
    return
