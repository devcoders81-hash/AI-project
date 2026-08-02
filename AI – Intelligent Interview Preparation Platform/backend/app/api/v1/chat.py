from fastapi import APIRouter, Depends

from app.dependencies.security import get_current_user
from app.schemas.chat_schema import ChatRequest, ChatResponse

from app.services.chat_service import chat_service

router = APIRouter(prefix="/chat", tags=["Chat"])


@router.post(
    "",
    response_model=ChatResponse,
)
async def chat(request: ChatRequest,current_user=Depends(get_current_user)):

    return chat_service.chat(

        resume_id=request.resume_id,

        question=request.question,

    )