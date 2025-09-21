from settings import DATABASE_URL
from typing import AsyncGenerator, Annotated
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from fastapi import Depends
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


engine = create_async_engine(DATABASE_URL, echo=True)
Session = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True, index=True)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with Session() as session:
        yield session


SessionDep = Annotated[AsyncSession, Depends(get_session)]
