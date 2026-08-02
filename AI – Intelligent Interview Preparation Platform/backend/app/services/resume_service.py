from uuid import UUID

from fastapi import UploadFile, HTTPException

from app.models.resume import Resume
from app.models.resume import ResumeStatus

from app.repositories.resume_repository import ResumeRepository
from app.schemas.resume_schema import ResumeStatusResponse
from app.services.storage_service import StorageService
from app.task.resume_tasks import process_resume
from app.utils.file_utils import FileValidator


class ResumeService:

    def __init__(
        self,
        repository: ResumeRepository,
    ):
        self.repository = repository
        self.storage = StorageService()

    async def upload_resume(
        self,
        user,
        file: UploadFile,
    ):

        await FileValidator.validate(file)

        stored_name, path = await self.storage.save_file(file)

        resume = Resume(

            user_id=user.id,

            original_filename=file.filename,

            stored_filename=stored_name,

            file_path=path,

            mime_type=file.content_type,

            file_size=file.size,

            status=ResumeStatus.UPLOADED,
        )

        resume= await self.repository.create(resume)
        process_resume.delay(
            str(resume.id)
        )
        return resume

    async def get_resume_status(
            self,
            resume_id: UUID,
    ) :
        resume = await self.repository.get_resume(resume_id)

        if resume is None:
            raise HTTPException(
                status_code=404,
                detail="Resume not found"
            )

        return ResumeStatusResponse(
            resume_id=resume.id,
            status=resume.status
        )