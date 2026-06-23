# Assignment 05 - Redis 캐시 최적화

Redis 캐시로 데이터 조회 흐름을 최적화하는 legacy 과제 예시입니다.

## 요구사항

1. 캐시 대상 데이터를 정합니다.
2. cache hit/cache miss 흐름을 설명합니다.
3. TTL 기준을 정합니다.
4. 캐시가 오래된 데이터를 반환할 수 있는 상황을 설명합니다.

## 현재 과정에서의 대응

현재 과정에서는 Upstash Redis의 TTL 캐시와 cache-aside 예제를 사용합니다.
