from __future__ import annotations

from enum import StrEnum
from functools import lru_cache
from typing import Any

from pydantic import computed_field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Environment(StrEnum):
    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"
    TEST = "test"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    app_name: str = "enterprise-ai-ops-copilot"
    app_env: Environment = Environment.DEVELOPMENT
    debug: bool = False
    api_v1_prefix: str = "/api/v1"
    log_level: str = "INFO"

    backend_cors_origins: list[str] = ["http://localhost:3000", "http://127.0.0.1:3000"]

    postgres_host: str = "localhost"
    postgres_port: int = 5432
    postgres_db: str = "enterprise_ai_ops"
    postgres_user: str = "enterprise_user"
    postgres_password: str = "change_me"

    redis_host: str = "localhost"
    redis_port: int = 6379
    redis_db: int = 0
    redis_password: str | None = None

    qdrant_host: str = "localhost"
    qdrant_port: int = 6333
    qdrant_api_key: str | None = None
    qdrant_https: bool = False

    jwt_access_token_expire_minutes: int = 15
    jwt_refresh_token_expire_days: int = 7
    jwt_algorithm: str = "HS256"
    jwt_private_key: str = "replace_with_secure_private_key"
    jwt_public_key: str = "replace_with_secure_public_key"
    jwt_refresh_secret: str = "replace_with_secure_refresh_secret"

    @field_validator("backend_cors_origins", mode="before")
    @classmethod
    def parse_cors_origins(cls, value: Any) -> list[str]:
        if isinstance(value, str):
            return [origin.strip() for origin in value.split(",") if origin.strip()]
        if isinstance(value, list):
            return [str(origin).strip() for origin in value if str(origin).strip()]
        raise TypeError("BACKEND_CORS_ORIGINS must be a comma-separated string or list of strings")

    @computed_field  # type: ignore[prop-decorator]
    @property
    def sqlalchemy_database_uri(self) -> str:
        return (
            f"postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )

    @computed_field  # type: ignore[prop-decorator]
    @property
    def redis_url(self) -> str:
        credentials = f":{self.redis_password}@" if self.redis_password else ""
        return f"redis://{credentials}{self.redis_host}:{self.redis_port}/{self.redis_db}"

    @computed_field  # type: ignore[prop-decorator]
    @property
    def qdrant_url(self) -> str:
        scheme = "https" if self.qdrant_https else "http"
        return f"{scheme}://{self.qdrant_host}:{self.qdrant_port}"

    @property
    def is_production(self) -> bool:
        return self.app_env == Environment.PRODUCTION


@lru_cache
def get_settings() -> Settings:
    return Settings()
