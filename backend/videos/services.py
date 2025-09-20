from .models import VideoModel
from sqlalchemy.ext.asyncio import AsyncSession


async def save_video_metadata(
    title: str,
    duration: int,
    path: str,
    session: AsyncSession,
) -> VideoModel:
    created_video = VideoModel(
        title=title,
        duration=duration,
        path=path,
    )
    session.add(created_video)
    await session.commit()

    return created_video
