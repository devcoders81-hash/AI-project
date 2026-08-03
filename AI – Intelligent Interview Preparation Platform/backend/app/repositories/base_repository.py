from typing import Generic, TypeVar, Type
from uuid import UUID

from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.base import Base

ModelType = TypeVar("ModelType", bound=Base)


class BaseRepository(Generic[ModelType]):

    def __init__(
        self,
        model: Type[ModelType],
        db: AsyncSession,
    ):
        self.model = model
        self.db = db

    async def create(
        self,
        obj: ModelType,
    ) -> ModelType:

        self.db.add(obj)
        await self.db.commit()
        await self.db.refresh(obj)

        return obj
    async def create_all(self,obj:list[ModelType]) -> list[ModelType]:
        self.db.add_all(obj)
        await self.db.commit()
        return obj

    async def get_by_id(
        self,
        obj_id: UUID,
    ) -> ModelType | None:

        result = await self.db.execute(
            select(self.model).where(
                self.model.id == obj_id
            )
        )

        return result.scalar_one_or_none()

    async def get_all(self):

        result = await self.db.execute(
            select(self.model)
        )

        return result.scalars().all()

    async def delete(
        self,
        obj_id: UUID,
    ) -> bool:

        result = await self.db.execute(
            delete(self.model).where(
                self.model.id == obj_id
            )
        )

        await self.db.commit()

        return result.rowcount > 0