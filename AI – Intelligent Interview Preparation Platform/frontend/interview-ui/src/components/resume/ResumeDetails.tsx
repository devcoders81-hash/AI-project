import type { Resume } from "../../types/resume";

type Props = {
    resume: Resume;
};

export default function ResumeDetails({ resume }: Props) {
    return (
        <div className="bg-white rounded-xl shadow-md p-8">

            <h2 className="text-2xl font-bold mb-6">
                Resume Details
            </h2>

            <div className="space-y-4">

                <div>
                    <strong>Resume Name:</strong>
                    <p>{resume.original_filename}</p>
                </div>

                <div>
                    <strong>Status:</strong>
                    <p>{resume.status}</p>
                </div>

                <div>
                    <strong>Uploaded:</strong>
                    <p>{new Date(resume.created_at).toLocaleString()}</p>
                </div>

                <div>
                    <strong>File Size:</strong>
                    <p>{Math.round(resume.file_size / 1024)} KB</p>
                </div>

            </div>

        </div>
    );
}