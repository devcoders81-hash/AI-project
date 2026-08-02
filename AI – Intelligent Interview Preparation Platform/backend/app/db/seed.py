from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.role import Role


async def seed_roles(db: AsyncSession):

    result = await db.execute(
        select(Role).where(Role.name == "USER")
    )

    user_role = result.scalar_one_or_none()

    if not user_role:
        db.add(Role(name="USER"))

    result = await db.execute(
        select(Role).where(Role.name == "ADMIN")
    )

    admin_role = result.scalar_one_or_none()

    if not admin_role:
        db.add(Role(name="ADMIN"))

    await db.commit()