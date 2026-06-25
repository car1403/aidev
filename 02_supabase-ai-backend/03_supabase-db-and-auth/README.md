# 03_supabase-db-and-auth

이 단원은 FastAPI 백엔드에서 Supabase를 사용해 데이터 저장, 인증, 사용자별 접근 제어, 대화 이력, 서비스 로그를 다루는 과정입니다.

`02_supabase-ai-backend`는 Supabase 중심으로 진행합니다. Redis는 Docker로 직접 실행하지 않고, Upstash Redis를 사용해 캐시, TTL, 임시 세션 상태, 요청 횟수 제한을 가볍게 실습합니다. Docker, Docker Compose, 로컬 PostgreSQL/Redis 운영은 `C:\aidev\07_multi-agent-service-ops`에서 본격적으로 학습합니다.

## 학습 목표

- Supabase 프로젝트를 만들고 API URL/key를 설정합니다.
- Supabase Table Editor와 SQL Editor로 테이블을 설계합니다.
- Python Supabase client로 CRUD를 실행합니다.
- FastAPI endpoint에서 Supabase를 호출합니다.
- Supabase Auth와 RLS의 역할을 이해합니다.
- 사용자 대화 이력과 서비스 로그를 Supabase 테이블에 저장하는 구조를 설계합니다.
- Upstash Redis로 TTL 기반 캐시, 임시 세션, 요청 횟수 제한을 실습합니다.
- Supabase에 저장할 데이터와 Redis에 저장할 데이터를 구분합니다.

## 이 단원에서 만드는 것

| 구분 | 결과물 | 설명 |
|---|---|---|
| Supabase 설정 | `.env` 환경변수 확인 스크립트 | URL/key가 정확히 들어갔는지 안전하게 확인합니다. |
| DB 기초 | `learning_notes` CRUD 예제 | Python에서 Supabase 테이블에 생성/조회/수정/삭제를 실행합니다. |
| API 연동 | FastAPI `notes` API | 백엔드 endpoint가 Supabase를 호출하는 구조를 익힙니다. |
| 인증/보안 | Auth/RLS 설계 문서와 예제 | 로그인 사용자와 데이터 접근 정책의 관계를 이해합니다. |
| 로그/이력 | 대화 이력/서비스 로그 저장 예제 | AI 서비스에서 남겨야 하는 데이터를 Supabase에 저장합니다. |
| Redis | Upstash Redis TTL/cache/session/rate limit 예제 | 오래 저장하지 않아도 되는 임시 상태를 Redis에 저장합니다. |
| 실습/과제 | `10_labs`, `20_assignments` | 따라 하기 실습과 제출 과제를 분리해서 진행합니다. |

## 단원 구조

```text
03_supabase-db-and-auth
├─ 00_references
├─ 01_supabase-project-and-env
├─ 02_supabase-table-and-crud
├─ 03_fastapi-supabase-integration
├─ 04_supabase-auth-and-rls
├─ 05_conversation-history-and-service-logs
├─ 06_upstash-redis-cache-and-session
├─ 10_labs
├─ 20_assignments
└─ 90_legacy-docker-postgresql-redis-reference
```

## 권장 학습 순서

```text
00_references/README.md
-> 00_references/supabase-first-notes.md
-> 01_supabase-project-and-env
-> 02_supabase-table-and-crud
-> 03_fastapi-supabase-integration
-> 04_supabase-auth-and-rls
-> 05_conversation-history-and-service-logs
-> 06_upstash-redis-cache-and-session
-> 10_labs
-> 20_assignments
```

## 먼저 준비할 것

최상위 폴더에서 `.env`를 준비합니다.

```powershell
cd C:\aidev\02_supabase-ai-backend
Copy-Item .env.example .env
```

`.env`에 Supabase 값을 입력합니다.

```env
SUPABASE_URL=https://your-project-ref.supabase.co
SUPABASE_ANON_KEY=your-supabase-anon-key
SUPABASE_SERVICE_ROLE_KEY=your-supabase-service-role-key
UPSTASH_REDIS_REST_URL=https://your-upstash-redis-url.upstash.io
UPSTASH_REDIS_REST_TOKEN=your-upstash-redis-rest-token
```

위 값은 예시입니다. 실제 실습에서는 Supabase Dashboard와 Upstash Console에서 발급받은 실제 값을 `.env`에 넣어야 합니다. `.env`는 GitHub에 올리지 않습니다.

가상환경을 활성화하고 패키지를 설치합니다.

```powershell
cd C:\aidev\02_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Supabase 테이블 준비

기본 실습용 SQL은 아래 파일에 있습니다.

```text
C:\aidev\02_supabase-ai-backend\03_supabase-db-and-auth\00_references\supabase-schema.sql
```

Supabase Dashboard의 SQL Editor에서 실행합니다.

처음에는 `learning_notes` 테이블 하나로 시작하고, 이후 `conversations`, `messages`, `service_logs`로 확장합니다.

## 기본 실행 순서

환경변수 확인:

```powershell
cd C:\aidev\02_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
python .\03_supabase-db-and-auth\01_supabase-project-and-env\01_check_supabase_env.py
```

Supabase CRUD 확인:

```powershell
python .\03_supabase-db-and-auth\02_supabase-table-and-crud\01_learning_notes_crud.py
```

FastAPI + Supabase 실행:

```powershell
cd C:\aidev\02_supabase-ai-backend\03_supabase-db-and-auth\03_fastapi-supabase-integration
..\..\.venv\Scripts\Activate.ps1
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

확인 주소:

```text
http://127.0.0.1:8000/docs
```

대화 이력과 서비스 로그 저장:

```powershell
cd C:\aidev\02_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
python .\03_supabase-db-and-auth\05_conversation-history-and-service-logs\01_insert_conversation_and_log.py
```

Upstash Redis 환경변수 확인:

```powershell
python .\03_supabase-db-and-auth\06_upstash-redis-cache-and-session\01_check_upstash_env.py
```

Upstash Redis TTL 캐시 실습:

```powershell
python .\03_supabase-db-and-auth\06_upstash-redis-cache-and-session\02_cache_set_get_ttl.py
```

Upstash Redis 요청 제한 실습:

```powershell
python .\03_supabase-db-and-auth\06_upstash-redis-cache-and-session\03_rate_limit_example.py
```

Upstash Redis 세션 상태 실습:

```powershell
python .\03_supabase-db-and-auth\06_upstash-redis-cache-and-session\04_session_state_example.py
```

캐시 우선 조회 흐름 실습:

```powershell
python .\03_supabase-db-and-auth\06_upstash-redis-cache-and-session\05_cache_aside_mock.py
```

FastAPI 요청 제한 구조 확인:

```powershell
cd C:\aidev\02_supabase-ai-backend\03_supabase-db-and-auth\06_upstash-redis-cache-and-session
..\..\.venv\Scripts\Activate.ps1
uvicorn 06_fastapi_rate_limit_dependency:app --reload --host 127.0.0.1 --port 8001
```

확인 주소:

```text
http://127.0.0.1:8001/docs
```

## Supabase와 Redis를 함께 보는 기준

가장 자주 헷갈리는 부분은 “어떤 데이터는 Supabase에 넣고, 어떤 데이터는 Redis에 넣어야 하는가”입니다.

| 데이터 예시 | 저장 위치 | 이유 |
|---|---|---|
| 사용자 프로필 | Supabase | 나중에 다시 조회해야 하는 영구 데이터입니다. |
| 대화 이력 | Supabase | 사용자가 과거 대화를 다시 볼 수 있어야 합니다. |
| 서비스 로그 | Supabase | 오류 분석, 사용 기록, 품질 개선에 사용합니다. |
| 30초짜리 검색 결과 캐시 | Upstash Redis | 잠깐만 빠르게 재사용하면 됩니다. |
| 로그인 후 임시 세션 상태 | Upstash Redis | 만료 시간이 있고 빠르게 조회해야 합니다. |
| 사용자별 1분 요청 횟수 | Upstash Redis | 시간이 지나면 자동으로 초기화되어도 됩니다. |

중요한 기준은 다음과 같습니다.

```text
오래 보관해야 한다 -> Supabase
검색/분석/조회가 중요하다 -> Supabase
짧게 보관하고 자동 만료되어도 된다 -> Upstash Redis
빠르게 카운트하거나 중복 요청을 막아야 한다 -> Upstash Redis
```

## Lab과 Assignment

따라 하기 실습은 아래 폴더에서 진행합니다.

```text
C:\aidev\02_supabase-ai-backend\03_supabase-db-and-auth\10_labs
```

제출 과제는 아래 폴더에서 진행합니다.

```text
C:\aidev\02_supabase-ai-backend\03_supabase-db-and-auth\20_assignments
```

## Docker 자료 안내

이전 PostgreSQL/Redis/Docker 자료는 삭제하지 않고 아래 참고 폴더로 분리했습니다.

```text
C:\aidev\02_supabase-ai-backend\03_supabase-db-and-auth\90_legacy-docker-postgresql-redis-reference
```

현재 과정에서는 이 폴더를 먼저 사용하지 않아도 됩니다. Docker로 PostgreSQL/Redis를 직접 실행하고 운영하는 방식은 아래 과정에서 다룹니다.

```text
C:\aidev\07_multi-agent-service-ops
```

## 자주 만나는 오류

### Supabase 값이 없다고 나오는 경우

`.env`가 있는지 확인합니다.

```powershell
cd C:\aidev\02_supabase-ai-backend
dir .env
```

### relation learning_notes does not exist

Supabase SQL Editor에서 `supabase-schema.sql`의 테이블 생성 SQL을 먼저 실행합니다.

### Could not find the table conversations

대화 이력 실습용 테이블이 아직 없다는 뜻입니다. `00_references/supabase-schema.sql`을 Supabase SQL Editor에서 실행한 뒤 다시 시도합니다.

### FastAPI에서 Supabase 연결 실패

확인할 것:

1. `.env`가 최상위 폴더에 있는가?
2. `SUPABASE_URL`이 정확한가?
3. `SUPABASE_SERVICE_ROLE_KEY`가 실제 값인가?
4. Supabase 프로젝트가 paused 상태는 아닌가?

### Upstash Redis 연결 실패

확인할 것:

1. `.env`에 `UPSTASH_REDIS_REST_URL`이 있는가?
2. `.env`에 `UPSTASH_REDIS_REST_TOKEN`이 있는가?
3. Upstash Redis database가 삭제되거나 비활성화되지 않았는가?
4. URL 끝에 불필요한 공백이 들어가지 않았는가?
