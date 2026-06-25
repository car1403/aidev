# 02. Prompting For Code

이 단원에서는 Codex에게 코드 생성 또는 코드 수정을 요청할 때 필요한 정보를 구조화하는 방법을 학습합니다.

좋은 요청은 “코드를 만들어 줘”에서 끝나지 않습니다. 무엇을 만들지, 어떤 입력을 받을지, 어떤 출력을 반환할지, 어떤 제약을 지켜야 하는지, 완료 기준이 무엇인지 함께 알려 주어야 합니다.

## 이번 단계의 목표

- 코드 생성 요청을 기능, 입력, 출력, 조건, 완료 기준으로 나눌 수 있습니다.
- 큰 기능을 작은 요청으로 나누는 방법을 익힙니다.
- FastAPI, Pydantic, Supabase, mock-first LLM 코드 요청에 필요한 정보를 구분합니다.
- Codex가 만든 코드를 바로 믿지 않고 실행 기준으로 검증하는 습관을 만듭니다.
- 실제 API key나 token을 요청문에 포함하지 않는 기준을 확인합니다.

## 기본 요청 구조

아래 구조를 사용하면 코드 요청이 훨씬 명확해집니다.

```text
목표:
현재 상태:
만들 기능:
입력:
출력:
제약 조건:
완료 기준:
수정 범위:
```

각 항목의 의미는 다음과 같습니다.

| 항목 | 설명 |
| --- | --- |
| 목표 | 왜 이 코드를 만들려고 하는지 |
| 현재 상태 | 이미 있는 파일, 함수, API 구조 |
| 만들 기능 | 새로 만들거나 고칠 기능 |
| 입력 | 함수 인자, 요청 JSON, 환경변수 등 |
| 출력 | 반환값, 응답 JSON, 저장 결과 등 |
| 제약 조건 | 사용해야 할 이름, 바꾸면 안 되는 구조, 보안 기준 |
| 완료 기준 | 어떤 결과가 나오면 성공인지 |
| 수정 범위 | 어떤 파일만 수정해야 하는지 |

## 나쁜 요청과 좋은 요청 비교

### 부족한 요청

```text
FastAPI 코드 만들어줘.
```

이 요청은 어떤 URL이 필요한지, 어떤 데이터를 받을지, 어떤 응답을 반환할지 알 수 없습니다.

### 개선된 요청

```text
목표:
질문을 등록하고 mock-first 답변을 반환하는 FastAPI endpoint를 만들고 싶습니다.

현재 상태:
Pydantic 모델은 아직 없습니다.

만들 기능:
POST /questions endpoint

입력:
{
  "user_id": "student01",
  "question": "FastAPI에서 Pydantic은 왜 사용하나요?",
  "provider": "gemini",
  "model": "gemini-2.5-flash-lite"
}

출력:
{
  "ok": true,
  "item": {
    "id": "...",
    "user_id": "...",
    "question": "...",
    "answer": "...",
    "provider": "gemini",
    "model": "gemini-2.5-flash-lite",
    "actual_api_called": false,
    "llm_call_mode": "mock-first"
  }
}

제약 조건:
- 실제 LLM API를 호출하지 말고 mock-first 함수를 사용해 주세요.
- API key는 코드에 넣지 마세요.
- 초보자가 이해할 수 있도록 핵심 주석을 넣어 주세요.

완료 기준:
- Swagger UI에서 POST /questions를 실행할 수 있어야 합니다.
- 응답에 ok와 item이 포함되어야 합니다.
```

## 작은 요청으로 나누기

한 번에 “백엔드 서비스 전체를 만들어 주세요”라고 요청하면 결과를 검증하기 어렵습니다.

아래처럼 작은 단위로 나누는 것이 좋습니다.

```text
1. Pydantic 요청 모델을 먼저 만들어 주세요.
2. mock-first 답변 생성 함수를 만들어 주세요.
3. POST /questions endpoint를 만들어 주세요.
4. GET /questions endpoint를 추가해 주세요.
5. 서비스 로그 저장 함수를 추가해 주세요.
6. Supabase 저장 버전으로 확장할 때 바뀌는 부분을 설명해 주세요.
```

작게 나누면 각 단계마다 실행하고 검증할 수 있습니다.

## Python 함수 요청 예시

```text
목표:
점수 리스트의 평균을 계산하는 함수를 만들고 싶습니다.

만들 기능:
calculate_average 함수

입력:
숫자 리스트 scores

출력:
평균 점수 float

제약 조건:
- sum과 len을 사용해 주세요.
- 빈 리스트는 0.0을 반환해 주세요.
- 초보자가 이해할 수 있도록 주석을 달아 주세요.

완료 기준:
- calculate_average([90, 80, 70]) 결과가 80.0이어야 합니다.
- calculate_average([]) 결과가 0.0이어야 합니다.
```

## FastAPI endpoint 요청 예시

```text
목표:
미니 서비스에서 질문 등록 API를 만들고 싶습니다.

현재 상태:
08_backend-mini-service-practice에서는 /questions API를 사용합니다.

만들 기능:
POST /questions

입력:
user_id, question, provider, model

출력:
ok, item 구조의 JSON 응답

제약 조건:
- 실제 LLM API 호출 대신 generate_mock_answer 함수를 사용해 주세요.
- provider 기본값은 gemini, model 기본값은 gemini-2.5-flash-lite로 해 주세요.
- 응답에는 actual_api_called=false, llm_call_mode=mock-first를 포함해 주세요.
- 응답 형식은 {"ok": true, "item": ...}로 맞춰 주세요.
- 오류 응답은 HTTPException으로 처리해 주세요.
- API key는 사용하지 마세요.

완료 기준:
- Swagger UI에서 테스트할 수 있어야 합니다.
- 질문 생성 후 id, question, answer, provider, model, actual_api_called, llm_call_mode가 응답에 포함되어야 합니다.
```

## Pydantic 모델 요청 예시

```text
목표:
POST /questions 요청 데이터를 검증하는 Pydantic 모델을 만들고 싶습니다.

모델 이름:
QuestionCreateRequest

필드:
- user_id: str, 필수, 최소 1글자
- question: str, 필수, 최소 1글자, 최대 500글자
- provider: str, 선택, 기본값 gemini
- model: str, 선택, 기본값 gemini-2.5-flash-lite

제약 조건:
- Field를 사용해 examples와 description을 넣어 주세요.
- 초보자가 이해할 수 있도록 각 필드 위에 짧은 주석을 달아 주세요.
```

## Supabase 저장 코드 요청 예시

```text
목표:
질문과 답변을 Supabase의 mini_questions 테이블에 저장하고 싶습니다.

현재 상태:
Supabase client를 만드는 get_supabase 함수가 이미 있습니다.

저장 테이블:
mini_questions

저장할 컬럼:
- user_id
- question
- answer
- provider
- model
- actual_api_called
- llm_call_mode

제약 조건:
- 테이블명은 mini_questions를 사용해 주세요.
- service role key 값을 코드에 직접 넣지 마세요.
- Supabase 오류가 발생하면 HTTPException으로 바꿔 주세요.
- insert 결과에 data가 없으면 저장 실패로 처리해 주세요.

완료 기준:
- 저장 성공 시 {"ok": true, "item": ...}를 반환해야 합니다.
```

## 오류 수정 요청 예시

```text
목표:
FastAPI 서버 실행 오류를 해결하고 싶습니다.

실행 명령:
uvicorn main_mock:app --reload --host 127.0.0.1 --port 8004

오류 메시지:
ModuleNotFoundError: No module named 'fastapi'

현재 위치:
C:\aidev\02_supabase-ai-backend\08_backend-mini-service-practice\04_implementation-guide

기대 결과:
서버가 실행되고 http://127.0.0.1:8004/docs 에 접속되어야 합니다.

요청:
가능한 원인과 확인 순서를 알려 주세요. 코드는 아직 수정하지 말고, 먼저 점검 순서만 설명해 주세요.
```

## 코드 수정 요청 시 주의할 점

Codex에게 수정을 요청할 때는 “무엇을 바꾸지 말아야 하는지”도 알려 주는 것이 좋습니다.

```text
수정해 주세요.

단, 아래 내용은 유지해 주세요.
- API 경로는 /questions를 유지
- 테이블명은 mini_questions 유지
- 응답 형식은 ok/item/items 유지
- 실제 API key는 코드에 넣지 않기
- 기존 README 구조는 유지
```

## 완료 기준을 쓰는 방법

완료 기준은 결과를 검증하기 위한 문장입니다.

좋은 완료 기준:

```text
- python -m py_compile main_mock.py가 성공해야 합니다.
- Swagger UI에서 POST /questions가 201 응답을 반환해야 합니다.
- GET /questions에서 방금 만든 질문이 조회되어야 합니다.
- 서비스 로그에 question_created가 저장되어야 합니다.
```

모호한 완료 기준:

```text
- 잘 되게 해 주세요.
- 예쁘게 만들어 주세요.
- 오류 없게 해 주세요.
```

## 민감정보 보호 기준

요청문에 실제 값을 붙여 넣지 않습니다.

```text
붙여 넣으면 안 되는 값:
- GEMINI_API_KEY 실제 값
- OPENAI_API_KEY 실제 값
- SUPABASE_SERVICE_ROLE_KEY 실제 값
- UPSTASH_REDIS_REST_TOKEN 실제 값
- 비밀번호
- access token
```

가짜 값으로 바꾸어 설명합니다.

```text
SUPABASE_URL=https://example.supabase.co
SUPABASE_SERVICE_ROLE_KEY=your-service-role-key
GEMINI_API_KEY=your-gemini-api-key
```

## 직접 작성 연습

아래 주제로 Codex 요청문을 직접 작성해 봅니다.

```text
1. Python 함수 생성 요청
2. Pydantic 모델 생성 요청
3. FastAPI endpoint 생성 요청
4. Supabase 저장 코드 생성 요청
5. 오류 메시지 분석 요청
```

각 요청에는 반드시 다음 항목을 포함합니다.

```text
목표
현재 상태
입력
출력
제약 조건
완료 기준
```

## 완료 체크리스트

- [ ] 코드 요청문에 목표가 들어 있습니다.
- [ ] 입력과 출력이 구분되어 있습니다.
- [ ] 제약 조건이 명확합니다.
- [ ] 완료 기준이 실행 가능한 문장으로 작성되어 있습니다.
- [ ] 실제 API key나 token이 포함되어 있지 않습니다.
- [ ] 한 번에 너무 큰 작업을 요청하지 않았습니다.
- [ ] Codex 답변을 실행 전 검토할 기준이 있습니다.

## 다음 단계

다음 폴더인 `03_debugging-with-codex`에서는 오류 메시지와 실행 결과를 바탕으로 디버깅을 요청하는 방법을 학습합니다.
