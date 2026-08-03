from uuid import uuid4

from sqlalchemy import (
    String,
    ForeignKey,
    Enum, Integer,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.resume import Resume
from app.models.user import User
from app.enums.InterviewStatus import InterviewStatus


class Interview(Base):
    __tablename__ = "interviews"

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )

    user_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
    )

    resume_id: Mapped[UUID] = mapped_column(
        ForeignKey("resumes.id", ondelete="CASCADE"),
        nullable=False,
    )

    role: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    experience: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )
    total_questions: Mapped[int] = mapped_column(
        default=10
    )

    current_question: Mapped[int] = mapped_column(
        default=0
    )

    score: Mapped[int] = mapped_column(
        default=0
    )

    status: Mapped[InterviewStatus] = mapped_column(
        Enum(InterviewStatus),
        default=InterviewStatus.CREATED,
        nullable=False,
    )

    user = relationship(
        User,
        back_populates="interviews",
    )

    resume = relationship(
        Resume,
        back_populates="interviews",
    )

    questions = relationship(
        "InterviewQuestion",
        back_populates="interview",
        cascade="all, delete-orphan",
    )