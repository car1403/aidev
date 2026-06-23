# 05. LLM API Integration

이 단원에서는 FastAPI 백엔드에서 LLM API를 호출하는 기본 흐름을 배웁니다.

01~03 과정에서는 **Gemini API를 기본 LLM 실습 provider**로 사용합니다. 기본 모델 예시는 `gemini-2.5-flash-lite`입니다. OpenAI API는 선택 비교용으로 다루며, 기존 OpenAI 예제 파일은 필요할 때 추가 설명이나 비교 실습에 사용할 수 있도록 유지합니다. OpenAI를 사용할 경우 예시 모델은 `gpt-4.1-mini`로 맞춥니다.

중요한 원칙은 **mock-first**입니다. 처음부터 실제 API를 호출하면 API key, 비용, 네트워크 오류 때문에 학습 흐름이 복잡해질 수 있습니다. 먼저 mock 응답으로 요청/응답 구조를 이해한 뒤, 실제 key가 준비된 경우에만 Gemini 또는 OpenAI 호출 예제를 선택적으로 실행합니다.

## 학습 목표

- LLM API가 무엇인지 설명할 수 있습니다.
- ChatGPT 화면 사용과 코드에서 API를 호출하는 방식의 차이를 이해합니다.
- Gemini API key를 `.env`에 저장하고 코드에서 안전하게 읽는 흐름을 이해합니다.
- OpenAI API는 Gemini와 비교하거나 추가 실습이 필요할 때 선택적으로 사용할 수 있습니다.
- token, model, message, prompt, parameter의 의미를 구분합니다.
- `temperature`, `top_p`, `max_tokens`가 응답 방식과 비용에 어떤 영향을 주는지 이해합니다.
- single-turn 호출과 multi-turn 호출의 차이를 이해합니다.
- FastAPI endpoint에서 LLM 호출 흐름을 설계합니다.
- 실제 API 호출과 mock 호출을 `actual_api_called` 값으로 명확히 구분합니다.
- 이후 Supabase에 저장할 대화 이력 구조를 고려해 응답 데이터를 설계합니다.

## 단원 구성

```text
05_llm-api-integration
├─ README.md
├─ 00_references
├─ 01_llm-api-concepts
├─ 02_api-key-and-billing
├─ 03_single-turn-call
├─ 04_multi-turn-call
├─ 05_fastapi-llm-endpoint
├─ 10_labs
└─ 20_assignments
```

## 학습 흐름

| 순서 | 폴더 | 핵심 내용 |
| --- | --- | --- |
| 1 | `01_llm-api-concepts` | LLM API 개념, message 구조, 주요 파라미터 이해 |
| 2 | `02_api-key-and-billing` | API key, `.env`, placeholder key, 비용 안전 점검 |
| 3 | `03_single-turn-call` | 질문 하나에 대한 mock/Gemini SDK/Gemini REST/OpenAI 호출 구조 |
| 4 | `04_multi-turn-call` | 이전 대화 이력을 포함한 mock/Gemini SDK/Gemini REST/OpenAI multi-turn 호출 구조 |
| 5 | `05_fastapi-llm-endpoint` | FastAPI에서 mock endpoint와 Gemini SDK 기본 endpoint 구성 |
| 6 | `10_labs` | 단계별 실습 |
| 7 | `20_assignments` | 제출 과제와 미니 서비스 설계 |

## 기본 모델 기준

| 구분 | 용도 | 기본 예시 |
| --- | --- | --- |
| Gemini | 01~03 과정 기본 LLM 실습 | `gemini-2.5-flash-lite` |
| OpenAI | 선택 비교 및 추가 실습 | `gpt-4.1-mini` |
| Mock | 비용 없는 구조 학습 | 실제 API 호출 없음 |

실습 코드에서는 실제 호출 여부를 반드시 구분합니다.

```json
{
  "provider": "gemini",
  "model": "gemini-2.5-flash-lite",
  "actual_api_called": false
}
```

`actual_api_called`가 `false`이면 실제 Gemini/OpenAI API를 호출하지 않았다는 뜻입니다. 처음에는 이 값을 `false`로 두고 구조를 익힌 뒤, 실제 key와 비용 조건을 확인한 경우에만 실제 호출 예제를 실행합니다.

## 공통 실행 준비

```powershell
cd C:\aidev\01_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
```

API key 설정 상태를 확인합니다.

```powershell
python .\05_llm-api-integration\02_api-key-and-billing\01_check_llm_env.py
```

비용 없는 mock single-turn 호출:

```powershell
python .\05_llm-api-integration\03_single-turn-call\01_mock_single_turn.py
```

Gemini single-turn 호출:

```powershell
python .\05_llm-api-integration\03_single-turn-call\02_gemini_sdk_single_turn.py
```

Gemini 실제 호출은 SDK 방식을 먼저 사용합니다. SDK 방식은 코드가 짧고 응답 텍스트를 쉽게 확인할 수 있어 초보자가 처음 실제 호출을 성공시키기에 좋습니다. REST 방식인 `03_gemini_rest_single_turn.py`는 URL, payload, 응답 JSON 구조를 직접 확인하는 보충 예제로 유지합니다.

비용 없는 mock multi-turn 호출:

```powershell
python .\05_llm-api-integration\04_multi-turn-call\01_mock_multi_turn.py
```

Gemini multi-turn 호출:

```powershell
python .\05_llm-api-integration\04_multi-turn-call\02_gemini_sdk_multi_turn.py
```

멀티턴 호출도 Gemini SDK 방식을 기본으로 사용합니다. REST 방식인 `03_gemini_rest_multi_turn.py`는 HTTP payload 구조를 직접 확인하는 보충 예제입니다.

FastAPI mock LLM endpoint 실행:

```powershell
cd C:\aidev\01_supabase-ai-backend\05_llm-api-integration\05_fastapi-llm-endpoint
..\..\.venv\Scripts\Activate.ps1
uvicorn 01_mock_llm_endpoint:app --reload
```

Gemini FastAPI endpoint 실행:

```powershell
cd C:\aidev\01_supabase-ai-backend\05_llm-api-integration\05_fastapi-llm-endpoint
..\..\.venv\Scripts\Activate.ps1
uvicorn 02_gemini_sdk_endpoint:app --reload
```

FastAPI 프로젝트 구현도 `02_gemini_sdk_endpoint.py`를 기준으로 진행합니다. `03_gemini_rest_optional_endpoint.py`는 REST 요청 구조를 확인할 때 사용합니다.

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## FastAPI 연동 흐름

```text
사용자 질문
-> FastAPI endpoint
-> Pydantic 요청 데이터 검증
-> mock 함수 또는 Gemini/OpenAI API 호출
-> 응답 구조 정리
-> JSON 응답 반환
-> 이후 Supabase 대화 이력 저장으로 확장
```

## 보안과 비용 기준

```text
API key는 코드에 직접 작성하지 않습니다.
.env 파일에 API key를 저장합니다.
.env 파일은 GitHub에 올리지 않습니다.
your-... 형태의 placeholder key는 실제 key로 취급하지 않습니다.
실제 API 호출 전 무료 한도와 과금 조건을 확인합니다.
반복문 안에서 실제 API를 무제한 호출하지 않습니다.
과제 제출 시 실제 API key를 포함하지 않습니다.
```

## 참고 문서

기본 개념이 헷갈릴 때는 `00_references`를 먼저 확인합니다.

| 문서 | 내용 |
| --- | --- |
| `llm-api-cheatsheet.md` | LLM API 전체 흐름과 핵심 용어 |
| `message-format-guide.md` | system/user/assistant 메시지 구조 |
| `parameter-guide.md` | temperature, top_p, max_tokens 설명 |
| `model-parameter-comparison-guide.md` | Gemini/OpenAI/mock 사용 기준과 파라미터 비교 |
| `token-cost-safety-guide.md` | token, 비용, API key 안전 기준 |

## 다음 단계

이 단원에서 LLM API 호출 구조를 이해한 뒤, `06_supabase-db-and-auth`에서 사용자 정보와 대화 데이터를 Supabase에 저장하는 흐름으로 확장합니다. 이후 `07_backend-service-data-management`와 `08_backend-mini-service-practice`에서는 사용자별 데이터 관리와 작은 백엔드 서비스를 구성합니다.
