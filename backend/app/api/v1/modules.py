from fastapi import APIRouter

from app.schemas.modules import ModuleCreateRequest, ModuleResponse
from app.services.dependencies import module_service

router = APIRouter()


@router.post("", response_model=ModuleResponse, summary="Register a new adventure module")
async def create_module(payload: ModuleCreateRequest) -> ModuleResponse:
    """Store minimal metadata about a module so that it can be processed later."""
    return module_service.register_module(payload)


@router.get("", response_model=list[ModuleResponse], summary="List registered modules")
async def list_modules() -> list[ModuleResponse]:
    return module_service.list_modules()
