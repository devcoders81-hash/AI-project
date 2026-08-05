from sentence_transformers import SentenceTransformer
from app.core.config import settings

_model = None
def get_embedding_model():
    global _model
    if _model is None:
        print("Loading Embedding Model")
        _model = SentenceTransformer(
            settings.EMBEDDING_MODEL
        )
    return _model
class EmbeddingService:



    def __init__(self):
        self.model = get_embedding_model()



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

    def generate_query_embedding(
            self,
            question: str
    ) -> list[float]:
        embedding = self.model.encode(
            question,
            normalize_embeddings=True
        )

        return embedding.tolist()
embedding_service = EmbeddingService()