from sqlalchemy import select

from app.models.role import Role
from app.repositories.base_repository import BaseRepository


class RoleRepository(
    BaseRepository[Role]
):

    def __init__(self, db):
        super().__init__(Role, db)

    async def get_by_name(
        self,
        name: str,
    ) -> Role | None:

        result = await self.db.execute(
            select(Role).where(
                Role.name == name
            )
        )

        return result.scalar_one_or_none()