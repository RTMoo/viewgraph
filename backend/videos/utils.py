import math

from fastapi import UploadFile
from moviepy import VideoFileClip


def get_video_duration(path: str) -> int:
    clip = VideoFileClip(path)
    duration = math.ceil(clip.duration)

    return duration


async def save_video(video: UploadFile, upload_path: str):
    contents = await video.read()

    with open(upload_path, "wb") as file:
        file.write(contents)
