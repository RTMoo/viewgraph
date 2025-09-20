from fastapi import FastAPI
from videos.routers import router as video_router


app = FastAPI()
app.include_router(video_router, prefix="/videos")


@app.get("/ping")
async def ping():
    return "pong"
