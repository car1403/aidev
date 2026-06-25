# 03. Debugging With Codex

이 단원에서는 Codex를 활용해 오류 원인을 분석하고 수정 방향을 찾는 방법을 학습합니다.

디버깅은 “오류를 AI에게 던지고 답을 받는 것”이 아닙니다. 실행 명령, 오류 메시지, 현재 위치, 관련 파일, 기대 결과를 정리하고, 가능한 원인을 하나씩 좁혀 가는 과정입니다.

## 이번 단계의 목표

- 오류 메시지를 그대로 복사해서 전달하는 습관을 만듭니다.
- 실행 명령과 실행 위치가 디버깅에 왜 중요한지 이해합니다.
- 기대 결과와 실제 결과를 구분합니다.
- FastAPI, Supabase, Upstash Redis, LLM API, `.venv` 오류를 유형별로 정리합니다.
- Codex가 제안한 수정안을 적용하기 전에 확인해야 할 기준을 익힙니다.
- 수정 후 반드시 다시 실행해서 검증하는 흐름을 익힙니다.

## 디버깅 기본 흐름

```text
1. 오류가 발생한 명령을 기록합니다.
2. 터미널에 나온 오류 메시지를 그대로 복사합니다.
3. 실행한 폴더 위치를 확인합니다.
4. 관련 파일 이름을 정리합니다.
5. 기대한 결과와 실제 결과를 구분합니다.
6. 이미 시도한 해결 방법을 적습니다.
7. Codex에게 원인 추정과 확인 순서를 요청합니다.
8. 제안된 수정안을 읽고 이해합니다.
9. 코드를 수정한 뒤 다시 실행합니다.
10. 해결 결과를 기록합니다.
```

## 기본 디버깅 요청 템플릿

```text
문제 상황:

실행 위치:

실행한 명령:

오류 메시지:

관련 파일:

기대한 결과:

실제 결과:

내가 이미 시도한 것:

요청:
가능한 원인을 단계별로 추정하고, 초보자가 따라 할 수 있는 확인 순서와 수정 방법을 알려 주세요.
```

## 좋지 않은 디버깅 요청

```text
에러 나요. 고쳐 주세요.
```

```text
실행이 안 돼요.
```

이런 요청은 오류 원인을 찾기 어렵습니다. 어떤 명령을 어디에서 실행했는지, 어떤 오류가 나왔는지, 어떤 결과를 기대했는지가 빠져 있기 때문입니다.

## 좋은 디버깅 요청 예시

```text
문제 상황:
FastAPI mock 서버를 실행하려고 했는데 패키지 import 오류가 발생했습니다.

실행 위치:
C:\aidev\02_supabase-ai-backend\05_backend-mini-service-practice\04_implementation-guide

실행한 명령:
uvicorn main_mock:app --reload --host 127.0.0.1 --port 8004

오류 메시지:
ModuleNotFoundError: No module named 'fastapi'

기대한 결과:
서버가 실행되고 http://127.0.0.1:8004/docs 에 접속되어야 합니다.

내가 이미 시도한 것:
python --version은 확인했습니다.

요청:
가능한 원인을 가상환경, 패키지 설치, 실행 위치 순서로 점검해 주세요.
```

## 자주 만나는 오류 유형

| 오류 유형 | 흔한 원인 | 먼저 확인할 것 |
| --- | --- | --- |
| `ModuleNotFoundError` | 가상환경 미활성화, 패키지 미설치 | `.venv` 활성화, `pip install -r requirements.txt` |
| `ImportError` | 파일명 충돌, 잘못된 import 경로 | 현재 폴더, 파일 이름, import 문 |
| `uvicorn` 실행 오류 | 실행 위치 오류, app 이름 오류 | `main_mock:app`에서 파일명과 객체명 확인 |
| 404 응답 | URL 경로 불일치 | API 설계 문서의 `/questions` 경로와 일치하는지 확인 |
| 422 응답 | Pydantic 요청 검증 실패 | Request Body 필드와 타입 확인 |
| Supabase 저장 실패 | 테이블명/컬럼명 불일치, key 오류 | `mini_questions`, `mini_service_logs`, `.env` 확인 |
| Redis 오류 | Upstash URL/token 누락 | `UPSTASH_REDIS_REST_URL`, `UPSTASH_REDIS_REST_TOKEN` 확인 |
| LLM API 오류 | API key 누락, 모델명 오류, 과금/제한 | `GEMINI_API_KEY`, 모델명, 호출 제한 확인 |

## 가상환경 오류 디버깅 요청

```text
문제 상황:
패키지를 설치했는데 Python 실행 시 import 오류가 납니다.

실행 위치:
C:\aidev\02_supabase-ai-backend

실행한 명령:
python .\05_backend-mini-service-practice\04_implementation-guide\main_mock.py

오류 메시지:
ModuleNotFoundError: No module named 'fastapi'

확인한 것:
- .venv 폴더는 있습니다.
- PowerShell 앞에 (.venv)가 보이지 않습니다.

요청:
가상환경 활성화 여부와 패키지 설치 위치를 확인하는 순서를 알려 주세요.
```

## FastAPI 오류 디버깅 요청

```text
문제 상황:
FastAPI 서버는 실행되지만 Swagger UI에서 404가 발생합니다.

실행 명령:
uvicorn main_mock:app --reload --host 127.0.0.1 --port 8004

실제로 요청한 URL:
POST /wrong-path

설계 문서의 URL:
POST /questions

관련 파일:
main_mock.py

요청:
현재 API 설계 기준과 실제 요청 URL이 맞는지 확인해 주세요.
```

## Pydantic 422 오류 디버깅 요청

```text
문제 상황:
POST /questions 요청에서 422 오류가 발생합니다.

요청 JSON:
{
  "question": "FastAPI에서 Pydantic은 왜 사용하나요?"
}

오류 메시지:
field required: user_id

관련 파일:
schemas.py

요청:
Pydantic 검증 오류의 의미와 올바른 요청 JSON 예시를 설명해 주세요.
```

## Supabase 오류 디버깅 요청

```text
문제 상황:
main_supabase.py에서 질문 저장 시 Supabase 오류가 발생합니다.

실행 위치:
C:\aidev\02_supabase-ai-backend\05_backend-mini-service-practice\04_implementation-guide

실행 명령:
uvicorn main_supabase:app --reload --host 127.0.0.1 --port 8005

오류 메시지:
relation "mini_questions" does not exist

관련 파일:
main_supabase.py
03_supabase-schema/mini-service-schema.sql

확인한 것:
- .env에 실제 key 값은 적혀 있지만 여기에는 공유하지 않습니다.
- Supabase SQL Editor에서 SQL을 실행했는지 확실하지 않습니다.

요청:
테이블 생성 여부, 테이블명 불일치, SQL 실행 여부를 확인하는 순서를 알려 주세요.
```

## Upstash Redis 오류 디버깅 요청

```text
문제 상황:
Upstash Redis REST API 호출에서 인증 오류가 발생합니다.

오류 메시지:
401 Unauthorized

관련 환경변수:
UPSTASH_REDIS_REST_URL
UPSTASH_REDIS_REST_TOKEN

주의:
실제 token 값은 공유하지 않습니다.

요청:
URL과 token 설정, .env 로딩, 요청 헤더 확인 순서를 알려 주세요.
```

## LLM API 오류 디버깅 요청

```text
문제 상황:
Gemini API 호출 예제에서 인증 오류가 발생합니다.

오류 메시지:
API key not valid

관련 환경변수:
GEMINI_API_KEY
GEMINI_MODEL=gemini-2.5-flash-lite

주의:
실제 API key 값은 공유하지 않습니다.

요청:
API key 설정, .env 로딩, 모델명, 무료 사용 제한 확인 순서를 알려 주세요.
```

## 디버깅할 때 민감정보 보호

오류 메시지를 공유할 때 실제 key가 포함되어 있으면 반드시 가립니다.

```text
나쁜 예:
GEMINI_API_KEY=실제-gemini-api-key-값

좋은 예:
GEMINI_API_KEY=your-gemini-api-key
```

가려야 하는 값:

```text
SUPABASE_SERVICE_ROLE_KEY
SUPABASE_ANON_KEY 실제 값
UPSTASH_REDIS_REST_TOKEN
GEMINI_API_KEY
OPENAI_API_KEY
비밀번호
access token
refresh token
```

## Codex 답변을 적용하기 전 확인할 것

| 확인 항목 | 질문 |
| --- | --- |
| 파일 위치 | 답변이 실제 파일 위치와 맞나요? |
| 실행 위치 | 명령을 어느 폴더에서 실행해야 하나요? |
| 기존 구조 | 현재 API 이름과 테이블명을 유지하나요? |
| 보안 | key나 token을 코드에 직접 넣으라고 하지 않나요? |
| 의존성 | 새 패키지를 설치해야 한다면 이유가 명확한가요? |
| 검증 | 수정 후 어떤 명령으로 확인할 수 있나요? |

## 수정 후 재실행 기준

수정이 끝나면 반드시 다시 실행합니다.

```powershell
python -m py_compile main_mock.py
uvicorn main_mock:app --reload --host 127.0.0.1 --port 8004
```

FastAPI 서버라면 Swagger UI에서 직접 확인합니다.

```text
http://127.0.0.1:8004/docs
```

Supabase 저장 오류였다면 Table Editor에서 데이터가 저장되었는지도 확인합니다.

## 디버깅 기록 템플릿

```text
오류 이름:

발생 위치:

실행 명령:

오류 메시지:

원인:

수정한 내용:

다시 실행한 명령:

결과:

다음에 조심할 점:
```

## 완료 체크리스트

- [ ] 실행 위치를 기록했습니다.
- [ ] 실행 명령을 기록했습니다.
- [ ] 오류 메시지를 그대로 복사했습니다.
- [ ] 기대 결과와 실제 결과를 구분했습니다.
- [ ] 실제 key와 token은 공유하지 않았습니다.
- [ ] Codex 답변을 읽고 이해했습니다.
- [ ] 수정 후 다시 실행했습니다.
- [ ] 해결 결과를 기록했습니다.

## 다음 단계

다음 폴더인 `04_refactoring-with-codex`에서는 동작은 유지하면서 코드 구조를 더 읽기 쉽게 개선하는 방법을 학습합니다.
