# 05_fastapi-llm-endpoint

이 단원에서는 FastAPI endpoint에서 LLM 호출 흐름을 연결하는 방법을 학습합니다.

앞 단원까지는 Python 파일에서 싱글턴/멀티턴 호출 구조를 확인했습니다. 이번 단원에서는 프론트엔드나 API client가 `POST /ai/chat`으로 질문을 보내면, FastAPI가 요청을 검증하고 LLM 응답 형태의 JSON을 반환하는 구조를 만듭니다.

## 핵심 요약

```text
FastAPI LLM endpoint
  사용자의 질문을 HTTP API로 받고 LLM 호출 결과를 JSON으로 반환하는 서버 API입니다.

mock endpoint
  실제 API를 호출하지 않고 LLM 응답 구조만 흉내 내는 안전한 실습 endpoint입니다.

Gemini optional endpoint
  GEMINI_API_KEY가 실제 key일 때만 Gemini API를 호출하는 선택 실행 파일입니다.

OpenAI optional endpoint
  OPENAI_API_KEY가 실제 key일 때만 OpenAI API를 호출하는 선택/비교 실행 파일입니다.
```

## 폴더 파일

| 파일 | 역할 |
| --- | --- |
| `main.py` | 기본 실행 파일. 실제 API 호출 없는 mock LLM endpoint |
| `main_mock.py` | 기존 mock endpoint 예제. `main.py`와 비교용으로 유지 |
| `main_gemini_optional.py` | Gemini REST API 실제 호출 선택 예제 |
| `main_openai_optional.py` | OpenAI API 실제 호출 선택/비교 예제 |

## 실행 준비

가상환경은 `01_supabase-ai-backend` 폴더 아래의 `.venv`를 사용합니다.

```powershell
cd C:\aidev\01_supabase-ai-backend\05_llm-api-integration\05_fastapi-llm-endpoint
..\..\.venv\Scripts\Activate.ps1
```

## 1. 기본 mock endpoint 실행

```powershell
uvicorn main:app --reload
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

확인할 endpoint:

```text
GET /health
POST /ai/chat
```

## 2. POST /ai/chat 요청 예시

Swagger UI에서 `POST /ai/chat`을 열고 아래 JSON을 입력합니다.

```json
{
  "message": "FastAPI에서 Pydantic을 왜 사용하나요?",
  "memo_context": "Pydantic은 요청 데이터를 검증하고 응답 모델을 정리합니다.",
  "temperature": 0.3,
  "max_tokens": 300
}
```

예상 응답 구조:

```json
{
  "provider": "mock",
  "model": "mock-fastapi-llm",
  "actual_api_called": false,
  "answer": "...",
  "usage": {
    "input_length": 123,
    "max_tokens": 300
  }
}
```

`actual_api_called`가 `false`이면 실제 Gemini/OpenAI API를 호출하지 않았다는 의미입니다.

## 3. Gemini endpoint 선택 실행

Gemini는 01~03 과정의 기본 LLM 실습 provider입니다.

실행 전 `.env`에 실제 key가 필요합니다.

```env
GEMINI_API_KEY=your-real-gemini-api-key
GEMINI_MODEL=gemini-2.5-flash-lite
```

실행:

```powershell
uvicorn main_gemini_optional:app --reload
```

이 파일은 `GEMINI_API_KEY`가 없거나 `your-gemini-api-key` 같은 placeholder 값이면 실제 API를 호출하지 않고 안내 응답을 반환합니다.

## 4. OpenAI endpoint 선택/비교 실행

OpenAI 예제는 필수가 아닙니다. 모델 공급자별 endpoint 구현 차이를 비교할 때 사용합니다.

실행 전 `.env`에 실제 key가 필요합니다.

```env
OPENAI_API_KEY=your-real-openai-api-key
OPENAI_MODEL=gpt-4.1-mini
```

실행:

```powershell
uvicorn main_openai_optional:app --reload
```

OpenAI API 결제는 ChatGPT/Codex 앱 결제와 별개입니다. 실제 호출 전 OpenAI Platform의 Billing 화면을 확인합니다.

## endpoint 처리 흐름

```text
프론트엔드 요청
-> FastAPI POST /ai/chat
-> Pydantic 요청 검증
-> prompt/context 구성
-> mock 또는 실제 LLM API 호출
-> provider/model/answer/usage 응답 반환
```

## 실제 서비스로 확장할 때 필요한 것

```text
1. 사용자 인증
2. 사용자별 대화 이력 조회
3. Supabase에 질문/응답 저장
4. API 호출 실패 처리
5. 호출 제한과 비용 관리
6. SSE 기반 실시간 응답 스트리밍
```

SSE 기반 AI 응답 스트리밍은 `03_supabase-ai-mini-project`에서 백엔드, Streamlit 화면, Supabase 저장 흐름과 함께 통합 실습으로 다룹니다.

## 이후 단원과의 연결

```text
06_supabase-db-and-auth:
  사용자 정보와 대화 이력을 Supabase에 저장합니다.

02_supabase-ai-frontend:
  Streamlit 화면에서 /ai/chat endpoint를 호출합니다.

03_supabase-ai-mini-project:
  실시간 스트리밍, 로그 저장, 배포까지 연결합니다.
```

## 확인 질문

```text
1. FastAPI endpoint에서 LLM API를 직접 호출할 때 왜 요청 검증이 필요한가요?
2. actual_api_called 값을 응답에 포함하면 어떤 점이 좋나요?
3. mock endpoint를 먼저 만드는 이유는 무엇인가요?
4. Gemini endpoint와 OpenAI endpoint를 분리해 둔 이유는 무엇인가요?
5. 이 endpoint를 Streamlit 화면과 연결하면 어떤 흐름이 되나요?
```
