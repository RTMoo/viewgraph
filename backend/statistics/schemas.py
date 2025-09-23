from pydantic import BaseModel


class Interval(BaseModel):
    start: float
    end: float


class WatchedIntervals(BaseModel):
    intervals: list[Interval]
