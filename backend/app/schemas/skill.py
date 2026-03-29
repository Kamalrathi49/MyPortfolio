from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class SkillRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    name: str
    proficiency: int = Field(..., ge=1, le=5)
    years: Optional[int] = Field(None, ge=0, le=80)
    highlights: List[str] = Field(default_factory=list, max_length=20)


class SkillCategoryRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    skills: List[SkillRead]


class SkillsResponse(BaseModel):
    categories: List[SkillCategoryRead]
