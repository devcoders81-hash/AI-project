import { useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { generateInterview } from "../api/interviewApi";

export default function GenerateInterviewPage() {

    const { resume_id } = useParams();

    const navigate = useNavigate();

    const [role, setRole] = useState("");

    const [experience, setExperience] = useState(0);

    const [loading, setLoading] = useState(false);

    const handleSubmit = async () => {

        setLoading(true);

        try {
                console.log("Generating interview for resumeId:", resume_id, "role:", role, "experience:", experience);
             await generateInterview({
                resume_id: resume_id as string,

                role: role as string,

                experience: experience as number,
                total_question: 10,

            });

            navigate(`/dashboard`);

        } finally {

            setLoading(false);

        }

    };

    return (

        <div className="max-w-xl mx-auto mt-10 bg-white shadow rounded-xl p-8">

            <h1 className="text-3xl font-bold mb-8">

                Generate Interview

            </h1>

            <div className="space-y-6">

                <div>

                    <label className="block mb-2">

                        Job Role

                    </label>

                    <input
                        value={role}
                        onChange={(e)=>setRole(e.target.value)}
                        className="w-full border rounded p-3"
                        placeholder="Backend Developer"
                    />

                </div>

                <div>

                    <label className="block mb-2">

                        Experience

                    </label>

                    <input
                        type="number"
                        value={experience}
                        onChange={(e)=>setExperience(Number(e.target.value))}
                        className="w-full border rounded p-3"
                    />

                </div>

                <button

                    onClick={handleSubmit}

                    disabled={loading}

                    className="w-full bg-indigo-600 text-white rounded p-3"

                >

                    {

                        loading

                        ?

                        "Generating..."

                        :

                        "Generate Interview"

                    }

                </button>

            </div>

        </div>

    );

}