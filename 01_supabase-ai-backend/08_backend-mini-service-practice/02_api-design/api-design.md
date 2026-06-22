# API Design

## POST /qa

사용자의 질문을 받고 AI 답변을 생성합니다.

### Request Body

```json
{
 "user_id": "student01",
 "question": "FastAPI에서 Pydantic은 왜 사용하나요?",
 "model": "mock-teacher"
}
```

### Response Body

```json
{
 "item": {
 "id": "qa-001",
 "user_id": "student01",
 "question": "FastAPI에서 Pydantic은 왜 사용하나요?",
 "answer": "요청 검증과 응답 모델 정의를 쉽게 하기 위해 사용합니다.",
 "model": "mock-teacher"
 }
}
```

## GET /qa

저장된 질문/답변 목록을 조회합니다.

## GET /qa/{item_id}

질문/답변 1개를 조회합니다.

## GET /service-logs

서비스 처리 로그를 조회합니다.

## 공통 설계 기준

- URL은 리소스 중심으로 작성합니다.
- 요청 데이터는 Pydantic 모델로 검증합니다.
- 응답은 `{"item":...}` 또는 `{"items": [...]}` 형태로 통일합니다.
- 오류 상황은 HTTP status code와 메시지로 명확히 표현합니다.
