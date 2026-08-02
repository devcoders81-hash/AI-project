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


llm_service = LLMService()