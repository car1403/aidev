# 10_labs

이 폴더는 `03_supabase-db-and-auth`에서 배운 내용을 작은 실습 단위로 다시 확인하는 공간입니다.

앞쪽 챕터에서는 Supabase 프로젝트 생성, 테이블 설계, FastAPI 연동, Auth/RLS 개념, 대화 이력 저장, Upstash Redis 캐시와 세션을 각각 따로 학습했습니다. 이 폴더에서는 그 내용을 순서대로 다시 실행하면서 “내가 어떤 데이터를 어디에 저장하고 있는지”를 확인합니다.

Docker, Docker Compose, 로컬 PostgreSQL, 로컬 Redis 운영은 이 과정에서 진행하지 않습니다. Docker 기반 서비스 운영은 `C:\aidev\07_multi-agent-service-ops`에서 본격적으로 다룹니다.

## 실습 전 준비

먼저 백엔드 과정 루트에서 가상환경을 활성화합니다.

```powershell
cd C:\aidev\02_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

필요 패키지는 앞선 과정에서 `requirements.txt`로 이미 설치되어 있다는 전제로 진행합니다. 설치가 안 되어 있다면 아래 명령으로 다시 설치할 수 있습니다.

```powershell
pip install -r requirements.txt
```

Supabase 관련 실습을 진행하려면 `.env`에 Supabase 값이 필요합니다.

```text
SUPABASE_URL=...
SUPABASE_ANON_KEY=...
SUPABASE_SERVICE_ROLE_KEY=...
```

Upstash Redis 관련 실습을 진행하려면 `.env`에 Upstash 값이 필요합니다.

```text
UPSTASH_REDIS_REST_URL=...
UPSTASH_REDIS_REST_TOKEN=...
```

## 실습 순서

| 순서 | 폴더 | 연결 챕터 | 핵심 결과 |
|---|---|---|---|
| 1 | `lab-01_supabase-env-check` | `01_supabase-project-and-env` | Supabase 환경변수 준비 상태 확인 |
| 2 | `lab-02_supabase-schema-preparation` | `00_references`, `02_supabase-table-and-crud` | 테이블 생성 전 체크리스트 확인 |
| 3 | `lab-03_learning-notes-crud` | `02_supabase-table-and-crud` | Python으로 Supabase CRUD 흐름 실행 |
| 4 | `lab-04_fastapi-supabase-notes-api` | `03_fastapi-supabase-integration` | FastAPI API와 Supabase 연결 확인 |
| 5 | `lab-05_auth-rls-policy-check` | `04_supabase-auth-and-rls` | 보호 API와 RLS 개념 연결 |
| 6 | `lab-06_conversation-log-storage` | `05_conversation-history-and-service-logs` | 대화 이력과 서비스 로그 저장 흐름 확인 |
| 7 | `lab-07_upstash-env-check` | `06_upstash-redis-cache-and-session` | Upstash Redis 환경변수 확인 |
| 8 | `lab-08_upstash-ttl-cache` | `06_upstash-redis-cache-and-session` | TTL 캐시 저장과 만료 흐름 확인 |
| 9 | `lab-09_upstash-rate-limit` | `06_upstash-redis-cache-and-session` | 요청 횟수 제한 구조 확인 |
| 10 | `lab-10_upstash-session-cache-aside` | `06_upstash-redis-cache-and-session` | 임시 세션과 cache-aside 구조 확인 |
| 11 | `lab-11_fastapi-rate-limit-dependency` | `06_upstash-redis-cache-and-session` | FastAPI 의존성 기반 rate limit 확인 |

## Supabase 테이블 준비 기준

대화 이력과 서비스 로그 실습은 Supabase에 테이블이 있어야 정상 동작합니다. 테이블이 없다면 Supabase에서 `PGRST205` 또는 `Could not find the table` 같은 오류가 발생할 수 있습니다.

이 경우 Supabase Dashboard의 SQL Editor에서 아래 파일을 실행합니다.

```text
C:\aidev\02_supabase-ai-backend\03_supabase-db-and-auth\00_references\supabase-schema.sql
```

## 실습 결과 정리 방법

각 lab을 진행한 뒤 아래 내용을 짧게 기록하면 좋습니다.

- 실행한 파일 또는 접속한 URL
- 정상 실행 결과
- 발생한 오류 메시지
- 오류를 해결한 방법
- Supabase에 저장되는 데이터와 Redis에 저장되는 데이터의 차이

## Legacy Docker Labs

이전 Docker/PostgreSQL/Redis 직접 실행 labs는 아래 참고 폴더에 남겨 두었습니다.

```text
C:\aidev\02_supabase-ai-backend\03_supabase-db-and-auth\90_legacy-docker-postgresql-redis-reference\labs
```

이 과정의 현재 실습 기준은 Supabase와 Upstash Redis입니다.
