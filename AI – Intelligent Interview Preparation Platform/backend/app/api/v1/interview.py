from uuid import UUID

from fastapi import APIRouter, Depends

from app.dependencies.security import get_current_user
from app.dependencies.get_interview_service import get_interview_service
from app.models import User

from app.schemas.interview_schema import (
    InterviewCreateRequest,
    InterviewResponse,
    AnswerQuestionRequest,
    AnswerQuestionResponse, InterviewQuestionResponse, InterviewAnswerRequest,
)

from app.services.interview_service import InterviewService

router = APIRouter(
    prefix="/interviews",
    tags=["Interview"],
)


@router.post(
    "",
    response_model=InterviewResponse,
)
async def create_interview(
    request: InterviewCreateRequest,
    user=Depends(get_current_user),
    service: InterviewService = Depends(get_interview_service),
):
    return await service.create_interview(
        user=user,
        request=request,
    )


@router.post(
    "/{interview_id}/answer"
)
async def submit_answer(
    interview_id: UUID,
    request: InterviewAnswerRequest,
    service: InterviewService = Depends(get_interview_service),
):
    print(f"interview_id: {interview_id}")
    print(f"request: {request.answer}")
    return await service.submit_answer(
        interview_id,
        request.answer,
    )


@router.get(
    "/{interview_id}/question"
)
async def get_next_question(
    interview_id: UUID,
        current_user:User=Depends(get_current_user),
    service: InterviewService = Depends(get_interview_service),
):
    try:
        return await service.get_question(interview_id,current_user.id)
    except Exception as ex:
        print(ex)
        return {
            'message':ex,
            'status':False,
        }
