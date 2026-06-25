# 캐싱 패턴

## Cache Hit / Miss

- Cache Hit: Redis에 데이터가 있어서 DB 조회를 생략
- Cache Miss: Redis에 데이터가 없어 DB를 조회하고 Redis에 저장

## 키 예시

```text
cache:user-profile:{user_id}
cache:log-summary:{user_id}
```

## 원칙

- 자주 조회되는 데이터를 캐싱한다.
- TTL을 설정한다.
- 데이터 변경 시 캐시를 삭제하거나 갱신한다.

