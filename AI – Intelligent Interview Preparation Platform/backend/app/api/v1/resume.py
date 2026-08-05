from uuid import UUID

from fastapi import APIRouter
from fastapi import Depends
from fastapi import UploadFile
from fastapi import File

from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies.database import get_db
from app.dependencies.security import get_current_user
from app.models import User

from app.repositories.resume_repository import ResumeRepository
from app.schemas.resume_schema import ResumeStatusResponse
from app.services.resume_service import ResumeService


router = APIRouter(
    prefix="/resumes",
    tags=["Resume"],
)


@router.post("/upload")
async def upload_resume(

    file: UploadFile = File(...),

    db: AsyncSession = Depends(get_db),

    current_user=Depends(get_current_user),
):

    repository = ResumeRepository(db)

    service = ResumeService(repository)

    return await service.upload_resume(
        current_user,
        file,
    )

@router.get(
    "/{resume_id}/status",
    response_model=ResumeStatusResponse,
)
async def get_resume_status(
    resume_id: UUID,
    current_user=Depends(get_current_user),
    db=Depends(get_db),
):

    repository = ResumeRepository(db)

    service = ResumeService(repository)

    return await service.get_resume_status(resume_id)

# @router.get("/{resume_id}")
# async def get_resume_by_id(
#     resume_id: UUID,
#     current_user=Depends(get_current_user),
#     service: ResumeService = Depends(get_current_user),
# ):
#     return await service.get_resume(resume_id)

@router.get("/all")
async def get_resume(
        current_user:User=Depends(get_current_user),
        db=Depends(get_db),
):
    repository = ResumeRepository(db)
    service= ResumeService(repository)
    return await service.get_all_resumes(current_user.id)