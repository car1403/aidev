# API Design Document

이 문서는 FastAPI 엔드포인트 설계 문서입니다.

## 1. API 설계 원칙

- URL은 리소스 중심으로 작성합니다.
- HTTP Method는 의미에 맞게 사용합니다.
- Request/Response는 Pydantic 모델 기준으로 설명합니다.
- 에러 응답 형식을 통일합니다.
- 4xx/5xx 상황별 처리 규칙을 문서화합니다.
- 문서에 적은 endpoint는 실제 FastAPI 코드와 Streamlit 호출 코드에 모두 존재해야 합니다.

## 2. Endpoint Summary

| Method | Path | Resource | Description | Request Model | Response Model |
| --- | --- | --- | --- | --- | --- |
| GET | `/health` | health | 서버 상태 확인 | - | `HealthResponse` |
| GET | `/api/logs` | logs | 로그 목록 조회 | query params | `LogListResponse` |
| POST | `/api/logs` | logs | 로그 생성 | `LogCreateRequest` | `LogResponse` |
| GET | `/api/logs/{log_id}` | logs | 로그 상세 조회 | path param | `LogResponse` |
| PUT | `/api/logs/{log_id}` | logs | 로그 수정 | `LogUpdateRequest` | `LogResponse` |
| DELETE | `/api/logs/{log_id}` | logs | 로그 삭제 | path param | `DeleteResponse` |
| GET | `/api/dashboard/summary` | dashboard | 대시보드 요약 지표 조회 | query params | `DashboardSummaryResponse` |
| POST | `/api/feedback` | feedback | 사용자 피드백 저장 | `FeedbackCreateRequest` | `FeedbackResponse` |
| POST | `/api/chat` | chat | AI 응답 일괄 생성 | `ChatRequest` | `ChatResponse` |
| POST | `/api/chat/stream` | chat | SSE 기반 AI 응답 스트리밍 | `ChatRequest` | `text/event-stream` |

## 2-1. Endpoint Naming Checklist

- [ ] URL은 동사가 아니라 리소스명 중심으로 작성했습니다. 예: `/api/logs`, `/api/feedback`
- [ ] 단건 조회, 수정, 삭제는 path parameter를 사용했습니다. 예: `/api/logs/{log_id}`
- [ ] 검색, 필터, 페이지네이션은 query parameter를 사용했습니다.
- [ ] HTTP Method는 의미에 맞게 사용했습니다.
- [ ] Streamlit 화면에서 호출하는 API 경로와 문서의 API 경로가 일치합니다.

## 3. Pydantic Models

### LogCreateRequest

| Field | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| user_id | string | optional | `user-001` | 사용자 식별자 |
| event_type | string | required | `ai_response` | 로그 유형 |
| message | string | required | `AI 응답 생성 완료` | 로그 메시지 |
| status | string | required | `success` | 처리 상태 |
| metadata | object | optional | `{ "latency_ms": 1200 }` | 추가 정보 |

### ErrorResponse

모든 에러 응답은 아래 형식을 따릅니다.

```json
{
 "error": {
 "code": "LOG_NOT_FOUND",
 "message": "요청한 로그를 찾을 수 없습니다.",
 "detail": {
 "log_id": 10
 }
 }
}
```

## 4. Error Rules

| Status Code | Error Code | Situation | Handling Rule |
| --- | --- | --- | --- |
| 400 | `INVALID_REQUEST` | 요청 형식이 잘못됨 | 입력값과 필수 필드를 안내 |
| 404 | `LOG_NOT_FOUND` | 로그가 존재하지 않음 | 빈 화면 또는 안내 메시지 표시 |
| 422 | `VALIDATION_ERROR` | Pydantic 검증 실패 | 필드별 오류를 표시 |
| 500 | `INTERNAL_ERROR` | 서버 내부 오류 | 사용자에게 일반 오류 메시지 표시, 상세 로그 저장 |

## 4-1. Standard Error Response Checklist

- [ ] 모든 에러 응답에 HTTP Status Code가 명확합니다.
- [ ] 에러 코드, 메시지, 상세 정보가 분리되어 있습니다.
- [ ] 4xx 오류는 사용자 입력 또는 권한 문제로 설명되어 있습니다.
- [ ] 5xx 오류는 서버 내부 오류로 설명되어 있고, 서비스 로그 저장 규칙이 있습니다.
- [ ] Streamlit 화면에서 에러 메시지를 사용자에게 이해 가능한 문장으로 표시합니다.

## 5. Nested JSON Rule

중첩 JSON은 문자열로 뭉개지 않고 nested 모델로 표현합니다.

```json
{
 "event_type": "ai_response",
 "metadata": {
 "model": "gpt",
 "latency_ms": 1200,
 "token_usage": {
 "input": 100,
 "output": 250
 }
 }
}
```

## 6. Final API Review Checklist

- [ ] Request 모델과 Response 모델이 모두 문서화되어 있습니다.
- [ ] 필수 필드와 선택 필드가 구분되어 있습니다.
- [ ] 타입 힌트와 예시값이 있습니다.
- [ ] nested JSON은 nested model 또는 명확한 JSON 예시로 표현되어 있습니다.
- [ ] Swagger UI에서 주요 API를 테스트했습니다.
- [ ] Postman 또는 Streamlit 화면에서 주요 API를 호출해 보았습니다.
