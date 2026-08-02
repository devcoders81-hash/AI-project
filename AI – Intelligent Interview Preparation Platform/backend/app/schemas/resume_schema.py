from uuid import UUID

from pydantic import BaseModel

from app.enums.resume_status import ResumeStatus


class ResumeResponse(BaseModel):

    id: UUID

    original_filename: str

    status: str

    class Config:
        from_attributes = True

class ResumeStatusResponse(BaseModel):
    resume_id: UUID
    status: ResumeStatus

    class Config:
        from_attributes = True