from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True, index=True)


class Video(Base):
    __tablename__ = "video"

    title: Mapped[str]
    duration: Mapped[int | None]
    path: Mapped[str | None]
