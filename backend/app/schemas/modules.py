from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class ModuleCreateRequest(BaseModel):
    title: str = Field(..., description="Module title")
    summary: str | None = Field(
        default=None, description="Optional short synopsis for quick browsing"
    )
    source_url: str | None = Field(
        default=None, description="Optional URL for the original module material"
    )


class ModuleResponse(BaseModel):
    id: UUID
    title: str
    summary: str | None
    source_url: str | None
    created_at: datetime

    class Config:
        orm_mode = True


class Module(BaseModel):
    """In-memory representation of a module record."""

    id: UUID = Field(default_factory=uuid4)
    title: str
    summary: str | None = None
    source_url: str | None = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
