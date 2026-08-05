import api from "./axios";

export const uploadResume = async (
    formData: FormData,
) => {

    const response = await api.post(
        "/resumes/upload",
        formData,
        {
            headers: {
                "Content-Type": "multipart/form-data",
            },
        },
    );
    localStorage.setItem("resumeId", response.data.id);
    //console.log("Resume uploaded successfully:", response.data);
    return response.data;

};

export const getResumes = async () => {

    const response = await api.get(
        "/resumes/all",
    );

    return response.data;

};

export const getResume = async (
    id: string,
) => {

    const response = await api.get(
        `/resumes/${id}`,
    );

    return response.data;

};