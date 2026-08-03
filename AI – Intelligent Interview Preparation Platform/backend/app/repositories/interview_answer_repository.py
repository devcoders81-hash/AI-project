from sqlalchemy import select

from app.models.interview_answer import InterviewAnswer
from app.repositories.base_repository import BaseRepository


class InterviewAnswerRepository(BaseRepository[InterviewAnswer]):

    def __init__(self, db):
        super().__init__(InterviewAnswer, db)
