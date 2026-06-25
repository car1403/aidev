"""Docker Compose에서 실행할 backend API 서비스입니다."""

from fastapi import FastAPI


app = FastAPI(title="Multi Service Backend")


@app.get("/health")
def health() -> dict[str, str]:
    """backend 컨테이너의 정상 실행 여부를 반환합니다."""

    return {"status": "ok", "service": "backend"}


@app.get("/agent/status")
def agent_status() -> dict[str, str]:
    """worker나 monitor가 확인할 수 있는 Agent 상태 예시입니다."""

    return {
        "agent": "ops_agent",
        "status": "ready",
        "message": "Docker Compose 기반 멀티 서비스가 준비되었습니다.",
    }
