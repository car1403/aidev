# 04. Implementation Guide

이 폴더에서는 앞에서 만든 요구사항, API 설계, Supabase 스키마를 실제 FastAPI 코드로 구현합니다.

구현은 두 단계로 나눕니다. 먼저 Supabase와 실제 LLM API 없이 `main_mock.py`로 전체 API 흐름을 확인합니다. 그 다음 `main_supabase.py`에서 Supabase 테이블에 실제 데이터를 저장하는 방식으로 확장합니다.

앞 단원인 `05_llm-api-integration`의 변경 방향에 맞춰 실제 LLM 연동은 Gemini SDK를 기본 확장 방향으로 봅니다. 이 단원에서는 실제 Gemini SDK를 바로 호출하지 않고, `provider`, `model`, `actual_api_called`, `llm_call_mode` 값을 저장하면서 나중에 실제 호출 함수로 교체할 준비를 합니다.

## 이번 단계의 목표

- Pydantic 모델로 요청 데이터를 검증합니다.
- mock-first 함수로 비용 없이 답변 생성 흐름을 연습합니다.
- `/questions` API로 질문 등록과 조회를 구현합니다.
- `/service-logs` API로 서비스 로그 저장과 조회를 구현합니다.
- Supabase 테이블 `mini_questions`, `mini_service_logs`와 코드 이름을 일치시킵니다.

## 구현 파일

```text
schemas.py
-> 요청/응답 데이터 구조를 Pydantic 모델로 정의합니다.

llm_mock.py
-> 실제 LLM API를 호출하지 않고 답변을 생성하는 mock-first 함수입니다.

service_logger.py
-> 서비스 로그 dict를 만드는 보조 함수입니다.

supabase_client.py
-> Supabase client 생성 코드를 분리합니다.

main_mock.py
-> 메모리 저장소로 실행하는 FastAPI 앱입니다.

main_supabase.py
-> Supabase에 실제 저장하는 FastAPI 앱입니다.
```

## 구현 순서

1. `schemas.py`에서 요청 모델을 정의합니다.
2. `llm_mock.py`에서 비용 없는 답변 생성 함수를 확인합니다.
3. `service_logger.py`에서 로그 데이터 생성 방식을 확인합니다.
4. `main_mock.py`를 실행해서 `/questions` API 흐름을 먼저 확인합니다.
5. `03_supabase-schema/mini-service-schema.sql`을 Supabase SQL Editor에서 실행합니다.
6. `.env`에 Supabase 연결 정보를 설정합니다.
7. `main_supabase.py`를 실행해서 실제 저장 흐름을 확인합니다.
8. 이후 실제 LLM 호출로 확장할 때는 `llm_mock.py`의 답변 생성 함수를 Gemini SDK 호출 함수로 교체합니다.

## mock 버전 실행

mock 버전은 Supabase 키가 없어도 실행할 수 있습니다.

```powershell
cd C:\aidev\02_supabase-ai-backend\08_backend-mini-service-practice\04_implementation-guide
..\..\.venv\Scripts\Activate.ps1
uvicorn main_mock:app --reload --host 127.0.0.1 --port 8004
```

브라우저에서 Swagger UI를 엽니다.

```text
http://127.0.0.1:8004/docs
```

확인 순서는 다음과 같습니다.

```text
GET /health
POST /questions
GET /questions
GET /questions/{question_id}
POST /service-logs
GET /service-logs
```

## Supabase 버전 실행

Supabase 버전은 SQL 파일 실행과 `.env` 설정이 필요합니다.

```powershell
cd C:\aidev\02_supabase-ai-backend\08_backend-mini-service-practice\04_implementation-guide
..\..\.venv\Scripts\Activate.ps1
uvicorn main_supabase:app --reload --host 127.0.0.1 --port 8005
```

Swagger UI:

```text
http://127.0.0.1:8005/docs
```

## .env 설정 예시

`.env` 파일은 `C:\aidev\02_supabase-ai-backend\.env` 위치에 둡니다.

```text
SUPABASE_URL=본인의 Supabase Project URL
SUPABASE_ANON_KEY=본인의 Supabase anon public key
SUPABASE_SERVICE_ROLE_KEY=본인의 Supabase service role key
```

`SUPABASE_SERVICE_ROLE_KEY`는 서버 코드에서만 사용해야 합니다. 브라우저 화면이나 공개 저장소에 노출하면 안 됩니다.

## API 이름 기준

이번 단원에서는 API와 테이블 이름을 다음처럼 통일합니다.

| 구분 | 이름 |
| --- | --- |
| 질문 생성 API | `POST /questions` |
| 질문 목록 API | `GET /questions` |
| 질문 상세 API | `GET /questions/{question_id}` |
| 질문 저장 테이블 | `mini_questions` |
| 로그 저장 테이블 | `mini_service_logs` |

## 다음 단계 연결

이 구현 파일은 `10_labs`와 `20_assignments`에서 다시 사용합니다. 따라서 API 이름과 테이블 이름을 임의로 바꾸지 않는 것이 좋습니다.
