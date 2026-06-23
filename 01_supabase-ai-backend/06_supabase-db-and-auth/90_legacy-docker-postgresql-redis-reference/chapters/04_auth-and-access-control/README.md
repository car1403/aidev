# 04_auth-and-access-control

직접 인증과 접근 제어를 구현하던 legacy 참고 챕터입니다.

현재 과정에서는 Supabase Auth와 RLS를 사용해 사용자별 데이터 접근을 제어합니다.

## 핵심 개념

- 인증: 사용자가 누구인지 확인
- 권한: 어떤 데이터에 접근할 수 있는지 결정
- 보호 API: 로그인한 사용자만 접근 가능한 endpoint
- 사용자별 데이터 제한: 본인 데이터만 조회하도록 제어

## 현재 과정에서의 대응

| Legacy 방식 | 현재 과정 방식 |
|---|---|
| 직접 토큰 검증 | Supabase Auth JWT |
| 직접 권한 조건 작성 | Supabase RLS 정책 |
| 사용자별 로그 조회 API | Auth/RLS 기반 접근 제어 |

## 참고 위치

```text
C:\aidev\01_supabase-ai-backend\06_supabase-db-and-auth\04_supabase-auth-and-rls
```
