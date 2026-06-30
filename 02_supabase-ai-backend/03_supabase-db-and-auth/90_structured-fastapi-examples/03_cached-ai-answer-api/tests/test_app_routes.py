from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_route_is_ready() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_openapi_has_cache_routes() -> None:
    schema = client.get("/openapi.json").json()
    assert "/ai/mock-answer" in schema["paths"]
    assert "/ai/mock-answer-cache" in schema["paths"]
