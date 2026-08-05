from fastapi import APIRouter, Depends

from app.dependencies.security import get_current_user
from app.models import User

router = APIRouter(prefix="/user", tags=["User"])
@router.get("/profile")
async def get_profile(
    current_user: User = Depends(get_current_user),
):
    return {
        "first_name": current_user.first_name,
        "last_name": current_user.last_name,
        "email": current_user.email,
        "id": current_user.id,
    }
