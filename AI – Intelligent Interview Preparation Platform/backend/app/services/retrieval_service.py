from app.services.embedding_service import EmbeddingService
from app.services.vector_store_service import vector_store_service


class RetrievalService:

    def __init__(self):

        self.embedding_service = EmbeddingService()

    def retrieve(
        self,
        resume_id: str,
        question: str,
        top_k: int = 5,
    ):

        query_embedding = self.embedding_service.generate_query_embedding(
            question
        )

        results = vector_store_service.search(

            resume_id=resume_id,

            embedding=query_embedding,

            top_k=top_k,

        )

        documents = results["documents"][0]

        distances = results["distances"][0]

        chunks = []

        for document, distance in zip(documents, distances):

            chunks.append(
                {
                    "text": document,
                    "score": round(1 - distance, 3),
                }
            )

        return chunks


retrieval_service = RetrievalService()