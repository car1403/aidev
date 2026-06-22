# SETUP

`02_supabase-ai-frontend` 과정의 개발 환경 설정 문서입니다.

이 문서는 수업 시간에 그대로 따라 할 수 있도록 작성했습니다. 이 과정은 Streamlit 프론트엔드를 만들고, `01_supabase-ai-backend`의 Supabase 기반 FastAPI API를 호출하는 방식으로 진행합니다.

Docker, Docker Compose, AWS 배포는 여기서 설정하지 않습니다. 해당 내용은 `06_multi-agent-service-ops`에서 다룹니다.

React는 필수 실습이 아닙니다. 이 과정은 Streamlit을 기본 UI 도구로 사용하고, React 기반 UI 구조는 진도와 난이도에 따라 선택 확장으로 소개합니다.

## 1. 작업 폴더로 이동

PowerShell을 열고 프론트엔드 과정 폴더로 이동합니다.

```powershell
cd C:\aidev\02_supabase-ai-frontend
```

현재 위치가 맞는지 확인합니다.

```powershell
Get-Location
```

결과가 다음과 비슷하면 됩니다.

```text
C:\aidev\02_supabase-ai-frontend
```

## 2. 가상환경 만들기

각 과정 폴더는 자기 폴더 안에 `.venv`를 둡니다. 이 과정에서는 `02_supabase-ai-frontend\.venv` 하나를 사용합니다.

```powershell
C:\Users\jeanm\AppData\Local\Programs\Python\Python312\python.exe -m venv.venv
```

이미 `.venv`가 있다면 이 단계는 다시 실행하지 않아도 됩니다.

## 3. 가상환경 활성화

```powershell
.\.venv\Scripts\Activate.ps1
```

PowerShell 줄 앞에 `(.venv)`가 보이면 활성화된 상태입니다.

확인 명령:

```powershell
python --version
pip --version
```

## 4. 패키지 설치

Streamlit 화면, API 호출, 예제 백엔드 실행에 필요한 패키지를 설치합니다.

```powershell
pip install -r requirements.txt
```

설치가 끝난 뒤 Streamlit이 설치되었는지 확인합니다.

```powershell
streamlit --version
```

## 5. 환경변수 파일 만들기

`.env.example`을 복사해서 `.env` 파일을 만듭니다.

```powershell
Copy-Item.env.example.env
```

기본값은 로컬에서 실행 중인 `01_supabase-ai-backend` FastAPI 서버를 바라봅니다.

```env
API_BASE_URL=http://127.0.0.1:8000
```

주의할 점:

- 프론트엔드 `.env`에는 `SUPABASE_SERVICE_ROLE_KEY`를 넣지 않습니다.
- Supabase URL, anon key, service role key는 `01_supabase-ai-backend`에서 관리합니다.
- 프론트엔드는 백엔드 API 주소만 알고 있으면 됩니다.

## 6. 백엔드 먼저 실행하기

API 연동 실습을 할 때는 백엔드 서버가 먼저 실행되어 있어야 합니다. PowerShell을 하나 더 열고 아래 명령을 실행합니다.

```powershell
cd C:\aidev\01_supabase-ai-backend\06_supabase-db-and-auth\03_ch3_fastapi-supabase-integration
..\..\.venv\Scripts\Activate.ps1
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

브라우저에서 다음 주소를 열어 확인합니다.

```text
http://127.0.0.1:8000/docs
```

Swagger 문서 화면이 보이면 백엔드가 실행 중입니다.

## 7. 프론트엔드 실행하기

다시 프론트엔드 PowerShell로 돌아와서 Streamlit 예제를 실행합니다.

```powershell
cd C:\aidev\02_supabase-ai-frontend
.\.venv\Scripts\Activate.ps1
streamlit run.\03_api-integration\02_ch2_fastapi-backend-connect\01_fastapi-health-check.py
```

브라우저에서 다음 주소가 열립니다.

```text
http://localhost:8501
```

## 8. 학습 순서

권장 순서는 다음과 같습니다.

1. `01_streamlit-basic`에서 화면 실행 방식을 익힙니다.
2. `02_streamlit-ui-components`에서 입력, 버튼, 표, 차트를 연습합니다.
3. `03_api-integration`에서 Supabase 백엔드 API 호출을 연습합니다.
4. `04_ai-chatbot-interface`에서 챗봇 화면을 만듭니다.
5. `05_state-session-and-data`에서 로그인 상태와 사용자별 대화 이력을 다룹니다.
6. `05_state-session-and-data/06_ch6_service-log-and-integration-check`에서 서비스 로그 조회와 통합 점검을 연습합니다.
7. `90_ai-assisted-ui-review-and-debugging`에서 AI를 활용해 코드 리뷰와 디버깅을 연습합니다.

## 9. 오류 확인 순서

오류가 나면 아래 순서대로 확인합니다.

1. 현재 위치가 `C:\aidev\02_supabase-ai-frontend`인지 확인합니다.
2. PowerShell 앞에 `(.venv)`가 보이는지 확인합니다.
3. `pip install -r requirements.txt`를 실행했는지 확인합니다.
4. 백엔드 서버가 `http://127.0.0.1:8000/docs`에서 열리는지 확인합니다.
5. `.env`의 `API_BASE_URL`이 백엔드 주소와 같은지 확인합니다.
6. Supabase 설정은 `01_supabase-ai-backend`에서 완료했는지 확인합니다.

## 10. Docker 학습 위치

이 과정에서는 Docker를 사용하지 않습니다.

Docker, Docker Compose, AWS, GitHub Actions, 서비스 운영, 모니터링은 다음 과정에서 다룹니다.

```text
C:\aidev\06_multi-agent-service-ops
```

## 11. SSE와 실제 배포 학습 위치

이 과정에서는 `st.spinner`, `st.status`, `st.empty`로 응답 생성 중 상태를 표시하는 기초를 다룹니다.

Server-Sent Events(SSE) 기반 실시간 응답 스트리밍은 백엔드 스트리밍 응답, Streamlit 표시, Supabase 최종 메시지 저장이 함께 연결되어야 하므로 다음 과정에서 통합 실습으로 진행합니다.

```text
C:\aidev\03_supabase-ai-mini-project
```

무료 배포 서비스 기반의 초보자용 배포 흐름은 이 과정의 마지막 통합 점검 단계에서 안내합니다.

```text
C:\aidev\02_supabase-ai-frontend\05_state-session-and-data\06_ch6_service-log-and-integration-check\03_free-deployment-guide.md
```

이 문서에서는 다음 흐름을 다룹니다.

```text
FastAPI -> Render
Redis -> Upstash
Streamlit -> Streamlit Community Cloud
```

Docker, AWS, GitHub Actions를 활용한 운영 자동화와 모니터링은 다음 과정에서 다룹니다.

```text
C:\aidev\06_multi-agent-service-ops
```
