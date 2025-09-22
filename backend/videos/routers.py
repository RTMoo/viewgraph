from fastapi import UploadFile, APIRouter, HTTPException
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
    session: SessionDep,
):
    title = video.filename

    if title is None:
        raise HTTPException(status_code=400)

    upload_path = str(MEDIA_DIR / title)

    await save_video(
        video=video,
        upload_path=upload_path,
    )
    duration = get_video_duration(path=upload_path)
    created_video = await save_video_metadata(
        title=title,
        path=upload_path,
        duration=duration,
        session=session,
    )

    return created_video
