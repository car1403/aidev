# 00_references

Supabase 중심 DB/인증/로그 실습을 위한 참고 자료입니다.

이 과정에서 영구 저장은 Supabase를 사용하고, 캐시/TTL/요청 제한 같은 임시 데이터는 Upstash Redis를 사용합니다.

## 먼저 볼 문서

```text
supabase-first-notes.md
supabase-schema.sql
auth-basic-guide.md
env-and-secret-management.md
fastapi-db-patterns.md
session-patterns.md
```

Upstash Redis 실습은 아래 챕터에서 진행합니다.

```text
../06_ch6_upstash-redis-cache-and-session
```

## Docker 자료 위치

Docker/PostgreSQL/Redis 이전 자료는 아래 폴더로 분리했습니다.

```text
../90_legacy-docker-postgresql-redis-reference/references
```

`01_supabase-ai-backend`에서는 Supabase와 Upstash Redis 중심으로 진행하고, Docker 기반 운영은 `C:\aidev\06_multi-agent-service-ops`에서 진행합니다.
