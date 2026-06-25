# 10. Labs

이 폴더는 `05_backend-mini-service-practice`의 실습 안내를 담고 있습니다.

실습은 요구사항 확인에서 시작해 API 설계, Supabase 스키마, mock 서버 실행, Supabase 서버 실행, 최종 점검 순서로 진행합니다. 각 실습은 앞 단원에서 만든 문서와 예제 파일을 다시 열어 보면서 진행합니다.

LLM 답변 생성은 `02_llm-api-integration`의 변경 방향에 맞춰 `mock-first -> Gemini SDK 기본 구현 -> REST 보충 -> OpenAI 선택 비교` 흐름으로 바라봅니다. 이 단원에서는 실제 SDK 호출보다 저장 구조와 로그 구조를 먼저 완성합니다.

## 실습 흐름

```text
Lab 01 요구사항 확인
-> Lab 02 API 설계 확인
-> Lab 03 Supabase 스키마 확인
-> Lab 04 mock-first 함수 이해
-> Lab 05 mock FastAPI 서버 실행
-> Lab 06 Supabase 테이블 생성
-> Lab 07 Supabase FastAPI 서버 실행
-> Lab 99 최종 점검
```

## 실습 목록

| 실습 | 폴더 | 핵심 내용 |
| --- | --- | --- |
| Lab 01 | `lab-01_requirements-review` | 요구사항과 제외 범위 확인 |
| Lab 02 | `lab-02_api-design-review` | `/questions` API 설계 확인 |
| Lab 03 | `lab-03_supabase-schema-review` | `mini_questions`, `mini_service_logs` 스키마 확인 |
| Lab 04 | `lab-04_mock-llm-flow` | mock-first 함수와 비용 없는 테스트 흐름 이해 |
| Lab 05 | `lab-05_mock-fastapi-run` | `main_mock.py` 실행 및 Swagger UI 테스트 |
| Lab 06 | `lab-06_supabase-table-setup` | Supabase SQL Editor에서 테이블 생성 |
| Lab 07 | `lab-07_supabase-fastapi-run` | `main_supabase.py` 실행 및 실제 저장 확인 |
| Lab 99 | `lab-99_final-checklist` | API, 테이블, 로그, 오류 응답 최종 점검 |

## 공통 준비

실습은 `02_supabase-ai-backend`의 `.venv`를 사용합니다.

```powershell
cd C:\aidev\02_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
```

mock 서버는 Supabase 설정 없이 실행할 수 있습니다. Supabase 서버는 `.env`와 테이블 생성이 완료된 뒤 실행합니다.

## 공통 API 기준

이번 실습에서는 다음 API 이름을 사용합니다.

```text
GET /health
POST /questions
GET /questions
GET /questions/{question_id}
POST /service-logs
GET /service-logs
```

## 공통 테이블 기준

이번 실습에서는 다음 Supabase 테이블을 사용합니다.

```text
mini_questions
mini_service_logs
```

## 완료 기준

- 요구사항과 API 설계가 서로 연결되어 있어야 합니다.
- API 설계와 Supabase 테이블 컬럼이 서로 맞아야 합니다.
- mock 서버에서 질문 생성, 목록 조회, 상세 조회, 로그 조회가 가능해야 합니다.
- 질문/답변과 서비스 로그에 `provider`, `model`, `actual_api_called`, `llm_call_mode` 기준이 반영되어야 합니다.
- Supabase 서버에서 실제 데이터 저장과 조회가 가능해야 합니다.
- 오류가 발생했을 때 원인을 확인할 수 있는 응답과 로그 기준이 있어야 합니다.
