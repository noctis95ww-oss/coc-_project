from fastapi import APIRouter

from . import status, modules, sessions, generation

api_router = APIRouter()
api_router.include_router(status.router, prefix="/status", tags=["status"])
api_router.include_router(modules.router, prefix="/modules", tags=["modules"])
api_router.include_router(sessions.router, prefix="/sessions", tags=["sessions"])
api_router.include_router(generation.router, prefix="/generation", tags=["generation"])
