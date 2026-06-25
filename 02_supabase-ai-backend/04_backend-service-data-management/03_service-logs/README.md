# 03_service-logs

이 챕터는 AI 백엔드 서비스에서 서비스 로그를 어떻게 설계하고 저장할지 학습합니다.

서비스 로그는 사용자가 직접 보는 데이터가 아니라, 서비스가 잘 동작하는지 확인하고 문제가 생겼을 때 원인을 찾기 위한 기록입니다. AI 서비스에서는 답변 내용만 저장하는 것보다 “어떤 요청이 성공했는지, 실패했는지, 얼마나 오래 걸렸는지”를 함께 남기는 것이 중요합니다.

앞 단원인 `02_llm-api-integration`에서는 LLM 호출 흐름을 `mock-first -> Gemini SDK 기본 구현 -> REST 보충 -> OpenAI 선택 비교`로 정리했습니다. 따라서 이 챕터의 서비스 로그는 mock 응답과 Gemini SDK 응답을 모두 기록할 수 있는 구조로 설계합니다.

## 서비스 로그가 필요한 이유

서비스 로그는 아래 상황에서 필요합니다.

```text
API가 정상 호출되었는지 확인
오류가 발생한 endpoint 확인
AI 응답 생성 시간이 너무 긴지 확인
어떤 모델 또는 기능에서 문제가 자주 생기는지 확인
서비스 품질 개선을 위한 운영 데이터 수집
```

## service_logs 테이블 구조

`03_supabase-db-and-auth/00_references/supabase-schema.sql`에는 아래 구조가 포함되어 있습니다.

```sql
create table if not exists service_logs (
  id uuid primary key default gen_random_uuid(),
  user_id uuid,
  event_type text not null,
  message text not null,
  metadata jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now()
);
```

## 컬럼 역할

| 컬럼 | 의미 | 예시 |
|---|---|---|
| `event_type` | 로그 종류를 구분하는 이름 | `ai.answer.created`, `practice.error` |
| `message` | 사람이 읽을 수 있는 짧은 설명 | `AI 응답 생성이 완료되었습니다.` |
| `metadata` | endpoint, 상태 코드, 처리 시간 같은 추가 정보 | `{ "duration_ms": 320 }` |
| `user_id` | 어떤 사용자와 관련된 로그인지 연결 | `uuid` 또는 `null` |
| `created_at` | 로그가 생성된 시간 | 자동 생성 |

## metadata에 넣기 좋은 정보

`metadata`는 JSON 형태이므로 상황마다 다른 정보를 넣을 수 있습니다.

```json
{
  "endpoint": "/ai/chat",
  "status_code": 200,
  "duration_ms": 320,
  "provider": "gemini",
  "model": "gemini-2.5-flash-lite",
  "actual_api_called": false,
  "llm_call_mode": "mock-first"
}
```

실제 Gemini SDK endpoint에서 응답을 생성했다면 아래처럼 기록할 수 있습니다.

```json
{
  "endpoint": "/ai/chat",
  "status_code": 200,
  "duration_ms": 840,
  "provider": "gemini",
  "model": "gemini-2.5-flash-lite",
  "actual_api_called": true,
  "llm_call_mode": "gemini-sdk"
}
```

오류 로그라면 아래 정보가 도움이 됩니다.

```json
{
  "error_type": "ValueError",
  "endpoint": "/ai/chat",
  "retryable": false
}
```

## 실습 파일

| 파일 | 내용 |
|---|---|
| `01_service_log_schema_example.py` | Supabase에 접속하지 않고 서비스 로그 구조를 Python dict로 이해합니다. |
| `02_insert_service_log.py` | Supabase `service_logs` 테이블에 성공 로그를 저장합니다. |
| `03_error_log_example.py` | 예외가 발생했을 때 오류 로그를 저장하는 흐름을 실습합니다. |

## 실행 순서

먼저 구조 예제를 실행합니다. 이 파일은 Supabase에 접속하지 않습니다.

```powershell
cd C:\aidev\02_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
python .\04_backend-service-data-management\03_service-logs\01_service_log_schema_example.py
```

Supabase에 실제 로그를 저장하려면 `.env`와 `service_logs` 테이블이 준비되어 있어야 합니다.

```powershell
python .\04_backend-service-data-management\03_service-logs\02_insert_service_log.py
```

오류 로그 예제:

```powershell
python .\04_backend-service-data-management\03_service-logs\03_error_log_example.py
```

## 확인 기준

- `service_logs` 테이블에 성공 로그가 저장됩니다.
- 오류 예제 실행 후 `practice.error` 로그가 저장됩니다.
- `metadata`에 endpoint, status_code, duration_ms, provider, model, actual_api_called, error_type 같은 추가 정보가 저장됩니다.
- 실제 API key나 민감한 사용자 정보가 로그에 그대로 저장되지 않습니다.

## 로그 작성 기준

좋은 로그는 “나중에 문제를 찾을 수 있을 만큼 충분하지만, 민감한 정보는 담지 않는 기록”입니다.

```text
좋은 예:
AI 응답 생성 실패, endpoint=/ai/chat, error_type=TimeoutError

나쁜 예:
사용자의 전체 질문, access token, service role key, 비밀번호 원문
```

## 정리 질문

- 성공 로그와 오류 로그는 어떤 점이 달라야 하나요?
- `metadata`를 JSON으로 저장하면 어떤 장점이 있나요?
- 로그에 사용자의 질문 전체를 항상 저장하면 어떤 문제가 생길 수 있나요?
- 이후 운영 대시보드를 만든다면 어떤 event_type을 먼저 보고 싶나요?
- mock 응답과 Gemini SDK 응답을 같은 `service_logs` 테이블에 기록하려면 어떤 metadata가 필요할까요?
