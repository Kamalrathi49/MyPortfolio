from typing import Annotated, Optional

from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.common import VisitAccepted, VisitCreate
from app.services import analytics_service

router = APIRouter()


def _client_ip(request: Request) -> Optional[str]:
    forwarded = request.headers.get("X-Forwarded-For")
    if forwarded:
        return forwarded.split(",")[0].strip()
    if request.client:
        return request.client.host
    return None


@router.post("/visit", response_model=VisitAccepted, status_code=201)
def record_visit(
    request: Request,
    db: Annotated[Session, Depends(get_db)],
    body: VisitCreate,
) -> VisitAccepted:
    row = analytics_service.record_page_visit(db, body.path, _client_ip(request))
    return VisitAccepted(id=row.id)
