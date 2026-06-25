# Legacy Chapters

이 폴더는 Docker 기반 PostgreSQL/Redis 학습 흐름을 챕터 단위로 보관한 참고 자료입니다.

현재 `03_supabase-db-and-auth` 과정에서는 Supabase와 Upstash Redis를 사용하므로, 이 챕터들은 필수 학습이 아니라 비교 참고 자료입니다.

## 챕터 목록

| 순서 | 폴더 | 내용 |
|---|---|---|
| 1 | `01_docker-postgresql-setup` | Docker로 PostgreSQL 컨테이너 실행 |
| 2 | `02_postgresql-table-and-crud` | PostgreSQL 테이블과 CRUD |
| 3 | `03_fastapi-postgresql-integration` | FastAPI와 로컬 PostgreSQL 연결 |
| 4 | `04_auth-and-access-control` | 직접 구현하는 인증/접근 제어 개념 |
| 5 | `05_docker-redis-setup` | Docker로 Redis 컨테이너 실행 |
| 6 | `06_redis-session-and-conversation-history` | Redis 세션과 대화 이력 구조 |
| 7 | `07_redis-cache-optimization` | Redis 캐시 최적화 패턴 |

## 참고 기준

Supabase 과정에서 같은 개념은 아래처럼 연결됩니다.

| Legacy 개념 | 현재 과정에서의 대응 |
|---|---|
| 로컬 PostgreSQL | Supabase managed PostgreSQL |
| 직접 SQL 접속 | Supabase Dashboard, Supabase Python SDK |
| 직접 인증 구현 | Supabase Auth, RLS |
| 로컬 Redis | Upstash Redis |
| Docker 컨테이너 관리 | `07_multi-agent-service-ops`에서 본격 학습 |
