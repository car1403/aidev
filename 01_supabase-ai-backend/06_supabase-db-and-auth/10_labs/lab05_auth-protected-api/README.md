# Lab 05 - 인증 보호 API

## 목표

토큰이 있는 사용자만 접근할 수 있는 API를 만듭니다.

## 요구사항

1. 회원가입 API
2. 로그인 API
3. `/me` 보호 API
4. 토큰이 없으면 401 반환

## starter 실행

```powershell
cd C:\aidev\01_supabase-ai-backend\06_supabase-db-and-auth\10_labs\lab05_auth-protected-api
..\..\..\.venv\Scripts\Activate.ps1
uvicorn starter:app --reload --host 127.0.0.1 --port 8002
```

Swagger UI:

```text
http://127.0.0.1:8002/docs
```

## 수업 진행 방법

처음에는 실제 Supabase Auth를 바로 연결하지 않습니다. 먼저 `Authorization` 헤더가 없을 때 401을 반환하는 구조를 이해합니다.

테스트용 헤더:

```text
Authorization: Bearer demo-token
```

이 구조를 이해한 뒤 다음 단계에서 Supabase Auth가 발급한 JWT를 검증하는 방식으로 확장합니다.

