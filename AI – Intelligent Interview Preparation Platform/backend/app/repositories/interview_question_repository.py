from typing import Any, Sequence, List
from uuid import UUID

from sqlalchemy import select, Row, func

from app.models.interview_question import InterviewQuestion
from app.repositories.base_repository import BaseRepository


class InterviewQuestionRepository(
    BaseRepository[InterviewQuestion]
):

    def __init__(self, db):
        super().__init__(InterviewQuestion, db)

    async def get_by_interview(
            self,
            interview_id: UUID,
    ) -> list[InterviewQuestion]:
        result = await self.db.execute(
            select(InterviewQuestion)
            .where(
                InterviewQuestion.interview_id == interview_id,
                InterviewQuestion.is_asked.is_(False),
            )
            .order_by(InterviewQuestion.sequence)
        )

        return result.scalars().all()

    # async def get_question(self,interview_id: UUID) -> InterviewQuestion | None:
    #     result = await self.db.execute(
    #         select(InterviewQuestion)
    #         .where(
    #             InterviewQuestion.interview_id == interview_id,
    #         )
    #         .order_by(
    #             InterviewQuestion.sequence
    #         )
    #     )

    async def get_total_question(
        self,
        interview_id: UUID,
    ) -> Any | None:
        result = await self.db.execute(
            select(func.max(InterviewQuestion.sequence)).where(
                InterviewQuestion.interview_id == interview_id
            )
        )

        return result.scalar() or 0

    async def get_question(
        self,
        interview_id: UUID,
        question_number: int,
    ) -> InterviewQuestion | None:

        result = await self.db.execute(
            select(InterviewQuestion)
            .where(
                InterviewQuestion.interview_id == interview_id,
                InterviewQuestion.question_number == question_number,
            )
        )

        return result.scalar_one_or_none()

    async def create_many(
        self,
        questions: list[InterviewQuestion],
    ) -> list[InterviewQuestion]:

        self.db.add_all(questions)

        await self.db.commit()

        for question in questions:
            await self.db.refresh(question)

        return questions

    async def update(
        self,
        question: InterviewQuestion,
    ) -> InterviewQuestion:

        self.db.add(question)

        await self.db.commit()

        await self.db.refresh(question)

        return question

    async def get_unanswered_questions(
        self,
        interview_id: UUID,
    ) -> list[InterviewQuestion]:

        result = await self.db.execute(
            select(InterviewQuestion)
            .where(
                InterviewQuestion.interview_id == interview_id,
                InterviewQuestion.user_answer.is_(None),
            )
            .order_by(
                InterviewQuestion.question_number
            )
        )

        return result.scalars().all()

    async def get_answered_questions(
        self,
        interview_id: UUID,
    ) -> list[InterviewQuestion]:

        result = await self.db.execute(
            select(InterviewQuestion)
            .where(
                InterviewQuestion.interview_id == interview_id,
                InterviewQuestion.user_answer.is_not(None),
            )
            .order_by(
                InterviewQuestion.question_number
            )
        )

        return result.scalars().all()

    async def get_by_sequence(
            self,
            interview_id,
            sequence,
    ):
        result = await self.db.execute(

            select(InterviewQuestion)

            .where(
                InterviewQuestion.id == interview_id,
                InterviewQuestion.sequence == sequence,
            )

        )

        return result.scalar_one_or_none()

    async def get_question_by_sequence(
            self,
            interview_id,
            sequence,
    ):
        result = await self.db.execute(
            select(InterviewQuestion)
            .where(
                InterviewQuestion.interview_id == interview_id,
                InterviewQuestion.sequence == sequence,
            )
        )

        return result.scalar_one_or_none()

    async def get_next_unasked_question(
            self,
            interview_id,
    ):
        result = await self.db.execute(
            select(InterviewQuestion)
            .where(
                InterviewQuestion.interview_id == interview_id,
                InterviewQuestion.is_asked == False,
            )
            .order_by(InterviewQuestion.sequence)
            .limit(1)
        )

        return result.scalar_one_or_none()

    async def mark_as_asked(
            self,
            question: InterviewQuestion,
    ):
        question.is_asked = True

        await self.db.commit()
        await self.db.refresh(question)