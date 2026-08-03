from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import BaseModel


class InterviewMessage(BaseModel):
    __tablename__ = "interview_messages"

    interview_id: Mapped[str] = mapped_column(
        ForeignKey("interviews.id", ondelete="CASCADE"),
        nullable=False,
    )

    role: Mapped[str] = mapped_column(nullable=False)

    message: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    interview = relationship(
        "Interview",
        back_populates="messages",
    )