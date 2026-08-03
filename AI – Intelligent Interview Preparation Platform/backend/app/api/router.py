from fastapi import APIRouter

from app.api.v1.auth import router as auth_router
from app.api.v1.resume import router as resume_router
from app.api.v1.chat import router as chat_router
from app.api.v1.interview import router as interview_router
api_router = APIRouter()

api_router.include_router(auth_router)
api_router.include_router(resume_router)
api_router.include_router(chat_router)
api_router.include_router(interview_router)