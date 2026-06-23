# API Design

이 문서는 `AI 질문 응답 백엔드 미니 서비스`의 API 설계서입니다.

요구사항 문서에서 정한 기능을 FastAPI 엔드포인트로 옮기기 위한 기준 문서입니다.

## 1. 공통 응답 구조

### 정상 응답

단일 데이터를 반환할 때는 `item`을 사용합니다.

```json
{
  "ok": true,
  "item": {
    "id": "question-001"
  }
}
```

여러 데이터를 반환할 때는 `items`를 사용합니다.

```json
{
  "ok": true,
  "items": []
}
```

### 오류 응답

오류가 발생하면 `ok: false`와 `error` 객체를 반환합니다.

```json
{
  "ok": false,
  "error": {
    "code": "question_required",
    "message": "질문 내용은 비어 있을 수 없습니다."
  }
}
```

## 2. GET /health

서버가 정상 실행 중인지 확인합니다.

### Request

요청 본문이 없습니다.

### Response

```json
{
  "ok": true,
  "status": "healthy",
  "service": "backend-mini-service"
}
```

### 사용 상황

- 서버 실행 확인
- Swagger UI 테스트 시작 전 확인
- 배포 후 헬스 체크

## 3. POST /questions

사용자의 질문을 받고 AI 답변을 생성합니다.

처음에는 외부 LLM API를 바로 호출하지 않고 mock LLM 함수로 답변을 생성합니다. 이렇게 하면 API 구조와 저장 흐름을 먼저 안정적으로 확인할 수 있습니다.

### Request Body

```json
{
  "user_id": "student01",
  "question": "FastAPI에서 Pydantic은 왜 사용하나요?",
  "model": "mock-teacher"
}
```

### 요청 필드 기준

| 필드 | 타입 | 필수 | 설명 |
| --- | --- | --- | --- |
| `user_id` | string | 필수 | 질문을 보낸 사용자 id |
| `question` | string | 필수 | 사용자의 질문 내용 |
| `model` | string | 선택 | 사용할 모델 이름, 기본값은 `mock-teacher` |

### Response Body

```json
{
  "ok": true,
  "item": {
    "id": "question-001",
    "user_id": "student01",
    "question": "FastAPI에서 Pydantic은 왜 사용하나요?",
    "answer": "Pydantic은 요청 데이터 검증과 응답 구조 정의를 쉽게 하기 위해 사용합니다.",
    "model": "mock-teacher",
    "created_at": "2026-06-23T10:00:00Z"
  }
}
```

### 처리 흐름

```text
요청 수신
-> user_id 검증
-> question 검증
-> mock LLM 답변 생성
-> 질문/답변 저장
-> 서비스 로그 저장
-> 응답 반환
```

## 4. GET /questions

저장된 질문/답변 목록을 조회합니다.

### Query Parameters

| 이름 | 필수 | 설명 |
| --- | --- | --- |
| `user_id` | 선택 | 특정 사용자의 질문만 조회할 때 사용 |
| `limit` | 선택 | 조회할 최대 개수, 기본값 예: 20 |

### Request 예시

```text
GET /questions?user_id=student01&limit=10
```

### Response Body

```json
{
  "ok": true,
  "items": [
    {
      "id": "question-001",
      "user_id": "student01",
      "question": "FastAPI에서 Pydantic은 왜 사용하나요?",
      "answer": "Pydantic은 요청 데이터 검증과 응답 구조 정의를 쉽게 하기 위해 사용합니다.",
      "model": "mock-teacher",
      "created_at": "2026-06-23T10:00:00Z"
    }
  ]
}
```

## 5. GET /questions/{question_id}

질문/답변 1개를 조회합니다.

### Path Parameters

| 이름 | 설명 |
| --- | --- |
| `question_id` | 조회할 질문/답변 기록 id |

### Response Body

```json
{
  "ok": true,
  "item": {
    "id": "question-001",
    "user_id": "student01",
    "question": "FastAPI에서 Pydantic은 왜 사용하나요?",
    "answer": "Pydantic은 요청 데이터 검증과 응답 구조 정의를 쉽게 하기 위해 사용합니다.",
    "model": "mock-teacher",
    "created_at": "2026-06-23T10:00:00Z"
  }
}
```

### 데이터가 없을 때

```json
{
  "ok": false,
  "error": {
    "code": "question_not_found",
    "message": "질문 기록을 찾을 수 없습니다."
  }
}
```

## 6. POST /service-logs

서비스 로그를 저장합니다.

실제 구현에서는 질문 생성 API 내부에서 자동으로 로그를 저장할 수 있습니다. 하지만 API 설계 연습을 위해 로그 저장 엔드포인트를 따로 설계해 봅니다.

### Request Body

```json
{
  "event_type": "question_created",
  "message": "질문 답변 생성 성공",
  "metadata": {
    "user_id": "student01",
    "question_id": "question-001",
    "duration_ms": 120
  }
}
```

### Response Body

```json
{
  "ok": true,
  "item": {
    "id": "log-001",
    "event_type": "question_created",
    "message": "질문 답변 생성 성공"
  }
}
```

## 7. GET /service-logs

서비스 로그 목록을 조회합니다.

### Query Parameters

| 이름 | 필수 | 설명 |
| --- | --- | --- |
| `event_type` | 선택 | 특정 로그 종류만 조회 |
| `limit` | 선택 | 조회할 최대 개수 |

### Response Body

```json
{
  "ok": true,
  "items": [
    {
      "id": "log-001",
      "event_type": "question_created",
      "message": "질문 답변 생성 성공",
      "metadata": {
        "user_id": "student01",
        "duration_ms": 120
      },
      "created_at": "2026-06-23T10:00:00Z"
    }
  ]
}
```

## 8. HTTP Status Code 기준

| 상황 | Status Code | 오류 코드 예시 | 설명 |
| --- | --- | --- | --- |
| 정상 처리 | 200 | 없음 | 조회 또는 처리 성공 |
| 생성 성공 | 201 | 없음 | 질문/로그 생성 성공 |
| 요청 검증 실패 | 422 | `question_required` | 입력값이 올바르지 않음 |
| 데이터 없음 | 404 | `question_not_found` | 요청한 데이터가 없음 |
| 환경 설정 누락 | 500 | `server_config_error` | Supabase URL/Key 등 설정 누락 |
| 외부 저장 실패 | 502 | `storage_error` | Supabase 등 외부 저장소 처리 실패 |

## 9. Pydantic 모델로 옮길 항목

다음 단계에서 `schemas.py`를 작성할 때 아래 모델로 옮길 수 있습니다.

| 모델 이름 | 용도 |
| --- | --- |
| `QuestionCreateRequest` | `POST /questions` 요청 검증 |
| `QuestionResponse` | 질문/답변 응답 구조 |
| `QuestionListResponse` | 질문/답변 목록 응답 구조 |
| `ServiceLogCreateRequest` | `POST /service-logs` 요청 검증 |
| `ErrorResponse` | 오류 응답 구조 |

## 10. 완료 체크리스트

- [ ] API URL이 리소스 중심으로 작성되어 있다.
- [ ] HTTP Method가 기능에 맞게 사용되어 있다.
- [ ] 요청 JSON 예시가 있다.
- [ ] 응답 JSON 예시가 있다.
- [ ] 오류 응답 형식이 통일되어 있다.
- [ ] HTTP Status Code 기준이 정리되어 있다.
- [ ] 다음 구현 단계에서 만들 Pydantic 모델이 정리되어 있다.
