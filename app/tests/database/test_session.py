from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import Settings
from app.database.session import create_engine, create_session_factory, get_session


def test_create_engine_uses_async_postgres_driver() -> None:
    settings = Settings()

    engine = create_engine(settings)

    assert str(engine.url).startswith("postgresql+asyncpg://")


def test_create_session_factory_builds_async_sessions() -> None:
    settings = Settings()
    engine = create_engine(settings)

    factory = create_session_factory(engine)

    session = factory()

    assert isinstance(session, AsyncSession)


async def test_get_session_yields_async_session() -> None:
    session_generator = get_session()

    session = await anext(session_generator)

    assert isinstance(session, AsyncSession)

    await session_generator.aclose()
