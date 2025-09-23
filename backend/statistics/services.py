from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from statistics.models import VideoStatisticModel


async def get_video_stat(
    video_id: int,
    session: AsyncSession,
) -> VideoStatisticModel:
    stmt = select(VideoStatisticModel).where(VideoStatisticModel.video_id == video_id)
    result = await session.execute(stmt)
    stat = result.scalar_one()

    return stat
