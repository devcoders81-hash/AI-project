from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.logging import logger
from app.db.session import AsyncSessionLocal
from app.services.embedding_service import get_embedding_model
from app.db.seed import seed_roles

@asynccontextmanager
async def lifespan(app: FastAPI):

    logger.info("InterviewGPT Started")
    async with AsyncSessionLocal() as db:
        await seed_roles(db)
    yield
    logger.info("Embedding Model Loading")

    get_embedding_model()
    logger.info("Embedding Model Loaded Successfully")
    yield

    logger.info("InterviewGPT Shutdown")