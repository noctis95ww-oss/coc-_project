from datetime import datetime
from typing import Any
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class SessionCreateRequest(BaseModel):
    module_id: UUID = Field(..., description="Identifier of the module being played")
    title: str = Field(..., description="Friendly name for the keeper session")


class SessionUpdateRequest(BaseModel):
    state: dict[str, Any] = Field(
        default_factory=dict,
        description="Arbitrary JSON payload describing the current story state",
    )
    last_player_action: str | None = Field(
        default=None,
        description="Optional summary of the latest player decision for context",
    )


class SessionResponse(BaseModel):
    id: UUID
    module_id: UUID
    title: str
    state: dict[str, Any]
    last_player_action: str | None
    created_at: datetime
    updated_at: datetime


class Session(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    module_id: UUID
    title: str
    state: dict[str, Any] = Field(default_factory=dict)
    last_player_action: str | None = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
