from statistics.models import VideoStatisticModel
from statistics.schemas import Interval

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


async def get_video_stat(
    video_id: int,
    session: AsyncSession,
) -> VideoStatisticModel:
    stmt = select(VideoStatisticModel).where(VideoStatisticModel.video_id == video_id)
    result = await session.execute(stmt)
    stat = result.scalar_one()

    return stat


async def update_diff_chunks(
    stat: VideoStatisticModel,
    chunks: list[Interval],
    session: AsyncSession,
) -> dict[str, int]:
    for chunk in chunks:
        stat.diff_chunks[str(chunk.start)] += 1
        stat.diff_chunks[str(chunk.end)] -= 1

    session.add(stat)
    await session.commit()

    return stat.diff_chunks
