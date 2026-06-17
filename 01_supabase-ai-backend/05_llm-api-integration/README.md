# 05. LLM API Integration

이 단원은 FastAPI 백엔드에서 LLM API를 호출하는 방법을 배우는 단계입니다. 01~03 과정에서는 Gemini API를 기본 실습 모델로 사용하고, OpenAI API는 선택/비교 실습으로 유지합니다.

이미지 기준의 “LLM API 개념 및 동작 원리, Gemini API 키 발급, 토큰/과금, 제어 파라미터, 싱글턴·멀티턴 호출, FastAPI 연동” 내용을 이 단원에서 다룹니다.

## 학습 목표

- LLM API가 무엇인지 설명할 수 있습니다.
- API key가 왜 필요한지 이해합니다.
- Gemini API를 기본으로 실제 LLM API 호출 흐름을 실습할 수 있습니다.
- OpenAI API 예제는 모델 공급자 차이를 비교하거나 추가 강의를 진행할 때 선택적으로 사용할 수 있습니다.
- 토큰과 과금 개념을 이해합니다.
- `temperature`, `top_p`, `max_tokens` 같은 기본 파라미터의 의미를 이해합니다.
- 모델별 파라미터 차이와 Gemini 계열에서 언급될 수 있는 `thinkingLevel` 같은 공급자별 설정을 개념 수준에서 이해합니다.
- 단일 질문 응답과 이전 대화를 포함한 멀티턴 응답의 차이를 이해합니다.
- FastAPI endpoint에서 LLM API를 호출하는 흐름을 설계할 수 있습니다.
- 실제 비용이 발생할 수 있는 API 호출과 비용 없는 mock 호출을 구분할 수 있습니다.
- API key가 없을 때도 학습할 수 있도록 placeholder/mock 구조를 먼저 만들 수 있습니다.

## 권장 구성

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

## 수업에서 다루는 내용

| 주제 | 설명 |
| --- | --- |
| LLM API | 코드에서 AI 모델을 호출해 응답을 받는 방식입니다. |
| Gemini API | 01~03 과정의 기본 LLM 실습 API입니다. 무료 범위가 있을 수 있으나 실제 사용 조건은 수업 시점의 공식 화면에서 확인합니다. |
| OpenAI API | 선택/비교 실습용 API입니다. 기존 OpenAI 예제 파일은 유지하며, ChatGPT/Codex 앱 결제와 API 결제는 별개입니다. |
| 토큰 | 모델이 입력과 출력을 처리하는 단위입니다. 사용량과 비용 계산에 영향을 줍니다. |
| 파라미터 | 응답의 창의성, 길이, 다양성을 조절하는 설정입니다. |
| 모델별 설정 | `thinkingLevel`처럼 특정 모델 또는 SDK에서만 제공될 수 있는 설정은 공식 문서 확인이 필요합니다. |
| 싱글턴 호출 | 이전 대화 없이 현재 질문만 보내는 방식입니다. |
| 멀티턴 호출 | 이전 대화 이력을 함께 보내 문맥을 유지하는 방식입니다. |

## 실습 방식

이 단원은 아래 순서로 진행합니다.

```text
1. API key 없이 mock 응답 구조 이해
2. .env에서 Gemini API key 설정 여부 확인
3. temperature, top_p, max_tokens 같은 파라미터 의미 확인
4. 모델별 파라미터 차이와 `thinkingLevel` 같은 공급자별 설정 확인
5. Gemini 싱글턴 호출 구조 실습
6. Gemini 멀티턴 메시지 구조 실습
7. FastAPI endpoint로 Gemini 호출 흐름 연결
8. OpenAI 예제는 선택적으로 비교 실행
9. 실제 API 호출 전 무료 범위, 비용, 보안 체크
```

실제 Gemini 또는 OpenAI API 호출 예제는 `.env`에 key가 있을 때만 실행합니다. key가 없으면 안내 메시지를 출력하고 종료하도록 구성합니다.

## 예제 실행 순서

먼저 가상환경을 활성화합니다.

```powershell
cd C:\aidev\01_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
```

API key 설정 확인:

```powershell
python .\05_llm-api-integration\02_api-key-and-billing\01_check_llm_env.py
```

비용 없는 mock 싱글턴 호출:

```powershell
python .\05_llm-api-integration\03_single-turn-call\01_mock_single_turn.py
```

Gemini 싱글턴 호출:

```powershell
python .\05_llm-api-integration\03_single-turn-call\03_gemini_rest_single_turn.py
```

비용 없는 mock 멀티턴 호출:

```powershell
python .\05_llm-api-integration\04_multi-turn-call\01_mock_multi_turn.py
```

Gemini 멀티턴 호출:

```powershell
python .\05_llm-api-integration\04_multi-turn-call\04_gemini_rest_multi_turn.py
```

FastAPI mock LLM endpoint 실행:

```powershell
cd C:\aidev\01_supabase-ai-backend\05_llm-api-integration\05_fastapi-llm-endpoint
..\..\.venv\Scripts\Activate.ps1
uvicorn main_mock:app --reload
```

Gemini FastAPI endpoint 실행:

```powershell
cd C:\aidev\01_supabase-ai-backend\05_llm-api-integration\05_fastapi-llm-endpoint
..\..\.venv\Scripts\Activate.ps1
uvicorn main_gemini_optional:app --reload
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## FastAPI 연동 흐름

```text
사용자 요청
-> FastAPI endpoint
-> 요청 데이터 검증
-> Gemini API 호출 또는 mock 함수 호출
-> 응답 정리
-> JSON 응답 반환
```

## 보안 주의사항

```text
API key는 코드에 직접 적지 않습니다.
API key는 .env 파일에 저장합니다.
.env 파일은 GitHub에 올리지 않습니다.
수업 중 화면 공유에서 API key가 보이지 않게 합니다.
실제 API 호출 전 과금 여부를 확인합니다.
반복문 안에서 실제 API를 무제한 호출하지 않습니다.
```

## 다음 단계

LLM API 호출 흐름을 이해한 뒤 `06_supabase-db-and-auth`에서 데이터를 저장하고, `07_backend-service-data-management`에서 사용자 정보와 대화 이력을 관리하는 구조로 확장합니다.
