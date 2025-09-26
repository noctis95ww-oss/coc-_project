"""High-level orchestration for narrative generation.

This placeholder service wires up future retrieval + LLM calls while keeping the
API responsive during early development.
"""

from __future__ import annotations

from typing import Any

from app.core.config import settings
from app.schemas.generation import GenerationRequest, GenerationResponse, NarrativeSegment
from app.services.session_service import SessionService


class GenerationService:
    def __init__(self, session_service: SessionService | None = None) -> None:
        self._session_service = session_service or SessionService()

    async def generate(self, payload: GenerationRequest) -> GenerationResponse:
        session = self._session_service.get_session(str(payload.session_id))

        # TODO: plug in retrieval augmented generation. For now, we return a stub
        # response that echoes the prompt and session state to validate the API
        # contract between frontend and backend teams.
        segments: list[NarrativeSegment] = [
            NarrativeSegment(
                role=expected_output,
                title=f"Draft {expected_output.replace('_', ' ').title()}",
                content=self._build_placeholder_content(expected_output, payload.prompt, session.state),
                metadata={
                    "model": "stub",
                    "note": "Replace with actual LLM output once integrated",
                },
            )
            for expected_output in payload.expected_outputs
        ]

        return GenerationResponse(
            session_id=payload.session_id,
            segments=segments,
            model="openai-gpt-placeholder" if settings.OPENAI_API_KEY else "stub",
            prompt_tokens=None,
            completion_tokens=None,
        )

    def _build_placeholder_content(self, role: str, prompt: str, state: dict[str, Any]) -> str:
        state_summary = "\n".join(f"- **{key}**: {value}" for key, value in state.items()) or "(no state recorded yet)"
        return (
            f"### {role.title()} draft\n\n"
            f"**Prompt:** {prompt}\n\n"
            f"**Known state:**\n{state_summary}\n\n"
            "_Replace this placeholder once the LLM integration is complete._"
        )
