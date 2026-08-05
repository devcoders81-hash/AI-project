from uuid import UUID

from sqlalchemy import select

from app.models.interview import Interview
from app.repositories.base_repository import BaseRepository


class InterviewRepository(BaseRepository[Interview]):

    def __init__(self, db):
        super().__init__(Interview, db)

    async def get_by_resume(
        self,
        resume_id: UUID,
    ):
        result = await self.db.execute(
            select(Interview).where(
                Interview.resume_id == resume_id
            )
        )

        return result.scalars().all()

    async def get_by_resume_user_id(
        self,
        resume_id: UUID,
            user_id: UUID,
    ):
        result = await self.db.execute(
            select(Interview).where(
                Interview.resume_id == resume_id,
                Interview.user_id == user_id
            )
        )

        return result.scalar_one_or_none()