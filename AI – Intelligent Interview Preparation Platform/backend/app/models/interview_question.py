from uuid import uuid4

from sqlalchemy import (
    Integer,
    String,
    ForeignKey, Boolean,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.db.base import Base


class InterviewQuestion(Base):
    __tablename__ = "interview_questions"

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )

    interview_id: Mapped[UUID] = mapped_column(
        ForeignKey(
            "interviews.id",
            ondelete="CASCADE",
        ),
        nullable=False,
    )

    question: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    sequence: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    is_asked: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    difficulty: Mapped[str] = mapped_column(
        String(30),
        default="MEDIUM",
    )

    interview = relationship(
        "Interview",
        back_populates="questions",
    )

    answers = relationship(
        "InterviewAnswer",
        back_populates="question",
        cascade="all, delete-orphan",
    )