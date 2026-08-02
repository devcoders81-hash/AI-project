import uuid
import aiofiles
from app.constant.file_constant import (RESUME_DIRECTORY,UPLOAD_DIRECTORY)
from pathlib import Path
from fastapi import UploadFile


class StorageService:

    async def save_file(
        self,
        file: UploadFile,
    ):

        extension = Path(file.filename).suffix

        unique_name = f"{uuid.uuid4()}{extension}"

        save_path = RESUME_DIRECTORY / unique_name

        RESUME_DIRECTORY.mkdir(
            parents=True,
            exist_ok=True,
        )

        async with aiofiles.open(
            save_path,
            "wb",
        ) as out:
            while chunk := await file.read(1024 * 1024):
                await out.write(chunk)

        await file.seek(0)

        return unique_name, str(save_path)