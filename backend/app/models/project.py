import uuid
from datetime import datetime
from typing import Any, List, Optional

from sqlalchemy import JSON, Boolean, DateTime, Integer, String, Text, Uuid, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Project(Base):
    __tablename__ = "projects"

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    slug: Mapped[str] = mapped_column(String(120), unique=True, nullable=False, index=True)
    summary: Mapped[str] = mapped_column(String(500), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    impact_highlights: Mapped[Optional[List[Any]]] = mapped_column(JSON, nullable=True)
    tech_stack: Mapped[List[Any]] = mapped_column(JSON, nullable=False, default=list)
    repo_url: Mapped[str] = mapped_column(String(2048), nullable=False)
    demo_url: Mapped[Optional[str]] = mapped_column(String(2048), nullable=True)
    featured: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    sort_order: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )
