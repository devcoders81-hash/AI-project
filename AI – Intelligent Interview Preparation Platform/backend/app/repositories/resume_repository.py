from uuid import UUID

from sqlalchemy import select

from app.models.resume import Resume
from app.repositories.base_repository import BaseRepository


class ResumeRepository(BaseRepository[Resume]):

    def __init__(self, db):
        super().__init__(Resume, db)

    async def get_by_user(
        self,
        user_id: UUID,
    ):

        result = await self.db.execute(
            select(Resume).where(
                Resume.user_id == user_id
            )
        )

        return result.scalars().all()

    async def get_resume(
        self,
        resume_id: UUID,
    ):

        return await self.get_by_id(resume_id)
