from videos.models import VideoModel
from statistics.models import VideoStatisticModel
from sqlalchemy.ext.asyncio import AsyncSession


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
    video.statistics = VideoStatisticModel()
    session.add(video)
    await session.commit()

    return video
