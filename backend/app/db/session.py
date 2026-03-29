from collections.abc import Generator

from sqlalchemy import create_engine, event
from sqlalchemy.orm import Session, sessionmaker

from app.core.config import get_settings

_engine = None
SessionLocal = sessionmaker(autocommit=False, autoflush=False)


def get_engine():
    global _engine
    if _engine is None:
        url = get_settings().database_url
        connect_args = {}
        if url.startswith("sqlite"):
            connect_args["check_same_thread"] = False
        _engine = create_engine(
            url,
            pool_pre_ping=True,
            connect_args=connect_args,
        )
        if url.startswith("sqlite"):

            @event.listens_for(_engine, "connect")
            def _sqlite_fk(dbapi_connection, connection_record):
                cursor = dbapi_connection.cursor()
                cursor.execute("PRAGMA foreign_keys=ON")
                cursor.close()

    return _engine


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal(bind=get_engine())
    try:
        yield db
    finally:
        db.close()
