from typing import List, Optional, Tuple

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.core.exceptions import ConflictError
from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectRead


def _featured_filter(q, featured: Optional[bool]):
    if featured is True:
        return q.where(Project.featured.is_(True))
    if featured is False:
        return q.where(Project.featured.is_(False))
    return q


def list_projects(
    db: Session,
    featured: Optional[bool] = None,
    limit: int = 20,
    offset: int = 0,
) -> Tuple[List[ProjectRead], int]:
    count_q = select(func.count()).select_from(Project)
    count_q = _featured_filter(count_q, featured)
    total = db.scalar(count_q) or 0
    list_q = select(Project)
    list_q = _featured_filter(list_q, featured)
    list_q = list_q.order_by(Project.sort_order.asc(), Project.created_at.desc())
    list_q = list_q.offset(offset).limit(min(limit, 50))
    rows = db.scalars(list_q).all()
    return [ProjectRead.model_validate(r) for r in rows], total


def create_project(db: Session, data: ProjectCreate) -> ProjectRead:
    existing = db.scalar(select(Project).where(Project.slug == data.slug))
    if existing is not None:
        raise ConflictError("A project with this slug already exists")
    payload = data.model_dump()
    payload["repo_url"] = str(payload["repo_url"])
    payload["demo_url"] = str(payload["demo_url"]) if payload.get("demo_url") else None
    if not payload.get("impact_highlights"):
        payload["impact_highlights"] = []
    row = Project(**payload)
    db.add(row)
    db.commit()
    db.refresh(row)
    return ProjectRead.model_validate(row)
