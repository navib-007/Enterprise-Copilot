from redis.asyncio import Redis

from app.core.config import Settings
from app.database.redis import create_redis_client


def test_create_redis_client_uses_configured_url() -> None:
    settings = Settings(redis_host="cache", redis_port=6380, redis_db=5, redis_password="secret")

    client = create_redis_client(settings)

    assert isinstance(client, Redis)
    assert client.connection_pool.connection_kwargs["host"] == "cache"
    assert client.connection_pool.connection_kwargs["port"] == 6380
    assert client.connection_pool.connection_kwargs["db"] == 5
