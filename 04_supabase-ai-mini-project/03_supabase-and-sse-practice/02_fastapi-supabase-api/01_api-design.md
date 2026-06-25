# 01. API 설계

API를 만들기 전에 먼저 어떤 리소스를 다룰지 정합니다.

이 프로젝트에서는 대화형 AI 서비스의 기본 데이터를 아래처럼 나눕니다.

```text
conversation
-> 대화방 또는 대화 묶음

message
-> 사용자의 질문과 AI의 답변

service_log
-> API 실행 상태, 오류, 주요 이벤트

feedback
-> 사용자가 남긴 응답 평가
```

## URL 이름 규칙

URL은 동사보다 리소스 이름을 중심으로 작성합니다.

좋은 예시:

```text
GET /api/conversations
POST /api/conversations
GET /api/conversations/{conversation_id}/messages
POST /api/conversations/{conversation_id}/messages
```

피하는 예시:

```text
GET /api/getConversationList
POST /api/saveMessage
```

## 응답 형식 예시

```json
{
  "ok": true,
  "data": {
    "id": "conversation-id",
    "title": "학습 기록 대화"
  }
}
```

오류 응답은 아래처럼 통일합니다.

```json
{
  "ok": false,
  "error": {
    "code": "SUPABASE_INSERT_FAILED",
    "message": "데이터 저장 중 오류가 발생했습니다."
  }
}
```

## 설계 기준

- URL은 리소스 중심으로 작성합니다.
- `GET`은 조회, `POST`는 생성, `PUT` 또는 `PATCH`는 수정, `DELETE`는 삭제에 사용합니다.
- 요청 데이터는 Pydantic 모델로 검증합니다.
- 오류 응답 형식은 한 가지로 통일합니다.
