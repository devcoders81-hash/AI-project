from sqlalchemy import select

from app.models.refresh_token import RefreshToken
from app.repositories.base_repository import BaseRepository


class RefreshTokenRepository(
    BaseRepository[RefreshToken]
):

    def __init__(self, db):
        super().__init__(RefreshToken, db)

    async def get_token(
        self,
        token: str,
    ) -> RefreshToken | None:

        result = await self.db.execute(
            select(RefreshToken).where(
                RefreshToken.token == token
            )
        )

        return result.scalar_one_or_none()

    async def revoke_token(
        self,
        token: str,
    ):

        refresh = await self.get_token(token)

        if refresh:
            refresh.revoked = True
            await self.db.commit()

        return refresh