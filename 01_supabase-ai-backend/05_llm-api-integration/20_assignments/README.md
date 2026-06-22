# 20_assignments

`05_llm-api-integration` 단원의 제출 과제 모음입니다.

`10_labs`가 수업 중 단계별 연습이라면, 이 폴더는 같은 내용을 스스로 정리하고 제출하는 과제입니다. 모든 과제는 **실제 Gemini/OpenAI API 호출 전 mock 구조를 먼저 완성**하는 방향으로 진행합니다.

01~03 과정의 기본 LLM 제공자는 Gemini이며 기본 모델 예시는 `gemini-2.5-flash-lite`입니다. OpenAI는 선택 비교용으로 다루며, 사용할 경우 예시 모델은 `gpt-4.1-mini`를 사용합니다.

## 과제 목록

| 순서 | 폴더 | 연결 단원 | 제출 주제 |
| --- | --- | --- | --- |
| 1 | `assignment-01_llm-message-design` | `01_llm-api-concepts` | LLM 메시지 구조와 파라미터 설계 |
| 2 | `assignment-02_api-key-and-cost-safety` | `02_api-key-and-billing` | API key, 비용, 실제 호출 전 안전 점검 |
| 3 | `assignment-03_single-turn-mock-service` | `03_single-turn-call` | single-turn mock LLM 호출 함수 구현 |
| 4 | `assignment-04_multi-turn-memory-design` | `04_multi-turn-call` | 대화 이력 기반 multi-turn 메시지 설계 |
| 99 | `assignment-99_fastapi-llm-mini-service` | 단원 마무리 | FastAPI 기반 mock LLM 미니 서비스 |

## 공통 제출 파일

각 과제 폴더 안에 아래 파일을 작성합니다.

```text
main.py
README.md
```

`starter.py`는 시작용 참고 파일입니다. 제출할 때는 완성한 코드를 `main.py`로 정리합니다.

## 공통 README 작성 기준

제출 README에는 다음 내용을 포함합니다.

```text
1. 과제 목표
2. 실행 방법
3. 구현한 기능 목록
4. 요청 데이터 예시
5. 응답 데이터 예시
6. 실제 API 호출 여부
7. API key와 비용을 안전하게 관리한 방법
8. 어려웠던 점과 해결 방법
```

## 공통 실행 준비

```powershell
cd C:\aidev\01_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
```

일반 Python 과제는 다음처럼 실행합니다.

```powershell
python .\05_llm-api-integration\20_assignments\assignment-01_llm-message-design\main.py
```

FastAPI 과제는 해당 과제 폴더로 이동한 뒤 실행합니다.

```powershell
cd C:\aidev\01_supabase-ai-backend\05_llm-api-integration\20_assignments\assignment-99_fastapi-llm-mini-service
..\..\..\.venv\Scripts\Activate.ps1
uvicorn main:app --reload
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## 평가 기준

```text
실행 가능성:
  main.py가 오류 없이 실행되는가?

요청 구조:
  system/user/assistant 메시지 역할이 명확한가?

모델 기준:
  Gemini 기본 모델이 gemini-2.5-flash-lite로 정리되어 있는가?
  OpenAI 선택 모델이 gpt-4.1-mini로 정리되어 있는가?

안전성:
  API key를 코드에 직접 작성하지 않았는가?
  placeholder key를 실제 key로 착각하지 않도록 처리했는가?

비용 관리:
  실제 API 호출 여부를 actual_api_called로 명확히 표시했는가?

서비스 확장성:
  이후 Supabase 대화 이력 저장과 연결하기 쉬운 데이터 구조인가?

문서화:
  README만 보고 실행과 테스트가 가능한가?
```
