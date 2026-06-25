# 05_docker-redis-setup

Docker로 Redis 컨테이너를 실행하는 legacy 참고 챕터입니다.

현재 과정에서는 로컬 Redis 대신 Upstash Redis를 사용합니다.

## 핵심 개념

- Redis는 key/value 기반의 빠른 임시 저장소입니다.
- TTL을 사용해 일정 시간이 지나면 값을 자동으로 지울 수 있습니다.
- 세션, 캐시, 요청 제한 같은 임시 데이터에 적합합니다.

## 참고 명령

```powershell
docker pull redis
docker run --name aidev-redis -p 6379:6379 -d redis
docker exec -it aidev-redis redis-cli
```

## 현재 과정에서의 대응

| Legacy 방식 | 현재 과정 방식 |
|---|---|
| `docker run redis` | Upstash Redis 생성 |
| `redis-cli` 명령 | Upstash REST API 호출 |
| 로컬 Redis token 없음 | `UPSTASH_REDIS_REST_TOKEN` 관리 |
