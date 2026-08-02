from pydantic import BaseModel


class ChatRequest(BaseModel):
    resume_id: str
    question: str


class RetrievedChunk(BaseModel):
    text: str
    score: float


class ChatResponse(BaseModel):
    answer: str
    sources: list[RetrievedChunk]