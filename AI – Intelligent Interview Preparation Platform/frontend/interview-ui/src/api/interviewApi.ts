import api from "./axios";
import type {
  InterviewQuestion,
  SubmitAnswerRequest,
  SubmitAnswerResponse,
} from "../types/interview";

export const createInterview = async (resumeId: string) => {
  const response = await api.post("/api/v1/interviews", {
    resume_id: resumeId,
  });

  return response.data;
};

export const getNextQuestion = async (
  interviewId: string,
): Promise<InterviewQuestion> => {
  const response = await api.get(`/interviews/${interviewId}/question`);

  return response.data;
};

export const submitAnswer = async (
  interviewId: string,
  data: SubmitAnswerRequest,
): Promise<SubmitAnswerResponse> => {
  const response = await api.post(
    `/interviews/${interviewId}/answer`,
    data,
  );

  return response.data;
};
