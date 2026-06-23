# API Design

최종 프로젝트의 endpoint, HTTP Method, 요청/응답 모델, 오류 응답 형식을 작성합니다.

API 설계는 코드 작성 전에 먼저 정리하는 약속입니다. URL은 리소스 중심으로 이름을 붙이고, HTTP Method는 의미에 맞게 사용합니다.

## 필수 API

| Method | URL | 설명 |
| --- | --- | --- |
| GET | `/health` | 서버 상태 확인 |
| POST | `/questions` | 사용자 질문 등록 및 AI 답변 생성 |
| GET | `/questions` | 질문/답변 목록 조회 |
| GET | `/questions/{question_id}` | 질문/답변 단건 조회 |
| GET | `/service-logs` | 서비스 로그 조회 |

## 선택 API

| Method | URL | 설명 |
| --- | --- | --- |
| POST | `/feedback` | AI 답변에 대한 사용자 평가 저장 |
| GET | `/profiles/{user_id}` | 사용자 프로필 조회 |
| POST | `/service-logs` | 별도 로그 저장 endpoint가 필요한 경우 사용 |

## 요청/응답 설계 기준

- 정상 응답은 `ok: true`를 포함합니다.
- 단건 응답은 `item`을 사용합니다.
- 목록 응답은 `items`를 사용합니다.
- 오류 응답은 `ok: false`, `error.code`, `error.message` 형식을 사용합니다.
- 요청/응답 모델은 Pydantic 모델과 일치해야 합니다.

## `POST /questions` 요청 예시

```json
{
  "user_id": "user-001",
  "question": "FastAPI에서 Pydantic을 왜 사용하나요?",
  "provider": "gemini",
  "model": "gemini-2.5-flash-lite"
}
```

## `POST /questions` 응답 예시

```json
{
  "ok": true,
  "item": {
    "id": "question-001",
    "user_id": "user-001",
    "question": "FastAPI에서 Pydantic을 왜 사용하나요?",
    "answer": "요청 데이터 검증과 응답 구조 정의를 쉽게 하기 위해 사용합니다.",
    "provider": "gemini",
    "model": "gemini-2.5-flash-lite",
    "actual_api_called": false,
    "llm_call_mode": "mock-first",
    "created_at": "2026-06-23T10:00:00Z"
  }
}
```

## 오류 응답 예시

```json
{
  "ok": false,
  "error": {
    "code": "question_required",
    "message": "질문 내용은 비어 있을 수 없습니다."
  }
}
```

## API 설계 체크리스트

- [ ] URL이 리소스 중심으로 작성되었습니다.
- [ ] HTTP Method가 의미에 맞습니다.
- [ ] 요청 JSON과 응답 JSON 예시가 있습니다.
- [ ] 오류 응답 형식이 통일되어 있습니다.
- [ ] Pydantic 모델과 응답 예시가 일치합니다.
- [ ] `provider`, `model`, `actual_api_called`, `llm_call_mode`로 mock-first와 실제 Gemini SDK 호출을 구분합니다.
- [ ] Swagger UI에서 테스트할 수 있습니다.
