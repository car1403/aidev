import os

from fastapi.testclient import TestClient

from app.main import app


def test_product_ai_description_flow():
    os.environ["SUPABASE_URL"] = ""
    os.environ["SUPABASE_SERVICE_ROLE_KEY"] = ""

    client = TestClient(app)

    health = client.get("/health")
    assert health.status_code == 200
    assert health.json()["storage"] == "memory"

    product = client.post(
        "/products",
        json={
            "name": "AI 노트",
            "description": "학습 내용을 정리하는 노트",
            "target_audience": "입문자",
        },
    )
    assert product.status_code == 200

    product_id = product.json()["id"]
    ai_response = client.post(f"/products/{product_id}/ai-description")
    assert ai_response.status_code == 200
    assert ai_response.json()["actual_api_called"] is False

    logs = client.get("/service-logs")
    assert logs.status_code == 200
    assert len(logs.json()) >= 2
