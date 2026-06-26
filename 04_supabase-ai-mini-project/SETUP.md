# SETUP

`04_supabase-ai-mini-project`를 로컬에서 실행하기 위한 준비 문서입니다.

## 1. 작업 위치

```powershell
cd C:\aidev\04_supabase-ai-mini-project
```

## 2. Python 가상환경 만들기

이 과정은 최상위 `.venv` 하나를 사용합니다. `backend`, `frontend`, 팀 프로젝트 하위 폴더 안에 별도 `.venv`를 만들지 않습니다.

```powershell
python -m venv .venv
```

이미 `.venv`가 있다면 다시 만들 필요는 없습니다.

## 3. 가상환경 활성화

```powershell
.\.venv\Scripts\Activate.ps1
```

PowerShell 앞에 `(.venv)`가 보이면 활성화된 상태입니다.

VS Code에서 `C:\aidev\04_supabase-ai-mini-project` 폴더 자체를 열면 `.vscode/settings.json` 설정에 따라 새 터미널에서 `.venv`가 자동 활성화됩니다. `C:\aidev` 루트를 열어 수업을 진행할 때는 새 터미널을 연 뒤 아래 확인 명령으로 현재 Python 경로가 이 과정의 `.venv`를 가리키는지 먼저 확인합니다.

활성화 후 현재 Python이 이 과정의 `.venv`를 사용하는지 확인합니다.

```powershell
echo $env:VIRTUAL_ENV
python -c "import sys; print(sys.executable)"
```

정상이라면 아래 경로를 가리켜야 합니다.

```text
C:\aidev\04_supabase-ai-mini-project\.venv
C:\aidev\04_supabase-ai-mini-project\.venv\Scripts\python.exe
```

## 4. 패키지 설치

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 5. 환경변수 파일 만들기

```powershell
Copy-Item .env.example .env
```

`.env`에는 실제 Supabase와 Gemini 값을 넣습니다. `.env.example`에는 예시 값만 둡니다.

필수 값:

```env
SUPABASE_URL=
SUPABASE_ANON_KEY=
SUPABASE_SERVICE_ROLE_KEY=
GEMINI_API_KEY=
GEMINI_MODEL=gemini-2.5-flash-lite
API_BASE_URL=http://127.0.0.1:8000
```

OpenAI API Key는 선택/비교 실습에서만 사용합니다.

## 6. 샘플 프로젝트 실행

샘플 백엔드:

```powershell
cd C:\aidev\04_supabase-ai-mini-project\02_instructor-sample-project\backend
..\..\.venv\Scripts\Activate.ps1
uvicorn main:app --reload --port 8000
```

샘플 프론트엔드:

```powershell
cd C:\aidev\04_supabase-ai-mini-project\02_instructor-sample-project\frontend
..\..\.venv\Scripts\Activate.ps1
streamlit run app.py
```

## 7. 제출 전 확인

- [ ] `.env`를 GitHub에 올리지 않는다.
- [ ] 필수 산출물 4종을 `docs` 폴더에 작성한다.
- [ ] 로컬에서 FastAPI와 Streamlit이 실행된다.
- [ ] Supabase 테이블과 API 응답 구조가 문서와 일치한다.
- [ ] SSE, 무료 배포, 발표 자료는 선택 보조 산출물임을 표시한다.
