from fastapi import APIRouter

from app.api.v1.routes import analytics, contact, experience, projects, skills

api_router = APIRouter()
api_router.include_router(projects.router, prefix="/projects", tags=["projects"])
api_router.include_router(skills.router, prefix="/skills", tags=["skills"])
api_router.include_router(experience.router, prefix="/experience", tags=["experience"])
api_router.include_router(contact.router, prefix="/contact", tags=["contact"])
api_router.include_router(analytics.router, prefix="/analytics", tags=["analytics"])
