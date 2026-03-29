from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.experience import ExperienceListResponse
from app.services import experience_service

router = APIRouter()


@router.get("", response_model=ExperienceListResponse)
def list_experience(db: Annotated[Session, Depends(get_db)]) -> ExperienceListResponse:
    return experience_service.list_experience(db)
