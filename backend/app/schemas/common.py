from typing import Generic, List, Optional, TypeVar
from uuid import UUID

from pydantic import BaseModel, Field

T = TypeVar("T")


class ErrorDetail(BaseModel):
    code: str
    message: str
    request_id: Optional[str] = None


class ErrorResponse(BaseModel):
    error: ErrorDetail


class PaginatedResponse(BaseModel, Generic[T]):
    items: List[T]
    total: int


class VisitCreate(BaseModel):
    path: str = Field(..., min_length=1, max_length=512)


class VisitAccepted(BaseModel):
    id: UUID
    status: str = "recorded"
