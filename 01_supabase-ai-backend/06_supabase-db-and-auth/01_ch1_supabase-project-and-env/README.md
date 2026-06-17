# 01_ch1_supabase-project-and-env

이 단원은 Supabase 프로젝트를 만들고 Python/FastAPI에서 사용할 환경변수를 준비하는 단계입니다.

이 과정에서는 Docker로 PostgreSQL이나 Redis를 직접 실행하지 않습니다. PostgreSQL은 Supabase를 사용하고, Redis는 Upstash Redis를 사용합니다. Docker 기반 서비스 운영은 `C:\aidev\06_multi-agent-service-ops`에서 본격적으로 다룹니다.

## 학습 목표

- Supabase 프로젝트를 생성합니다.
- Project URL, anon key, service role key의 차이를 이해합니다.
- `.env` 파일에 Supabase 접속 정보를 설정합니다.
- 이후 챕터에서 사용할 Upstash Redis 환경변수 위치를 확인합니다.
- Python 코드에서 환경변수를 읽어 Supabase 연결 준비 상태를 확인합니다.

## 준비 순서

1. Supabase에 로그인합니다.
2. 새 프로젝트를 생성합니다.
3. Project Settings에서 API 정보를 확인합니다.
4. `C:\aidev\01_supabase-ai-backend\.env.example`을 `.env`로 복사합니다.
5. `.env`에 `SUPABASE_URL`, `SUPABASE_ANON_KEY`, `SUPABASE_SERVICE_ROLE_KEY`를 입력합니다.
6. Upstash Redis는 `06_ch6_upstash-redis-cache-and-session`에서 설정하고 확인합니다.

## 환경변수 예시

```env
SUPABASE_URL=https://your-project-ref.supabase.co
SUPABASE_ANON_KEY=your-supabase-anon-key
SUPABASE_SERVICE_ROLE_KEY=your-supabase-service-role-key
UPSTASH_REDIS_REST_URL=https://your-upstash-redis-url.upstash.io
UPSTASH_REDIS_REST_TOKEN=your-upstash-redis-rest-token
```

## 실행 예시

```powershell
cd C:\aidev\01_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
python .\06_supabase-db-and-auth\01_ch1_supabase-project-and-env\01_check_supabase_env.py
```

정상이라면 Supabase URL과 key 설정 여부가 출력됩니다.
