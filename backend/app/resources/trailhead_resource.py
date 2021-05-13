from fastapi import APIRouter, HTTPException

from .resource_models import Trailhead_Model

from models.trailhead import Trailhead

router = APIRouter(
    prefix="/trailhead",
    tags=["booking"],
)


@router.get("/{trailhead_id}")
async def get_trailhead(trailhead_id: int):
    trailhead = Trailhead.get_by_id(trailhead_id)
    if not trailhead:
        raise HTTPException(status_code=404, detail='No trailhead found for that ID.')
    return trailhead


@router.get("/")
async def get_all_trailheads():
    return Trailhead.get_all_trailheads()



