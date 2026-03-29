from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from app.models.skill import SkillCategory
from app.schemas.skill import SkillCategoryRead, SkillRead, SkillsResponse


def list_skills(db: Session) -> SkillsResponse:
    q = (
        select(SkillCategory)
        .options(selectinload(SkillCategory.skills))
        .order_by(SkillCategory.sort_order.asc(), SkillCategory.name.asc())
    )
    cats = db.scalars(q).unique().all()
    categories: list[SkillCategoryRead] = []
    for c in cats:
        ordered = sorted(c.skills, key=lambda x: (x.sort_order, x.name))
        categories.append(
            SkillCategoryRead(
                name=c.name,
                skills=[SkillRead.model_validate(s) for s in ordered],
            )
        )
    return SkillsResponse(categories=categories)
