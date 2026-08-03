import { useEffect, useState } from "react";
import ResumeTable from "../components/resume/ResumeTable";
import { getResumes } from "../api/resumeApi";
import type { Resume } from "../types/resume";
import { createInterview } from "../api/interviewApi";
import { useNavigate } from "react-router-dom";

export default function ResumeListPage() {
  const [resumes, setResumes] = useState<Resume[]>([]);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    loadResumes();
  }, []);

  const loadResumes = async () => {
    try {
      const data = await getResumes();
      setResumes(data);
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  const handleStartInterview = async (resumeId: string) => {
    try {
      const interview = await createInterview(resumeId);

      navigate(`/interview/${interview.id}`);
    } catch (error) {
      console.error(error);
    }
  };

  if (loading) {
    return <div className="p-10 text-center">Loading...</div>;
  }

  return (
    <div className="max-w-7xl mx-auto mt-8">
      <h2 className="text-3xl font-bold mb-6">My Resumes</h2>

      <ResumeTable resumes={resumes} onStartInterview={handleStartInterview} />
    </div>
  );
}
