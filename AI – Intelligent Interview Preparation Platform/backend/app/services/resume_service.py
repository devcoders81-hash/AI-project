from uuid import UUID

from fastapi import UploadFile, HTTPException

from app.models.resume import Resume
from app.models.resume import ResumeStatus

from app.repositories.resume_repository import ResumeRepository
from app.schemas.resume_schema import ResumeStatusResponse
from app.services.chunking_service import ChunkingService
from app.services.embedding_service import embedding_service
from app.services.pdf_service import PDFService
from app.services.storage_service import StorageService
from app.services.text_cleaner import TextCleaner
from app.services.vector_store_service import VectorStoreService
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
        resume = await self.repository.get_resume(resume.id)
        print("=" * 70)
        print(f"Resume ID : {resume.id}")
        print(f"File Path : {resume.file_path}")
        print("=" * 70)
        text = PDFService.extract_text(resume.file_path)
        print("=" * 70)
        print(f"Extracted {len(text)} characters")
        clean_text = TextCleaner.clean(text)

        print(f"Clean Length : {len(clean_text)}")
        print("=" * 70)
        chunk_service = ChunkingService()

        chunks = chunk_service.chunk_text(text)
        print("=" * 70)
        print(f"Total Chunks : {len(chunks)}")
        embeddings = embedding_service.generate_embeddings(chunks)

        print(f"Generated {len(embeddings)} embeddings")
        print(len(embeddings[0]))
        print("=" * 70)
        vector_store = VectorStoreService()
        vector_store.save_chunks(

            resume_id=str(resume.id),

            chunks=chunks,

            embeddings=embeddings

        )

        print(f"Saved {len(chunks)} chunks into ChromaDB")
        print("=" * 70)
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

    async def get_resume(
            self,
            resume_id: UUID,
    ):
        resume = await self.repository.get_by_id(
            resume_id
        )

        if resume is None:
            raise HTTPException(
                status_code=404,
                detail="Resume not found",
            )

        return resume

    async def get_all_resumes(
            self,
            user_id: UUID,
    ):
        return await self.repository.get_by_user(user_id)