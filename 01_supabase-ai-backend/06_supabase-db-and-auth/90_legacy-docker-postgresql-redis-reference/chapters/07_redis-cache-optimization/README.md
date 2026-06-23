# 07_redis-cache-optimization

Redis 캐시를 사용해 조회 속도와 API 비용을 줄이는 legacy 참고 챕터입니다.

현재 과정에서는 Upstash Redis로 TTL 캐시, cache-aside, rate limit을 학습합니다.

## 핵심 개념

- cache hit: 캐시에 값이 있어서 바로 반환하는 상황
- cache miss: 캐시에 값이 없어 원본 저장소를 조회하는 상황
- TTL: 캐시 데이터의 만료 시간
- rate limit: 사용자별 요청 횟수 제한

## 현재 과정에서의 대응

```text
06_upstash-redis-cache-and-session
10_labs
20_assignments
```
