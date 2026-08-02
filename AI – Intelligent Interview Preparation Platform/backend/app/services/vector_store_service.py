from uuid import uuid4

import chromadb

from app.core.config import settings


class VectorStoreService:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path=settings.CHROMA_PATH
        )

        self.collection = self.client.get_or_create_collection(
            name=settings.CHROMA_COLLECTION,
            metadata={
                "hnsw:space": "cosine"
            }
        )

    def save_chunks(
        self,
        resume_id: str,
        chunks: list[str],
        embeddings: list[list[float]]
    ):

        ids = []
        metadatas = []

        for index, chunk in enumerate(chunks):

            ids.append(str(uuid4()))

            metadatas.append({
                "resume_id": resume_id,
                "chunk_index": index
            })

        self.collection.add(
            ids=ids,
            documents=chunks,
            embeddings=embeddings,
            metadatas=metadatas
        )

    def search(
            self,
            resume_id: str,
            embedding: list[float],
            top_k: int = 5,
    ):
        return self.collection.query(

            query_embeddings=[embedding],

            n_results=top_k,

            where={
                "resume_id": resume_id
            }

        )


vector_store_service = VectorStoreService()