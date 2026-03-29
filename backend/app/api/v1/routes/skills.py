from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.skill import SkillsResponse
from app.services import skill_service

router = APIRouter()


@router.get("", response_model=SkillsResponse)
def list_skills(db: Annotated[Session, Depends(get_db)]) -> SkillsResponse:
    return skill_service.list_skills(db)
