from fastapi import APIRouter

from app.schemas.generation import GenerationRequest, GenerationResponse
from app.services.dependencies import generation_service

router = APIRouter()


@router.post("", response_model=GenerationResponse, summary="Generate narrative content")
async def generate_content(payload: GenerationRequest) -> GenerationResponse:
    return await generation_service.generate(payload)
