import type { InterviewQuestion } from "../../types/interview";

interface Props {
  question: InterviewQuestion;
}

export default function QuestionCard({
  question,
}: Props) {
  return (
    <div className="bg-white rounded-lg shadow p-6">

      <div className="flex justify-between">

        <h2 className="text-xl font-bold">
          Question {question.sequence}
        </h2>

        <span className="bg-blue-100 text-blue-700 px-3 py-1 rounded">
          {question.difficulty}
        </span>

      </div>

      <p className="mt-6 text-lg">
        {question.question}
      </p>

    </div>
  );
}