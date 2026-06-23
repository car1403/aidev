# 01. Codex Basic Usage

이 단원에서는 Codex를 AI 백엔드 개발 학습 도구로 사용하는 기본 방법을 익힙니다.

Codex는 코드를 대신 작성하게만 하는 도구가 아닙니다. 현재 폴더의 파일을 읽고, 코드 흐름을 설명하고, 오류 원인을 함께 찾고, 수정 방향을 제안하고, 변경 결과를 검증하는 데 사용할 수 있습니다.

중요한 기준은 “AI가 답한 내용을 그대로 믿는 것”이 아니라 “AI 답변을 읽고, 실행하고, 검증하면서 내 코드에 맞게 적용하는 것”입니다.

## 이번 단계의 목표

- Codex에게 어떤 정보를 주어야 좋은 답변을 받을 수 있는지 이해합니다.
- 코드 설명 요청, 폴더 구조 설명 요청, 오류 메시지 분석 요청을 구분합니다.
- 한 번에 큰 작업을 맡기기보다 작은 단위로 요청하는 습관을 만듭니다.
- Codex 답변을 실행 전 검토하는 기준을 익힙니다.
- API key, service role key, Redis token 같은 민감정보를 노출하지 않는 기준을 확인합니다.

## Codex를 사용할 때의 기본 순서

```text
1. 현재 무엇을 하려는지 먼저 정리합니다.
2. 관련 파일 또는 폴더 위치를 알려줍니다.
3. 기대하는 결과를 구체적으로 말합니다.
4. 오류가 있다면 실행 명령과 오류 메시지를 함께 제공합니다.
5. Codex 답변을 읽고 이해합니다.
6. 필요한 경우 코드를 실행해 검증합니다.
7. 변경 이유와 결과를 직접 정리합니다.
```

## 좋은 요청에 들어가야 하는 정보

| 항목 | 설명 | 예시 |
| --- | --- | --- |
| 목표 | 무엇을 하고 싶은지 | FastAPI 엔드포인트 구조를 이해하고 싶습니다. |
| 위치 | 어떤 파일 또는 폴더인지 | `04_fastapi-backend/01_fastapi-project-setup/main.py` |
| 현재 상태 | 지금 어떤 문제가 있는지 | 서버 실행은 되지만 응답 구조가 이해되지 않습니다. |
| 기대 결과 | 어떤 답변을 원하는지 | 초보자가 이해할 수 있게 실행 순서대로 설명해 주세요. |
| 제약 조건 | 지켜야 할 기준 | 코드는 수정하지 말고 설명만 해 주세요. |

## 요청 유형별 예시

### 1. 폴더 구조 설명 요청

```text
C:\aidev\01_supabase-ai-backend\08_backend-mini-service-practice 폴더 구조를 설명해 주세요.

특히 01_requirements, 02_api-design, 03_supabase-schema, 04_implementation-guide가 어떤 순서로 연결되는지 초보자도 이해할 수 있게 설명해 주세요.
```

### 2. 코드 설명 요청

```text
다음 파일의 코드 흐름을 위에서 아래 순서대로 설명해 주세요.

C:\aidev\01_supabase-ai-backend\08_backend-mini-service-practice\04_implementation-guide\main_mock.py

특히 FastAPI endpoint, Pydantic 모델, mock-first 함수, service_logs 저장 흐름을 구분해서 설명해 주세요.
```

### 3. 오류 메시지 분석 요청

```text
아래 명령을 실행했더니 오류가 발생했습니다.

실행 명령:
uvicorn main_mock:app --reload --host 127.0.0.1 --port 8004

오류 메시지:
ModuleNotFoundError: No module named 'fastapi'

가능한 원인과 확인 순서를 알려 주세요.
```

### 4. 코드 수정 전 검토 요청

```text
아래 파일을 수정하기 전에 어떤 부분을 먼저 확인해야 하는지 알려 주세요.

C:\aidev\01_supabase-ai-backend\08_backend-mini-service-practice\04_implementation-guide\main_supabase.py

수정 목적:
테이블명을 mini_questions로 맞추고 싶습니다.

주의할 점:
코드를 바로 수정하지 말고, 영향을 받는 함수와 확인해야 할 파일을 먼저 정리해 주세요.
```

### 5. 코드 리뷰 요청

```text
이 파일을 리뷰해 주세요.

C:\aidev\01_supabase-ai-backend\08_backend-mini-service-practice\04_implementation-guide\main_mock.py

리뷰 관점:
1. endpoint URL이 요구사항과 맞는가?
2. 요청 데이터 검증이 충분한가?
3. 오류 응답이 이해하기 쉬운가?
4. 서비스 로그에 민감정보가 들어갈 위험은 없는가?
5. 초보자가 읽기 어려운 부분에 주석이 필요한가?
```

## 좋지 않은 요청 예시

아래 요청은 정보가 부족해서 답변 품질이 낮아질 수 있습니다.

```text
이거 고쳐줘.
```

```text
에러 나는데 왜 그래?
```

```text
백엔드 만들어줘.
```

이런 요청은 Codex가 현재 목표와 상황을 정확히 알기 어렵습니다. 파일 위치, 실행 명령, 기대 결과, 오류 메시지를 함께 제공하는 것이 좋습니다.

## Codex 답변 검증 기준

Codex가 제안한 내용을 적용하기 전에 아래 항목을 확인합니다.

| 점검 항목 | 확인 질문 |
| --- | --- |
| 현재 파일 구조 | 답변이 실제 폴더와 파일 이름에 맞나요? |
| 실행 가능성 | 제안한 명령을 현재 위치에서 실행할 수 있나요? |
| 패키지 의존성 | 설치되지 않은 패키지를 갑자기 요구하지 않나요? |
| API 이름 | 현재 과정에서 사용하는 URL과 맞나요? |
| 테이블 이름 | Supabase 테이블명과 컬럼명이 실제 스키마와 맞나요? |
| 보안 | API key, service role key, token을 코드나 로그에 노출하지 않나요? |
| 비용 | 실제 LLM API 호출이 필요한 코드인지, mock-first 코드인지 구분되나요? |
| 이해 가능성 | 본인이 설명할 수 있는 수준으로 이해했나요? |

## 민감정보를 다루는 기준

Codex에게 질문할 때 실제 key 값을 붙여 넣지 않습니다.

공유하면 안 되는 값:

```text
SUPABASE_SERVICE_ROLE_KEY
SUPABASE_ANON_KEY 실제 값
UPSTASH_REDIS_REST_TOKEN
GEMINI_API_KEY
OPENAI_API_KEY
비밀번호
access token
refresh token
개인정보 원문
```

대신 아래처럼 가짜 값으로 바꿔서 설명합니다.

```text
SUPABASE_URL=https://example.supabase.co
SUPABASE_SERVICE_ROLE_KEY=your-service-role-key
GEMINI_API_KEY=your-gemini-api-key
```

## 03_git-github와의 역할 구분

`03_git-github`는 Git과 GitHub를 중심으로 다룹니다.

```text
03_git-github
-> git status
-> git diff
-> commit
-> branch
-> VS Code Source Control
-> GitHub push/pull
```

이번 `90_ai-assisted-code-review-and-debugging`에서는 AI를 활용한 코드 이해와 개선을 다룹니다.

```text
90_ai-assisted-code-review-and-debugging
-> 코드 설명 요청
-> 오류 원인 분석
-> 리팩토링 방향 검토
-> 코드 리뷰
-> 보안/비용 점검
-> 미니 서비스 개선
```

## 이번 단계에서 직접 해볼 것

아래 세 가지 요청을 직접 작성해 봅니다.

### 요청 1. 폴더 구조 설명

```text
C:\aidev\01_supabase-ai-backend\08_backend-mini-service-practice 폴더 구조를 설명해 주세요.
요구사항, API 설계, Supabase 스키마, 구현 파일이 어떤 순서로 연결되는지 알려 주세요.
```

### 요청 2. 코드 흐름 설명

```text
C:\aidev\01_supabase-ai-backend\08_backend-mini-service-practice\04_implementation-guide\main_mock.py의 실행 흐름을 설명해 주세요.
FastAPI endpoint별로 어떤 일이 일어나는지 정리해 주세요.
```

### 요청 3. 오류 원인 분석

```text
아래 오류가 발생했습니다.

명령:
python main_mock.py

오류:
ModuleNotFoundError: No module named 'fastapi'

가능한 원인과 확인 순서를 알려 주세요.
```

## 완료 기준

이 단원을 마치면 아래 내용을 설명할 수 있어야 합니다.

- Codex에게 질문할 때 목표, 파일 위치, 현재 상태, 기대 결과를 함께 제공해야 하는 이유
- 코드 설명 요청과 오류 분석 요청의 차이
- Codex 답변을 실행 전 검토해야 하는 이유
- 실제 API key와 token을 질문에 포함하면 안 되는 이유
- Git/GitHub 학습은 `03_git-github`, AI 기반 코드 리뷰와 디버깅은 `90_ai-assisted-code-review-and-debugging`에서 다룬다는 역할 구분

## 다음 단계

다음 폴더인 `02_prompting-for-code`에서는 코드 생성 또는 수정 요청을 더 구체적으로 작성하는 방법을 학습합니다.
