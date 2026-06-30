from fastapi.testclient import TestClient

from app.main import app
from app.services.memory_store import logs


client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_create_and_list_logs() -> None:
    logs.clear()

    payload = {
        "level": "info",
        "source": "test",
        "message": "테스트 로그입니다.",
        "request_path": "/test",
        "status_code": 200,
        "latency_ms": 10,
        "metadata": {"test": True},
    }

    create_response = client.post("/logs", json=payload)
    assert create_response.status_code == 200
    assert create_response.json()["message"] == "테스트 로그입니다."

    list_response = client.get("/logs")
    assert list_response.status_code == 200
    assert len(list_response.json()) >= 1


def test_log_summary() -> None:
    response = client.get("/logs/summary")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
