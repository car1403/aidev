# SETUP

`04_supabase-ai-mini-project` 과정의 개발 환경 설정 문서입니다.

이 과정은 `04_supabase-ai-mini-project` 최상위 `.venv` 하나를 사용합니다. 하위 `backend`, `frontend` 폴더 안에 별도 `.venv`를 만들지 않습니다.

## 1. 작업 폴더로 이동

```powershell
cd C:\aidev\04_supabase-ai-mini-project
Get-Location
```

## 2. 가상환경 만들기

```powershell
python -m venv .venv
```

## 3. 가상환경 활성화와 확인

```powershell
.\.venv\Scripts\Activate.ps1
python -c "import sys; print(sys.executable)"
python --version
pip --version
```

정상이라면 Python 경로가 아래처럼 보입니다.

```text
C:\aidev\04_supabase-ai-mini-project\.venv\Scripts\python.exe
```

## 4. 패키지 설치

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 5. `.env` 파일 만들기

```powershell
Copy-Item .env.example .env
```

필수 환경변수:

```env
API_BASE_URL=http://127.0.0.1:8000
SUPABASE_URL=https://your-project-id.supabase.co
SUPABASE_SERVICE_ROLE_KEY=your-supabase-service-role-key
REDIS_URL=redis://localhost:6379
```

수업 중 Redis 서버가 준비되지 않았다면 예제는 메모리 큐 fallback으로 동작합니다. 다만 04 과정의 기본 개념은 **DB는 영구 저장소, Redis는 실시간 이벤트 전달, SSE는 화면 표시 통로**라는 역할 구분입니다.

## 6. Supabase 테이블 만들기

`01_supabase-and-sse-practice/schema.sql` 또는 `03_project_structure/schema.sql`을 Supabase SQL Editor에서 실행합니다.

처음 실행 실습은 아래 파일을 사용합니다.

```text
C:\aidev\04_supabase-ai-mini-project\01_supabase-and-sse-practice\schema.sql
```

## 7. 01 실습 실행

PowerShell 1: backend 실행

```powershell
cd C:\aidev\04_supabase-ai-mini-project\01_supabase-and-sse-practice\backend
C:\aidev\04_supabase-ai-mini-project\.venv\Scripts\Activate.ps1
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

확인 주소:

```text
http://127.0.0.1:8000/health
http://127.0.0.1:8000/docs
```

PowerShell 2: frontend 실행

```powershell
cd C:\aidev\04_supabase-ai-mini-project\01_supabase-and-sse-practice\frontend
C:\aidev\04_supabase-ai-mini-project\.venv\Scripts\Activate.ps1
streamlit run .\app.py
```

## 8. 최종 프로젝트 starter 실행

`03_project_structure`는 학생용 최종 프로젝트 starter입니다. 기본 코드는 `/health`와 backend 연결 확인만 제공합니다. 로그 API, SSE, 피드백 API, 대시보드 화면은 학생들이 직접 구현합니다.

backend:

```powershell
cd C:\aidev\04_supabase-ai-mini-project\03_project_structure\backend
C:\aidev\04_supabase-ai-mini-project\.venv\Scripts\Activate.ps1
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

frontend:

```powershell
cd C:\aidev\04_supabase-ai-mini-project\03_project_structure\frontend
C:\aidev\04_supabase-ai-mini-project\.venv\Scripts\Activate.ps1
streamlit run .\app.py
```

## 9. 오류 확인 순서

1. 현재 Python이 `04_supabase-ai-mini-project\.venv`를 가리키는지 확인합니다.
2. `pip install -r requirements.txt`를 실행했는지 확인합니다.
3. 백엔드가 `http://127.0.0.1:8000/docs`에서 열리는지 확인합니다.
4. Streamlit의 `API_BASE_URL`이 백엔드 주소와 같은지 확인합니다.
5. Supabase 환경변수와 테이블 생성 여부를 확인합니다.
6. Redis가 꺼져 있어도 메모리 fallback으로 기본 SSE가 보이는지 확인합니다.
7. 8000 또는 8501 포트가 이미 사용 중이면 기존 프로세스를 종료합니다.

## 10. backend 테스트

01 실습 backend:

```powershell
cd C:\aidev\04_supabase-ai-mini-project\01_supabase-and-sse-practice\backend
C:\aidev\04_supabase-ai-mini-project\.venv\Scripts\Activate.ps1
pytest tests -q
```

03 starter backend:

```powershell
cd C:\aidev\04_supabase-ai-mini-project\03_project_structure\backend
C:\aidev\04_supabase-ai-mini-project\.venv\Scripts\Activate.ps1
pytest tests -q
```
