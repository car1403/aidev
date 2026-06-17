# Supabase First Notes

`01_supabase-ai-backend`는 Supabase 중심으로 진행합니다.

## 이 과정에서 사용하는 DB 기준

```text
주 DB: Supabase managed PostgreSQL
인증: Supabase Auth
접근 제어: Supabase RLS
로그/대화 이력: Supabase table
임시 캐시/TTL/요청 제한: Upstash Redis
```

## Supabase와 Upstash Redis의 역할

```text
Supabase
-> 오래 보관할 데이터
-> 사용자 정보, 대화 이력, 서비스 로그, 피드백

Upstash Redis
-> 짧게 보관할 임시 데이터
-> 캐시, TTL, 중복 요청 방지, 요청 횟수 제한, 임시 세션 상태
```

## 이 과정에서 하지 않는 것

아래 내용은 `06_multi-agent-service-ops`에서 본격적으로 다룹니다.

```text
Docker로 PostgreSQL 직접 실행
Docker로 Redis 직접 실행
Docker Compose 기반 여러 서비스 운영
AWS 배포
운영 모니터링
Auto Healing
```

## 강의 설명 문장

초보자에게는 이렇게 안내하면 좋습니다.

```text
이번 01 과정에서는 DB를 직접 설치하지 않고 Supabase를 사용합니다.
Redis는 Docker로 띄우지 않고 Upstash Redis를 사용해 캐시와 TTL 개념을 먼저 배웁니다.
Docker로 DB와 Redis를 직접 운영하는 방식은 나중에 06 운영 과정에서 배웁니다.
지금은 FastAPI가 Supabase와 Upstash Redis에 연결되는 흐름에 집중합니다.
```
