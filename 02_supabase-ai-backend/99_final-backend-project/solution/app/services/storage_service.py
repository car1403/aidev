import os
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4

from app.core import config  # noqa: F401  # .env 로드를 보장합니다.
from app.schemas.product_schema import ProductCreate

try:
    from supabase import create_client
except ImportError:
    create_client = None


memory_products: list[dict] = []
memory_logs: list[dict] = []


def now_text() -> str:
    return datetime.now(timezone.utc).isoformat()


def get_supabase_client() -> Any | None:
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

    if not url or not key or create_client is None:
        return None

    return create_client(url, key)


def get_storage_mode() -> str:
    return "supabase" if get_supabase_client() else "memory"


def save_log(action: str, status: str, detail: str | None = None) -> None:
    log = {
        "id": str(uuid4()),
        "action": action,
        "status": status,
        "detail": detail,
        "created_at": now_text(),
    }

    supabase = get_supabase_client()
    if supabase:
        supabase.table("final_service_logs").insert(
            {
                "action": action,
                "status": status,
                "detail": detail,
            }
        ).execute()
        return

    memory_logs.append(log)


def create_product(payload: ProductCreate) -> dict:
    product = {
        "id": str(uuid4()),
        "name": payload.name,
        "description": payload.description,
        "target_audience": payload.target_audience,
        "ai_description": None,
        "created_at": now_text(),
    }

    supabase = get_supabase_client()
    if supabase:
        result = supabase.table("final_products").insert(
            {
                "name": payload.name,
                "description": payload.description,
                "target_audience": payload.target_audience,
            }
        ).execute()
        product = result.data[0]
    else:
        memory_products.append(product)

    save_log("create_product", "success", f"상품 등록: {payload.name}")
    return product


def list_products() -> list[dict]:
    supabase = get_supabase_client()
    if supabase:
        result = (
            supabase.table("final_products")
            .select("*")
            .order("created_at", desc=True)
            .execute()
        )
        return result.data

    return list(reversed(memory_products))


def find_product(product_id: str) -> dict | None:
    supabase = get_supabase_client()
    if supabase:
        result = (
            supabase.table("final_products")
            .select("*")
            .eq("id", product_id)
            .execute()
        )
        if not result.data:
            return None
        return result.data[0]

    return next((item for item in memory_products if item["id"] == product_id), None)


def update_ai_description(product_id: str, ai_description: str) -> None:
    supabase = get_supabase_client()
    if supabase:
        (
            supabase.table("final_products")
            .update({"ai_description": ai_description})
            .eq("id", product_id)
            .execute()
        )
        return

    product = find_product(product_id)
    if product is not None:
        product["ai_description"] = ai_description


def list_service_logs() -> list[dict]:
    supabase = get_supabase_client()
    if supabase:
        result = (
            supabase.table("final_service_logs")
            .select("*")
            .order("created_at", desc=True)
            .execute()
        )
        return result.data

    return list(reversed(memory_logs))
