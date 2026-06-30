import hashlib
import json
from urllib.parse import quote

import httpx

from app.core.config import UPSTASH_REDIS_REST_TOKEN, UPSTASH_REDIS_REST_URL


def _cache_enabled() -> bool:
    return bool(UPSTASH_REDIS_REST_URL and UPSTASH_REDIS_REST_TOKEN)


def make_cache_key(user_id: str, message: str) -> str:
    digest = hashlib.sha256(message.strip().lower().encode("utf-8")).hexdigest()
    return f"frontend-chat:{user_id}:{digest}"


def get_cached_answer(cache_key: str) -> str | None:
    if not _cache_enabled():
        return None

    encoded_key = quote(cache_key, safe="")
    url = f"{UPSTASH_REDIS_REST_URL.rstrip('/')}/get/{encoded_key}"
    headers = {"Authorization": f"Bearer {UPSTASH_REDIS_REST_TOKEN}"}
    response = httpx.get(url, headers=headers, timeout=5.0)
    response.raise_for_status()

    value = response.json().get("result")
    if not value:
        return None

    return json.loads(value)["answer"]


def set_cached_answer(cache_key: str, answer: str) -> None:
    if not _cache_enabled():
        return

    payload = json.dumps({"answer": answer}, ensure_ascii=False)
    encoded_key = quote(cache_key, safe="")
    encoded_payload = quote(payload, safe="")
    url = f"{UPSTASH_REDIS_REST_URL.rstrip('/')}/set/{encoded_key}/{encoded_payload}"
    headers = {"Authorization": f"Bearer {UPSTASH_REDIS_REST_TOKEN}"}
    response = httpx.post(url, headers=headers, timeout=5.0)
    response.raise_for_status()
