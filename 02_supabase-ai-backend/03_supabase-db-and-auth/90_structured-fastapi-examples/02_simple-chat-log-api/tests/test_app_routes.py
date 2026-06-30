from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_route_is_ready() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_openapi_has_chat_routes() -> None:
    schema = client.get("/openapi.json").json()
    assert "/chat" in schema["paths"]
    assert "/logs" in schema["paths"]
