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

    return response.data;

};

export const getResumes = async () => {

    const response = await api.get(
        "/resumes",
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