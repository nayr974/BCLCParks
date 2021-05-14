from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from .resource_models import *
from managers.lottery import LotteryPool
from models.trailhead import Trailhead
from database import get_db

router = APIRouter(
    prefix="/trailhead",
    tags=["booking"],
)


@router.get("/{trailhead_id}")
async def get_trailhead(trailhead_id: int, db: Session = Depends(get_db)):
    trailhead = Trailhead.get_by_id(db, trailhead_id)
    if not trailhead:
        raise HTTPException(status_code=404, detail='No trailhead found for that ID.')
    return trailhead


@router.get("/")
async def get_all_trailheads(db: Session = Depends(get_db)):
    return Trailhead.get_all_trailheads(db)



@router.get("/{trailhead_id}/allocation",  response_model=TrailheadReservationsResponse)
async def get_trailhead_reservations(trailhead_id: int,
                            body: TrailheadReservationsRequest,
                            db:Session = Depends(get_db)
                            ) :
    th = Trailhead.get_trialhead_by_id(db, trailhead_id)
    lp = LotteryPool(date=body.date, am_or_pm=body.am_or_pm, th=th, db=db)    

    return TrailheadReservationsResponse(
        total_bookings=len(lp.get_all_bookings()),
        total_interest=lp.get_total_interest(),
        num_allocated_bookings=len(lp.get_allocated_bookings()),
        allocated_capacity=lp.get_current_allocation(),
        trailhead_capacity=lp.get_max_allocation(),
        allocated_bookings=[x.__dict__ for x in lp.get_allocated_bookings()])

