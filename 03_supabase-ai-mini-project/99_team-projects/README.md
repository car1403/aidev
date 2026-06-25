# 99_team-projects

이 폴더는 03 미니 프로젝트의 최종 팀 프로젝트 작업 공간입니다.

`01_local-dev-basic`에서 로컬 실행 감각을 익히고, `02_instructor-sample-project`에서 완성된 샘플을 확인한 뒤, `03_supabase-and-sse-practice`와 `04_team-project-guide`를 거쳐 이 폴더에서 실제 프로젝트를 진행합니다.

## 전체 흐름

```text
01_local-dev-basic
-> 로컬 실행 감각 익히기

02_instructor-sample-project
-> 완성된 샘플 보기

03_supabase-and-sse-practice
-> 팀 프로젝트에 필요한 핵심 기능을 단계별로 실습

04_team-project-guide
-> 팀 프로젝트 기획, 역할, 산출물 기준 정리

05_project-templates
-> 문서, SQL, 환경변수, 체크리스트 템플릿 확인

99_team-projects
-> 실제 팀 프로젝트 작업
```

## 폴더 구성

```text
99_team-projects
├─ README.md
└─ team-template
```

`team-template`은 팀별 프로젝트를 시작할 때 복사해서 사용하는 기본 구조입니다.

## 팀 프로젝트 폴더 만들기

PowerShell에서 아래처럼 복사합니다.

```powershell
cd C:\aidev\03_supabase-ai-mini-project
Copy-Item .\99_team-projects\team-template .\99_team-projects\team-01-service-log-dashboard -Recurse
```

팀 주제에 맞게 폴더명을 바꿉니다.

예시:

```text
team-01-service-log-dashboard
team-02-ai-feedback-dashboard
team-03-customer-support-log
```

## 팀 프로젝트 기본 구조

```text
team-project
├─ README.md
├─ .env.example
├─ backend
│  ├─ main.py
│  ├─ streaming_example.py
│  └─ requirements.txt
├─ frontend
│  ├─ app.py
│  ├─ streaming_app.py
│  └─ requirements.txt
├─ docs
│  ├─ project-plan.md
│  ├─ api-spec.md
│  ├─ ui-design.md
│  ├─ supabase-schema.md
│  ├─ dashboard-result.md
│  ├─ streaming-response-design.md
│  ├─ deployment-guide.md
│  ├─ test-checklist.md
│  └─ final-submission-checklist.md
├─ sql
│  ├─ supabase-base-schema.sql
│  └─ seed-sample-data.sql
└─ presentation
   └─ final-presentation.md
```

## 실행 기준

팀 프로젝트 폴더 안에 별도의 `.venv`를 만들지 않습니다.

```text
가상환경:
C:\aidev\03_supabase-ai-mini-project\.venv

환경변수:
C:\aidev\03_supabase-ai-mini-project\.env
```

팀 프로젝트 내부의 `.env.example`은 필요한 환경변수 목록을 보여주는 제출용 예시 파일입니다. 실제 key가 들어 있는 `.env`는 GitHub에 올리지 않습니다.

## 기본 테이블 기준

최종 팀 프로젝트 템플릿은 아래 테이블을 기준으로 구성되어 있습니다.

```text
service_logs
messages
feedbacks
```

`learning_logs`는 01, 02 단계에서 Supabase 연결을 처음 익히기 위한 입문용 샘플 테이블입니다. 최종 팀 프로젝트에서는 `service_logs`를 중심으로 로그 수집, 조회, 수정, 대시보드 시각화를 진행합니다.

## 기본 제출 기준

필수 기준:

- FastAPI 백엔드가 로컬에서 실행됩니다.
- Streamlit 프론트엔드가 로컬에서 실행됩니다.
- Supabase 테이블에 데이터가 저장되고 조회됩니다.
- Streamlit 화면에서 FastAPI API를 호출합니다.
- API 설계 문서, 화면 설계서, 데이터베이스 설계서, 대시보드 구현 결과 문서가 작성됩니다.

선택 확장:

- SSE 기반 실시간 응답 표시
- Gemini 기반 AI 응답 저장
- 사용자 피드백 기반 품질 개선 지표
- Render, Upstash, Streamlit Community Cloud를 활용한 무료 배포 시연

## 백엔드 실행

첫 번째 PowerShell에서 실행합니다.

```powershell
cd C:\aidev\03_supabase-ai-mini-project\99_team-projects\team-template\backend
..\..\..\.venv\Scripts\Activate.ps1
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

브라우저에서 확인합니다.

```text
http://127.0.0.1:8000/health
http://127.0.0.1:8000/docs
```

## 프론트엔드 실행

두 번째 PowerShell에서 실행합니다.

```powershell
cd C:\aidev\03_supabase-ai-mini-project\99_team-projects\team-template\frontend
..\..\..\.venv\Scripts\Activate.ps1
streamlit run app.py --server.port 8501
```

브라우저에서 확인합니다.

```text
http://127.0.0.1:8501
```

## 진행 순서

1. `team-template`을 팀 폴더로 복사합니다.
2. `docs/project-plan.md`에 프로젝트 주제와 사용자를 정리합니다.
3. `sql/supabase-base-schema.sql`을 Supabase SQL Editor에서 실행합니다.
4. `.env`에 Supabase URL/key, Gemini API key, API URL을 정리합니다.
5. FastAPI 백엔드를 실행하고 `/docs`에서 API를 확인합니다.
6. Streamlit 프론트엔드를 실행하고 로그 생성/조회 기능을 확인합니다.
7. `docs/api-spec.md`, `docs/ui-design.md`, `docs/supabase-schema.md`를 구현 결과와 맞춥니다.
8. `docs/dashboard-result.md`에 최종 대시보드 화면과 동작 결과를 기록합니다.
9. 시간이 충분하면 SSE 또는 무료 배포를 선택 확장으로 진행합니다.

## 선택 배포

03 과정에서 배포는 필수가 아닙니다.

배포를 선택하는 경우 다음 구조를 사용합니다.

```text
FastAPI backend -> Render
Streamlit frontend -> Streamlit Community Cloud
Redis 선택 사용 -> Upstash
Database/Auth -> Supabase Cloud
```

자세한 내용은 아래 문서를 참고합니다.

```text
00_references/08_free-deployment-guide.md
team-template/docs/deployment-guide.md
```

## 기억할 점

이 폴더의 목표는 “큰 서비스를 한 번에 완성하는 것”이 아니라, 다음 연결 흐름을 끝까지 확인하는 것입니다.

```text
Streamlit 화면
-> FastAPI API
-> Supabase 테이블
-> 로그/AI 응답/피드백 데이터
-> 대시보드 시각화
```

작은 기능을 하나씩 완성하고, 각 단계마다 문서와 코드가 서로 맞는지 확인하는 방식으로 진행합니다.
