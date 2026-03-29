from typing import List

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.work_experience import WorkExperience
from app.schemas.experience import ExperienceListResponse, ExperienceRead


def list_experience(db: Session) -> ExperienceListResponse:
    q = select(WorkExperience).order_by(WorkExperience.sort_order.asc())
    rows = db.scalars(q).all()
    items: List[ExperienceRead] = [ExperienceRead.model_validate(r) for r in rows]
    return ExperienceListResponse(items=items)
