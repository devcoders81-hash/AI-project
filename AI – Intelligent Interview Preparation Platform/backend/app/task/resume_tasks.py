from app.repositories.resume_repository import ResumeRepository
from app.services.chunking_service import ChunkingService
from app.services.embedding_service import EmbeddingService
from app.services.text_cleaner import TextCleaner
from app.services.vector_store_service import vector_store_service
print("resume_tasks imported")
from app.worker.celery_app import celery
from app.db.session import AsyncSessionLocal
from app.services.pdf_service import PDFService
import asyncio


@celery.task(name="process_resume")
def process_resume(resume_id: str):
    import asyncio

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    try:
        loop.run_until_complete(_process_resume(resume_id))
    finally:
        loop.close()


async def _process_resume(resume_id: str):
    async with AsyncSessionLocal() as db:

        try:
            repository = ResumeRepository(db=db)
            embedding_service = EmbeddingService()

            resume = await repository.get_resume(resume_id)
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
            vector_store_service.save_chunks(

                resume_id=str(resume.id),

                chunks=chunks,

                embeddings=embeddings

            )

            print(f"Saved {len(chunks)} chunks into ChromaDB")
            print("=" * 70)

        finally:
            await db.close()

        # Step 2
        # Update Status -> PROCESSING

        # Step 3
        # Extract Text

        # Step 4
        # Chunk Text

        # Step 5
        # Generate Embeddings

        # Step 6
        # Save Chunks

        # Step 7
        # Update Status -> COMPLETED