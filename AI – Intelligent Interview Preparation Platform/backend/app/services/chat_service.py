from app.schemas.chat_schema import ChatRequest, ChatResponse
from app.services.embedding_service import EmbeddingService
from app.services.llm_service import llm_service
from app.services.vector_store_service import vector_store_service


class ChatService:

    def __init__(self):
        self.embedding_service = EmbeddingService()

    def chat(
            self,
            resume_id: str,
            question: str,
    ):

        # Step 1: Generate query embedding
        query_embedding = self.embedding_service.generate_query_embedding(
            question
        )

        # Step 2: Search ChromaDB
        results = vector_store_service.search(
            embedding=query_embedding,
            top_k=5,
            resume_id=str(resume_id)   # remove if you haven't added filtering yet
        )

        # Step 3: Extract documents
        documents = results["documents"][0]

        # Step 4: Build context
        context = "\n\n".join(documents)

        # Step 5: Ask Groq LLM
        answer = llm_service.generate_answer(
            question=question,
            context=context
        )

        # Step 6: Build sources
        sources = []

        distances = results["distances"][0]

        for document, distance in zip(documents, distances):
            score = max(0.0, min(1.0, 1 - distance))
            sources.append(
                {
                    "text": document,
                    "score": round(score, 3)
                }
            )

        # Step 7: Return response
        return ChatResponse(
            answer=answer,
            sources=sources
        )


chat_service = ChatService()