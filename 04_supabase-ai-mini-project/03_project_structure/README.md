# 03_project_structure

이 폴더는 최종 팀 프로젝트를 시작할 때 참고하거나 복사해서 사용하는 학생용 starter 구조입니다.

`01_supabase-and-sse-practice`는 작게 실행해 보는 완성 예제이고, `03_project_structure`는 학생들이 직접 구현해 나가는 시작점입니다. 완성 코드보다 **어디에 무엇을 구현해야 하는지**가 보이도록 구성합니다.

## 구조

```text
03_project_structure
├─ README.md
├─ backend
│  ├─ README.md
│  ├─ requirements.txt
│  ├─ .env.example
│  ├─ app
│  │  ├─ main.py
│  │  ├─ core
│  │  ├─ routers
│  │  ├─ schemas
│  │  └─ services
│  └─ tests
├─ frontend
│  ├─ README.md
│  ├─ requirements.txt
│  └─ app.py
├─ database
│  ├─ README.md
│  └─ schema.sql
└─ docs
   ├─ api-design.md
   ├─ screen-design.md
   ├─ database-design.md
   ├─ dashboard-result-report.md
   └─ deployment-note.md
```

## 기본 제공 범위

| 항목 | 설명 |
| --- | --- |
| backend `/health` | FastAPI 서버 실행과 환경 변수 로드 여부를 확인합니다. |
| frontend health 확인 | Streamlit에서 backend 연결 상태를 확인합니다. |
| `database/schema.sql` | Supabase SQL Editor에서 실행할 기본 테이블 구조입니다. |
| `docs` | 최종 산출물 작성을 시작할 수 있는 문서 starter입니다. |
| README/TODO | 각 폴더에서 무엇을 구현해야 하는지 안내합니다. |

## 학생 구현 기능

| 기능 | 구현 위치 |
| --- | --- |
| 로그 생성 POST `/logs` | `backend/app/routers`, `schemas`, `services` |
| 로그 조회 GET `/logs` | `backend/app/routers`, `services` |
| 로그 요약 GET `/logs/summary` | `backend/app/routers`, `services` |
| 실시간 로그 GET `/stream/logs` | `backend/app/routers`, `services` |
| 피드백 저장 POST `/feedback` | `backend/app/routers`, `schemas`, `services` |
| Streamlit 대시보드 | `frontend/app.py` |
| API/화면/DB/결과 문서 | `docs` |

## 사용 방법

팀별 프로젝트를 만들 때 이 폴더를 복사해서 시작할 수 있습니다.

```powershell
cd C:\aidev\04_supabase-ai-mini-project
Copy-Item .\03_project_structure .\team-log-dashboard -Recurse
```

복사한 뒤에는 `01_supabase-and-sse-practice` 예제와 `02_project-deliverables` 산출물 샘플을 참고해 직접 구현합니다.

## 구현 순서 추천

1. `database/schema.sql`을 Supabase SQL Editor에서 실행합니다.
2. `docs/api-design.md`에 endpoint 설계를 먼저 작성합니다.
3. `backend/app/schemas`에 Request/Response 모델을 정의합니다.
4. `backend/app/routers`에 API endpoint를 구현합니다.
5. `backend/app/services`에 Supabase, Redis, SSE 처리 로직을 구현합니다.
6. `frontend/app.py`에서 로그 대시보드 화면을 구현합니다.
7. `docs/dashboard-result-report.md`에 실행 결과와 배포 여부를 정리합니다.
