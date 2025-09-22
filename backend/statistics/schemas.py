from pydantic import BaseModel


class Interval(BaseModel):
    start: int
    end: int


class WatchedIntervals(BaseModel):
    intervals: list[Interval]
