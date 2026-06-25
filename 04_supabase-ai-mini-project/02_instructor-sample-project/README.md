# 02_instructor-sample-project

Supabase 기반 학습 로그 대시보드 샘플 프로젝트입니다.

이 샘플은 `01_local-dev-basic`에서 확인한 로컬 실행 흐름을 한 단계 더 정리한 예시입니다. 이후 `03_supabase-and-sse-practice`에서 핵심 기능을 단계별로 연습하고, `04_team-project-guide`와 `99_team-projects`에서 팀별 프로젝트를 만들 때 참고할 수 있는 기준 프로젝트 역할을 합니다.

```text
Streamlit 화면
-> FastAPI API 호출
-> Supabase learning_logs 테이블 저장/조회
-> 화면에서 로그 등록, 조회, 상태 변경 확인
```

## 01/02 과정과의 연결

```text
02_supabase-ai-backend
-> FastAPI, Supabase, Pydantic, 환경 변수, key 보안 기준

03_supabase-ai-frontend
-> Streamlit 화면, API_BASE_URL, httpx API 호출, 서비스 로그 조회 UI

04_supabase-ai-mini-project
-> 위 내용을 하나의 미니 프로젝트 샘플로 연결
```

## 실행 환경 기준

이 샘플 프로젝트 안에 별도 `.venv`를 만들지 않습니다.

```text
가상환경:
C:\aidev\04_supabase-ai-mini-project\.venv

환경변수:
C:\aidev\04_supabase-ai-mini-project\.env
```

즉, `02_instructor-sample-project\.env`를 따로 만들지 않습니다. 03 과정 전체의 최상위 `.env`를 기준으로 실행합니다.

## 구조

```text
02_instructor-sample-project
├─ README.md
├─ backend
│ ├─ main.py
│ └─ requirements.txt
├─ frontend
│ ├─ app.py
│ └─ requirements.txt
└─ docs
  ├─ api-test-guide.md
  ├─ comparison-with-docker-compose.md
  └─ setup-supabase.md
```

## 실행 준비

1. Supabase 프로젝트를 준비합니다.
2. Supabase SQL Editor에서 `learning_logs` 테이블을 만듭니다.
3. `C:\aidev\04_supabase-ai-mini-project\.env`에 Supabase 값과 `API_BASE_URL`을 입력합니다.
4. 첫 번째 PowerShell에서 FastAPI 백엔드를 실행합니다.
5. 두 번째 PowerShell에서 Streamlit 프론트엔드를 실행합니다.

테이블 SQL은 다음 문서를 참고합니다.

```text
docs/setup-supabase.md
```

## FastAPI 실행

첫 번째 PowerShell에서 실행합니다.

```powershell
cd C:\aidev\04_supabase-ai-mini-project\02_instructor-sample-project\backend
..\..\.venv\Scripts\Activate.ps1
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

브라우저에서 확인합니다.

```text
http://127.0.0.1:8000/docs
```

## Streamlit 실행

두 번째 PowerShell에서 실행합니다.

```powershell
cd C:\aidev\04_supabase-ai-mini-project\02_instructor-sample-project\frontend
..\..\.venv\Scripts\Activate.ps1
streamlit run app.py --server.port 8501
```

브라우저에서 확인합니다.

```text
http://localhost:8501
```

## 주의사항

- 이 샘플은 Docker Compose를 사용하지 않습니다.
- DB는 Supabase 클라우드 PostgreSQL을 사용합니다.
- `SUPABASE_SERVICE_ROLE_KEY`는 백엔드에서만 사용합니다.
- Streamlit 프론트엔드에는 Supabase key, Gemini key, OpenAI key, Upstash token 같은 민감 정보를 직접 넣지 않습니다.
- Gemini 기반 AI 응답 생성, SSE 스트리밍, 피드백 반영은 이후 `03_supabase-and-sse-practice`와 팀 프로젝트 단계에서 확장합니다.
- 배포는 필수가 아닙니다. 기본 기준은 로컬에서 FastAPI, Streamlit, Supabase가 정상 연결되는 것입니다.
