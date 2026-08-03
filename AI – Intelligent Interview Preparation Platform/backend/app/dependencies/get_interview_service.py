from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.repositories.interview_answer_repository import InterviewAnswerRepository
from app.repositories.interview_repository import InterviewRepository
from app.repositories.interview_question_repository import (
    InterviewQuestionRepository,
)
from app.services.interview_service import InterviewService


async def get_interview_service(
    db: AsyncSession = Depends(get_db),
) -> InterviewService:

    interview_repository = InterviewRepository(db)
    answer_repo=InterviewAnswerRepository(db)

    question_repository = InterviewQuestionRepository(db)

    return InterviewService(
        repository=interview_repository,
        answer_repo=answer_repo,
        question_repository=question_repository,
    )