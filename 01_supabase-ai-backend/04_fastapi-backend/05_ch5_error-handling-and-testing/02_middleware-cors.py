"""CORS 미들웨어 예제.

CORS는 브라우저에서 다른 주소의 API를 호출할 때 적용되는 보안 규칙입니다.
예를 들어 Streamlit 화면이 localhost:8501에서 실행되고,
FastAPI 서버가 localhost:8000에서 실행되면 출처(origin)가 다릅니다.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="CORS Middleware Practice")


# 수업에서는 로컬 개발 주소만 허용합니다.
# 실제 운영에서는 "*"로 전체 허용하지 말고 필요한 도메인만 명시합니다.
allowed_origins = [
    "http://localhost:8501",
    "http://127.0.0.1:8501",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check():
    """프론트엔드에서 백엔드 연결 상태를 확인할 때 사용할 수 있습니다."""

    return {"status": "ok", "cors": "enabled"}
