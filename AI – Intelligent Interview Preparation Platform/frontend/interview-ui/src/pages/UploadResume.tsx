import { useEffect, useState } from "react";
import { uploadResume } from "../api/resumeApi";
import { useNavigate } from "react-router-dom";

export default function UploadResume() {
  const [file, setFile] = useState<File | null>(null);
  const navigate = useNavigate();

  useEffect(() => {
    console.log("useEffect called");

    const resumeId = localStorage.getItem("resumeId");
    console.log("resumeId:", resumeId);
  }, []);

//   const handleUpload = async () => {
//     debugger;
//     if (!file) {
//       alert("Select a PDF");
//       return;
//     }

//     const formData = new FormData();
//     formData.append("file", file);

//     await uploadResume(formData)
//       .then((res) => {
//         const id = res.id;
//         localStorage.setItem("resumeId", id);
//         alert("Resume uploaded successfully");
//         navigate(`/interview/${id}`);
//       })
//       .catch((err) => {
//         console.error(err);
//         alert("Failed to upload resume");
//       });
//   };
const handleUpload = async () => {
    debugger;

    if (!file) {
        alert("Select a PDF");
        return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
        const res = await uploadResume(formData);

        console.log("UPLOAD RESPONSE:", res);

        const id = res.id;

        console.log("Resume uploaded successfully:", id);

        localStorage.setItem("resumeId", id);

        alert("Resume uploaded successfully");

        navigate(`/interview/${id}`);

    } catch (err) {
        console.error("Upload error:", err);
        alert("Failed to upload resume");
    }
};

  return (
    <div className="p-10">
      <h1 className="text-3xl font-bold mb-6">Upload Resume</h1>

      <input
        type="file"
        accept=".pdf"
        onChange={(e) => {
          if (e.target.files?.length) {
            setFile(e.target.files[0]);
          }
        }}
      />

      <button
        onClick={handleUpload}
        className="block mt-6 bg-blue-600 text-white px-6 py-3 rounded"
      >
        Upload Resume
      </button>
    </div>
  );
}
