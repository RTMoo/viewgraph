from fastapi import UploadFile, APIRouter
from db import SessionDep
from videos.schemas import VideoSchema
from settings import MEDIA_DIR
from videos.services import save_video_metadata
from videos.utils import get_video_duration, save_video


router = APIRouter()


@router.post(
    "/upload",
    response_model=VideoSchema,
)
async def upload_video(
    video: UploadFile,
    title: str,
    session: SessionDep,
):
    upload_path = str(MEDIA_DIR / title)
    duration = get_video_duration(path=upload_path)
    await save_video(
        video=video,
        upload_path=upload_path,
    )

    created_video = await save_video_metadata(
        title=title,
        path=upload_path,
        duration=duration,
        session=session,
    )

    return created_video
