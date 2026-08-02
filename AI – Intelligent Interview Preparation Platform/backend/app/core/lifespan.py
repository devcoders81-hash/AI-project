from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.logging import logger
from app.db.seed import seed_roles
from app.db.session import AsyncSessionLocal


@asynccontextmanager
async def lifespan(app: FastAPI):

    logger.info("InterviewGPT Started")
    async with AsyncSessionLocal() as db:
        await seed_roles(db)

    yield

    logger.info("InterviewGPT Shutdown")