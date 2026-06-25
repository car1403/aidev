# Redis Docker 실행

이 문서는 Docker로 Redis 컨테이너를 실행할 때 사용하는 기본 명령어를 정리한 legacy 참고 문서입니다.

현재 과정에서는 로컬 Redis 대신 Upstash Redis를 사용합니다.

## Image 받기

```powershell
docker pull redis
```

## Container 실행

```powershell
docker run --name aidev-redis `
  -p 6379:6379 `
  -d redis
```

## Redis 접속

```powershell
docker exec -it aidev-redis redis-cli
```

## 기본 명령

```text
SET name Alice
GET name
EXPIRE name 60
TTL name
DEL name
```

## 중지와 재시작

```powershell
docker stop aidev-redis
docker start aidev-redis
```

## 현재 과정에서의 대응

현재 과정에서는 아래 환경변수로 Upstash Redis REST API를 사용합니다.

```env
UPSTASH_REDIS_REST_URL=...
UPSTASH_REDIS_REST_TOKEN=...
```
