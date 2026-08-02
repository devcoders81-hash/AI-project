from jose import JWTError
from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies.database import get_db
from app.repositories.user_repository import UserRepository
from app.security.auth import oauth2_scheme
from app.security.jwt import JWTService


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db),
):

    try:
        payload = JWTService.decode_token(token)
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )

    repository = UserRepository(db)

    user = await repository.get_by_id(
        payload["sub"]
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="User not found",
        )

    return user