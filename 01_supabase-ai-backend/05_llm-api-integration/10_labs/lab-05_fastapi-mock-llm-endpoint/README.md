# Lab 05. FastAPI mock LLM 엔드포인트

이번 실습에서는 LLM 호출 구조를 FastAPI 엔드포인트로 감쌉니다.

실제 Gemini API를 호출하지 않고 mock 응답을 반환하지만, 요청 모델과 응답 모델은 실제 서비스에 가깝게 구성합니다. 이 구조는 이후 Supabase 저장과 프론트엔드 연동으로 이어질 수 있습니다.

## 학습 목표

- `POST /ai/chat` 엔드포인트를 만듭니다.
- Pydantic으로 요청과 응답 구조를 정의합니다.
- 응답에 `provider`, `model`, `actual_api_called`를 포함합니다.
- Swagger UI에서 직접 요청을 테스트합니다.

## 실행

```powershell
cd C:\aidev\01_supabase-ai-backend\05_llm-api-integration\10_labs\lab-05_fastapi-mock-llm-endpoint
..\..\..\.venv\Scripts\Activate.ps1
uvicorn starter:app --reload
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```
