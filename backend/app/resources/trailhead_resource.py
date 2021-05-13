from fastapi import APIRouter, HTTPException

from .resource_models import Trailhead_Model

from models.trailhead import Trailhead

router = APIRouter(
    prefix="/trailhead",
    tags=["booking"],
)


@router.get("/{trailhead_id}")
async def get_booking(trailhead_id: int):
    trailhead = Trailhead.get_by_id(trailhead_id)
    if not trailhead:
        raise HTTPException(status_code=404, detail='No trailhead found for that ID.')
    return trailhead


@router.get("/{park_name}")
async def get_all_bookings(park_name: str):
    trailheads = Trailhead.get_all_trailheads_by_park_name(park_name)
    if not trailheads:
        HTTPException(status_code=404, detail=f'There were no trailheads found for {park_name}')
    return trailheads
