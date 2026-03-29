import secrets
from typing import Annotated, Optional

from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.core.config import get_settings
from app.core.exceptions import UnauthorizedError

bearer_scheme = HTTPBearer(auto_error=False)


def verify_api_key(
    credentials: Annotated[Optional[HTTPAuthorizationCredentials], Depends(bearer_scheme)],
) -> None:
    if credentials is None or credentials.scheme.lower() != "bearer":
        raise UnauthorizedError("Authorization Bearer token required")
    settings = get_settings()
    if not secrets.compare_digest(credentials.credentials, settings.api_key):
        raise UnauthorizedError("Invalid API key")


AdminUser = Annotated[None, Depends(verify_api_key)]
