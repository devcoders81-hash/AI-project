import Card from "../components/common/Card";
import { useNavigate } from "react-router-dom";
import {
  Upload,
  Play,
  FileText,
  Users,
  CheckCircle,
  Trophy,
} from "lucide-react";

export default function Dashboard() {
  const navigate = useNavigate();

  return (
    <div className="min-h-screen bg-slate-100 p-8">

      {/* Header */}
      <div className="flex justify-between items-center mb-10">
        <div>
          <h1 className="text-4xl font-bold text-slate-900">
            Dashboard
          </h1>
          <p className="text-slate-500 mt-2">
            Manage your AI interview preparation
          </p>
        </div>
      </div>


      {/* Action Buttons */}
      <div className="flex gap-5 mb-10">

        <button
          onClick={() => navigate("/resume/upload")}
          className="
            flex items-center gap-3
            bg-indigo-600
            hover:bg-indigo-700
            text-white
            px-6 py-3
            rounded-xl
            shadow-md
            transition
          "
        >
          <Upload size={20} />
          Upload Resume
        </button>


        <button
          onClick={() =>
            navigate(
              `/interview/id`
            )
          }
          className="
            flex items-center gap-3
            bg-emerald-600
            hover:bg-emerald-700
            text-white
            px-6 py-3
            rounded-xl
            shadow-md
            transition
          "
        >
          <Play size={20} />
          Start Interview
        </button>

      </div>


      {/* Stats Cards */}
      <div className="
        grid 
        grid-cols-1
        sm:grid-cols-2
        lg:grid-cols-4
        gap-6
      ">

        <Card
          title="Resumes"
          value="0"
          icon={<FileText size={28} />}
        />

        <Card
          title="Interviews"
          value="0"
          icon={<Users size={28} />}
        />

        <Card
          title="Completed"
          value="0"
          icon={<CheckCircle size={28} />}
        />

        <Card
          title="Average Score"
          value="0%"
          icon={<Trophy size={28} />}
        />

      </div>


      {/* Recent Activity */}
      <div className="
        mt-10
        bg-white
        rounded-2xl
        shadow-sm
        p-6
      ">
        <h2 className="text-xl font-semibold text-slate-800 mb-4">
          Recent Activity
        </h2>

        <p className="text-slate-500">
          No interviews completed yet. Start your first AI interview.
        </p>
      </div>

    </div>
  );
}