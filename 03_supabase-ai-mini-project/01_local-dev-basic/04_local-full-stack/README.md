# 04_local-full-stack

FastAPI, Streamlit, Supabase를 연결하는 로컬 통합 실습입니다.

이 실습은 `05_supabase-sample-assets/sample-learning-log-dashboard`와 같은 구조를 사용합니다. 데이터 저장은 Supabase 테이블에서 처리하고, 로컬 PC에서는 백엔드와 프론트엔드를 각각 실행합니다.

## 실행 순서

1. Supabase 프로젝트와 `learning_logs` 테이블을 준비합니다.
2. 상위 폴더의 `.env`에 Supabase 값을 입력합니다.
3. FastAPI 백엔드를 실행합니다.
4. Streamlit 프론트엔드를 실행합니다.
5. 브라우저에서 등록, 조회, 상태 변경 기능을 확인합니다.

## FastAPI 실행

```powershell
cd C:\aidev\03_supabase-ai-mini-project\01_local-dev-basic\04_local-full-stack\backend
..\..\..\.venv\Scripts\Activate.ps1
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

확인 URL:

```text
http://127.0.0.1:8000/docs
```

## Streamlit 실행

```powershell
cd C:\aidev\03_supabase-ai-mini-project\01_local-dev-basic\04_local-full-stack\frontend
..\..\..\.venv\Scripts\Activate.ps1
streamlit run app.py --server.port 8501
```

확인 URL:

```text
http://127.0.0.1:8501
```

## 핵심 포인트

각 서비스를 따로 실행하면 어떤 서비스가 어떤 역할을 하는지 명확히 볼 수 있습니다.

- Streamlit: 사용자가 보는 화면
- FastAPI: 요청 검증과 API 응답
- Supabase: 데이터 저장과 조회

Docker 기반 실행은 이 실습에서 하지 않고 `06_multi-agent-service-ops`에서 학습합니다.
