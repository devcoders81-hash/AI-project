from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
)

from app.core.config import settings


worker_engine = create_async_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,
    future=True,
)

WorkerSessionLocal = async_sessionmaker(
    bind=worker_engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)