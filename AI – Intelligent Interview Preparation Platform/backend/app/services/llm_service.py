import json

from groq import Groq

from app.core.config import settings


class LLMService:

    def __init__(self):

        self.client = Groq(
            api_key=settings.GROQ_API_KEY
        )

    def generate_answer(
        self,
        question: str,
        context: str,
    ) -> str:

        prompt = f"""
        You are an AI Resume Assistant.
        
        Answer ONLY using the provided resume context.
        
        If the answer cannot be found in the context, reply:
        
        "I couldn't find that information in the resume."
        
        Resume Context:
        {context}
        
        Question:
        {question}
        
        Answer:
        """

        response = self.client.chat.completions.create(

            model=settings.GROQ_MODEL,

            temperature=0,

            messages=[
                {
                    "role": "system",
                    "content": "You answer questions about resumes."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content.strip()

    def generate(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=settings.GROQ_MODEL,
            temperature=0,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content.strip()

    def evaluate_answer(
            self,
            question: str,
            candidate_answer: str,
    ):
        prompt = f"""
        You are a Senior Technical Interviewer.
        
        Evaluate the candidate's answer.
        
        Interview Question:
        {question}
        
        Candidate Answer:
        {candidate_answer}
        
        Evaluate using these criteria:
        1. Technical correctness
        2. Completeness
        3. Communication
        4. Best practices
        
        Return ONLY valid JSON.
        
        Example:
        
        {{
            "score": 8,
            "feedback": "Good understanding of the concept. The answer is technically correct but misses some edge cases."
        }}
        """

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert technical interviewer."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2,
            response_format={"type": "json_object"},
        )

        result = response.choices[0].message.content

        return json.loads(result)


llm_service = LLMService()