# 03_api-integration

Streamlit 프론트엔드에서 HTTP 요청을 보내고 FastAPI 백엔드 응답을 화면에 표시하는 단원입니다.

이 단원부터는 화면만 만드는 것을 넘어, 사용자의 입력을 API 요청으로 보내고 JSON 응답을 처리하는 흐름을 학습합니다. 수업의 기본 연결 대상은 `01_supabase-ai-backend`의 Supabase 기반 FastAPI 서버입니다.

## 학습 목표

- HTTP 요청과 JSON 응답의 기본 흐름을 이해한다.
- `httpx`를 사용해 GET, POST 요청을 보낼 수 있다.
- Streamlit 화면에서 FastAPI 백엔드 API를 호출할 수 있다.
- Supabase에 저장된 데이터를 백엔드 API를 통해 화면에 표시하는 구조를 이해한다.
- API 호출 중 로딩 상태를 표시할 수 있다.
- API 오류, 타임아웃, 잘못된 응답을 화면에서 처리할 수 있다.

## 학습 순서

```text
01_ch1_httpx-api-call
-> 02_ch2_fastapi-backend-connect
-> 03_ch3_error-loading-and-response-handling
-> 10_labs
-> 20_assignments
```

## 기본 백엔드 실행 기준

수업에서는 `01_supabase-ai-backend`의 Supabase 연동 FastAPI 서버를 먼저 실행합니다.

```powershell
cd C:\aidev\01_supabase-ai-backend\06_supabase-db-and-auth\03_ch3_fastapi-supabase-integration
..\..\.venv\Scripts\Activate.ps1
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

정상 실행 확인:

```text
http://127.0.0.1:8000/health
http://127.0.0.1:8000/docs
```

## 보조 샘플 백엔드

백엔드 과정이 아직 준비되지 않았거나, HTTP 요청 개념만 빠르게 확인해야 할 때는 이 폴더의 샘플 백엔드를 사용할 수 있습니다.

```text
00_references/backend-integration-sample.py
```

실행 예시:

```powershell
cd C:\aidev\02_supabase-ai-frontend\03_api-integration\00_references
..\..\.venv\Scripts\Activate.ps1
uvicorn backend-integration-sample:app --reload --host 127.0.0.1 --port 8000
```

샘플 백엔드는 수업 보조용입니다. 실제 Supabase 데이터 저장과 인증 흐름은 `01_supabase-ai-backend`를 기준으로 진행합니다.

## 프론트엔드 실행 예시

```powershell
cd C:\aidev\02_supabase-ai-frontend
.\.venv\Scripts\Activate.ps1
streamlit run .\03_api-integration\02_ch2_fastapi-backend-connect\01_fastapi-health-check.py
```

## 실행 확인 기준

- FastAPI 서버가 `http://127.0.0.1:8000`에서 실행 중이다.
- Streamlit 화면에서 API 호출 버튼을 누르면 JSON 응답이 표시된다.
- POST 요청에서 입력값이 백엔드로 전달된다.
- 서버가 꺼져 있을 때 오류 메시지가 표시된다.
- 로딩 상태와 응답 검증 메시지가 화면에 표시된다.

## 수업 참여자가 꼭 구분해야 할 것

- Streamlit은 화면을 담당합니다.
- FastAPI는 요청을 받고 Supabase와 통신합니다.
- Supabase는 사용자, 대화, 로그 같은 데이터를 저장합니다.
- Docker 실행은 이 단원에서 하지 않고 `06_multi-agent-service-ops`에서 배웁니다.
- 이 단원에서의 실시간 표시는 로딩, 상태 메시지, 응답 검증 중심입니다. SSE 기반 응답 스트리밍은 `03_supabase-ai-mini-project`에서 통합 실습으로 다룹니다.
