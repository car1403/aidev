# 10_labs

이 폴더는 Supabase 중심 실습을 진행하는 공간입니다.

## 권장 실습

### Lab 01 - Supabase 환경변수 확인

목표:

- `.env`가 준비되어 있는지 확인합니다.
- Supabase URL/key가 설정되어 있는지 확인합니다.

실행:

```powershell
cd C:\aidev\01_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
python .\06_supabase-db-and-auth\01_ch1_supabase-project-and-env\01_check_supabase_env.py
```

### Lab 02 - Supabase 테이블 생성

목표:

- Supabase SQL Editor에서 `learning_notes` 테이블을 만듭니다.
- `00_references/supabase-schema.sql`을 사용합니다.

### Lab 03 - Python Supabase CRUD

목표:

- Python에서 Supabase 테이블에 데이터를 저장하고 조회합니다.

실행:

```powershell
python .\06_supabase-db-and-auth\02_ch2_supabase-table-and-crud\01_learning_notes_crud.py
```

### Lab 04 - FastAPI와 Supabase 연결

목표:

- `/health`
- `/notes` GET
- `/notes` POST

실행:

```powershell
cd C:\aidev\01_supabase-ai-backend\06_supabase-db-and-auth\03_ch3_fastapi-supabase-integration
..\..\.venv\Scripts\Activate.ps1
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

확인:

```text
http://127.0.0.1:8000/docs
```

### Lab 05 - Auth/RLS 설계

목표:

- Supabase Auth와 RLS의 역할을 설명합니다.
- 사용자별 데이터 접근 정책을 문서로 설계합니다.

실행:

```powershell
python .\06_supabase-db-and-auth\04_ch4_supabase-auth-and-rls\01_auth_rls_concept_check.py
```

확인 질문:

- 본인 데이터 접근 결과가 `True`인가?
- 다른 사용자 데이터 접근 결과가 `False`인가?
- 이 흐름이 RLS의 `auth.uid() = user_id` 조건과 어떻게 연결되는가?

### Lab 06 - Upstash Redis 환경변수 확인

목표:

- Upstash Redis REST URL과 token을 `.env`에 설정합니다.
- Python 코드에서 Upstash Redis 설정 여부를 확인합니다.
- Redis token을 프론트엔드나 GitHub에 노출하면 안 되는 이유를 설명합니다.

실행:

```powershell
cd C:\aidev\01_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
python .\06_supabase-db-and-auth\06_ch6_upstash-redis-cache-and-session\01_check_upstash_env.py
```

### Lab 07 - Upstash Redis TTL 캐시

목표:

- Redis에 key/value를 저장합니다.
- TTL을 설정해 일정 시간이 지나면 값이 사라지는 흐름을 확인합니다.
- Supabase에 저장할 데이터와 Redis에 잠시 둘 데이터를 구분합니다.

실행:

```powershell
python .\06_supabase-db-and-auth\06_ch6_upstash-redis-cache-and-session\02_cache_set_get_ttl.py
```

### Lab 08 - 요청 횟수 제한 흐름

목표:

- 사용자별 요청 횟수를 Redis에 저장합니다.
- 제한 횟수를 넘으면 요청을 거절하는 흐름을 이해합니다.
- AI API 비용 관리와 rate limit의 관계를 설명합니다.

실행:

```powershell
python .\06_supabase-db-and-auth\06_ch6_upstash-redis-cache-and-session\03_rate_limit_example.py
```

### Lab 09 - Redis 임시 세션 상태

목표:

- Redis에 JSON 문자열로 세션 상태를 저장합니다.
- TTL로 세션 상태가 자동 만료되는 흐름을 확인합니다.
- Supabase에 저장할 영구 데이터와 Redis에 저장할 임시 상태를 구분합니다.

실행:

```powershell
python .\06_supabase-db-and-auth\06_ch6_upstash-redis-cache-and-session\04_session_state_example.py
```

### Lab 10 - Cache-aside 패턴

목표:

- Redis cache hit/cache miss를 구분합니다.
- 캐시가 없을 때 Supabase 조회가 일어난다고 가정하는 흐름을 이해합니다.
- TTL 기반 캐시가 데이터베이스 부하를 줄이는 방식을 설명합니다.

실행:

```powershell
python .\06_supabase-db-and-auth\06_ch6_upstash-redis-cache-and-session\05_cache_aside_mock.py
```

### Lab 11 - FastAPI Rate Limit Dependency

목표:

- FastAPI `Depends`를 사용해 endpoint 실행 전 요청 제한을 적용합니다.
- Redis `INCR`, `EXPIRE` 명령이 요청 제한에 어떻게 쓰이는지 이해합니다.
- 요청 제한 초과 시 HTTP 429를 반환하는 흐름을 확인합니다.

실행:

```powershell
cd C:\aidev\01_supabase-ai-backend\06_supabase-db-and-auth\06_ch6_upstash-redis-cache-and-session
..\..\.venv\Scripts\Activate.ps1
uvicorn 06_fastapi_rate_limit_dependency:app --reload --host 127.0.0.1 --port 8001
```

Swagger UI:

```text
http://127.0.0.1:8001/docs
```

## Legacy Docker labs

이전 Docker/PostgreSQL/Redis 직접 실행 labs는 아래 참고 폴더로 이동했습니다.

```text
../90_legacy-docker-postgresql-redis-reference/labs
```

Docker 기반 실습은 `C:\aidev\06_multi-agent-service-ops`에서 진행합니다.
