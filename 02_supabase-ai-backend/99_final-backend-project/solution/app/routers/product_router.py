from fastapi import APIRouter, HTTPException

from app.schemas.product_schema import (
    AiDescriptionResponse,
    ProductCreate,
    ProductResponse,
    ServiceLogResponse,
)
from app.services.ai_service import build_mock_ai_description
from app.services.storage_service import (
    create_product,
    find_product,
    get_storage_mode,
    list_products,
    list_service_logs,
    save_log,
    update_ai_description,
)


router = APIRouter()


@router.get("/health")
def health() -> dict[str, str]:
    return {
        "status": "ok",
        "storage": get_storage_mode(),
        "message": "final backend project solution is running",
    }


@router.post("/products", response_model=ProductResponse)
def create_product_endpoint(payload: ProductCreate) -> dict:
    return create_product(payload)


@router.get("/products", response_model=list[ProductResponse])
def list_products_endpoint() -> list[dict]:
    return list_products()


@router.post("/products/{product_id}/ai-description", response_model=AiDescriptionResponse)
def generate_ai_description_endpoint(product_id: str) -> dict:
    product = find_product(product_id)
    if product is None:
        save_log("generate_ai_description", "failed", f"상품 없음: {product_id}")
        raise HTTPException(status_code=404, detail="상품을 찾을 수 없습니다.")

    ai_description = build_mock_ai_description(product)
    update_ai_description(product_id, ai_description)
    save_log("generate_ai_description", "success", f"mock 설명 생성: {product_id}")

    return {
        "product_id": product_id,
        "ai_description": ai_description,
        "actual_api_called": False,
        "provider": "mock",
        "model": "mock-product-description-v1",
    }


@router.get("/service-logs", response_model=list[ServiceLogResponse])
def list_service_logs_endpoint() -> list[dict]:
    return list_service_logs()
