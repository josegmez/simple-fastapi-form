from fastapi import APIRouter

from app.routes import incident, pages

api_router = APIRouter()

api_router.include_router(incident.router, prefix="/incidents", tags=["incidents"])
api_router.include_router(pages.router, tags=["pages"])
