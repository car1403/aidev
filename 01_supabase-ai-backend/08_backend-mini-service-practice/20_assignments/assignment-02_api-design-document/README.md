# Assignment 02. API Design Document

## 목표

미니 서비스에서 사용할 API를 설계 문서로 정리합니다.

## 참고 파일

```text
../02_api-design/README.md
../02_api-design/api-design.md
```

## 설계할 API

```text
GET /health
POST /questions
GET /questions
GET /questions/{question_id}
POST /service-logs
GET /service-logs
```

## 제출 내용

각 API마다 아래 항목을 작성합니다.

| 항목 | 설명 |
| --- | --- |
| HTTP Method | `GET`, `POST` 등 |
| URL | `/questions` 같은 엔드포인트 |
| 목적 | 이 API가 하는 일 |
| Request Body | 요청 JSON 예시 |
| Response Body | 정상 응답 JSON 예시 |
| Error Response | 오류 응답 JSON 예시 |
| 저장 테이블 | 사용하는 Supabase 테이블 |

## POST /questions 예시

```json
{
  "user_id": "student01",
  "question": "FastAPI에서 Pydantic은 왜 사용하나요?",
  "model": "mock-teacher"
}
```

## 완료 기준

- API URL이 리소스 중심으로 작성되어 있습니다.
- 요청/응답 JSON 예시가 있습니다.
- 오류 응답 형식이 `ok`, `error.code`, `error.message` 기준으로 정리되어 있습니다.
- API와 Supabase 테이블 연결이 설명되어 있습니다.
