# 04_local-full-stack

FastAPI, Streamlit, Supabase를 연결하는 로컬 통합 실습입니다.

이 실습은 `01_supabase-ai-backend`에서 배운 Supabase 저장 흐름과 `02_supabase-ai-frontend`에서 배운 Streamlit API 호출 흐름을 하나로 연결합니다.

```text
Streamlit 화면
-> FastAPI API 호출
-> Supabase learning_logs 테이블 저장/조회
-> Streamlit 화면에 표와 지표 표시
```

## 실행 환경 기준

하위 폴더에 `.venv`를 새로 만들지 않습니다.

```text
가상환경:
C:\aidev\03_supabase-ai-mini-project\.venv

환경변수:
C:\aidev\03_supabase-ai-mini-project\.env
```

## 준비 순서

1. Supabase 프로젝트를 준비합니다.
2. Supabase SQL Editor에서 `learning_logs` 테이블을 만듭니다.
3. `C:\aidev\03_supabase-ai-mini-project\.env`에 Supabase 값과 `API_BASE_URL`을 입력합니다.
4. 첫 번째 PowerShell에서 FastAPI 백엔드를 실행합니다.
5. 두 번째 PowerShell에서 Streamlit 프론트엔드를 실행합니다.
6. 브라우저에서 등록, 조회, 상태 변경 기능을 확인합니다.

Supabase 테이블 준비 방법은 아래 문서를 참고합니다.

```text
docs/setup-supabase.md
```

## FastAPI 실행

첫 번째 PowerShell에서 실행합니다.

```powershell
cd C:\aidev\03_supabase-ai-mini-project
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
cd C:\aidev\03_supabase-ai-mini-project\01_local-dev-basic\04_local-full-stack\backend
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

확인 URL:

```text
http://127.0.0.1:8000/docs
```

## Streamlit 실행

두 번째 PowerShell에서 실행합니다.

```powershell
cd C:\aidev\03_supabase-ai-mini-project
.\.venv\Scripts\Activate.ps1
cd C:\aidev\03_supabase-ai-mini-project\01_local-dev-basic\04_local-full-stack\frontend
streamlit run app.py --server.port 8501
```

확인 URL:

```text
http://127.0.0.1:8501
```

## 핵심 포인트

- Streamlit은 사용자가 보는 화면입니다.
- FastAPI는 요청을 검증하고 Supabase와 통신하는 백엔드입니다.
- Supabase는 `learning_logs` 데이터를 저장하고 조회하는 데이터베이스입니다.
- `SUPABASE_SERVICE_ROLE_KEY`는 프론트엔드 화면에 넣지 않습니다.
- 이 예제의 FastAPI 백엔드는 `SUPABASE_SERVICE_ROLE_KEY`가 있으면 서버 내부에서 우선 사용하고, 값이 없으면 `SUPABASE_ANON_KEY`로 기본 연결을 확인합니다.
- 팀 프로젝트에서는 어떤 작업에 service role key가 필요한지, 어떤 작업은 RLS 정책과 anon key로 처리할지 데이터베이스 설계서에 명확히 정리합니다.
- Docker 기반 실행은 이 실습에서 하지 않고 `06_multi-agent-service-ops`에서 학습합니다.

## 다음 단계

이 실습이 정상 동작하면 이후 단원에서 다음 내용을 확장합니다.

- API 설계 문서 작성
- 화면 설계서 작성
- Supabase 테이블과 RLS 정책 정리
- Gemini 기반 AI 응답 저장
- SSE 기반 실시간 응답 표시
- 서비스 로그와 피드백 대시보드 구성
