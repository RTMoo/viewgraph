import math
from fastapi import FastAPI, UploadFile
from backend.db import SessionDep
from backend.models import Video
from backend.schemas import VideoSchema
from moviepy import VideoFileClip


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
    upload_path = f"media/{title}"
    
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
