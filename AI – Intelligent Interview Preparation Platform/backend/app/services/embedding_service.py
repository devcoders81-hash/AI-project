from sentence_transformers import SentenceTransformer
from app.core.config import settings


class EmbeddingService:

    def __init__(self):
        self.model = SentenceTransformer(
            settings.EMBEDDING_MODEL
        )

    def generate_embedding(self, text: str) -> list[float]:
        embedding = self.model.encode(
            text,
            normalize_embeddings=True
        )

        return embedding.tolist()

    def generate_embeddings(self, chunks: list[str]) -> list[list[float]]:
        embeddings = self.model.encode(
            chunks,
            normalize_embeddings=True
        )

        return embeddings.tolist()