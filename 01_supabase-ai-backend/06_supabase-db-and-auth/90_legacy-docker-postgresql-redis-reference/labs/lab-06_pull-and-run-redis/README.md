# Lab 06 - Redis 컨테이너 실행

Docker로 Redis 컨테이너를 실행하는 legacy lab입니다.

## 목표

- `redis` Docker image를 다운로드합니다.
- Redis 컨테이너를 실행합니다.
- `redis-cli`로 Redis에 접속합니다.

## 참고 명령

```powershell
docker pull redis
docker run --name aidev-redis -p 6379:6379 -d redis
docker exec -it aidev-redis redis-cli
```

## 현재 과정에서의 대응

현재 과정에서는 로컬 Redis 대신 Upstash Redis를 사용합니다.

```text
C:\aidev\01_supabase-ai-backend\06_supabase-db-and-auth\06_upstash-redis-cache-and-session
```
