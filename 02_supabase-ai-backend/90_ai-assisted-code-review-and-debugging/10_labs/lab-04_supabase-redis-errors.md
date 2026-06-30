# Lab 04. Supabase and Redis Errors

## 목표

Supabase와 Upstash Redis 실습에서 자주 나오는 오류를 확인합니다.

## Supabase 확인

- `SUPABASE_URL`이 Project URL인가?
- `SUPABASE_ANON_KEY`와 `SUPABASE_SERVICE_ROLE_KEY`를 구분했는가?
- 테이블명과 컬럼명이 SQL과 같은가?
- RLS를 켠 테이블에 접근할 때 JWT가 필요한가?

## Redis 확인

- Upstash REST URL과 token을 `.env`에서 읽는가?
- TTL을 넣어야 하는 값에 만료 시간이 있는가?
- 캐시에 저장할 데이터와 Supabase에 영구 저장할 데이터가 구분되어 있는가?

## Codex 질문 예시

```text
Supabase 또는 Redis 호출이 실패했습니다.
아래 오류에서 key 값은 모두 ***로 가렸습니다.
테이블명, 컬럼명, 환경 변수, 권한 문제 중 무엇을 먼저 확인해야 하는지 알려주세요.
```
