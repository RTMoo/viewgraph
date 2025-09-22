from fastapi import FastAPI
from contextlib import asynccontextmanager

from videos.routers import router as video_router
from statistics.routers import router as stats_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    import all_models  # noqa

    yield


app = FastAPI(lifespan=lifespan)


app.include_router(video_router, prefix="/videos")
app.include_router(stats_router, prefix="/statistics")


@app.get("/ping")
async def ping():
    return "pong"
