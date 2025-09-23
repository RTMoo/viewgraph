from pydantic import BaseModel


class Timecodes(BaseModel):
    start: float
    end: float


class Interval(BaseModel):
    start: int
    end: int


class WatchedTimecodes(BaseModel):
    timecodes: list[Timecodes]
