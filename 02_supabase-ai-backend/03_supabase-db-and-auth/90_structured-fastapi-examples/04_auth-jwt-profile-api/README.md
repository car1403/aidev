# 04. Auth JWT Profile API

Supabase Auth, JWT, Bearer token, RLS SQL을 하나의 작은 profile 예제로 확인합니다.

본문 04에서는 RLS SQL을 필수로 다루지 않았습니다. 이 예제는 나중에 참고하는 심화 구조 예제입니다.

## 1. Supabase 설정

Supabase SQL Editor에서 `schema.sql`을 실행합니다.

```text
C:\aidev\02_supabase-ai-backend\03_supabase-db-and-auth\90_structured-fastapi-examples\04_auth-jwt-profile-api\schema.sql
```

이 SQL은 `ex90_profiles` 테이블을 만들고, 로그인한 사용자가 자기 profile만 읽고 수정할 수 있도록 RLS 정책을 설정합니다.

## 2. 환경변수 준비

```text
SUPABASE_URL=...
SUPABASE_ANON_KEY=...
SUPABASE_SERVICE_ROLE_KEY=...
```

## 3. 서버 실행

```powershell
cd C:\aidev\02_supabase-ai-backend\03_supabase-db-and-auth\90_structured-fastapi-examples\04_auth-jwt-profile-api
..\..\..\.venv\Scripts\Activate.ps1
uvicorn app.main:app --reload --host 127.0.0.1 --port 8014
```

Swagger UI:

```text
http://127.0.0.1:8014/docs
```

## 테스트 순서

1. `POST /auth/signup`으로 가입합니다.
2. Confirm email이 켜져 있으면 이메일 인증을 완료합니다.
3. `POST /auth/signin`으로 로그인합니다.
4. 응답의 `access_token`을 복사합니다.
5. Swagger `Authorize`에 token을 넣습니다.
6. `GET /me`로 현재 사용자를 확인합니다.
7. `PUT /profile`로 display name을 저장합니다.
8. `GET /profile`로 자기 profile만 조회되는지 확인합니다.

## RLS 핵심 문장

```sql
auth.uid() = id
```

이 조건은 “현재 로그인한 사용자의 id와 profile 행의 id가 같을 때만 허용한다”는 뜻입니다.
