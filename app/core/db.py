from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from app.core.settings import settings

engine = create_async_engine(settings.database_url)
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    """Base SQLAlchemy model."""


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    """Provides an asynchronous session generator for interacting with the database."""
    async with AsyncSessionLocal() as async_session:
        yield async_session
