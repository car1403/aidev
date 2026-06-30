from pydantic import BaseModel, Field


class ProductCreate(BaseModel):
    name: str = Field(min_length=1, description="상품 이름")
    description: str = Field(min_length=1, description="상품 기본 설명")
    target_audience: str = Field(default="초보자", min_length=1, description="주요 대상")


class ProductResponse(BaseModel):
    id: str
    name: str
    description: str
    target_audience: str
    ai_description: str | None = None
    created_at: str


class AiDescriptionResponse(BaseModel):
    product_id: str
    ai_description: str
    actual_api_called: bool
    provider: str
    model: str


class ServiceLogResponse(BaseModel):
    id: str
    action: str
    status: str
    detail: str | None = None
    created_at: str
