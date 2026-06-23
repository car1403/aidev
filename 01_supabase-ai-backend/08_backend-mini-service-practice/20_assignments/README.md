# 20. Assignments

이 폴더는 `08_backend-mini-service-practice`의 과제 안내를 담고 있습니다.

과제는 미니 서비스를 단순히 실행하는 것에서 끝나지 않고, 요구사항 문서, API 설계, Supabase 스키마, 구현 결과, 코드 리뷰 기록을 하나의 백엔드 미니 서비스 산출물로 정리하는 데 목적이 있습니다.

## 과제 흐름

```text
Assignment 01 요구사항 정리
-> Assignment 02 API 설계
-> Assignment 03 Supabase 테이블 설계
-> Assignment 04 구현 결과 보고서
-> Assignment 05 코드 리뷰 기록
-> Assignment 99 미니 서비스 최종 제출
```

## 과제 목록

| 과제 | 폴더 | 핵심 산출물 |
| --- | --- | --- |
| Assignment 01 | `assignment-01_requirements-summary` | 서비스 요구사항 요약 |
| Assignment 02 | `assignment-02_api-design-document` | `/questions` 중심 API 설계 |
| Assignment 03 | `assignment-03_supabase-schema-document` | `mini_questions`, `mini_service_logs` 테이블 설계 |
| Assignment 04 | `assignment-04_implementation-report` | mock/Supabase 구현 결과 보고 |
| Assignment 05 | `assignment-05_code-review-record` | 코드 리뷰와 수정 기록 |
| Assignment 99 | `assignment-99_backend-mini-service-submission` | 최종 제출 체크리스트 |

## 공통 기준

이번 과제에서는 다음 API와 테이블 이름을 기준으로 합니다.

```text
API:
GET /health
POST /questions
GET /questions
GET /questions/{question_id}
POST /service-logs
GET /service-logs

Supabase tables:
mini_questions
mini_service_logs
```

## 제출 시 확인할 것

- 요구사항, API 설계, DB 설계, 구현 결과가 서로 맞아야 합니다.
- API 이름과 테이블 이름이 문서마다 다르면 안 됩니다.
- mock 서버 실행 결과와 Supabase 저장 결과를 구분해서 정리합니다.
- mock-first 응답과 이후 Gemini SDK 응답을 구분할 수 있도록 `provider`, `model`, `actual_api_called`, `llm_call_mode` 기준을 포함합니다.
- 오류가 발생했다면 오류 메시지, 원인, 해결 과정을 함께 적습니다.
- API Key, 비밀번호, 토큰 같은 민감 정보는 제출 자료에 포함하지 않습니다.
