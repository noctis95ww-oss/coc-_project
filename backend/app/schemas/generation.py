from typing import Any
from uuid import UUID

from pydantic import BaseModel, Field


class NarrativeSegment(BaseModel):
    role: str = Field(..., description="Type of narrative element, e.g. scene, clue, npc_dialogue")
    title: str | None = Field(default=None, description="Optional title for quick scanning")
    content: str = Field(..., description="Markdown-formatted narrative output")
    metadata: dict[str, Any] = Field(
        default_factory=dict,
        description="Model-specific metadata such as tokens or retrieval references",
    )


class GenerationRequest(BaseModel):
    session_id: UUID
    prompt: str = Field(..., description="Keeper instructions or player actions to continue from")
    expected_outputs: list[str] = Field(
        default_factory=lambda: ["scene"],
        description="Desired narrative elements to generate (scene, clue, npc_dialogue, etc.)",
    )


class GenerationResponse(BaseModel):
    session_id: UUID
    segments: list[NarrativeSegment]
    model: str
    prompt_tokens: int | None = None
    completion_tokens: int | None = None
