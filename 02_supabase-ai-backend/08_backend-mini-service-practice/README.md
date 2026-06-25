# 08. Backend Mini Service Practice

이 단원은 `01`부터 `07`까지 배운 내용을 작은 백엔드 서비스로 묶어 보는 실습 단계입니다.

최종 백엔드 프로젝트로 가기 전에 FastAPI, Pydantic, Supabase, 서비스 로그, mock-first LLM 흐름을 하나의 작은 서비스 안에서 연결합니다. 처음에는 비용과 설정 부담을 줄이기 위해 mock 함수와 메모리 저장소로 시작하고, 이후 Supabase 테이블 저장 방식으로 확장합니다.

## 핵심 요약

- 요구사항을 먼저 정리한 뒤 API를 설계합니다.
- API 설계에 맞춰 Supabase 테이블을 설계합니다.
- mock 서버로 전체 흐름을 먼저 확인합니다.
- Supabase 서버로 실제 저장 흐름을 확인합니다.
- 서비스 로그를 통해 성공, 실패, 오류 상황을 추적합니다.
- 실제 LLM 연동은 앞 단원 기준에 맞춰 Gemini SDK를 기본 확장 방향으로 잡고, REST 호출은 구조 이해용 보충, OpenAI 예제는 선택 비교용으로 유지합니다.
- 저장 데이터와 서비스 로그에는 `provider`, `model`, `actual_api_called`, `llm_call_mode`를 남겨 mock 응답과 실제 Gemini SDK 응답을 구분합니다.

## 구현 주제

```text
AI 질문 응답 백엔드 미니 서비스
```

사용자가 질문을 보내면 백엔드가 다음 일을 처리합니다.

```text
사용자 질문 요청
-> FastAPI 요청 검증
-> mock-first 답변 생성
-> 질문/답변 저장
-> 서비스 로그 저장
-> JSON 응답 반환
```

## 폴더 구성

```text
08_backend-mini-service-practice
├─ README.md
├─ 00_references
├─ 01_requirements
├─ 02_api-design
├─ 03_supabase-schema
├─ 04_implementation-guide
├─ 10_labs
└─ 20_assignments
```

## 학습 순서

| 순서 | 폴더 | 내용 |
| --- | --- | --- |
| 1 | `00_references` | 미니 서비스 설계 기준과 체크리스트 확인 |
| 2 | `01_requirements` | 서비스 목적, 기능 요구사항, 제외 범위 정리 |
| 3 | `02_api-design` | `/questions`, `/service-logs` API 설계 |
| 4 | `03_supabase-schema` | `mini_questions`, `mini_service_logs` 테이블 설계 |
| 5 | `04_implementation-guide` | mock 서버와 Supabase 서버 구현 |
| 6 | `10_labs` | 단계별 실습 진행 |
| 7 | `20_assignments` | 요구사항, API, DB, 구현 결과 과제 정리 |

## API 기준

이번 단원에서는 다음 API 이름을 사용합니다.

```text
GET /health
POST /questions
GET /questions
GET /questions/{question_id}
POST /service-logs
GET /service-logs
```

## Supabase 테이블 기준

이번 단원에서는 다음 테이블을 사용합니다.

```text
mini_questions
mini_service_logs
```

| 테이블 | 역할 |
| --- | --- |
| `mini_questions` | 사용자 질문과 AI 답변 저장, mock-first/Gemini SDK 호출 기준 기록 |
| `mini_service_logs` | API 처리 성공/실패, 오류, 처리 정보 저장 |

## 실습 파일

```text
01_requirements/service-requirements.md
-> 미니 서비스 요구사항 정의서입니다.

02_api-design/api-design.md
-> endpoint, 요청/응답, 오류 형식을 설계합니다.

03_supabase-schema/table-design.md
-> Supabase 테이블 설계 기준을 설명합니다.

03_supabase-schema/mini-service-schema.sql
-> Supabase SQL Editor에서 실행할 테이블 생성 SQL입니다.

04_implementation-guide/schemas.py
-> FastAPI 요청/응답 Pydantic 모델입니다.

04_implementation-guide/llm_mock.py
-> 비용 없이 AI 답변 생성을 흉내 내는 함수입니다.

04_implementation-guide/service_logger.py
-> 서비스 로그 데이터를 만드는 보조 함수입니다.

04_implementation-guide/supabase_client.py
-> Supabase client 생성 함수를 분리한 파일입니다.

04_implementation-guide/main_mock.py
-> 외부 서비스 없이 메모리 저장소로 실행하는 FastAPI 앱입니다.

04_implementation-guide/main_supabase.py
-> Supabase 테이블에 실제 저장하는 FastAPI 앱입니다.
```

## 실행 준비

이 단원은 `02_supabase-ai-backend` 루트의 `.venv`를 사용합니다.

```powershell
cd C:\aidev\02_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
```

필요한 패키지는 앞 단원에서 `requirements.txt`로 설치되어 있어야 합니다.

```powershell
pip install -r requirements.txt
```

이미 설치했다면 다시 설치하지 않아도 됩니다. 새 터미널을 열었다면 가상환경 활성화는 다시 해야 합니다.

## mock 서버 실행

mock 서버는 Supabase URL이나 API Key 없이 실행할 수 있습니다.

```powershell
cd C:\aidev\02_supabase-ai-backend\08_backend-mini-service-practice\04_implementation-guide
..\..\.venv\Scripts\Activate.ps1
uvicorn main_mock:app --reload --host 127.0.0.1 --port 8004
```

Swagger UI:

```text
http://127.0.0.1:8004/docs
```

먼저 mock 서버에서 API 구조를 확인합니다.

```text
GET /health
POST /questions
GET /questions
GET /questions/{question_id}
GET /service-logs
```

## Supabase 서버 실행

Supabase 서버는 다음 준비가 완료된 뒤 실행합니다.

```text
1. Supabase 프로젝트 준비
2. .env에 Supabase URL과 Key 설정
3. 03_supabase-schema/mini-service-schema.sql 실행
4. mini_questions, mini_service_logs 테이블 생성 확인
```

실행 명령:

```powershell
cd C:\aidev\02_supabase-ai-backend\08_backend-mini-service-practice\04_implementation-guide
..\..\.venv\Scripts\Activate.ps1
uvicorn main_supabase:app --reload --host 127.0.0.1 --port 8005
```

Swagger UI:

```text
http://127.0.0.1:8005/docs
```

## 이번 단원에서 깊게 다루지 않는 것

| 항목 | 다루는 위치 |
| --- | --- |
| SSE 실시간 응답 스트리밍 | `04_supabase-ai-mini-project` |
| Streamlit 프론트엔드 통합 | `03_supabase-ai-frontend`, `04_supabase-ai-mini-project` |
| Docker 기반 실행 | `05_llm-agent-orchestration` 이후 |
| Docker Compose, AWS, GitHub Actions | `07_multi-agent-service-ops` |

## 완료 기준

- 요구사항 문서가 API 설계로 연결되어 있습니다.
- API 설계가 Supabase 테이블 설계로 연결되어 있습니다.
- mock 서버에서 질문 생성과 조회가 됩니다.
- Supabase 서버에서 실제 데이터 저장과 조회가 됩니다.
- 서비스 로그를 통해 API 처리 결과를 확인할 수 있습니다.
- `10_labs`와 `20_assignments`의 점검 기준을 완료했습니다.

## 다음 단계

이 단원을 마친 뒤 `90_ai-assisted-code-review-and-debugging`에서 코드 리뷰와 디버깅 흐름을 점검하고, `99_final-backend-project`에서 백엔드 최종 프로젝트로 확장합니다.
