# 05_fastapi-llm-endpoint

이 단원에서는 FastAPI endpoint에서 LLM 호출 흐름을 연결하는 방법을 학습합니다.

앞 단원까지는 Python 파일에서 싱글턴/멀티턴 호출 구조를 확인했습니다. 이번 단원에서는 프론트엔드나 API client가 `POST /ai/chat`으로 질문을 보내면, FastAPI가 요청을 검증하고 Gemini SDK를 통해 응답을 생성하는 구조를 만듭니다.

## 핵심 요약

```text
01_mock_llm_endpoint.py
  실제 API를 호출하지 않고 FastAPI 요청/응답 구조를 먼저 확인합니다.

02_gemini_sdk_endpoint.py
  이후 프로젝트에서 기본으로 사용할 Gemini SDK 기반 실제 endpoint입니다.

03_gemini_rest_optional_endpoint.py
  HTTP URL, payload, 응답 JSON 구조를 직접 확인하는 보충 endpoint입니다.

04_openai_optional_endpoint.py
  OpenAI API와 구현 방식을 비교할 때 사용하는 선택 endpoint입니다.

90_basic_mock_reference.py
  가장 단순한 mock endpoint를 다시 확인하는 참고 파일입니다.
```

## 폴더 파일

| 순서 | 파일 | 역할 |
| --- | --- | --- |
| 1 | `01_mock_llm_endpoint.py` | 실제 API 호출 없는 기본 mock LLM endpoint |
| 2 | `02_gemini_sdk_endpoint.py` | 실제 프로젝트에서 기본으로 사용할 Gemini SDK endpoint |
| 3 | `03_gemini_rest_optional_endpoint.py` | Gemini REST API 구조 확인용 보충 endpoint |
| 4 | `04_openai_optional_endpoint.py` | OpenAI API 선택/비교 endpoint |
| 90 | `90_basic_mock_reference.py` | 가장 단순한 mock endpoint 참고 예제 |

## 실행 준비

가상환경은 `01_supabase-ai-backend` 폴더 아래의 `.venv`를 사용합니다.

```powershell
cd C:\aidev\01_supabase-ai-backend\05_llm-api-integration\05_fastapi-llm-endpoint
..\..\.venv\Scripts\Activate.ps1
```

## 1. Mock endpoint 실행

```powershell
uvicorn 01_mock_llm_endpoint:app --reload
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

Swagger UI에서 `POST /ai/chat`을 열고 아래 JSON을 입력합니다.

```json
{
  "message": "FastAPI에서 Pydantic을 왜 사용하나요?",
  "memo_context": "Pydantic은 요청 데이터를 검증하고 응답 모델을 정리합니다.",
  "temperature": 0.3,
  "max_tokens": 300
}
```

`actual_api_called`가 `false`이면 실제 Gemini/OpenAI API를 호출하지 않았다는 의미입니다.

## 2. Gemini SDK endpoint 실행

Gemini SDK endpoint는 이후 프로젝트에서 기본으로 사용할 파일입니다.

실행 전 `.env`에 실제 key가 필요합니다.

```env
GEMINI_API_KEY=your-real-gemini-api-key
GEMINI_MODEL=gemini-2.5-flash-lite
```

실행:

```powershell
uvicorn 02_gemini_sdk_endpoint:app --reload
```

Swagger UI에서 `POST /ai/chat`을 열고 아래 JSON을 입력합니다.

```json
{
  "message": "FastAPI에서 Pydantic을 왜 사용하나요?",
  "memo_context": "Pydantic은 요청 데이터를 검증합니다.",
  "temperature": 0.3,
  "max_output_tokens": 300
}
```

처리 흐름:

```text
POST /ai/chat
-> Pydantic 요청 검증
-> prompt/context 구성
-> Gemini SDK generate_content 호출
-> provider/model/actual_api_called/answer 반환
```

이 파일은 `GEMINI_API_KEY`가 없거나 placeholder 값이면 실제 API를 호출하지 않고 안내 응답을 반환합니다.

## 3. Gemini REST optional endpoint 실행

REST endpoint는 HTTP 구조를 확인하는 보충 예제입니다.

```powershell
uvicorn 03_gemini_rest_optional_endpoint:app --reload
```

REST 예제에서 확인할 내용:

```text
1. Gemini REST API URL
2. API key 전달 방식
3. contents payload 구조
4. generationConfig 설정
5. 응답 JSON 파싱 방식
```

프로젝트 구현은 `02_gemini_sdk_endpoint.py`를 기준으로 진행하고, REST 파일은 HTTP 동작 원리를 이해할 때 참고합니다.

## 4. OpenAI endpoint 선택/비교 실행

OpenAI 예제는 필수가 아닙니다. 모델 공급자별 endpoint 구현 차이를 비교할 때 사용합니다.

실행 전 `.env`에 실제 key가 필요합니다.

```env
OPENAI_API_KEY=your-real-openai-api-key
OPENAI_MODEL=gpt-4.1-mini
```

실행:

```powershell
uvicorn 04_openai_optional_endpoint:app --reload
```

OpenAI API 결제는 ChatGPT/Codex 앱 결제와 별개입니다. 실제 호출 전 OpenAI Platform의 Billing 화면을 확인합니다.

## 실제 서비스로 확장할 때 필요한 것

```text
1. 사용자 인증
2. 사용자별 대화 이력 조회
3. Supabase에 질문/응답 저장
4. 서비스 로그 저장
5. API 호출 실패 처리
6. 호출 제한과 비용 관리
7. SSE 기반 실시간 응답 스트리밍
```

SSE 기반 AI 응답 스트리밍은 `03_supabase-ai-mini-project`에서 백엔드, Streamlit 화면, Supabase 저장 흐름과 함께 통합 실습으로 다룹니다.

## 이후 단원과의 연결

```text
06_supabase-db-and-auth:
  사용자 정보와 대화 이력을 Supabase에 저장합니다.

07_backend-service-data-management:
  사용자 프로필, 대화 이력, 서비스 로그를 API 구조로 관리합니다.

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
4. Gemini SDK endpoint를 프로젝트 기본 구현으로 두는 이유는 무엇인가요?
5. REST endpoint는 어떤 내용을 이해할 때 도움이 되나요?
```
