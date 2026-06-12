from __future__ import annotations

from qdrant_client import AsyncQdrantClient

from app.core.config import Settings, get_settings


def create_qdrant_client(settings: Settings) -> AsyncQdrantClient:
    return AsyncQdrantClient(
        url=settings.qdrant_url,
        api_key=settings.qdrant_api_key,
        prefer_grpc=False,
    )


qdrant_client: AsyncQdrantClient = create_qdrant_client(get_settings())
