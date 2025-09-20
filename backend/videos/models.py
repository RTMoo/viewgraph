from sqlalchemy.orm import Mapped, mapped_column
from backend.db import Base


class VideoModel(Base):
    __tablename__ = "video"

    title: Mapped[str]
    duration: Mapped[int]
    path: Mapped[str]
    views_count: Mapped[int] = mapped_column(default=0)
