import math
from pathlib import Path
from fastapi import FastAPI, UploadFile
from db import SessionDep
from models import Video
from schemas import VideoSchema
from moviepy import VideoFileClip

ROOT_DIR = Path(__file__).resolve().parent.parent
MEDIA_DIR = ROOT_DIR / "media"

app = FastAPI()


@app.get("/ping")
async def ping():
    return "pong"


@app.post(
    "/upload",
    response_model=VideoSchema,
)
async def upload_video(
    video: UploadFile,
    session: SessionDep,
):
    title = video.filename
    contents = await video.read()
    upload_path = str(MEDIA_DIR / title)
    
    with open(upload_path, "wb") as file:
        file.write(contents)
    

    clip = VideoFileClip(upload_path)
    
    uploaded_video = Video(
        title=title,
        duration=math.ceil(clip.duration),
        path=upload_path,
    )
    session.add(uploaded_video)
    await session.commit()

    return uploaded_video
