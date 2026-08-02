from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.repositories.role_repository import RoleRepository
from app.repositories.refresh_token_repository import RefreshTokenRepository

from app.security.hashing import PasswordHasher
from app.security.jwt import JWTService

from app.schemas.auth_schema import (
    RegisterRequest,
    LoginRequest,
)

from app.schemas.token_schema import TokenResponse

from app.common.exceptions import (
    UserAlreadyExistsException,
    InvalidCredentialsException, InvalidRefreshTokenException,
)
from app.services.refresh_token_service import RefreshTokenService


class AuthService:

    def __init__(
        self,
        db: AsyncSession,
    ):
        self.user_repository = UserRepository(db)
        self.role_repository = RoleRepository(db)
        self.refresh_repository = RefreshTokenRepository(db)

    async def register(
        self,
        request: RegisterRequest,
    ):

        exists = await self.user_repository.exists_by_email(
            request.email
        )

        if exists:
            raise UserAlreadyExistsException()

        role = await self.role_repository.get_by_name(
            "USER"
        )

        user = User(
            first_name=request.first_name,
            last_name=request.last_name,
            email=request.email,
            password=PasswordHasher.hash_password(
                request.password
            ),
            role_id=role.id,
        )

        user= await self.user_repository.create(user)
        return (
            user.first_name,
            user.last_name,
            user.email,
        )

    async def login(
        self,
        request: LoginRequest,
    ) -> TokenResponse:

        user = await self.user_repository.get_by_email(
            request.email
        )

        if (
            not user
            or not PasswordHasher.verify_password(
                request.password,
                user.password,
            )
        ):
            raise InvalidCredentialsException()

        access_token = JWTService.create_access_token(
            {
                "sub": str(user.id),
                "email": user.email,
            }
        )

        refresh_token = JWTService.create_refresh_token(
            {
                "sub": str(user.id),
            }
        )

        refresh_service = RefreshTokenService(
            self.refresh_repository
        )

        await refresh_service.create(
            user.id,
            refresh_token,
        )

        return TokenResponse(
            access_token=access_token,
            refresh_token=refresh_token,
        )

    async def refresh(
            self,
            refresh_token: str,
    ):

        service = RefreshTokenService(
            self.refresh_repository
        )

        stored = await service.validate(refresh_token)

        if not stored:
            raise InvalidRefreshTokenException()

        payload = JWTService.decode_token(
            refresh_token
        )

        access = JWTService.create_access_token(
            {
                "sub": payload["sub"]
            }
        )

        return TokenResponse(
            access_token=access,
            refresh_token=refresh_token,
        )

    async def logout(
            self,
            refresh_token: str,
    ):

        service = RefreshTokenService(
            self.refresh_repository
        )

        await service.revoke(refresh_token)