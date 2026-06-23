# Lab 08 - 대화 이력 구조

Redis와 대화 이력 저장 방식을 비교하는 legacy lab입니다.

## 목표

- 대화 이력의 저장 단위를 생각합니다.
- 장기 보관 데이터와 임시 상태를 구분합니다.
- Redis에 모든 대화를 영구 저장하는 방식의 한계를 이해합니다.

## 현재 과정에서의 대응

현재 과정에서는 대화 이력은 Supabase에 저장하고, 짧은 임시 상태만 Upstash Redis에 저장합니다.

```text
05_conversation-history-and-service-logs
06_upstash-redis-cache-and-session
```
