# 01_supabase-env-check

Supabase 미니 프로젝트를 시작하기 전에 `.env` 설정이 준비되어 있는지 확인하는 첫 실습입니다.

이 과정에서는 Docker로 PostgreSQL이나 Redis를 실행하지 않습니다. 데이터 저장은 Supabase 프로젝트를 사용하고, 로컬 PC에서는 FastAPI와 Streamlit만 Python 가상환경으로 실행합니다. Docker, Docker Compose, AWS 배포는 `06_multi-agent-service-ops`에서 학습합니다.

## 학습 목표

- `.env` 파일의 역할을 이해한다.
- Supabase URL과 key를 코드에 직접 쓰지 않는 이유를 설명할 수 있다.
- FastAPI가 사용할 Supabase 설정과 Streamlit이 호출할 API 주소를 구분할 수 있다.

## 준비

`03_supabase-ai-mini-project` 최상위 폴더에서 `.env.example`을 `.env`로 복사합니다.

```powershell
cd C:\aidev\03_supabase-ai-mini-project
Copy-Item .env.example .env
```

이 실습에서는 아래 위치의 `.env` 파일을 사용합니다.

```text
C:\aidev\03_supabase-ai-mini-project\.env
```

`C:\aidev\.env`, `01_supabase-ai-backend\.env`, `02_supabase-ai-frontend\.env`를 사용하는 구조가 아닙니다.

`.env` 파일에 본인의 Supabase 프로젝트 값을 입력합니다.

```env
SUPABASE_URL=https://your-project-ref.supabase.co
SUPABASE_ANON_KEY=your-supabase-anon-key
SUPABASE_SERVICE_ROLE_KEY=your-supabase-service-role-key
GEMINI_API_KEY=your-gemini-api-key
GEMINI_MODEL=gemini-2.5-flash-lite
OPENAI_API_KEY=your-openai-api-key
OPENAI_MODEL=gpt-4.1-mini
API_BASE_URL=http://127.0.0.1:8000
```

03 과정의 기본 AI API는 Gemini입니다. OpenAI key는 선택/비교 실습을 진행할 때만 필요합니다.

## 실행

이 과정에서는 `03_supabase-ai-mini-project` 최상위 `.venv` 하나를 사용합니다.

```powershell
cd C:\aidev\03_supabase-ai-mini-project
.\.venv\Scripts\Activate.ps1
python .\01_local-dev-basic\01_supabase-env-check\01_check_env.py
```

## 확인 기준

- `SUPABASE_URL`이 비어 있지 않다.
- `SUPABASE_ANON_KEY`가 비어 있지 않다.
- `SUPABASE_SERVICE_ROLE_KEY`는 백엔드에서만 사용한다는 점을 설명할 수 있다.
- `API_BASE_URL`은 Streamlit이 FastAPI를 호출할 주소라는 점을 설명할 수 있다.
- `GEMINI_API_KEY`는 기본 LLM 실습용이고, `OPENAI_API_KEY`는 선택 비교용이라는 점을 설명할 수 있다.
