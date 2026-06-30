# 01_supabase-and-sse-practice

이 단원은 최종 프로젝트를 만들기 전에 **Supabase DB + Redis + SSE + Streamlit 대시보드** 흐름을 작게 실행해 보는 실습입니다.

## 실습 목표

```text
POST /logs
-> Supabase DB에 로그 저장
-> Redis로 새 로그 이벤트 publish
-> GET /stream/logs에서 SSE로 이벤트 전송
-> Streamlit 화면에서 실시간 로그 표시
```

## 폴더 구조

```text
01_supabase-and-sse-practice
├─ README.md
├─ schema.sql
├─ backend
│  ├─ README.md
│  ├─ requirements.txt
│  ├─ .env.example
│  └─ app
└─ frontend
   ├─ README.md
   ├─ requirements.txt
   └─ app.py
```

## 실행 순서

1. Supabase SQL Editor에서 `schema.sql`을 실행합니다.
2. `C:\aidev\04_supabase-ai-mini-project\.env`를 준비합니다.
3. backend를 실행합니다.
4. frontend를 실행합니다.
5. Streamlit에서 로그를 생성하고 실시간 로그 영역을 확인합니다.

## backend 실행

```powershell
cd C:\aidev\04_supabase-ai-mini-project\01_supabase-and-sse-practice\backend
C:\aidev\04_supabase-ai-mini-project\.venv\Scripts\Activate.ps1
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

## frontend 실행

```powershell
cd C:\aidev\04_supabase-ai-mini-project\01_supabase-and-sse-practice\frontend
C:\aidev\04_supabase-ai-mini-project\.venv\Scripts\Activate.ps1
streamlit run .\app.py
```

## Redis와 fallback

`REDIS_URL`이 있으면 backend는 Redis publish/subscribe를 사용합니다. `REDIS_URL`이 비어 있으면 수업 중 실습이 멈추지 않도록 메모리 큐로 SSE 흐름을 확인합니다.

```text
REDIS_URL 있음 -> Redis 기반 실시간 이벤트
REDIS_URL 없음 -> 메모리 큐 기반 실시간 이벤트
```

최종 프로젝트 설명에서는 Redis를 기본 구성 요소로 다룹니다.
