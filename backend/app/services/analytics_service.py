import hashlib
from typing import Optional

from sqlalchemy.orm import Session

from app.models.analytics import AnalyticsVisit


def record_page_visit(db: Session, path: str, client_ip: Optional[str]) -> AnalyticsVisit:
    ip_hash = None
    if client_ip:
        ip_hash = hashlib.sha256(client_ip.encode()).hexdigest()[:32]
    row = AnalyticsVisit(path=path[:512], ip_hash=ip_hash)
    db.add(row)
    db.commit()
    db.refresh(row)
    return row
