# 05. FastAPI LLM Endpoint

FastAPI endpoint에서 LLM API를 호출하고 JSON 응답으로 반환하는 흐름을 학습합니다.

## 예제 파일

```text
main_mock.py
main_gemini_optional.py
main_openai_optional.py
```

`main_mock.py`는 실제 API를 호출하지 않습니다.

`main_gemini_optional.py`는 01~03 과정의 기본 실제 API 연동 예제입니다. `.env`에 `GEMINI_API_KEY`가 있을 때만 실제 API를 호출합니다.

`main_openai_optional.py`는 선택/비교 실습용입니다. 기존 파일은 유지하며, `.env`에 `OPENAI_API_KEY`가 있을 때만 실제 API를 호출합니다.

## 실행

```powershell
cd C:\aidev\01_supabase-ai-backend\05_llm-api-integration\05_fastapi-llm-endpoint
..\..\.venv\Scripts\Activate.ps1
uvicorn main_mock:app --reload
```

Gemini 연동 endpoint 실행:

```powershell
cd C:\aidev\01_supabase-ai-backend\05_llm-api-integration\05_fastapi-llm-endpoint
..\..\.venv\Scripts\Activate.ps1
uvicorn main_gemini_optional:app --reload
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## 확인할 endpoint

```text
GET /health
POST /ai/chat
```

이 구조는 이후 `02_supabase-ai-frontend`에서 Streamlit 화면이 호출하고, `03_supabase-ai-mini-project`에서 SSE 스트리밍과 Supabase 저장으로 확장됩니다.
