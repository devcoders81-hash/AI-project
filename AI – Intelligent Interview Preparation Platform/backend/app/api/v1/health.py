from fastapi import APIRouter
from sqlalchemy import text
from app.common.responses import success_response
from app.dependencies.database import Database
router = APIRouter()


@router.get(
    "/health",
    tags=["Health"],
)
async def health(db:Database):
    await db.execute(text("SELECT 1"))

    return success_response(
        {
            "status": "healthy"
        }
    )