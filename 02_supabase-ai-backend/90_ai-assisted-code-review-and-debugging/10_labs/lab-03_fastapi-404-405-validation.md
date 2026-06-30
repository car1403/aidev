# Lab 03. FastAPI 404, 405, 422

## 목표

Swagger와 브라우저에서 자주 만나는 FastAPI 오류를 구분합니다.

| 상태 코드 | 의미 | 예 |
| --- | --- | --- |
| 404 | 해당 주소의 endpoint가 없음 | `/ai/chat`이 없는데 접속함 |
| 405 | 주소는 있지만 HTTP Method가 다름 | POST endpoint를 브라우저 주소창에서 GET으로 호출함 |
| 422 | 요청 Body가 Pydantic 모델과 맞지 않음 | 필수 필드 누락, 빈 문자열 |

## 확인 방법

POST endpoint는 브라우저 주소창이 아니라 Swagger UI에서 실행합니다.

```text
http://127.0.0.1:8000/docs
```
