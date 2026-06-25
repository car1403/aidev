# 03_local-streamlit

Streamlit 앱을 로컬 Python 환경에서 실행하는 실습입니다.

이 실습도 `03_supabase-ai-mini-project` 최상위 `.venv`를 사용합니다. `frontend` 폴더 안에 `.venv`를 새로 만들지 않습니다.

```text
가상환경:
C:\aidev\03_supabase-ai-mini-project\.venv

환경변수:
C:\aidev\03_supabase-ai-mini-project\.env
```

## 실행 방법

FastAPI 연결 없이 Streamlit 화면이 정상적으로 열리는지 먼저 확인합니다.

```powershell
cd C:\aidev\03_supabase-ai-mini-project
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
cd C:\aidev\03_supabase-ai-mini-project\01_local-dev-basic\03_local-streamlit\frontend
streamlit run app.py --server.port 8501
```

## 확인

브라우저에서 아래 주소를 확인합니다.

```text
http://127.0.0.1:8501
```

## 확인할 점

- Streamlit 화면이 정상적으로 열리는지 확인합니다.
- 표 형태의 데이터가 화면에 표시되는지 확인합니다.
- 이 단계는 API 호출 전, Streamlit 화면 실행 감각을 확인하는 기본 단계입니다.
- FastAPI와 Supabase 연결은 `04_local-full-stack`에서 진행합니다.
