"""Simple service locator for early development.

In production we may switch to a dependency injection framework, but centralising
singletons here ensures in-memory stores stay consistent across routers.
"""

from app.services.generation_service import GenerationService
from app.services.module_service import ModuleService
from app.services.session_service import SessionService

module_service = ModuleService()
session_service = SessionService()
generation_service = GenerationService(session_service=session_service)
