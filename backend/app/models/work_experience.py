import uuid
from typing import Any, List

from sqlalchemy import Integer, JSON, String, Text, Uuid
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class WorkExperience(Base):
    __tablename__ = "work_experience"

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    role: Mapped[str] = mapped_column(String(200), nullable=False)
    company: Mapped[str] = mapped_column(String(200), nullable=False)
    period: Mapped[str] = mapped_column(String(120), nullable=False)
    summary: Mapped[str] = mapped_column(Text, nullable=False)
    key_points: Mapped[List[Any]] = mapped_column(JSON, nullable=False, default=list)
    sort_order: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
