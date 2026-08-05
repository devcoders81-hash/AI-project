import { useState } from "react";
import { uploadResume } from "../../api/resumeApi";
import { useNavigate } from "react-router-dom";

export default function ResumeUpload() {
    const navigate = useNavigate();

    const [file, setFile] = useState<File | null>(null);

    const [loading, setLoading] = useState(false);

    const upload = async () => {

        if (!file) {

            alert("Select Resume");

            return;
        }

        const formData = new FormData();

        formData.append("file", file);

        try {

            setLoading(true);

            const response=await uploadResume(formData);
            const id = response.id;
            console.log("Resume uploaded successfully:", id);
            //await new Promise(resolve => setTimeout(resolve, 2 * 60 * 1000));
            navigate(`/dashboard`);

            alert("Resume uploaded successfully.");

            setFile(null);

        } catch (err) {

            console.log(err);

            alert("Upload failed");

        } finally {

            setLoading(false);

        }

    };

    return (

        <div className="bg-white rounded-xl shadow p-8">

            <input

                type="file"

                accept=".pdf"

                onChange={(e) => {

                    if (e.target.files) {

                        setFile(e.target.files[0]);

                    }

                }}

            />

            <button

                onClick={upload}

                disabled={loading}

                className="bg-blue-600 text-white px-5 py-2 rounded ml-4"

            >

                {

                    loading

                        ? "Uploading..."

                        : "Upload Resume"

                }

            </button>

        </div>

    );

}