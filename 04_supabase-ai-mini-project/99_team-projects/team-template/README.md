# Team Project Template

이 폴더는 팀 프로젝트를 시작하기 위한 기본 템플릿입니다.

기준 주제는 **실시간 로그 대시보드 인터페이스**입니다. 팀은 이 폴더를 복사한 뒤 프로젝트 목적에 맞게 Supabase 테이블, FastAPI API, Streamlit 화면, 대시보드 지표, 문서를 수정해서 사용합니다.

## 프로젝트 진행 방향

```text
1. 백엔드, DB, UI 통합 아키텍처 구현 및 실행 실습
2. 실시간 데이터 스트리밍을 통한 로그 시각화 대시보드 최종 제작
3. 사용자 피드백 데이터를 반영한 AI 답변 품질 고도화 및 서비스 최적화
```

## 폴더 구조

```text
team-template
├─ README.md
├─ .env.example
├─ backend
│ ├─ main.py
│ ├─ streaming_example.py
│ └─ requirements.txt
├─ frontend
│ ├─ app.py
│ ├─ streaming_app.py
│ └─ requirements.txt
├─ docs
│ ├─ project-plan.md
│ ├─ api-spec.md
│ ├─ ui-design.md
│ ├─ supabase-schema.md
│ ├─ dashboard-result.md
│ ├─ streaming-response-design.md
│ ├─ deployment-guide.md
│ ├─ test-checklist.md
│ └─ final-submission-checklist.md
├─ sql
│ ├─ supabase-base-schema.sql
│ └─ seed-sample-data.sql
└─ presentation
  └─ final-presentation.md
```

## 실행 환경

팀 프로젝트 안에 별도 `.venv`를 만들지 않습니다.

```text
가상환경:
C:\aidev\04_supabase-ai-mini-project\.venv

환경변수:
C:\aidev\04_supabase-ai-mini-project\.env
```

`.env.example`은 제출용 예시 파일입니다. 실제 API key는 `.env.example`에 넣지 않습니다.

## 팀에서 먼저 할 일

1. 이 폴더를 팀 이름으로 복사합니다.
2. `README.md`의 프로젝트명과 설명을 팀 주제에 맞게 수정합니다.
3. 필요하면 선택 보조 문서인 `docs/project-plan.md`를 작성합니다.
4. `sql/supabase-base-schema.sql`을 팀 주제에 맞게 수정합니다.
5. Supabase SQL Editor에서 SQL을 실행합니다.
6. `backend/main.py`의 테이블명과 API 경로를 수정합니다.
7. `frontend/app.py`의 화면 제목, 입력 항목, 대시보드 지표를 수정합니다.
8. `docs/api-spec.md`, `docs/ui-design.md`, `docs/supabase-schema.md`를 코드와 맞춥니다.

## FastAPI 실행

```powershell
cd C:\aidev\04_supabase-ai-mini-project\99_team-projects\team-template\backend
..\..\..\.venv\Scripts\Activate.ps1
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

브라우저에서 확인합니다.

```text
http://127.0.0.1:8000/docs
```

## Streamlit 실행

```powershell
cd C:\aidev\04_supabase-ai-mini-project\99_team-projects\team-template\frontend
..\..\..\.venv\Scripts\Activate.ps1
streamlit run app.py --server.port 8501
```

브라우저에서 확인합니다.

```text
http://localhost:8501
```

## 필수 산출물

| 산출물 | 파일 |
| --- | --- |
| API 설계 문서 | `docs/api-spec.md` |
| 화면 설계서 | `docs/ui-design.md` |
| 데이터베이스 스키마 설계서 | `docs/supabase-schema.md` |
| 대시보드 구현 결과물 | `docs/dashboard-result.md` |

04 과정의 필수 산출물은 위 4가지입니다. 아래 문서들은 프로젝트 진행과 발표를 돕는 선택 보조 산출물입니다.

## 선택 확장

프로젝트 계획, 테스트, 제출 점검, 발표를 정리하는 경우:

```text
docs/project-plan.md
docs/test-checklist.md
docs/final-submission-checklist.md
presentation/final-presentation.md
```

SSE를 적용하는 경우:

```text
backend/streaming_example.py
frontend/streaming_app.py
docs/streaming-response-design.md
```

무료 배포를 진행하는 경우:

```text
docs/deployment-guide.md
```

배포는 필수가 아닙니다. 기본 제출 기준은 로컬에서 FastAPI, Streamlit, Supabase가 정상 연결되는 것입니다.

## 보안 기준

- `.env`는 제출하지 않습니다.
- `.env.example`에는 실제 key를 넣지 않습니다.
- `SUPABASE_SERVICE_ROLE_KEY`는 FastAPI 백엔드에서만 사용합니다.
- Streamlit에는 service role key를 넣지 않습니다.
- Gemini API key와 OpenAI API key를 코드에 직접 적지 않습니다.
