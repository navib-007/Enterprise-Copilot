from __future__ import annotations

from redis.asyncio import Redis

from app.core.config import Settings, get_settings


def create_redis_client(settings: Settings) -> Redis:
    return Redis.from_url(
        settings.redis_url,
        encoding="utf-8",
        decode_responses=True,
    )


redis_client: Redis = create_redis_client(get_settings())
