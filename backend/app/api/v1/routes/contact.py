from typing import Annotated

from fastapi import APIRouter, BackgroundTasks, Depends, Request
from sqlalchemy.orm import Session

from app.core.rate_limit import check_contact_rate_limit
from app.db.session import get_db
from app.schemas.contact import ContactAccepted, ContactCreate
from app.services import contact_service, email_service

router = APIRouter()


def _client_ip(request: Request) -> str:
    forwarded = request.headers.get("X-Forwarded-For")
    if forwarded:
        return forwarded.split(",")[0].strip()
    if request.client:
        return request.client.host
    return "unknown"


@router.post("", response_model=ContactAccepted, status_code=202)
def submit_contact(
    request: Request,
    background_tasks: BackgroundTasks,
    db: Annotated[Session, Depends(get_db)],
    body: ContactCreate,
) -> ContactAccepted:
    ip = _client_ip(request)
    check_contact_rate_limit(ip)
    row = contact_service.create_contact_record(db, body)

    def _send() -> None:
        email_service.send_contact_email(
            name=row.name,
            email=row.email,
            subject=row.subject,
            message=row.message,
            company=row.company,
        )

    background_tasks.add_task(_send)
    return contact_service.to_accepted(row)
