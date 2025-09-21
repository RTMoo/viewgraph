from fastapi import FastAPI
from videos.routers import router as video_router
from statistics.routers import router as stats_router


app = FastAPI()
app.include_router(video_router, prefix="/videos")
app.include_router(stats_router, prefix="/statistics")


@app.get("/ping")
async def ping():
    return "pong"
