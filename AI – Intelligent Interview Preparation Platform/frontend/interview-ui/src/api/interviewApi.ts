import api from "./axios";
import type {
  InterviewQuestion,
  SubmitAnswerRequest,
  SubmitAnswerResponse,
  GenerateInterview,
} from "../types/interview";

export const createInterview = async (data: GenerateInterview) => {
  const response = await api.post("/api/v1/interviews", {
    data,
  });

  return response.data;
};
export const generateInterview = async (data: GenerateInterview) => {
  const response = await api.post("/interviews",data);

  return response.data;

};

export const getNextQuestion = async (
  resumeId: string,
): Promise<InterviewQuestion> => {
  const response = await api.get(`/interviews/${resumeId}/question`);

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
