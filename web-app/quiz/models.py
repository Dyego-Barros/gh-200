from sqlalchemy import CheckConstraint, ForeignKey, String, Text, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Question(Base):
    __tablename__ = 'questions'
    id: Mapped[int] = mapped_column(primary_key=True)
    number: Mapped[int] = mapped_column()
    domain: Mapped[str] = mapped_column(String(200))
    level: Mapped[str] = mapped_column(String(30))
    statement: Mapped[str] = mapped_column(Text)
    a: Mapped[str] = mapped_column(Text)
    b: Mapped[str] = mapped_column(Text)
    c: Mapped[str] = mapped_column(Text)
    d: Mapped[str] = mapped_column(Text)
    correct: Mapped[str] = mapped_column(String(1))
    explanation: Mapped[str] = mapped_column(Text)
    is_active: Mapped[bool] = mapped_column(default=True, server_default="1")
    source_hash: Mapped[str] = mapped_column(String(64))
    __table_args__ = (
        UniqueConstraint("source_hash", "number", name="uq_questions_source_number"),
        CheckConstraint("level IN ('Básico','Intermediário','Avançado')"),
        CheckConstraint("correct IN ('A','B','C','D')"),
    )


class Attempt(Base):
    __tablename__ = 'attempts'
    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    owner: Mapped[str] = mapped_column(String(64), index=True)
    started_at: Mapped[int]
    deadline: Mapped[int]
    finished_at: Mapped[int | None]
    items: Mapped[list['AttemptItem']] = relationship(order_by='AttemptItem.position', cascade='all, delete-orphan')


class AttemptItem(Base):
    __tablename__ = 'attempt_items'
    id: Mapped[int] = mapped_column(primary_key=True)
    attempt_id: Mapped[str] = mapped_column(ForeignKey('attempts.id'), index=True)
    question_id: Mapped[int] = mapped_column(ForeignKey('questions.id'))
    position: Mapped[int]
    answer: Mapped[str | None] = mapped_column(String(1))
    question: Mapped[Question] = relationship()
    __table_args__ = (
        UniqueConstraint('attempt_id', 'question_id'),
        UniqueConstraint('attempt_id', 'position'),
        CheckConstraint("answer IS NULL OR answer IN ('A','B','C','D')"),
    )
