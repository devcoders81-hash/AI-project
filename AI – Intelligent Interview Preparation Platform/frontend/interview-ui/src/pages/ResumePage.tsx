import { useEffect, useState } from "react";

import { useNavigate } from "react-router-dom";

import ResumeTable from "../components/resume/ResumeTable";

import { getResumes } from "../api/resumeApi";
import type { Resume } from "../types/resume";

export default function ResumePage() {
  const navigate = useNavigate();

  const [resumes, setResumes] = useState<Resume[]>([]);

  const loadResumes = async () => {
    try {
      const data = await getResumes();
      setResumes(data);
    } catch (err) {
      console.error(err);
    }
  };

  useEffect(() => {
    loadResumes();
  }, []);

  return (
    <div className="p-8">
      <div className="flex justify-between mb-8">
        <h1 className="text-3xl font-bold">My Resumes</h1>

        <button
          onClick={() => navigate("/resume/upload")}
          className="bg-green-600 text-white px-5 py-2 rounded"
        >
          Upload Resume
        </button>
      </div>

      <ResumeTable
        resumes={resumes}
        onStartInterview={(resumeId) =>
          navigate(`/interview/create/${resumeId}`)
        }
        onGenerateInterview={(resumeId) =>
          navigate(`/interview/generate/${resumeId}`)
        }
      />
    </div>
  );
}
