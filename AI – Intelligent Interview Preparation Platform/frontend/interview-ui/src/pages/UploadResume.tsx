import { useState } from "react";
import { uploadResume } from "../api/resumeApi";

export default function UploadResume() {

    const [file, setFile] = useState<File | null>(null);

    const handleUpload = async () => {

        if (!file) {
            alert("Select a PDF");
            return;
        }

        const formData = new FormData();
        formData.append("file", file);

        await uploadResume(formData);

        alert("Resume uploaded successfully");
    };

    return (
        <div className="p-10">

            <h1 className="text-3xl font-bold mb-6">
                Upload Resume
            </h1>

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