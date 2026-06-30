from fastapi.testclient import TestClient

from app.main import app
from app.services.memory_store import reset_store


def test_auth_chat_log_flow():
    reset_store()
    client = TestClient(app)

    health = client.get("/health")
    assert health.status_code == 200

    signup = client.post(
        "/auth/signup",
        json={
            "email": "student@example.com",
            "password": "pass1234",
            "display_name": "수강생",
        },
    )
    assert signup.status_code == 200

    signin = client.post(
        "/auth/signin",
        json={
            "email": "student@example.com",
            "password": "pass1234",
        },
    )
    assert signin.status_code == 200
    token = signin.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    me = client.get("/me", headers=headers)
    assert me.status_code == 200
    assert me.json()["email"] == "student@example.com"

    chat = client.post("/chat", headers=headers, json={"message": "오늘 배운 내용을 요약해줘"})
    assert chat.status_code == 200
    assert chat.json()["actual_api_called"] is False

    conversations = client.get("/conversations", headers=headers)
    assert conversations.status_code == 200
    assert len(conversations.json()) == 1

    logs = client.get("/service-logs", headers=headers)
    assert logs.status_code == 200
    assert len(logs.json()) >= 3

    signout = client.post("/auth/signout", headers=headers)
    assert signout.status_code == 200
