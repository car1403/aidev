# API Design

최종 프로젝트의 endpoint, HTTP Method, 요청/응답 모델, 오류 응답 형식을 작성합니다.

## 필수 API

| Method | URL | 설명 |
| --- | --- | --- |
| GET | `/health` | 서버 상태 확인 |
| POST | `/qa` | 사용자 질문 등록 및 AI 답변 생성 |
| GET | `/qa` | 질문/답변 목록 조회 |
| GET | `/qa/{id}` | 질문/답변 단건 조회 |
| GET | `/service-logs` | 서비스 로그 조회 |

## 선택 API

| Method | URL | 설명 |
| --- | --- | --- |
| POST | `/feedback` | AI 답변에 대한 사용자 피드백 저장 |
| GET | `/profiles/{user_id}` | 사용자 프로필 조회 |
| POST | `/cache/test` | Upstash Redis 캐시 동작 확인 |

## 작성할 내용

각 API마다 아래 항목을 작성합니다.

```text
목적:
HTTP Method:
URL:
Request Body:
Response Body:
성공 Status Code:
오류 Status Code:
Supabase 테이블:
서비스 로그 저장 여부:
```

## 예시

```text
POST /qa

목적:
사용자 질문을 받고 AI 답변을 생성한 뒤 Supabase에 저장한다.

Request Body:
{
  "user_id": "student01",
  "question": "FastAPI에서 Pydantic은 왜 사용하나요?",
  "model": "mock-teacher"
}

Response Body:
{
  "item": {
    "id": "...",
    "question": "...",
    "answer": "...",
    "model": "mock-teacher"
  }
}
```
