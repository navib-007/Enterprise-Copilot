from app.core.config import Environment, Settings


def test_settings_builds_infrastructure_urls() -> None:
    settings = Settings(
        postgres_host="db",
        postgres_port=5433,
        postgres_db="copilot",
        postgres_user="copilot_user",
        postgres_password="super-secret",
        redis_host="redis",
        redis_port=6380,
        redis_db=2,
        redis_password="redis-secret",
        qdrant_host="vector-db",
        qdrant_port=7000,
        qdrant_https=True,
    )

    assert settings.sqlalchemy_database_uri == (
        "postgresql+asyncpg://copilot_user:super-secret@db:5433/copilot"
    )
    assert settings.redis_url == "redis://:redis-secret@redis:6380/2"
    assert settings.qdrant_url == "https://vector-db:7000"


def test_settings_parses_cors_origins_from_string() -> None:
    settings = Settings(backend_cors_origins="http://localhost:3000, http://127.0.0.1:3000")

    assert settings.backend_cors_origins == ["http://localhost:3000", "http://127.0.0.1:3000"]


def test_environment_defaults_to_development() -> None:
    settings = Settings()

    assert settings.app_env == Environment.DEVELOPMENT
    assert settings.is_production is False
