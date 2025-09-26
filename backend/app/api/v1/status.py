from datetime import datetime

from fastapi import APIRouter

from app.core.config import settings

router = APIRouter()


@router.get("", summary="Service health check")
async def get_status() -> dict[str, str]:
    """Expose minimal service metadata for uptime checks."""
    return {
        "service": "coc-keeper-copilot",
        "version": settings.VERSION,
        "status": "ok",
        "timestamp": datetime.utcnow().isoformat() + "Z",
    }
