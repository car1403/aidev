# 02_ch2_fastapi-backend-connect

Streamlit 화면에서 FastAPI 백엔드를 호출하는 방법을 학습합니다.

이 챕터의 기본 연결 대상은 `01_supabase-ai-backend`의 Supabase 기반 FastAPI 서버입니다. 프론트엔드는 Supabase에 직접 접속하지 않고 백엔드 API 주소를 호출합니다.

## 예제 파일

```text
01_fastapi-health-check.py
02_fastapi-message-client.py
03_fastapi-course-list.py
04_fastapi-score-feedback.py
```

## 기본 백엔드 실행

PowerShell을 하나 더 열고 백엔드를 먼저 실행합니다.

```powershell
cd C:\aidev\01_supabase-ai-backend\06_supabase-db-and-auth\03_ch3_fastapi-supabase-integration
..\..\.venv\Scripts\Activate.ps1
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

정상 실행 확인:

```text
http://127.0.0.1:8000/docs
```

## 보조 샘플 백엔드

백엔드 과정이 아직 준비되지 않았을 때만 아래 샘플을 사용합니다.

```powershell
cd C:\aidev\02_supabase-ai-frontend\03_api-integration\00_references
..\..\.venv\Scripts\Activate.ps1
uvicorn backend-integration-sample:app --reload --host 127.0.0.1 --port 8000
```

## 프론트엔드 실행 예시

```powershell
cd C:\aidev\02_supabase-ai-frontend
.\.venv\Scripts\Activate.ps1
streamlit run .\03_api-integration\02_ch2_fastapi-backend-connect\02_fastapi-message-client.py
```

## 확인할 내용

- Streamlit 버튼이 API 호출 시점으로 동작하는가?
- 입력값이 JSON으로 백엔드에 전달되는가?
- 백엔드 응답이 화면에 표시되는가?
- 백엔드가 꺼졌을 때 오류 메시지를 확인할 수 있는가?

## 수업 메모

Docker 실행은 이 챕터에서 하지 않습니다. Docker, Docker Compose, AWS 배포는 `06_multi-agent-service-ops`에서 학습합니다.
