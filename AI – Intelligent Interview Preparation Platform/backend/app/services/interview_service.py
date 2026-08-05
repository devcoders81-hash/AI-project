import uuid

from fastapi import HTTPException

from app.models import InterviewAnswer
from app.models.interview import Interview
from app.models.interview_question import InterviewQuestion
from app.enums.InterviewStatus import InterviewStatus
from app.repositories.interview_answer_repository import InterviewAnswerRepository

from app.repositories.interview_repository import InterviewRepository
from app.repositories.interview_question_repository import (
    InterviewQuestionRepository,
)

from app.schemas.interview_schema import (
    InterviewCreateRequest,
    InterviewResponse,
)
from app.services.llm_service import LLMService

from app.services.question_generator import QuestionGenerator


class InterviewService:

    def __init__(
        self,
        repository: InterviewRepository,
        answer_repo: InterviewAnswerRepository,
        question_repository: InterviewQuestionRepository,
    ):
        self.repository = repository

        self.question_repository = question_repository
        self.question_generator = QuestionGenerator()
        self.answer_repository=answer_repo
        self.llm_service = LLMService()
        self.question_cache = {}

    async def create_interview(
        self,
        user,
        request: InterviewCreateRequest,
    ) -> InterviewResponse:

        # --------------------------------------------------
        # Step 1 : Create Interview
        # --------------------------------------------------

        interview = Interview(

            user_id=user.id,

            resume_id=request.resume_id,

            role=request.role,

            experience=request.experience,

            total_questions=request.total_questions,

            current_question=1,

            score=0,

            status=InterviewStatus.CREATED,
        )

        interview = await self.repository.create(interview)

        # --------------------------------------------------
        # Step 2 : Decide Question Difficulty
        # --------------------------------------------------

        difficulty = self._get_difficulty(1)

        # --------------------------------------------------
        # Step 3 : Generate First Question
        # --------------------------------------------------

        questions = self.question_generator.generate_questions(
            resume_id=str(request.resume_id),
            role=request.role,
            experience=request.experience,
            total_questions=request.total_questions,
        )
        get_all_question=[]
        for q in questions:
            question = InterviewQuestion(
                interview_id=interview.id,
                sequence=q["sequence"],
                question=q["question"],
                difficulty=q["difficulty"],
            )
            get_all_question.append(question)

        await self.question_repository.create_all(get_all_question)

        # --------------------------------------------------
        # Step 5 : Return Response
        # --------------------------------------------------

        return InterviewResponse(

            interview_id=interview.id,

            status=interview.status.value,

            question_number=1,

            question=question.question,

        )

    def _get_difficulty(
        self,
        question_number: int,
    ) -> str:

        if question_number <= 2:
            return "Easy"

        elif question_number <= 5:
            return "Medium"

        elif question_number <= 8:
            return "Hard"

        return "Expert"

    async def get_interview(
        self,
        interview_id: uuid,
    ) -> list[InterviewQuestion]:
        question = (
            await self.question_repository.get_by_interview(
                interview_id
            )
        )

        return question

    # async def load_questions(self, interview_id: str):
    #
    #     if interview_id not in self.question_cache:
    #         questions = await self.question_repository.get_by_interview(
    #             interview_id=interview_id
    #         )
    #
    #         self.question_cache[interview_id] = questions
    #
    #     return self.question_cache[interview_id]

    async def get_question(
            self,
            interview_id,
            user_id
    ):
        try:

            interview = await self.repository.get_by_resume_user_id(
                interview_id,user_id
            )
            if interview is None:
                raise HTTPException(
                    status_code=404,
                    detail="Interview not found",
                )
            interview_question_list=await self.question_repository.get_by_interview(
                interview.id
            )
            unanswered_question=interview_question_list[0].sequence
            print(f"unanswered question {unanswered_question}")
            total_question = interview_question_list[-1].sequence
            print(f"total_question question {total_question}")
            #total_question=interview_by_desc_sequence.sequence

            # print(f"result of interview will be {type(interview)}")
            # if interview is None:
            #     raise HTTPException(
            #         status_code=404,
            #         detail="Interview not found",
            #     )
            # print(f"result of interview id will be {interview.id}")
            # print(f"result of interview sequence will be {interview.sequence}")
            # question = await self.question_repository.get_by_sequence(
            #     interview_id=interview.id,
            #     sequence=interview.sequence,
            # )
            #
            # if question is None:
            #     return {
            #         "completed": True
            #     }
            return {
                "sequence": unanswered_question,
                "question": interview_question_list[0].question,
                #"difficulty": interview[o.difficulty,
                "completed": interview_question_list[0].is_asked,
                "id": interview_question_list[0].id,
                "total_question":total_question
            }
        except Exception as ex:
            return {
                "message": str(ex),
                "status": InterviewStatus.FAILED,
            }

    async def submit_answer(
            self,
            interview_id,
            candidate_answer,
    ):

        interview = await self.question_repository.get_by_id(
            interview_id
        )
        if interview is None:
            raise HTTPException(
                status_code=404,
                detail="Interview not found",
            )

        question = await self.question_repository.get_by_sequence(
            interview.id,
            interview.sequence,
        )
        feedback = self.llm_service.evaluate_answer(
            question.question,
            candidate_answer,
        )

        answer = InterviewAnswer(
            question_id=question.id,
            candidate_answer=candidate_answer,
            feedback=feedback["feedback"],
            score=feedback["score"],
        )

        await self.answer_repository.create(
            answer
        )
        question.is_asked = True
        await self.question_repository.update(question)
        #await self.question_repository.mark_as_asked(question)

        return {
            "score": feedback["score"],
            "feedback": feedback["feedback"],
            #"next_question": interview.,
        }