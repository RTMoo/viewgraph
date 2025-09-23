from statistics.models import VideoStatisticModel

from settings import CHUNKS_QUANTITY
from sqlalchemy.ext.asyncio import AsyncSession
from videos.models import VideoModel


async def save_video_metadata(
    title: str,
    duration: int,
    path: str,
    session: AsyncSession,
) -> VideoModel:
    video = VideoModel(
        title=title,
        duration=duration,
        path=path,
    )
    chunk_size = duration / CHUNKS_QUANTITY
    video.statistics = VideoStatisticModel(
        chunk_size=chunk_size,
    )
    session.add(video)
    await session.commit()

    return video
