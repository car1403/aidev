# Deployment Guide

이 문서는 팀 프로젝트를 무료 배포 서비스에 올릴 때 사용하는 배포 설명서입니다.

배포는 필수 운영 자동화가 아니라, 팀 프로젝트를 외부 URL로 시연하기 위한 선택 확장입니다.

## 1. 배포 목표

```text
FastAPI 백엔드 -> Render
Redis 캐시/세션/로그 보조 저장소 -> Upstash
Streamlit 프론트엔드 -> Streamlit Community Cloud
Supabase Database/Auth -> Supabase Cloud
```

## 2. 배포 대상 프로젝트 구조

```text
team-project
├─ backend
│  ├─ main.py
│  └─ requirements.txt
├─ frontend
│  ├─ app.py
│  └─ requirements.txt
├─ docs
│  ├─ deployment-guide.md
│  └─ dashboard-result.md
└─ .env.example
```

`backend`와 `frontend`가 분리되어 있어야 Render와 Streamlit Community Cloud에서 각각 배포하기 쉽습니다.

## 3. 로컬 실행 확인

배포하기 전에 로컬에서 먼저 실행합니다.

```powershell
cd C:\aidev\03_supabase-ai-mini-project\99_team-projects\team-template\backend
..\..\..\.venv\Scripts\Activate.ps1
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

확인 URL:

```text
http://127.0.0.1:8000/health
http://127.0.0.1:8000/docs
```

다른 PowerShell에서 프론트엔드를 실행합니다.

```powershell
cd C:\aidev\03_supabase-ai-mini-project\99_team-projects\team-template\frontend
..\..\..\.venv\Scripts\Activate.ps1
streamlit run app.py --server.port 8501
```

확인 URL:

```text
http://localhost:8501
```

## 4. GitHub 업로드 전 확인

- [ ] `.env` 파일을 올리지 않았습니다.
- [ ] `.env.example` 파일은 포함했습니다.
- [ ] `.venv` 폴더를 올리지 않았습니다.
- [ ] `__pycache__` 폴더를 올리지 않았습니다.
- [ ] `backend/requirements.txt`가 있습니다.
- [ ] `frontend/requirements.txt`가 있습니다.

## 5. Render 백엔드 배포

Render Web Service 설정:

| 항목 | 값 |
| --- | --- |
| Root Directory | `backend` |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `uvicorn main:app --host 0.0.0.0 --port $PORT` |

Render 환경변수:

```env
SUPABASE_URL=본인 Supabase URL
SUPABASE_ANON_KEY=본인 Supabase anon key
SUPABASE_SERVICE_ROLE_KEY=필요한 경우만 등록
UPSTASH_REDIS_REST_URL=선택
UPSTASH_REDIS_REST_TOKEN=선택
```

배포 후 확인:

```text
Render Backend URL:
/health 확인 결과:
/docs 확인 결과:
```

## 6. Upstash Redis 선택 사용

Upstash는 Redis를 로컬에 설치하지 않고 사용할 수 있게 해주는 서비스입니다.

사용 예:

- 사용자 세션 임시 저장
- 자주 조회되는 대시보드 요약값 캐싱
- API 호출 제한
- 짧은 실행 로그 임시 저장

Upstash에서 복사할 값:

```text
UPSTASH_REDIS_REST_URL
UPSTASH_REDIS_REST_TOKEN
```

이 값은 Render 백엔드 환경변수에 등록합니다. Streamlit 프론트엔드에는 넣지 않습니다.

## 7. Streamlit Community Cloud 프론트엔드 배포

Streamlit 설정:

| 항목 | 값 |
| --- | --- |
| Repository | 팀 프로젝트 GitHub 저장소 |
| Branch | 배포할 브랜치 |
| Main file path | `frontend/app.py` |

Streamlit Secrets:

```toml
API_BASE_URL = "https://your-render-service.onrender.com"
```

배포 후 확인:

```text
Streamlit Frontend URL:
메인 화면 접속 결과:
FastAPI 호출 결과:
로그 조회 결과:
대시보드 표시 결과:
```

## 8. 배포 결과 기록

| 항목 | 값 |
| --- | --- |
| Render Backend URL |  |
| Streamlit Frontend URL |  |
| Supabase Project URL |  |
| Upstash 사용 여부 |  |
| 배포 확인 날짜 |  |
| 담당자 |  |

## 9. 배포 오류와 해결 과정

| 오류 상황 | 원인 | 해결 방법 |
| --- | --- | --- |
| 예: Streamlit에서 API 호출 실패 | API_BASE_URL이 로컬 주소로 남아 있음 | Streamlit Secrets를 Render URL로 수정 |
|  |  |  |

## 10. 03에서 06으로 이어지는 부분

03에서는 무료 배포 서비스로 프로젝트를 시연하는 것까지만 다룹니다.

06에서는 Docker Compose, AWS, GitHub Actions, 모니터링, Auto Healing 같은 운영 자동화를 별도로 학습합니다.
