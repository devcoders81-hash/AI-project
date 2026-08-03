import type { Resume } from "../../types/resume";

interface Props {

    resumes: Resume[];

    onStartInterview: (
        resumeId: string,
    ) => void;

}

export default function ResumeTable({

    resumes,

    onStartInterview,

}: Props) {

    return (

        <table className="w-full bg-white rounded-xl shadow">

            <thead>

                <tr className="border-b">

                    <th className="p-4 text-left">
                        Resume
                    </th>

                    <th className="p-4">
                        Status
                    </th>

                    <th className="p-4">
                        Created
                    </th>

                    <th className="p-4">
                        Action
                    </th>

                </tr>

            </thead>

            <tbody>

                {

                    resumes.map((resume) => (

                        <tr
                            key={resume.id}
                            className="border-b"
                        >

                            <td className="p-4">

                                {resume.file_name}

                            </td>

                            <td className="p-4 text-center">

                                {resume.status}

                            </td>

                            <td className="p-4 text-center">

                                {new Date(
                                    resume.created_at,
                                ).toLocaleDateString()}

                            </td>

                            <td className="p-4 text-center">

                                {

                                    resume.status === "COMPLETED"

                                    ?

                                    <button

                                        onClick={() =>
                                            onStartInterview(
                                                resume.id,
                                            )
                                        }

                                        className="bg-blue-600 text-white px-4 py-2 rounded"

                                    >

                                        Start Interview

                                    </button>

                                    :

                                    <span className="text-gray-500">

                                        Processing...

                                    </span>

                                }

                            </td>

                        </tr>

                    ))

                }

            </tbody>

        </table>

    );

}