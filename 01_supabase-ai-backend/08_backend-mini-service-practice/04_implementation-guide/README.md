# 04. Implementation Guide

FastAPI, Supabase, LLM API를 연결하는 구현 순서를 정리합니다.

## 구현 파일

```text
schemas.py
-> 요청/응답 데이터 구조를 Pydantic 모델로 정의합니다.

llm_mock.py
-> 실제 LLM API를 호출하지 않고 답변을 생성하는 mock 함수입니다.

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

1. `schemas.py`에서 요청/응답 모델을 정의합니다.
2. `llm_mock.py`에서 비용 없는 답변 생성 함수를 만듭니다.
3. `main_mock.py`에서 API 흐름을 먼저 완성합니다.
4. `mini-service-schema.sql`을 Supabase SQL Editor에서 실행합니다.
5. `supabase_client.py`로 Supabase 연결을 분리합니다.
6. `main_supabase.py`에서 실제 저장 흐름으로 확장합니다.

## 실행

mock 버전:

```powershell
cd C:\aidev\01_supabase-ai-backend\08_backend-mini-service-practice\04_implementation-guide
..\..\.venv\Scripts\Activate.ps1
uvicorn main_mock:app --reload --host 127.0.0.1 --port 8004
```

Supabase 버전:

```powershell
uvicorn main_supabase:app --reload --host 127.0.0.1 --port 8005
```
