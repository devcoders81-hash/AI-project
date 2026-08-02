from datetime import datetime, timedelta, timezone

from app.models.refresh_token import RefreshToken
from app.repositories.refresh_token_repository import (
    RefreshTokenRepository,
)
from app.core.config import settings


class RefreshTokenService:

    def __init__(self, repository: RefreshTokenRepository):
        self.repository = repository

    async def create(
        self,
        user_id,
        token: str,
    ):

        refresh = RefreshToken(
            user_id=user_id,
            token=token,
            expires_at=datetime.now(
                timezone.utc
            )
            + timedelta(
                days=settings.REFRESH_TOKEN_EXPIRE_DAYS
            ),
        )

        return await self.repository.create(refresh)

    async def validate(
        self,
        token: str,
    ):

        refresh = await self.repository.get_token(token)

        if not refresh:
            return None

        if refresh.revoked:
            return None

        if refresh.expires_at < datetime.now(
            timezone.utc
        ):
            return None

        return refresh

    async def revoke(
        self,
        token: str,
    ):
        return await self.repository.revoke_token(token)