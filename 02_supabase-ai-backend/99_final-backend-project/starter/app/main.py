from fastapi import FastAPI

app = FastAPI(title="Final Backend Project Starter")


@app.get("/health")
def health() -> dict[str, str]:
    """프로젝트 서버가 정상 실행 중인지 확인하는 가장 작은 API입니다."""
    return {
        "status": "ok",
        "message": "final project starter is running",
    }
