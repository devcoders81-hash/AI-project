import json

from app.services.embedding_service import EmbeddingService
from app.services.vector_store_service import vector_store_service
from app.services.llm_service import llm_service


class QuestionGenerator:

    def __init__(self):
        self.embedding = EmbeddingService()

    def generate_questions(
        self,
        resume_id: str,
        role: str,
        experience: int,
        total_questions: int,
    ):

        embedding = self.embedding.generate_query_embedding(
            f"{role} skills experience projects"
        )

        results = vector_store_service.search(
            resume_id=resume_id,
            embedding=embedding,
            top_k=8,
        )

        if (
            not results
            or not results["documents"]
            or not results["documents"][0]
        ):
            raise Exception("Resume context not found.")

        context = "\n\n".join(results["documents"][0])

        prompt = f"""
You are a Senior Technical Interviewer.

Candidate Resume

{context}

Job Role:
{role}

Experience:
{experience} years

Generate exactly {total_questions} interview questions.

Rules:

1. Questions MUST match the Job Role.
2. Use the resume to personalize questions.
3. No duplicate questions.
4. Increase difficulty gradually.

Difficulty Distribution

First 30% Easy

Next 40% Medium

Last 30% Hard

Focus Areas

- Core concepts
- Projects
- Problem solving
- Best practices
- Scenario based
- System Design (last questions)

Return ONLY valid JSON.

Example

[
{{
"sequence":1,
"difficulty":"Easy",
"question":"Explain Dependency Injection."
}},
{{
"sequence":2,
"difficulty":"Easy",
"question":"Difference between JDK and JVM?"
}}
]
"""

        response = llm_service.generate(prompt)

        return json.loads(response)


question_generator = QuestionGenerator()