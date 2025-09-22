from fastapi import APIRouter
from db import SessionDep
from statistics.schemas import WatchedIntervals


router = APIRouter()


@router.post(
    "/set_chunks",
)
async def set_video_view_chunks(
    stats: WatchedIntervals,
    session: SessionDep,
):
    pass
