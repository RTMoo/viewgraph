from pydantic import BaseModel


class Interval(BaseModel):
    start: int
    end: int


class VideoViewStats(BaseModel):
    intervals: list[Interval]
