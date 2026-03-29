from typing import List
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, field_validator


class ExperienceRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    role: str
    company: str
    period: str
    summary: str
    key_points: List[str] = Field(default_factory=list, max_length=20)

    @field_validator("key_points", mode="before")
    @classmethod
    def coerce_points(cls, v: object) -> object:
        if v is None:
            return []
        return v

    @field_validator("key_points")
    @classmethod
    def validate_points(cls, v: List[str]) -> List[str]:
        for item in v:
            if not item or len(item) > 400:
                raise ValueError("Each key point must be 1–400 characters")
        return v


class ExperienceListResponse(BaseModel):
    items: List[ExperienceRead]
