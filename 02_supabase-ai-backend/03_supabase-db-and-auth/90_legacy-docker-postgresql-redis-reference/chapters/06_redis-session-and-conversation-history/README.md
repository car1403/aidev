# 06_redis-session-and-conversation-history

Redis를 세션과 대화 흐름 관리에 사용하는 legacy 참고 챕터입니다.

현재 과정에서는 장기 보관 데이터는 Supabase에 저장하고, 짧게 유지할 임시 상태는 Upstash Redis에 저장합니다.

## 핵심 구분

| 데이터 | 적합한 저장 위치 |
|---|---|
| 사용자 대화 이력 | Supabase |
| AI 응답 로그 | Supabase |
| 로그인 중 임시 상태 | Redis |
| 최근 요청 횟수 | Redis |
| 짧은 시간 재사용할 캐시 | Redis |

## 현재 과정에서의 대응

```text
05_conversation-history-and-service-logs
06_upstash-redis-cache-and-session
```
