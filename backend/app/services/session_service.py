from datetime import datetime

from fastapi import HTTPException, status

from app.schemas.sessions import (
    Session,
    SessionCreateRequest,
    SessionResponse,
    SessionUpdateRequest,
)


class SessionService:
    """Manage keeper sessions in memory until persistence is added."""

    def __init__(self) -> None:
        self._sessions: dict[str, Session] = {}

    def create_session(self, payload: SessionCreateRequest) -> SessionResponse:
        session = Session(module_id=payload.module_id, title=payload.title)
        self._sessions[str(session.id)] = session
        return SessionResponse(**session.dict())

    def update_session(self, session_id: str, payload: SessionUpdateRequest) -> SessionResponse:
        try:
            session = self._sessions[session_id]
        except KeyError as exc:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Session {session_id} not found",
            ) from exc

        update_data = payload.dict(exclude_unset=True)
        session.state.update(update_data.get("state", {}))
        if "last_player_action" in update_data:
            session.last_player_action = update_data["last_player_action"]
        session.updated_at = datetime.utcnow()
        self._sessions[session_id] = session
        return SessionResponse(**session.dict())

    def list_sessions(self) -> list[SessionResponse]:
        return [SessionResponse(**session.dict()) for session in self._sessions.values()]

    def get_session(self, session_id: str) -> Session:
        try:
            return self._sessions[session_id]
        except KeyError as exc:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Session {session_id} not found",
            ) from exc
