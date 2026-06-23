# 10_labs

`05_llm-api-integration` 단원에서 배운 내용을 짧은 실습으로 복습합니다.

이 실습은 **mock-first**로 시작합니다. 먼저 비용 없이 요청/응답 구조를 만든 뒤, Gemini SDK로 실제 호출을 연결할 수 있는 위치를 확인합니다. 01~03 과정의 기본 LLM 제공자는 Gemini이며, 기본 모델 예시는 `gemini-2.5-flash-lite`입니다. OpenAI는 선택 비교용으로 다루며, 사용할 경우 예시 모델은 `gpt-4.1-mini`로 맞춥니다.

## 실습 목록

| 순서 | 폴더 | 연결 단원 | 핵심 내용 |
| --- | --- | --- | --- |
| 1 | `lab-01_llm-message-and-parameters` | `01_llm-api-concepts` | LLM 메시지 구조와 주요 파라미터 정리 |
| 2 | `lab-02_api-key-safety-check` | `02_api-key-and-billing` | `.env`, placeholder key, 비용 안전 점검 |
| 3 | `lab-03_single-turn-mock-to-gemini-sdk` | `03_single-turn-call` | single-turn mock 구조와 Gemini SDK 확장 위치 확인 |
| 4 | `lab-04_multi-turn-mock-to-gemini-sdk` | `04_multi-turn-call` | multi-turn 대화 이력 구조와 Gemini SDK 확장 위치 확인 |
| 5 | `lab-05_fastapi-llm-endpoint` | `05_fastapi-llm-endpoint` | `POST /ai/chat` mock endpoint를 Gemini SDK endpoint 구조로 확장 |
| 99 | `lab-99_llm-integration-review` | 단원 마무리 | LLM 연동 흐름을 작은 FastAPI 서비스로 종합 복습 |

## 공통 실행 준비

```powershell
cd C:\aidev\01_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
```

각 lab 폴더에서 `starter.py`를 먼저 실행하고, 막히면 `solution.py`와 비교합니다.

```powershell
python .\05_llm-api-integration\10_labs\lab-01_llm-message-and-parameters\starter.py
```

FastAPI lab은 해당 lab 폴더로 이동한 뒤 실행합니다.

```powershell
cd C:\aidev\01_supabase-ai-backend\05_llm-api-integration\10_labs\lab-05_fastapi-llm-endpoint
uvicorn starter:app --reload
```

브라우저에서 Swagger UI를 확인합니다.

```text
http://127.0.0.1:8000/docs
```

## 진행 기준

1. 실제 Gemini/OpenAI API 호출 전에는 mock으로 요청과 응답 구조를 먼저 이해합니다.
2. API key는 코드에 직접 적지 않고 `.env` 또는 환경 변수로 관리합니다.
3. `your-...` 형태의 placeholder 값은 실제 key로 취급하지 않습니다.
4. 응답에는 `provider`, `model`, `actual_api_called`를 포함해 실제 호출 여부를 구분합니다.
5. 대화 이력은 이후 Supabase에 저장할 데이터라는 관점으로 구조를 설계합니다.
6. 실제 프로젝트 기본 구현은 Gemini SDK 방식이며, REST 방식은 HTTP 구조 확인용 보충 예제로 구분합니다.
