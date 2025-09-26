from fastapi import APIRouter

from app.schemas.sessions import SessionCreateRequest, SessionResponse, SessionUpdateRequest
from app.services.dependencies import session_service

router = APIRouter()


@router.post("", response_model=SessionResponse, summary="Start a new keeper session")
async def create_session(payload: SessionCreateRequest) -> SessionResponse:
    return session_service.create_session(payload)


@router.patch("/{session_id}", response_model=SessionResponse, summary="Update session state")
async def update_session(session_id: str, payload: SessionUpdateRequest) -> SessionResponse:
    return session_service.update_session(session_id, payload)


@router.get("", response_model=list[SessionResponse], summary="List active sessions")
async def list_sessions() -> list[SessionResponse]:
    return session_service.list_sessions()
