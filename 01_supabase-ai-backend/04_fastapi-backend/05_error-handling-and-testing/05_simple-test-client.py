"""FastAPI TestClient 예제.

TestClient는 실제 서버를 uvicorn으로 띄우지 않고도 API를 호출해 볼 수 있게 해줍니다.
초보자는 먼저 "API를 코드로 테스트할 수 있다"는 개념을 이해하면 됩니다.
"""

from fastapi.testclient import TestClient

from app_for_test import app


# TestClient는 브라우저나 Postman 대신 API를 호출해 주는 테스트 도구입니다.
client = TestClient(app)


def test_health_check():
    """GET /health가 정상 응답하는지 확인합니다."""

    response = client.get("/health")

    print("GET /health")
    print("status_code:", response.status_code)
    print("json:", response.json())


def test_create_message():
    """POST /messages가 요청 body를 처리하는지 확인합니다."""

    response = client.post("/messages", json={"text": "hello fastapi"})

    print("\nPOST /messages")
    print("status_code:", response.status_code)
    print("json:", response.json())


if __name__ == "__main__":
    test_health_check()
    test_create_message()
