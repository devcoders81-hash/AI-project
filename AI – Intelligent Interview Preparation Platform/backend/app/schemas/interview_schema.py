from uuid import UUID
from typing import Optional

from pydantic import BaseModel


# ============================================================
# Create Interview
# ============================================================

class InterviewCreateRequest(BaseModel):
    resume_id: UUID
    role: str
    experience: int
    total_questions: int = 10


class InterviewResponse(BaseModel):
    interview_id: UUID
    status: str


# ============================================================
# Start Interview
# ============================================================

class StartInterviewResponse(BaseModel):
    interview_id: UUID
    question_number: int
    question: str


# ============================================================
# Answer Question
# ============================================================

class AnswerQuestionRequest(BaseModel):
    interview_id: UUID
    answer: str


class AnswerQuestionResponse(BaseModel):
    interview_completed: bool
    next_question: Optional[str] = None
    feedback: str
    score: int


# ============================================================
# Interview Result
# ============================================================

class InterviewResultResponse(BaseModel):
    interview_id: UUID
    score: int
    total_questions: int
    status: str

from uuid import UUID

from pydantic import BaseModel


class InterviewQuestionResponse(BaseModel):

    id: UUID

    sequence: int

    question: str

    difficulty: str

    class Config:
        from_attributes = True

from pydantic import BaseModel


class InterviewAnswerRequest(BaseModel):

    answer: str