# 05_ch5_docker-redis-setup

Docker image로 Redis 컨테이너를 실행하고 기본 명령을 실습합니다.

## 핵심 명령

```powershell
docker pull redis
docker run --name aidev-redis `
 -p 6379:6379 `
 -d redis
docker exec -it aidev-redis redis-cli
```

## Redis 기본 명령

```text
SET name Alice
GET name
SETEX session:abc 3600 user-1
TTL session:abc
DEL name
```

