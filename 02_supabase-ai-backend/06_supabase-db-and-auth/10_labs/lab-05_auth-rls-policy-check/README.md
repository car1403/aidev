# Lab 05 - Auth/RLS 보호 흐름 확인

이 실습은 Supabase Auth와 RLS를 바로 연결하기 전에, “로그인한 사용자만 접근할 수 있는 API”의 기본 흐름을 FastAPI로 연습합니다.

## 학습 목표

- 인증이 필요한 API와 공개 API를 구분할 수 있습니다.
- `Authorization: Bearer ...` 헤더의 역할을 이해합니다.
- Supabase RLS의 `auth.uid() = user_id` 조건이 왜 필요한지 설명할 수 있습니다.

## 실행 방법

```powershell
cd C:\aidev\02_supabase-ai-backend\06_supabase-db-and-auth\10_labs\lab-05_auth-rls-policy-check
..\..\..\.venv\Scripts\Activate.ps1
python -m uvicorn solution:app --reload --host 127.0.0.1 --port 8002
```

Swagger UI:

```text
http://127.0.0.1:8002/docs
```

## 테스트 방법

`GET /me`를 호출할 때 아래 헤더를 넣습니다.

```text
Authorization: Bearer demo-token
```

## 확인 기준

- 토큰이 없으면 HTTP 401이 반환됩니다.
- 잘못된 토큰이면 HTTP 401이 반환됩니다.
- `Bearer demo-token`이면 사용자 정보가 반환됩니다.

## Supabase RLS와 연결해서 생각하기

이 예제의 `demo-token` 검사는 실제 서비스에서는 Supabase Auth JWT 검증으로 바뀝니다. 인증된 사용자의 `user_id`를 알 수 있어야 Supabase RLS 정책에서 “자기 데이터만 조회” 같은 규칙을 적용할 수 있습니다.
