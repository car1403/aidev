# Lab 99 - 사용자 세션 캐시 API

PostgreSQL과 Redis를 함께 사용하는 legacy 미니 실습입니다.

## 목표

- 사용자 데이터는 PostgreSQL에 저장합니다.
- 임시 세션과 캐시는 Redis에 저장합니다.
- FastAPI API로 저장소 역할 분리를 확인합니다.

## 현재 과정에서의 대응

현재 과정에서는 PostgreSQL은 Supabase로, Redis는 Upstash Redis로 대체합니다.

통합 흐름은 아래 현재 과정 자료와 연결됩니다.

```text
10_labs
20_assignments
99_final-backend-project
```
