from statistics.schemas import WatchedTimecodes
from statistics.services import get_video_stat, update_diff_chunks
from statistics.utils import get_chunks_from_timecodes

from db import SessionDep
from fastapi import APIRouter

router = APIRouter()


@router.post(
    "/set_chunks",
)
async def set_video_stats_chunks(
    timecodes: WatchedTimecodes,
    video_id: int,
    session: SessionDep,
):
    stat = await get_video_stat(
        video_id=video_id,
        session=session,
    )

    chunks = get_chunks_from_timecodes(
        timecodes=timecodes.timecodes,
        chunk_size=stat.chunk_size,
    )

    diff_chunks = await update_diff_chunks(
        chunks=chunks,
        stat=stat,
        session=session,
    )

    return diff_chunks
