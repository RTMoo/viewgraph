from pathlib import Path
from typing import AsyncGenerator, Annotated
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from fastapi import Depends

ROOT_DIR = Path(__file__).resolve().parent.parent
DATABASE_URL = f"sqlite+aiosqlite:///{ROOT_DIR}/db.sqlite3"

engine = create_async_engine(DATABASE_URL, echo=True)
Session = async_sessionmaker(engine, expire_on_commit=False)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with Session() as session:
        yield session


SessionDep = Annotated[AsyncSession, Depends(get_session)]
