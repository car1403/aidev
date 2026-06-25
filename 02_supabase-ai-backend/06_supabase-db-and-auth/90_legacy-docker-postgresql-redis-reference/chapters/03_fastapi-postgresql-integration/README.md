# 03_fastapi-postgresql-integration

FastAPI와 로컬 PostgreSQL을 직접 연결하는 legacy 참고 챕터입니다.

현재 과정에서는 FastAPI가 Supabase SDK 또는 Supabase REST API를 통해 데이터를 다룹니다.

## 핵심 개념

- FastAPI endpoint
- DB 연결 문자열
- 요청 데이터 검증
- 데이터 저장과 조회 API

## 현재 과정에서의 대응

| Legacy 방식 | 현재 과정 방식 |
|---|---|
| PostgreSQL 연결 문자열 사용 | `SUPABASE_URL`, `SUPABASE_SERVICE_ROLE_KEY` 사용 |
| SQL 직접 실행 | Supabase SDK 사용 |
| 로컬 DB 접속 오류 처리 | Supabase API 오류 처리 |

## 참고 위치

현재 과정에서는 아래 폴더를 우선 학습합니다.

```text
C:\aidev\02_supabase-ai-backend\06_supabase-db-and-auth\03_fastapi-supabase-integration
```
