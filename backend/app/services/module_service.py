from collections.abc import Iterable

from app.schemas.modules import Module, ModuleCreateRequest, ModuleResponse


class ModuleService:
    """Temporary in-memory module registry.

    The service hides storage details so that a database-backed implementation can
    replace it later without touching the API layer.
    """

    def __init__(self) -> None:
        self._modules: dict[str, Module] = {}

    def register_module(self, payload: ModuleCreateRequest) -> ModuleResponse:
        module = Module(**payload.dict())
        self._modules[str(module.id)] = module
        return ModuleResponse(**module.dict())

    def list_modules(self) -> list[ModuleResponse]:
        return [ModuleResponse(**module.dict()) for module in self._modules.values()]

    def get_modules(self) -> Iterable[Module]:
        return self._modules.values()
