import os  # 운영체제 환경변수에서 API 주소나 비밀 키를 읽기 위해 os 모듈을 가져옵니다.

from fastapi import FastAPI  # FastAPI 서버 생성, 라우팅, HTTP 오류 응답에 필요한 클래스를 가져옵니다.

APP_NAME = os.getenv("APP_NAME", "FastAPI App")  # 환경변수 값을 읽어 설정값으로 저장합니다. 코드에 비밀 값을 직접 쓰지 않기 위한 방식입니다.

app = FastAPI(title=APP_NAME)  # FastAPI 서버 객체를 생성합니다. 이후 데코레이터로 API 경로를 이 객체에 등록합니다.


@app.get("/health")  # HTTP GET 요청을 처리할 API 엔드포인트를 등록합니다.
def health_check():  # 서버와 외부 연결 상태를 확인하는 health check 요청을 처리합니다.
    return {"status": "ok", "app": APP_NAME}  # API 클라이언트가 받을 JSON 형태의 응답 데이터를 반환합니다.


@app.get("/api/message")  # HTTP GET 요청을 처리할 API 엔드포인트를 등록합니다.
def get_message():  # 저장된 데이터를 조회하는 요청을 처리합니다.
    return {"message": "FastAPI is running locally."}  # API 클라이언트가 받을 JSON 형태의 응답 데이터를 반환합니다.

