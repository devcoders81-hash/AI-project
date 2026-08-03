import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

import QuestionCard from "../components/interview/QuestionCard";
import AnswerBox from "../components/interview/AnswerBox";
import FeedbackCard from "../components/interview/FeedbackCard";
import InterviewHeader from "../components/interview/InterviewHeader";

import { getNextQuestion, submitAnswer } from "../api/interviewApi";

import type { InterviewQuestion } from "../types/interview";

export default function InterviewPage() {
  const { id } = useParams();

  const [loading, setLoading] = useState(true);

  const [question, setQuestion] = useState<InterviewQuestion | null>(null);

  const [answer, setAnswer] = useState("");

  const [feedback, setFeedback] = useState("");

  const [score, setScore] = useState<number | null>(null);

  const loadQuestion = async () => {
    if (!id) return;

    try {
      setLoading(true);

      const response = await getNextQuestion(id);

      setQuestion(response);

      setAnswer("");

      setFeedback("");

      setScore(null);
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadQuestion();
  }, []);

  const handleSubmit = async () => {
    if (!id || !question) return;

    try {
      const response = await submitAnswer(question.id, {
        answer: answer,
      });

      setFeedback(response.feedback);

      setScore(response.score);
      loadQuestion();
    } catch (error) {
      console.error(error);
    }
  };

  if (loading) {
    return <div className="p-8">Loading Interview...</div>;
  }

  if (!question) {
    return <div className="p-8">No Question Found</div>;
  }

  return (
    <div className="max-w-5xl mx-auto p-8">
      <InterviewHeader
        sequence={question.sequence}
        total={question.total_question}
      />

      <QuestionCard question={question} />

      <AnswerBox
        answer={answer}
        setAnswer={setAnswer}
        onSubmit={handleSubmit}
      />

      {feedback && score !== null && (
        <FeedbackCard feedback={feedback} score={score} />
      )}
    </div>
  );
}
