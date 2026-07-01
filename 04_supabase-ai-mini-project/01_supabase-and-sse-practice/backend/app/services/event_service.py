import asyncio
import json

from app.core.config import REDIS_CHANNEL, REDIS_URL, is_redis_configured
from app.services.memory_store import (
    publish_memory_event,
    subscribe_memory,
    unsubscribe_memory,
)


async def publish_log_event(item: dict) -> None:
    # Redis가 실제 값으로 설정되어 있으면 Redis pub/sub으로 이벤트를 보냅니다.
    # 설정이 없으면 수업용 memory queue로 fallback합니다.
    if is_redis_configured():
        try:
            import redis.asyncio as redis

            client = redis.from_url(REDIS_URL, decode_responses=True)
            await client.publish(REDIS_CHANNEL, json.dumps(item, ensure_ascii=False))
            await client.aclose()
            return
        except Exception:
            pass

    await publish_memory_event(item)


async def redis_event_stream():
    import redis.asyncio as redis

    client = redis.from_url(REDIS_URL, decode_responses=True)
    pubsub = client.pubsub()
    await pubsub.subscribe(REDIS_CHANNEL)

    try:
        while True:
            message = await pubsub.get_message(ignore_subscribe_messages=True, timeout=1.0)
            if message and message.get("data"):
                yield json.loads(message["data"])
            await asyncio.sleep(0.1)
    finally:
        await pubsub.unsubscribe(REDIS_CHANNEL)
        await pubsub.aclose()
        await client.aclose()


async def memory_event_stream():
    queue = subscribe_memory()
    try:
        while True:
            item = await queue.get()
            yield item
    finally:
        unsubscribe_memory(queue)


async def event_stream():
    if is_redis_configured():
        try:
            async for item in redis_event_stream():
                yield item
            return
        except Exception:
            pass

    async for item in memory_event_stream():
        yield item
