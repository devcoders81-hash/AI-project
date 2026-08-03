from uuid import UUID

from sqlalchemy import select

from app.models.interview_message import InterviewMessage
from app.repositories.base_repository import BaseRepository


class InterviewMessageRepository(
    BaseRepository[InterviewMessage]
):

    def __init__(self, db):
        super().__init__(
            InterviewMessage,
            db
        )

    async def get_messages(
        self,
        interview_id: UUID,
    ):

        result = await self.db.execute(
            select(InterviewMessage)
            .where(
                InterviewMessage.interview_id == interview_id
            )
            .order_by(
                InterviewMessage.created_at
            )
        )

        return result.scalars().all()