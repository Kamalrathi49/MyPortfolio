from typing import Annotated, Optional

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.core.security import AdminUser
from app.db.session import get_db
from app.schemas.common import PaginatedResponse
from app.schemas.project import ProjectCreate, ProjectRead
from app.services import project_service

router = APIRouter()


@router.get("", response_model=PaginatedResponse[ProjectRead])
def list_projects(
    db: Annotated[Session, Depends(get_db)],
    featured: Optional[bool] = Query(None),
    limit: int = Query(20, ge=1, le=50),
    offset: int = Query(0, ge=0),
) -> PaginatedResponse[ProjectRead]:
    items, total = project_service.list_projects(db, featured=featured, limit=limit, offset=offset)
    return PaginatedResponse(items=items, total=total)


@router.post("", response_model=ProjectRead, status_code=201)
def create_project(
    data: ProjectCreate,
    db: Annotated[Session, Depends(get_db)],
    _: AdminUser,
) -> ProjectRead:
    return project_service.create_project(db, data)
