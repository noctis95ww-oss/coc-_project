from functools import lru_cache
from typing import Literal

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    ENVIRONMENT: Literal["development", "production", "test"] = Field(
        default="development", description="Runtime environment label"
    )
    API_V1_PREFIX: str = "/api/v1"
    VERSION: str = "0.1.0"
    OPENAI_API_KEY: str | None = Field(
        default=None,
        description="Optional OpenAI API key used for narrative generation",
    )

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
