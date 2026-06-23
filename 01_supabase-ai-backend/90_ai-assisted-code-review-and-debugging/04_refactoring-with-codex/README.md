# 04. Refactoring With Codex

이 단원에서는 Codex를 활용해 코드의 동작은 유지하면서 구조를 더 읽기 쉽고 관리하기 좋게 개선하는 방법을 학습합니다.

리팩토링은 “기능을 새로 추가하는 작업”이 아닙니다. 이미 동작하는 코드를 더 명확하게 나누고, 중복을 줄이고, 이름을 개선하고, 나중에 수정하기 쉽게 만드는 작업입니다.

## 이번 단계의 목표

- 리팩토링과 기능 추가의 차이를 이해합니다.
- 동작을 바꾸지 않는다는 조건을 명확히 적는 방법을 익힙니다.
- 변수명 개선, 함수 분리, 중복 제거, 파일 분리 요청 방법을 학습합니다.
- FastAPI, Supabase, mock-first 코드에서 리팩토링할 수 있는 부분을 구분합니다.
- 리팩토링 전후 실행 결과를 비교하는 습관을 만듭니다.

## 리팩토링이 필요한 경우

| 상황 | 리팩토링 방향 |
| --- | --- |
| 코드가 너무 길다 | 역할별 함수로 분리 |
| 같은 코드가 반복된다 | 공통 함수로 분리 |
| 변수명이 모호하다 | 의미가 드러나는 이름으로 변경 |
| 한 함수가 여러 일을 한다 | 검증, 처리, 저장, 응답 생성을 나눔 |
| 파일 하나에 모든 코드가 있다 | `schemas.py`, `service_logger.py`, `main.py`처럼 역할별 파일 분리 |
| 오류 처리가 중복된다 | 공통 오류 처리 함수로 분리 |

## 리팩토링할 때 지켜야 할 기준

```text
1. 동작을 바꾸지 않습니다.
2. API URL을 임의로 바꾸지 않습니다.
3. 요청/응답 JSON 구조를 임의로 바꾸지 않습니다.
4. Supabase 테이블명과 컬럼명을 임의로 바꾸지 않습니다.
5. 한 번에 너무 많은 파일을 바꾸지 않습니다.
6. 수정 전후 실행 결과를 비교합니다.
```

## 좋은 리팩토링 요청 구조

```text
목표:
현재 코드의 동작:
리팩토링하고 싶은 이유:
수정할 파일:
바꾸어도 되는 것:
바꾸면 안 되는 것:
완료 기준:
```

## 기본 요청 예시

```text
아래 파일을 리팩토링해 주세요.

파일:
C:\aidev\01_supabase-ai-backend\08_backend-mini-service-practice\04_implementation-guide\main_mock.py

현재 동작:
- POST /questions로 질문을 등록합니다.
- mock 답변을 생성합니다.
- 메모리 리스트에 저장합니다.
- service_logs에 로그를 남깁니다.

리팩토링 목표:
- 질문 item을 만드는 부분을 함수로 분리해 주세요.
- 서비스 로그를 저장하는 부분을 함수로 분리해 주세요.
- 변수명을 더 명확하게 바꿔 주세요.

바꾸면 안 되는 것:
- API 경로 /questions
- 응답 형식 {"ok": true, "item": ...}
- request 모델 이름
- mock-first 사용 방식

완료 기준:
- 기존 Swagger UI 테스트가 그대로 통과해야 합니다.
- POST /questions 응답 구조가 바뀌면 안 됩니다.
```

## 좋지 않은 리팩토링 요청

```text
전체적으로 깔끔하게 바꿔줘.
```

```text
좋은 구조로 고쳐줘.
```

이런 요청은 기준이 모호합니다. Codex가 API 이름이나 응답 구조까지 바꿔 버릴 수 있습니다.

## Python 스크립트 리팩토링 예시

### 수정 전 문제

```text
하나의 파일에 입력, 계산, 출력 코드가 모두 섞여 있음
변수명이 a, b, c처럼 의미가 없음
같은 계산 코드가 반복됨
```

### 요청 예시

```text
아래 Python 스크립트를 리팩토링해 주세요.

조건:
- 실행 결과는 바꾸지 마세요.
- 입력 처리, 계산, 출력 부분을 함수로 나누어 주세요.
- 변수명을 의미 있게 바꿔 주세요.
- 초보자가 이해할 수 있도록 핵심 주석을 추가해 주세요.

완료 기준:
- 리팩토링 전과 후의 출력 결과가 같아야 합니다.
```

## FastAPI 코드 리팩토링 예시

FastAPI에서는 API 경로와 응답 형식을 유지하는 것이 중요합니다.

```text
파일:
main_mock.py

리팩토링 목표:
- question item 생성 로직을 build_question_item 함수로 분리
- 로그 생성 로직을 append_question_created_log 함수로 분리
- endpoint 함수는 요청 흐름만 보이도록 정리

바꾸면 안 되는 것:
- POST /questions
- GET /questions
- GET /questions/{question_id}
- 응답의 ok, item, items 구조
```

## Supabase 코드 리팩토링 예시

Supabase 코드는 테이블명과 컬럼명이 바뀌면 바로 오류가 발생합니다.

```text
파일:
main_supabase.py

리팩토링 목표:
- Supabase insert 코드를 save_question_to_supabase 함수로 분리
- 서비스 로그 저장 코드를 insert_service_log 함수로 유지
- APIError 처리 함수를 공통화

바꾸면 안 되는 것:
- mini_questions 테이블명
- mini_service_logs 테이블명
- user_id, question, answer, provider, model, actual_api_called, llm_call_mode 컬럼명
- service role key를 코드에 직접 넣지 않는 기준
```

## 리팩토링 전 점검

수정하기 전에 현재 동작을 먼저 확인합니다.

```powershell
python -m py_compile main_mock.py
uvicorn main_mock:app --reload --host 127.0.0.1 --port 8004
```

Swagger UI:

```text
http://127.0.0.1:8004/docs
```

확인할 API:

```text
GET /health
POST /questions
GET /questions
GET /questions/{question_id}
GET /service-logs
```

## 리팩토링 후 점검

리팩토링 후에는 같은 명령을 다시 실행합니다.

```powershell
python -m py_compile main_mock.py
uvicorn main_mock:app --reload --host 127.0.0.1 --port 8004
```

비교할 내용:

| 항목 | 확인 |
| --- | --- |
| 서버 실행 | 오류 없이 실행되는가? |
| API 경로 | 기존 경로가 유지되는가? |
| 응답 구조 | `ok`, `item`, `items` 구조가 유지되는가? |
| 로그 저장 | `question_created` 로그가 계속 생성되는가? |
| 코드 이해 | 함수 이름과 변수명이 더 명확해졌는가? |

## 리팩토링 결과 기록 템플릿

```text
리팩토링 대상 파일:

수정 전 문제:

수정한 내용:

바꾸지 않은 것:

실행 확인 명령:

수정 후 결과:

남은 개선점:
```

## Codex 답변을 검토할 때 확인할 것

| 점검 항목 | 확인 질문 |
| --- | --- |
| 동작 유지 | 기능이 바뀌지 않았나요? |
| API 경로 | URL이 바뀌지 않았나요? |
| 응답 형식 | JSON 구조가 바뀌지 않았나요? |
| 테이블명 | Supabase 테이블명이 유지되었나요? |
| 보안 | key나 token을 코드에 직접 넣지 않았나요? |
| 범위 | 요청하지 않은 파일까지 과하게 바꾸지 않았나요? |
| 이해 가능성 | 수정된 코드를 설명할 수 있나요? |

## 완료 체크리스트

- [ ] 리팩토링 전 실행 결과를 확인했습니다.
- [ ] 바꾸면 안 되는 조건을 요청문에 적었습니다.
- [ ] 한 번에 너무 큰 범위를 수정하지 않았습니다.
- [ ] 리팩토링 후 다시 실행했습니다.
- [ ] API 경로와 응답 구조가 유지되었습니다.
- [ ] 테이블명과 컬럼명이 유지되었습니다.
- [ ] 수정 이유를 설명할 수 있습니다.

## 다음 단계

다음 폴더인 `05_code-review-with-codex`에서는 코드가 요구사항, 안정성, 보안, 가독성 기준을 만족하는지 리뷰하는 방법을 학습합니다.
