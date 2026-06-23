# Lab 09 - 사용자 프로필 캐시

Redis cache-aside 패턴을 연습하는 legacy lab입니다.

## 목표

- cache hit와 cache miss를 구분합니다.
- 캐시가 없을 때 원본 저장소를 조회하는 흐름을 이해합니다.
- TTL로 캐시 만료를 설정합니다.

## 현재 과정에서의 대응

현재 과정에서는 Upstash Redis 예제로 cache-aside 패턴을 다룹니다.

```text
06_upstash-redis-cache-and-session\05_cache_aside_mock.py
```
