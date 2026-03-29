from sqlalchemy.orm import Session

from app.models.contact import Contact
from app.schemas.contact import ContactAccepted, ContactCreate


def create_contact_record(db: Session, data: ContactCreate) -> Contact:
    row = Contact(
        name=data.name,
        email=str(data.email).lower(),
        subject=data.subject,
        message=data.message,
        company=data.company,
    )
    db.add(row)
    db.commit()
    db.refresh(row)
    return row


def to_accepted(row: Contact) -> ContactAccepted:
    return ContactAccepted(id=row.id, status="queued")
