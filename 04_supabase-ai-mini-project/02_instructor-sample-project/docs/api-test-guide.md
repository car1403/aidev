# API Test Guide

`02_instructor-sample-project` 백엔드 API를 PowerShell에서 직접 확인하는 방법입니다.

먼저 FastAPI 백엔드가 실행 중이어야 합니다.

```powershell
cd C:\aidev\04_supabase-ai-mini-project
.\.venv\Scripts\Activate.ps1
cd C:\aidev\04_supabase-ai-mini-project\02_instructor-sample-project\backend
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

## 1. Health Check

```powershell
Invoke-RestMethod http://127.0.0.1:8000/health
```

확인할 내용:

```text
api 값이 ok인가?
supabase 값이 ok인가?
sample_count 값이 숫자로 나오는가?
```

## 2. Logs 조회

```powershell
Invoke-RestMethod http://127.0.0.1:8000/api/logs
```

Supabase `learning_logs` 테이블에 데이터가 있으면 `items` 목록이 표시됩니다.

## 3. Logs 등록

```powershell
Invoke-RestMethod `
  -Method Post `
  -Uri http://127.0.0.1:8000/api/logs `
  -ContentType "application/json" `
  -Body '{"learner_name":"Sample","topic":"Instructor Sample","minutes":30,"memo":"샘플 프로젝트 API 테스트"}'
```

## 4. 상태 변경

아래 예시는 `id`가 1인 로그의 상태를 `done`으로 바꿉니다.

```powershell
Invoke-RestMethod `
  -Method Patch `
  -Uri http://127.0.0.1:8000/api/logs/1 `
  -ContentType "application/json" `
  -Body '{"status":"done"}'
```

## 5. 자주 확인할 오류

```text
Supabase environment variables are missing.
-> C:\aidev\04_supabase-ai-mini-project\.env 위치와 Supabase 값을 확인합니다.

Learning log not found
-> 수정하려는 id가 실제 테이블에 있는지 확인합니다.

Connection refused
-> FastAPI 서버가 실행 중인지 확인합니다.
```
