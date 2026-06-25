# API Spec Template

FastAPI API 설계 문서 템플릿입니다.

## 1. API 기본 정보

```text
Base URL:
예: http://127.0.0.1:8000
```

## 2. 공통 응답 형식

성공 응답:

```json
{
  "ok": true,
  "data": {}
}
```

오류 응답:

```json
{
  "ok": false,
  "error": {
    "code": "ERROR_CODE",
    "message": "사용자가 이해할 수 있는 오류 메시지"
  }
}
```

## 3. API 목록

| Method | URL | 설명 | 요청 Body | 응답 |
| --- | --- | --- | --- | --- |
| GET | `/health` | 서버 상태 확인 | 없음 | 상태 정보 |
| GET | `/api/logs` | 로그 목록 조회 | 없음 | 로그 목록 |
| POST | `/api/logs` | 로그 생성 | 로그 정보 | 생성된 로그 |
| GET | `/api/logs/{log_id}` | 로그 상세 조회 | 없음 | 로그 상세 |
| POST | `/api/feedbacks` | 피드백 저장 | 피드백 정보 | 저장 결과 |
| POST | `/api/chat` | 일반 AI 응답 | 질문 | AI 응답 |
| POST | `/api/chat/stream` | SSE AI 응답 | 질문 | 스트리밍 응답 |

## 4. 엔드포인트 상세

### GET /health

목적:

```text
FastAPI 서버가 실행 중인지 확인합니다.
```

응답 예시:

```json
{
  "ok": true,
  "data": {
    "status": "healthy"
  }
}
```

### POST /api/logs

요청 예시:

```json
{
  "action": "chat_request",
  "status": "success",
  "metadata": {
    "model": "gemini-2.5-flash-lite"
  }
}
```

응답 예시:

```json
{
  "ok": true,
  "data": {
    "id": "generated-log-id"
  }
}
```

## 5. 오류 코드

| 코드 | 의미 | 처리 방법 |
| --- | --- | --- |
| SUPABASE_SELECT_FAILED | Supabase 조회 실패 | key, 테이블, RLS 확인 |
| SUPABASE_INSERT_FAILED | Supabase 저장 실패 | 요청 데이터와 테이블 컬럼 확인 |
| AI_API_FAILED | AI API 호출 실패 | API key와 요청 제한 확인 |
| VALIDATION_FAILED | 입력 데이터 검증 실패 | 요청 Body 확인 |
