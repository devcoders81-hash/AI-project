from fastapi import HTTPException

from app.constant.file_constant import (
    MAX_FILE_SIZE,
    ALLOWED_CONTENT_TYPES,
)


class FileValidator:

    @staticmethod
    async def validate(file):

        if file.content_type not in ALLOWED_CONTENT_TYPES:

            raise HTTPException(
                status_code=400,
                detail="Unsupported file type",
            )

        content = await file.read()

        if len(content) > MAX_FILE_SIZE:

            raise HTTPException(
                status_code=400,
                detail="File size exceeded",
            )

        await file.seek(0)