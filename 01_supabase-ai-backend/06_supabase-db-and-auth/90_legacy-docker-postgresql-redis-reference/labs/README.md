# Legacy Labs

이 폴더는 Docker 기반 PostgreSQL/Redis 실습을 보관한 참고 자료입니다.

현재 과정의 기본 실습은 `10_labs`에서 Supabase와 Upstash Redis 기준으로 진행합니다. 이 legacy lab은 로컬 Docker 방식과 비교하고 싶을 때만 선택적으로 확인합니다.

## Lab 목록

| 순서 | 폴더 | 내용 |
|---|---|---|
| 1 | `lab-01_pull-and-run-postgresql` | PostgreSQL Docker image 다운로드와 실행 |
| 2 | `lab-02_create-tables-and-crud` | PostgreSQL 테이블 생성과 CRUD |
| 3 | `lab-03_python-postgresql-crud` | Python에서 로컬 PostgreSQL 연결 |
| 4 | `lab-04_fastapi-user-api-with-postgresql` | FastAPI 사용자 API와 PostgreSQL 연결 |
| 6 | `lab-06_pull-and-run-redis` | Redis Docker image 다운로드와 실행 |
| 7 | `lab-07_redis-session-store` | Redis 세션 저장 |
| 8 | `lab-08_conversation-history` | Redis와 대화 이력 구조 |
| 9 | `lab-09_cache-user-profile` | Redis 캐시 패턴 |
| 99 | `lab-99_user-session-cache-api` | 사용자 세션 캐시 API 예시 |

## 실행 전 확인

- Docker Desktop이 실행 중이어야 합니다.
- PostgreSQL 포트 `5432`가 비어 있어야 합니다.
- Redis 포트 `6379`가 비어 있어야 합니다.
- 현재 Supabase 과정에서는 이 lab을 실행하지 않아도 됩니다.
