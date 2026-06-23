# Assignment 04 - Redis 대화 세션

Redis를 사용해 대화 세션을 저장하는 legacy 과제 예시입니다.

## 요구사항

1. 사용자별 세션 key를 설계합니다.
2. TTL이 있는 세션 값을 저장합니다.
3. 대화 상태를 JSON 구조로 표현합니다.
4. Redis에 저장할 데이터와 DB에 저장할 데이터를 구분합니다.

## 현재 과정에서의 대응

현재 과정에서는 Upstash Redis와 Supabase를 나누어 사용합니다.

```text
05_conversation-history-and-service-logs
06_upstash-redis-cache-and-session
```
