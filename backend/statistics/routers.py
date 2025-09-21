from fastapi import APIRouter
from db import SessionDep
from statistics.schemas import VideoViewStats


router = APIRouter()


@router.post(
    "/set_moments",
)
async def set_user_view_moments(
    stats: VideoViewStats,
    session: SessionDep,
):
    for interval in stats.intervals:
        print(interval.start, interval.end)

    return 0
