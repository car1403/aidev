"""Lab 01 starter: FastAPI 서버 시작하기."""

from fastapi import FastAPI


# TODO: title 값을 원하는 이름으로 바꿔 보세요.
app = FastAPI(title="Lab 01 Starter")


@app.get("/health")
def health_check():
    """서버 상태를 확인하는 API입니다."""

    # TODO: status 값이 ok가 되도록 수정해 보세요.
    return {"status": "TODO"}
