from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, HttpUrl, field_validator


class ProjectBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=120)
    slug: str = Field(..., min_length=1, max_length=120, pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
    summary: str = Field(..., min_length=1, max_length=500)
    description: Optional[str] = Field(None, max_length=20000)
    impact_highlights: List[str] = Field(default_factory=list, max_length=15)
    tech_stack: List[str] = Field(default_factory=list, max_length=30)
    repo_url: HttpUrl
    demo_url: Optional[HttpUrl] = None
    featured: bool = False
    sort_order: int = Field(0, ge=0, le=1_000_000)

    @field_validator("impact_highlights", mode="before")
    @classmethod
    def impact_none_to_empty(cls, v: object) -> object:
        if v is None:
            return []
        return v

    @field_validator("impact_highlights")
    @classmethod
    def validate_impact(cls, v: List[str]) -> List[str]:
        for item in v:
            if not item or len(item) > 280:
                raise ValueError("Each impact line must be 1–280 characters")
        return v

    @field_validator("tech_stack")
    @classmethod
    def validate_tech_stack(cls, v: List[str]) -> List[str]:
        for item in v:
            if not item or len(item) > 80:
                raise ValueError("Each tech item must be 1–80 characters")
        return v


class ProjectCreate(ProjectBase):
    pass


class ProjectRead(ProjectBase):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    created_at: datetime
    updated_at: datetime

    @field_validator("repo_url", "demo_url", mode="before")
    @classmethod
    def url_to_str(cls, v: object) -> object:
        return v
