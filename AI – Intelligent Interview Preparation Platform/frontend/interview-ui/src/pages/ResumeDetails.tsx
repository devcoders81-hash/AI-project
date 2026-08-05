import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

import { getResume } from "../api/resumeApi";

import ResumeDetails from "../components/resume/ResumeDetails";

import type { Resume } from "../types/resume";

export default function ResumeDetailsPage() {

    const { id } = useParams();

    const [resume, setResume] = useState<Resume>();

    useEffect(() => {

        if (id) {

            loadResume(id);

        }

    }, [id]);

    async function loadResume(id: string) {

        const data = await getResume(id);

        setResume(data);

    }

    if (!resume) {

        return <div>Loading...</div>;

    }

    return (

        <div className="max-w-5xl mx-auto p-8">

            <ResumeDetails resume={resume} />

        </div>

    );
}