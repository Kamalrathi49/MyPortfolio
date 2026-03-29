from typing import Optional
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field, field_validator


class ContactCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    subject: str = Field(..., min_length=1, max_length=200)
    message: str = Field(..., min_length=10, max_length=5000)
    company: Optional[str] = Field(None, max_length=200)
    honeypot: Optional[str] = Field(None, max_length=200)

    @field_validator("honeypot")
    @classmethod
    def honeypot_empty(cls, v: Optional[str]) -> Optional[str]:
        if v is not None and str(v).strip() != "":
            raise ValueError("Invalid submission")
        return v


class ContactAccepted(BaseModel):
    id: UUID
    status: str = "queued"
