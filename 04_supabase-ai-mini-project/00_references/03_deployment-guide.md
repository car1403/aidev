# 03. Deployment Guide

이 문서는 04 미니 프로젝트를 무료 배포 서비스로 시연할 때 참고하는 가이드입니다.

배포는 수업 시간과 훈련생 수준에 따라 선택 적용합니다. 다만 프로젝트 구조는 배포 가능한 형태로 작성합니다.

## 권장 배포 구조

```text
FastAPI backend -> Render
Redis -> Upstash Redis
Streamlit frontend -> Streamlit Community Cloud
Supabase DB -> Supabase Cloud
```

## 배포 전 체크

- [ ] `.env` 파일이 GitHub에 올라가지 않는다.
- [ ] Supabase service role key는 backend 환경변수에만 둔다.
- [ ] Redis URL은 backend 환경변수에만 둔다.
- [ ] Streamlit에는 `API_BASE_URL`만 둔다.
- [ ] Supabase SQL Editor에서 `schema.sql`을 실행했다.
- [ ] 로컬에서 `/health`, `/logs`, `/stream/logs`가 동작한다.

## Render backend

Root Directory 예시:

```text
04_supabase-ai-mini-project/03_project_structure/backend
```

Build Command:

```text
pip install -r requirements.txt
```

Start Command:

```text
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

Environment Variables:

| Key | 설명 |
| --- | --- |
| `SUPABASE_URL` | Supabase project URL |
| `SUPABASE_SERVICE_ROLE_KEY` | backend 전용 service role key |
| `REDIS_URL` | Upstash Redis URL |
| `CORS_ALLOW_ORIGINS` | Streamlit 배포 주소 |

## Upstash Redis

1. Upstash에서 Redis database를 만듭니다.
2. Redis URL을 확인합니다.
3. Render backend 환경변수 `REDIS_URL`에 등록합니다.

Upstash token 또는 URL은 Streamlit에 넣지 않습니다.

## Streamlit Community Cloud

Main file path 예시:

```text
04_supabase-ai-mini-project/03_project_structure/frontend/app.py
```

Secrets 예시:

```toml
API_BASE_URL = "https://your-render-backend.onrender.com"
```

## 제출 시 기록할 것

- Streamlit 배포 URL
- Render `/health` URL
- Supabase 테이블 생성 여부
- Redis 연결 여부
- 대시보드 화면 캡처
- 실시간 로그가 표시되는 화면 캡처
