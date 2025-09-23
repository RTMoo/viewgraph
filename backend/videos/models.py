from typing import TYPE_CHECKING

from db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from statistics.models import VideoStatisticModel


class VideoModel(Base):
    __tablename__ = "video"

    title: Mapped[str]
    duration: Mapped[int]
    path: Mapped[str]
    views_count: Mapped[int] = mapped_column(default=0)

    statistics: Mapped["VideoStatisticModel"] = relationship(
        back_populates="video",
        uselist=False,
    )
