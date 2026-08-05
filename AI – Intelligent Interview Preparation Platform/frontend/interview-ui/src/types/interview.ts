export interface InterviewQuestion {
  id: string;
  sequence: number;
  question: string;
  difficulty: string;
  total_question: number;
}

export interface GenerateInterview{
  resume_id: string;
  role:string;
  experience:number;
  total_question:number;
}

export interface SubmitAnswerRequest {
//   #question_id: string;
  answer: string;
}

export interface SubmitAnswerResponse {
  feedback: string;
  score: number;
  next_question: boolean;
}