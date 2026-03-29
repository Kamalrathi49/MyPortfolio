import uuid
from typing import Any, List, Optional

from sqlalchemy import ForeignKey, Integer, JSON, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class SkillCategory(Base):
    __tablename__ = "skill_categories"

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    sort_order: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    skills: Mapped[List["Skill"]] = relationship(
        "Skill", back_populates="category", order_by="Skill.sort_order"
    )


class Skill(Base):
    __tablename__ = "skills"

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    category_id: Mapped[uuid.UUID] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("skill_categories.id", ondelete="CASCADE"), nullable=False
    )
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    proficiency: Mapped[int] = mapped_column(Integer, nullable=False, default=3)
    years: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    highlights: Mapped[List[Any]] = mapped_column(JSON, nullable=False, default=list)
    sort_order: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    category: Mapped["SkillCategory"] = relationship("SkillCategory", back_populates="skills")
