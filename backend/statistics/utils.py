import math
from statistics.schemas import Interval, Timecodes

from fastapi import HTTPException
from settings import CHUNKS_QUANTITY


def get_chunks_from_timecodes(
    timecodes: list[Timecodes],
    chunk_size: float,
) -> list[Interval]:
    duration = chunk_size * CHUNKS_QUANTITY

    for timecode in timecodes:
        start, end = timecode.start, timecode.end
        if start < 0 or end < 0:
            raise HTTPException(
                status_code=400,
                detail="Отрицательный таймкод",
            )
        if start > duration or end > duration:
            raise HTTPException(
                status_code=400,
                detail="Таймкод выходит за границы видео",
            )
        if start >= end:
            raise HTTPException(
                status_code=400,
                detail=f"Некорректный таймкод: {start=} >= {end=}",
            )

    chunk_intervals = [
        Interval(
            start=math.floor(timecode.start / chunk_size),
            end=math.ceil(timecode.end / chunk_size),
        )
        for timecode in timecodes
    ]

    return merge_intervals(chunk_intervals)


def merge_intervals(intervals: list[Interval]) -> list[Interval]:
    intervals.sort(key=lambda x: x.start)
    merged = [intervals[0]]

    for interval in intervals[1:]:
        last_start, last_end = merged[-1].start, merged[-1].end
        curr_start, curr_end = interval.start, interval.end

        if curr_start <= last_end + 1:  # пересекается или соприкасается
            merged[-1] = Interval(start=last_start, end=max(last_end, curr_end))
        else:
            merged.append(Interval(start=curr_start, end=curr_end))

    return merged
