from pathlib import Path

UPLOAD_DIRECTORY = Path("uploads")

RESUME_DIRECTORY = UPLOAD_DIRECTORY / "resumes"

MAX_FILE_SIZE = 10 * 1024 * 1024

ALLOWED_CONTENT_TYPES = {
    "application/pdf",

    "application/msword",

    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
}