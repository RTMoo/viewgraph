from typing import TYPE_CHECKING
from db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import JSON, ForeignKey
from settings import CHUNKS_QUANTITY
from sqlalchemy.ext.mutable import MutableDict


if TYPE_CHECKING:
    from videos.models import VideoModel


class VideoStatisticModel(Base):
    __tablename__ = "video_statistic"

    video_id: Mapped[int] = mapped_column(
        ForeignKey("video.id"),
        unique=True,
    )
    video: Mapped["VideoModel"] = relationship(
        back_populates="statistics",
        single_parent=True,
    )
    chunks: Mapped[dict[str, int]] = mapped_column(
        MutableDict.as_mutable(JSON),
        default=lambda: {str(i): 0 for i in range(CHUNKS_QUANTITY)},
    )
    diff_chunks: Mapped[dict[str, int]] = mapped_column(
        MutableDict.as_mutable(JSON),
        default=lambda: {str(i): 0 for i in range(CHUNKS_QUANTITY)},
    )
    chunk_size: Mapped[float]
