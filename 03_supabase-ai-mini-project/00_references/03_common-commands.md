# Common Commands

Supabase 기반 03 미니 프로젝트에서 자주 사용하는 명령어입니다.

이 과정에서는 Docker로 PostgreSQL이나 Redis를 실행하지 않습니다. Supabase 클라우드 프로젝트를 데이터 저장소로 사용하고, FastAPI와 Streamlit만 로컬 Python 가상환경에서 실행합니다.

## 과정 폴더 이동

```powershell
cd C:\aidev\03_supabase-ai-mini-project
```

## 가상환경 활성화

```powershell
.\.venv\Scripts\Activate.ps1
```

## 패키지 설치

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

`requirements.txt`에는 FastAPI, Streamlit, Supabase, Gemini SDK, OpenAI 선택 비교용 패키지가 포함되어 있습니다.

## 환경변수 파일 만들기

```powershell
Copy-Item .env.example .env
```

## Supabase 환경변수 확인

```powershell
python .\01_local-dev-basic\01_supabase-env-check\01_check_env.py
```

## FastAPI 실행

```powershell
cd C:\aidev\03_supabase-ai-mini-project\99_team-projects\team-template\backend
..\..\..\.venv\Scripts\Activate.ps1
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

## FastAPI 문서 확인

```text
http://127.0.0.1:8000/docs
```

## Streamlit 실행

```powershell
cd C:\aidev\03_supabase-ai-mini-project\99_team-projects\team-template\frontend
..\..\..\.venv\Scripts\Activate.ps1
streamlit run app.py --server.port 8501
```

## Streamlit 화면 확인

```text
http://127.0.0.1:8501
```

## 포트 사용 확인

```powershell
netstat -ano | findstr :8000
netstat -ano | findstr :8501
```

## 팀 템플릿 복사

```powershell
cd C:\aidev\03_supabase-ai-mini-project
Copy-Item .\99_team-projects\team-template .\99_team-projects\team-01-learning-chatbot -Recurse
```

## Docker 관련 명령어

03 과정에서는 Docker 명령어를 사용하지 않습니다. Docker, Docker Compose, AWS, GitHub Actions는 `06_multi-agent-service-ops`에서 학습합니다.
