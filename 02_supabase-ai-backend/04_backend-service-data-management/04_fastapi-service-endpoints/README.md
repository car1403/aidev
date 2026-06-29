# 04_fastapi-service-endpoints

이 챕터는 앞에서 학습한 사용자 프로필, 대화 이력, 서비스 로그를 FastAPI endpoint로 묶는 단계입니다.

`01_user-profile-data`, `02_conversation-history`, `03_service-logs`에서는 각각 데이터를 따로 다루었습니다. 이번 챕터에서는 그 기능들을 하나의 백엔드 API 형태로 연결합니다.

이 챕터의 endpoint는 LLM을 직접 호출하지 않습니다. 대신 앞 단원의 `02_llm-api-integration/05_fastapi-llm-endpoint/03_gemini_sdk_endpoint.py`에서 생성한 응답을 저장할 수 있도록 대화 메시지와 서비스 로그 구조를 준비합니다.

## 이 챕터에서 만드는 endpoint

| Method | URL | 설명 |
|---|---|---|
| `GET` | `/health` | 서버 상태 확인 |
| `GET` | `/profiles/{user_id}` | 사용자 프로필 조회 |
| `POST` | `/conversations` | 새 대화 묶음 생성 |
| `POST` | `/conversations/{conversation_id}/messages` | 대화에 메시지 추가 |
| `GET` | `/conversations/{conversation_id}/messages` | 특정 대화의 메시지 조회 |
| `POST` | `/service-logs` | 서비스 로그 저장 |

## mock 버전과 Supabase 버전의 차이

| 파일 | 저장 위치 | 사용 목적 |
|---|---|---|
| `main_mock.py` | 메모리 dict/list | Supabase 없이 API 구조와 Swagger UI를 먼저 연습 |
| `main_supabase.py` | Supabase 테이블 | 실제 `profiles`, `conversations`, `messages`, `service_logs` 테이블에 저장 |

처음에는 `main_mock.py`로 API 요청/응답 흐름을 익히고, 이후 `.env`와 Supabase 테이블이 준비되면 `main_supabase.py`로 넘어갑니다.

## 실행 전 준비

가상환경을 활성화합니다.

```powershell
cd C:\aidev\02_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
```

Supabase 버전을 실행하려면 아래 SQL 파일을 Supabase Dashboard의 SQL Editor에서 먼저 실행합니다.

```text
C:\aidev\02_supabase-ai-backend\03_supabase-db-and-auth\00_references\supabase-schema.sql
```

## mock 서버 실행

```powershell
cd C:\aidev\02_supabase-ai-backend\04_backend-service-data-management\04_fastapi-service-endpoints
..\..\.venv\Scripts\Activate.ps1
uvicorn main_mock:app --reload --host 127.0.0.1 --port 8003
```

Swagger UI:

```text
http://127.0.0.1:8003/docs
```

## Supabase 서버 실행

```powershell
cd C:\aidev\02_supabase-ai-backend\04_backend-service-data-management\04_fastapi-service-endpoints
..\..\.venv\Scripts\Activate.ps1
uvicorn main_supabase:app --reload --host 127.0.0.1 --port 8004
```

Swagger UI:

```text
http://127.0.0.1:8004/docs
```

## 추천 실습 순서

1. `GET /health`로 서버가 실행 중인지 확인합니다.
2. `GET /profiles/student01`을 호출해 mock 프로필 조회를 확인합니다.
3. `POST /conversations`로 새 대화를 만듭니다.
4. 응답에 나온 `id` 값을 복사합니다.
5. `POST /conversations/{conversation_id}/messages`로 user 메시지를 추가합니다.
6. 같은 endpoint로 assistant 메시지도 추가합니다.
7. `GET /conversations/{conversation_id}/messages`로 메시지 목록을 확인합니다.
8. `POST /service-logs`로 로그 저장 구조를 확인합니다.

## 요청 예시

`POST /conversations`

```json
{
  "user_id": "student01",
  "title": "FastAPI 질문"
}
```

`POST /conversations/{conversation_id}/messages`

```json
{
  "role": "user",
  "content": "대화 이력은 왜 저장하나요?"
}
```

`POST /service-logs`

```json
{
  "event_type": "ai.answer.created",
  "message": "AI 응답 생성 결과가 저장되었습니다.",
  "metadata": {
    "endpoint": "/ai/chat",
    "status_code": 200,
    "provider": "gemini",
    "model": "gemini-2.5-flash-lite",
    "actual_api_called": false,
    "llm_call_mode": "mock-first"
  }
}
```

## 확인 기준

- mock 서버에서 API 요청/응답 흐름을 Swagger UI로 확인할 수 있습니다.
- Supabase 서버에서는 실제 테이블에 데이터가 저장됩니다.
- `conversation_id`를 기준으로 메시지가 연결됩니다.
- 서비스 로그에는 민감 정보가 아니라 운영에 필요한 요약 정보만 저장됩니다.
- LLM 응답 저장 로그에는 `provider`, `model`, `actual_api_called`, `llm_call_mode`가 포함됩니다.

## 정리 질문

- mock 서버를 먼저 실행해 보는 이유는 무엇인가요?
- endpoint 안에서 모든 코드를 작성하는 방식은 언제 불편해질까요?
- Supabase에 저장할 데이터와 Upstash Redis에 저장할 데이터는 어떻게 구분하나요?
- 이 endpoint 구조를 `04_supabase-ai-mini-project`의 통합 챗봇 서비스로 확장한다면 어떤 API가 더 필요할까요?
