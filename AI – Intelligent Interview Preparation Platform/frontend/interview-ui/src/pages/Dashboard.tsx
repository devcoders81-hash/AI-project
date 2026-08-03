import Card from "../components/common/Card";
import { useNavigate } from "react-router-dom";
export default function Dashboard() {
  const navigate = useNavigate();

  return (
    <div className="p-10">
      <h1 className="text-4xl font-bold mb-8">Dashboard</h1>
      <button
        onClick={() => navigate("/resume/upload")}
        className="bg-blue-600 text-white px-5 py-2 rounded"
      >
        Upload Resume
      </button>

      <button
    onClick={() => navigate(`/interview/${'b6aae904-c079-4905-8961-e09154f8a2d5'}`)}
>
    Start Interview
</button>

      <div className="grid grid-cols-4 gap-6">
        <Card title="Resumes" value="0" />

        <Card title="Interviews" value="0" />

        <Card title="Completed" value="0" />

        <Card title="Average Score" value="0%" />
      </div>
    </div>
  );
}
