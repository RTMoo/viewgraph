from typing import TYPE_CHECKING
from db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import JSON, ForeignKey


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
    stats: Mapped[dict] = mapped_column(
        JSON, default=lambda: {i: 0 for i in range(1, 101)}
    )
    diff_stats: Mapped[dict] = mapped_column(
        JSON, default=lambda: {i: 0 for i in range(1, 101)}
    )
