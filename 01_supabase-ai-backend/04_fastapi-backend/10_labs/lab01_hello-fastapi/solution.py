"""Lab 01 solution: FastAPI 서버 시작하기."""

from fastapi import FastAPI


app = FastAPI(title="Lab 01 Hello FastAPI")


@app.get("/")
def read_root():
    """첫 화면 API입니다."""

    return {"message": "Hello FastAPI"}


@app.get("/health")
def health_check():
    """서버가 정상 실행 중인지 확인합니다."""

    return {"status": "ok"}
