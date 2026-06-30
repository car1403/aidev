# 03_project_structure

이 폴더는 최종 프로젝트를 시작할 때 사용하는 학생용 starter 구조입니다.

`01_supabase-and-sse-practice`는 완성된 작은 실행 예제이고, `03_project_structure`는 학생들이 직접 구현해 나가는 빈 구조에 가까운 시작점입니다.

## 구조

```text
03_project_structure
├─ README.md
├─ schema.sql
├─ backend
│  ├─ README.md
│  ├─ requirements.txt
│  ├─ .env.example
│  └─ app
│     ├─ main.py
│     ├─ core
│     ├─ routers
│     ├─ schemas
│     └─ services
└─ frontend
   ├─ README.md
   ├─ requirements.txt
   └─ app.py
```

## 기본 제공 범위

| 항목 | 설명 |
| --- | --- |
| backend `/health` | FastAPI 실행과 환경변수 로드 여부를 확인합니다. |
| frontend health 확인 | Streamlit에서 backend 연결을 확인합니다. |
| schema.sql | Supabase에 만들 테이블 기준을 제공합니다. |
| README/TODO | 각 폴더에 무엇을 구현해야 하는지 안내합니다. |

## 학생이 구현할 기능

| 기능 | 구현 위치 |
| --- | --- |
| 로그 생성 POST `/logs` | `backend/app/routers`, `schemas`, `services` |
| 로그 조회 GET `/logs` | `backend/app/routers`, `services` |
| 로그 요약 GET `/logs/summary` | `backend/app/routers`, `services` |
| 실시간 로그 GET `/stream/logs` | `backend/app/routers`, `services` |
| 피드백 저장 POST `/feedback` | `backend/app/routers`, `schemas`, `services` |
| Streamlit 대시보드 | `frontend/app.py` |

## 사용 방법

팀별 프로젝트를 만들 때 이 폴더를 복사하거나, 이 구조를 참고해 새 폴더를 만듭니다.

```powershell
cd C:\aidev\04_supabase-ai-mini-project
Copy-Item .\03_project_structure .\team-log-dashboard -Recurse
```

복사한 뒤에는 `01_supabase-and-sse-practice` 예제와 `02_project-deliverables` 산출물 샘플을 참고해 직접 구현합니다.
