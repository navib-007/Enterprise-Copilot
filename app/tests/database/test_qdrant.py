from qdrant_client import AsyncQdrantClient

from app.core.config import Settings
from app.database.qdrant import create_qdrant_client


def test_create_qdrant_client_uses_async_client() -> None:
    settings = Settings(qdrant_host="vector-store", qdrant_port=7443, qdrant_https=True)

    client = create_qdrant_client(settings)

    assert isinstance(client, AsyncQdrantClient)
