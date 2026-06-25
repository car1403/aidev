# 03_supabase-ai-frontend

## SSE 스트리밍 학습 위치 안내

Server-Sent Events(SSE) 기반 실시간 AI 응답 표시는 `04_supabase-ai-mini-project`에서 FastAPI SSE 엔드포인트와 함께 통합 실습으로 다룹니다.

이 과정에서는 Streamlit 화면 구성, API 호출, 대화 UI, 세션 상태 관리를 먼저 익힙니다. 실시간 응답은 `st.spinner`, `st.status`, `st.empty` 같은 Streamlit 표시 도구로 “응답 생성 중” 상태를 보여주는 기초까지 다룹니다.

SSE는 프론트엔드 화면만으로 끝나는 기능이 아니라 백엔드 스트리밍 응답과 Supabase 최종 메시지 저장까지 연결되어야 하므로 03 미니 프로젝트에서 본격적으로 구현합니다.

이 과정은 Streamlit으로 AI 서비스 화면을 만들고, `02_supabase-ai-backend`의 Supabase 기반 API와 연결하는 프론트엔드 수업입니다.

이 폴더에서는 화면을 만들고, 백엔드와 데이터를 직접 연결하는 흐름을 연습합니다. Supabase 프로젝트, 테이블, 인증, 대화 기록 저장은 `02_supabase-ai-backend`에서 준비하고, 이 과정에서는 그 백엔드 API를 호출하는 방식으로 진행합니다.

02~04 과정의 AI 응답 생성 API는 Gemini를 기본으로 사용합니다. 프론트엔드는 Gemini API key를 직접 다루지 않고, `02_supabase-ai-backend` 또는 `04_supabase-ai-mini-project`의 FastAPI 백엔드를 호출합니다. 기존 OpenAI 예제는 선택/비교 실습용으로 유지합니다.

Docker, Docker Compose, AWS 배포, 운영 자동화는 이 과정에서 다루지 않습니다. 해당 내용은 뒤의 `07_multi-agent-service-ops` 과정에서 별도로 학습합니다.

## 수업 기준

- 프론트엔드는 Streamlit으로 작성합니다.
- 데이터 저장소는 Supabase를 기준으로 이해합니다.
- 프론트엔드는 Supabase DB에 직접 접속하지 않고 `02_supabase-ai-backend`의 FastAPI API를 호출합니다.
- 기본 실습 기준으로 `.env`에는 프론트엔드가 호출할 백엔드 주소인 `API_BASE_URL`을 둡니다.
- Supabase `service_role` 키는 절대 프론트엔드 폴더에 두지 않습니다.
- 실제 서비스 구조에서는 Gemini 또는 OpenAI 같은 LLM API key를 프론트엔드 폴더에 두지 않습니다. 실제 AI API 호출은 백엔드에서 처리합니다.
- 단, `04_ai-chatbot-interface`의 Gemini SDK 예제는 API 호출 흐름을 이해하기 위한 로컬 선택 실습입니다. 이 경우에도 키는 GitHub에 올리지 않고, 실제 서비스 구현에서는 백엔드 호출 방식으로 바꿉니다.
- Docker 실행 방식은 사용하지 않고, 로컬 Python 가상환경과 Streamlit 실행 방식으로 진행합니다.
- React는 필수 과정이 아닙니다. Streamlit 수업을 기본으로 진행하고, 진도와 난이도와 수업 시간에 따라 React 기반 UI 구조는 선택 확장으로 소개합니다.
- 99 최종 프로젝트에서는 Render, Upstash, Streamlit Community Cloud 기반의 무료 배포 흐름을 안내합니다. Docker, AWS, GitHub Actions 기반 운영 자동화 배포는 `07_multi-agent-service-ops`에서 다룹니다.

## 학습 목표

이 과정을 마치면 다음 내용을 설명하고 직접 구현할 수 있어야 합니다.

- Streamlit 앱을 실행하고 화면 구조를 만들 수 있다.
- 버튼, 입력창, 폼, 표, 차트, 파일 업로드 UI를 사용할 수 있다.
- `pandas` 데이터를 Streamlit 화면에 표시할 수 있다.
- `httpx`로 FastAPI 백엔드 API를 호출할 수 있다.
- Supabase에 저장된 데이터를 백엔드 API를 통해 화면에 표시할 수 있다.
- 로그인 상태, access token, Authorization header 흐름을 이해할 수 있다.
- 사용자별 대화 이력을 화면에 표시하고 새 메시지를 저장하는 흐름을 만들 수 있다.
- AI 챗봇 화면에서 사용자 질문, AI 응답, 대화 기록을 구성할 수 있다.
- AI 응답 생성 중 로딩 상태와 단계별 안내 메시지를 표시할 수 있다.
- 백엔드가 저장한 서비스 로그를 조회하고 화면에서 운영 상태를 점검할 수 있다.
- 무료 배포 서비스 기반으로 FastAPI는 Render, Redis는 Upstash, Streamlit은 Streamlit Community Cloud에 배포하는 전체 흐름을 이해하고 따라 할 수 있다.
- AI 보조 도구를 사용해 Streamlit 코드의 오류를 찾고 개선할 수 있다.

## 전체 구조

```text
03_supabase-ai-frontend
├─.venv
├─.env.example
├─.gitignore
├─ requirements.txt
├─ README.md
├─ SETUP.md
├─ 00_references
├─ 01_streamlit-basic
├─ 02_streamlit-ui-components
├─ 03_api-integration
├─ 04_ai-chatbot-interface
├─ 05_state-session-and-data
│ └─ 06_service-log-and-integration-check
├─ 90_ai-assisted-ui-review-and-debugging
└─ 99_final-frontend-project
```

## 먼저 이해할 흐름

프론트엔드 수업은 아래 흐름으로 진행합니다.

```text
사용자
-> Streamlit 화면
-> httpx API 요청
-> 02_supabase-ai-backend FastAPI 서버
-> Gemini API 호출(필요한 경우)
-> Supabase Auth / Database 저장 또는 조회
-> FastAPI 응답
-> Streamlit 화면 표시
```

중요한 점은 Streamlit 화면이 Supabase에 바로 접속하지 않는다는 것입니다. 초보자는 처음에 "프론트엔드에서 Supabase 키를 넣고 바로 조회하면 되는 것 아닌가?"라고 생각하기 쉽습니다. 하지만 실제 서비스에서는 보안과 권한 관리를 위해 백엔드가 중간에서 요청을 검증하고 Supabase와 통신하는 구조를 먼저 익히는 것이 좋습니다.

## 처음 시작하는 순서

처음 수업을 시작할 때는 아래 순서대로 진행합니다.

1. `SETUP.md`를 열어 개발 환경을 준비합니다.
2. `03_supabase-ai-frontend` 폴더에 `.venv`를 만듭니다.
3. PowerShell에서 `.venv`를 활성화합니다.
4. `pip install -r requirements.txt`로 패키지를 설치합니다.
5. `Copy-Item .env.example .env`로 환경변수 파일을 만듭니다.
6. `00_references`를 읽고 수업 전체 방향, 보안 기준, 배포 범위를 확인합니다.
7. `01_streamlit-basic`부터 Streamlit 기본 예제를 실행합니다.
8. `03_api-integration`부터는 `02_supabase-ai-backend` 서버를 먼저 실행한 뒤 실습합니다.

이 과정에서는 각 하위 폴더마다 `.venv`를 따로 만들지 않습니다. `03_supabase-ai-frontend` 최상위의 `.venv` 하나를 모든 단원에서 함께 사용합니다.

`03_supabase-ai-frontend` 최상위 `.env`는 기본 단원 실습에서 사용할 백엔드 주소를 관리합니다. 단, `99_final-frontend-project`는 배포와 최종 통합 구조를 독립적으로 연습하기 위해 자기 폴더 안의 `.env`를 따로 사용합니다.

```text
기본 단원 실습:
C:\aidev\03_supabase-ai-frontend\.env

최종 프론트엔드 프로젝트:
C:\aidev\03_supabase-ai-frontend\99_final-frontend-project\.env
```

## 단원별 역할

### 00_references

프론트엔드 과정의 전체 방향을 잡는 참고 자료입니다. Streamlit, React 선택 확장, Supabase 백엔드 API 호출, SSE 학습 위치, 배포 범위, API key 보안 기준을 수업 전에 정리합니다.

### 01_streamlit-basic

Streamlit 앱을 처음 실행하고, 텍스트 출력, 입력값 처리, 기본 레이아웃을 학습합니다. 여기서는 백엔드 연결보다 화면이 어떻게 열리고 코드가 어떻게 화면으로 바뀌는지 이해하는 것이 중요합니다.

### 02_streamlit-ui-components

버튼, 체크박스, 슬라이더, 폼, 표, 차트, CSV 업로드를 연습합니다. 이후 AI 서비스 화면을 만들 때 필요한 작은 UI 부품을 익히는 단계입니다.

### 03_api-integration

`httpx`로 백엔드 API를 호출합니다. 이 단원부터는 `02_supabase-ai-backend`의 Supabase 기반 FastAPI 서버를 우선 연결 대상으로 사용합니다. 폴더 안의 샘플 백엔드는 백엔드가 아직 준비되지 않았을 때 개념 확인용으로만 사용합니다.

### 04_ai-chatbot-interface

AI 챗봇 화면을 만듭니다. 사용자 메시지 입력, assistant 응답 표시, mock 응답 함수, 간단한 대화 이력 미리보기, `/api/chat/mock` 같은 백엔드 API 호출 구조를 학습합니다.

이 단원에서는 완성형 저장 기능까지 한 번에 만들지 않습니다. 기본은 mock 응답으로 진행하고, Gemini SDK 응답 표시는 선택 실습으로만 다룹니다. 로그인 상태, 사용자별 대화 이력, 서비스 로그 관리는 `05_state-session-and-data`에서 본격적으로 다룹니다.

### 05_state-session-and-data

`st.session_state`로 로그인 상태와 사용자 데이터를 관리합니다. Supabase Auth는 백엔드에서 처리하고, 프론트엔드는 로그인 응답으로 받은 token을 저장한 뒤 Authorization header로 백엔드 API를 호출합니다.

이 단원 후반에서는 백엔드가 저장한 서비스 로그를 조회하는 화면과, UI-백엔드-데이터 연결 상태를 점검하는 통합 체크리스트를 다룹니다.

### React 선택 확장

이 과정의 기본 UI 도구는 Streamlit입니다. React는 필수 실습이 아니라 진도와 난이도에 따라 선택적으로 소개합니다.

초보자 수업에서는 먼저 Streamlit으로 화면, API 호출, 상태 관리를 이해한 뒤 React를 비교하면 좋습니다.

```text
Streamlit
-> Python만으로 빠르게 AI 서비스 화면을 만들기 좋습니다.

React
-> 실제 제품 수준의 복잡한 프론트엔드 구조를 만들 때 확장성이 좋습니다.
-> 이 과정에서는 개념 비교 또는 선택 확장으로만 다룹니다.
```

### 90_ai-assisted-ui-review-and-debugging

작성한 Streamlit 코드를 AI와 함께 점검합니다. 오류 메시지 읽기, UI 개선, API 호출 문제 분석, `session_state`와 Authorization header 점검, 코드 리팩토링을 연습합니다.

### 99_final-frontend-project

프론트엔드 최종 예제로 개인화 AI 챗봇 서비스 화면, FastAPI 백엔드 호출, 대화 이력 조회, 서비스 로그 조회, 무료 배포 흐름을 하나로 연결합니다.

이 폴더에서는 다음 흐름을 간단한 예제로 실습합니다.

```text
Streamlit 프론트엔드
-> FastAPI 백엔드
-> 대화 이력과 서비스 로그 확인
-> Render / Upstash / Streamlit Community Cloud 배포
```

03 미니 프로젝트로 넘어갈 때는 이 예제를 Supabase 저장, SSE 스트리밍, 피드백 데이터, 로그 대시보드 산출물로 확장합니다.

## 실행 준비

자세한 환경 준비는 [SETUP.md](./SETUP.md)를 참고합니다.

기본 준비 명령은 다음과 같습니다.

```powershell
cd C:\aidev\03_supabase-ai-frontend
C:\Users\jeanm\AppData\Local\Programs\Python\Python312\python.exe -m venv .venv
.\.venv\Scripts\Activate.ps1
python --version
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
```

이미 `.venv`가 있다면 다시 만들 필요가 없습니다. 다음 명령부터 시작합니다.

```powershell
cd C:\aidev\03_supabase-ai-frontend
.\.venv\Scripts\Activate.ps1
```

PowerShell 줄 앞에 `(.venv)`가 보이면 가상환경이 활성화된 상태입니다.

## Streamlit 실행 예시

가장 먼저 실행해 볼 파일은 다음 예제입니다.

```powershell
cd C:\aidev\03_supabase-ai-frontend
.\.venv\Scripts\Activate.ps1
streamlit run .\01_streamlit-basic\01_streamlit-project-setup\01_hello-streamlit.py
```

브라우저에서 보통 다음 주소가 열립니다.

```text
http://localhost:8501
```

서버를 멈출 때는 PowerShell에서 `Ctrl + C`를 누릅니다.

## Supabase 백엔드와 연결하기

API 연동 단원에서는 PowerShell을 두 개 열어 진행합니다.

첫 번째 PowerShell에서는 백엔드를 실행합니다.

```powershell
cd C:\aidev\02_supabase-ai-backend\06_supabase-db-and-auth\03_fastapi-supabase-integration
..\..\.venv\Scripts\Activate.ps1
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

백엔드가 실행되면 브라우저에서 아래 주소를 확인합니다.

```text
http://127.0.0.1:8000/docs
```

두 번째 PowerShell에서는 프론트엔드를 실행합니다.

```powershell
cd C:\aidev\03_supabase-ai-frontend
.\.venv\Scripts\Activate.ps1
streamlit run .\03_api-integration\02_fastapi-backend-connect\01_fastapi-health-check.py
```

프론트엔드가 호출할 백엔드 주소는 `.env` 파일에서 관리합니다.

```env
API_BASE_URL=http://127.0.0.1:8000
```

백엔드 포트를 바꾸면 `.env`의 `API_BASE_URL`도 함께 바꿔야 합니다.

## Docker를 여기서 다루지 않는 이유

이 과정의 목표는 화면, API 호출, 로그인 상태, 대화 이력 UI를 먼저 이해하는 것입니다. Docker까지 함께 넣으면 초보자 입장에서는 화면 문제인지, API 문제인지, 컨테이너 문제인지 구분하기 어려워집니다.

그래서 `03_supabase-ai-frontend`에서는 로컬 Python 가상환경과 Streamlit 중심으로 실습합니다. Docker, Docker Compose, AWS, GitHub Actions, 서비스 운영, 모니터링은 `07_multi-agent-service-ops`에서 단계적으로 다룹니다.

## 배포 전 점검 범위

이 과정에서는 초보자용 무료 배포 흐름도 함께 안내합니다. 다만 Docker, AWS, GitHub Actions처럼 운영 난도가 높은 배포 자동화는 `07_multi-agent-service-ops`에서 본격적으로 다룹니다.

```text
1. API_BASE_URL이 올바른 백엔드 주소를 가리키는가?
2. 로그인 token이 session_state에 저장되는가?
3. Authorization header가 보호된 API 호출에 포함되는가?
4. 대화 이력 조회와 저장 API가 정상 응답하는가?
5. 서비스 로그 조회 화면에서 백엔드 상태를 확인할 수 있는가?
6. 오류가 발생했을 때 사용자가 이해할 수 있는 안내 메시지가 보이는가?
```

초보자용 무료 배포 실습은 다음 문서를 기준으로 진행합니다.

```text
C:\aidev\03_supabase-ai-frontend\99_final-frontend-project\docs\free-deployment-guide.md
```

배포 기본 흐름:

```text
FastAPI 백엔드 -> Render
Redis 캐시/세션 -> Upstash
Streamlit 프론트엔드 -> Streamlit Community Cloud
```

운영 자동화, Docker Compose, AWS, GitHub Actions, 모니터링은 `07_multi-agent-service-ops`에서 더 깊게 다룹니다.

## 자주 만나는 오류

`streamlit` 명령을 찾을 수 없으면 가상환경이 활성화되어 있는지 확인합니다.

```powershell
cd C:\aidev\03_supabase-ai-frontend
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

브라우저가 자동으로 열리지 않으면 직접 주소를 입력합니다.

```text
http://localhost:8501
```

API 호출에서 `Connection refused`가 나오면 백엔드 서버가 실행 중인지 확인합니다.

```text
http://127.0.0.1:8000/docs
```

로그인 또는 사용자 데이터 호출이 실패하면 access token이 저장되어 있는지, Authorization header가 포함되어 있는지, 백엔드의 Supabase 설정이 완료되어 있는지 확인합니다.

## 수업 진행 팁

수업 진행에서는 먼저 화면이 단독으로 실행되는 예제를 보여준 뒤, 같은 화면이 백엔드 API를 호출하도록 바뀌는 과정을 보여주면 좋습니다.

 오류가 발생했을 때 아래 순서로 확인합니다.

1. `.venv`가 활성화되어 있는가?
2. 필요한 패키지가 설치되어 있는가?
3. Streamlit 파일 경로가 맞는가?
4. 백엔드 서버가 실행 중인가?
5. `.env`의 `API_BASE_URL`이 맞는가?
6. Supabase 설정은 `02_supabase-ai-backend`에서 완료했는가?

## 커리큘럼 점검

이미지의 `AI 인터페이스 및 UX 설계` 영역을 기준으로 `03_supabase-ai-frontend`에 반영된 내용을 점검한 표입니다.

이 과정은 전체적으로 Supabase 기반 백엔드와 연결하는 프론트엔드 수업입니다. 프론트엔드에서 Supabase DB를 직접 다루기보다, `02_supabase-ai-backend`의 FastAPI API를 호출하는 흐름을 기준으로 합니다.

요약하면 다음과 같습니다.

- Streamlit 기반 UI, 챗봇 UI, API 연동, 프롬프트 입력, 로그인 상태, 사용자별 대화 이력, 캐시는 현재 구조에 포함되어 있습니다.
- Supabase Auth, RLS, 대화 테이블, 서비스 로그는 `02_supabase-ai-backend`에서 구현하고, 이 과정에서는 해당 API를 호출하는 화면을 만듭니다.
- 실시간 응답 표시는 이 과정에서 `st.spinner`, `st.status`, `st.empty` 기반 기초를 다루고, SSE 기반 스트리밍은 `04_supabase-ai-mini-project`에서 통합 실습으로 다룹니다.
- 사용 로그 화면과 통합 점검은 `05_state-session-and-data/06_service-log-and-integration-check`에서 다룹니다.
- 무료 서비스 기반 최종 배포 흐름은 초보자용 가이드로 다룹니다. Docker/AWS/GitHub Actions 기반 운영 자동화는 `07_multi-agent-service-ops`에서 다룹니다.
- React 기반 UI 구조는 필수가 아니라 선택 확장입니다. 기본 수업은 Streamlit으로 진행합니다.

| 커리큘럼 항목 | 현재 위치 | 상태 | 검토 의견 |
| --- | --- | --- | --- |
| Streamlit 기반 챗봇 UI 구현 | `04_ai-chatbot-interface` | 포함 | 사용자 입력, assistant 응답, 대화 이력 UI를 학습합니다. |
| React 기반 AI 서비스 UI 구조 이해 | 선택 확장 | 선택 | 진도와 난이도에 따라 비교 개념으로만 다룹니다. 기본 구현은 Streamlit입니다. |
| 화면 설계 | `01_streamlit-basic`, `02_streamlit-ui-components`, `90_ai-assisted-ui-review-and-debugging` | 포함 | 화면 구성, 입력 컴포넌트, UI 개선 흐름을 다룹니다. |
| AI 모델 API 연동 | `04_ai-chatbot-interface/04_mock-and-optional-gemini-interface` | 부분 포함 | 기본은 mock API 호출이며, Gemini SDK는 선택 실습으로 다룹니다. 실제 서비스 연동은 백엔드 API를 통해 진행합니다. |
| 프롬프트 작성 | `04_ai-chatbot-interface/02_prompt-input-and-response` | 포함 | 사용자 질문과 응답 템플릿을 학습합니다. |
| 사용자 질문 응답 기능 구현 | `04_ai-chatbot-interface` | 포함 | 화면 중심 구현 후 백엔드 API 호출로 확장합니다. |
| 로그인 상태 유지 | `05_state-session-and-data/03_auth-token-and-login-state` | 포함 | Supabase Auth는 백엔드에서 처리하고, 프론트엔드는 token 저장과 화면 분기를 담당합니다. |
| 사용자별 대화 기록 조회 및 관리 | `05_state-session-and-data/04_user-data-and-conversation-history` | 포함 | Supabase 대화 테이블 API를 호출하는 화면으로 연결합니다. |
| 이전 대화를 활용한 연속 대화 기능 | `04_ai-chatbot-interface/03_conversation-history-preview`, `05_state-session-and-data` | 포함 | 04에서는 간단한 화면 이력 미리보기를 만들고, 05에서 사용자별 저장 이력과 연결합니다. |
| 프롬프트 설계 및 응답 품질 개선 | `04_ai-chatbot-interface/02_prompt-input-and-response`, assignments | 포함 | 과제에서 질문 개선, 응답 검토, UI 메시지 품질 개선을 다룹니다. |
| AI 응답 생성 과정을 실시간으로 표시 | `03_api-integration`, `04_ai-chatbot-interface` | 포함 방향 | `st.spinner`, `st.status`, 단계별 메시지 표시를 다룹니다. SSE는 03 미니 프로젝트에서 통합합니다. |
| 사용자 인터랙션 및 사용 로그 기록 | `05_state-session-and-data/06_service-log-and-integration-check` | 보강 | 백엔드의 service log API 또는 Supabase log table을 조회하는 화면으로 다룹니다. |
| 개인화 AI 챗봇 서비스 통합 구현 | `99_final-frontend-project` | 포함 | Streamlit 화면, FastAPI 호출, 사용자별 대화 이력, 서비스 로그 조회를 하나의 간단한 예제로 통합합니다. |
| 서비스 로그 수집 | `99_final-frontend-project`, `05_state-session-and-data/06_service-log-and-integration-check` | 보강 | 수집 자체는 백엔드 영역이며, 프론트엔드는 로그 조회와 상태 점검 화면을 담당합니다. |
| 최종 배포 실습 | `99_final-frontend-project/docs/free-deployment-guide.md` | 보강 | FastAPI는 Render, Redis는 Upstash, Streamlit은 Streamlit Community Cloud에 배포하는 초보자용 흐름을 안내합니다. Docker/AWS/GitHub Actions는 07에서 진행합니다. |

## 강의 운영 메모

수업 진행에서는 `02_supabase-ai-backend`에서 Supabase 설정과 API 실행을 먼저 보여준 뒤, 이 과정에서 같은 API를 Streamlit 화면에서 호출하도록 수업을 연결하면 좋습니다.

다음 기준을 반복해서 확인합니다.

- Supabase 연결 설정은 백엔드에서 합니다.
- 프론트엔드는 `API_BASE_URL`로 백엔드를 호출합니다.
- 프론트엔드에는 Supabase service role key를 두지 않습니다.
- React는 선택 확장이고, 기본 실습은 Streamlit으로 진행합니다.
- SSE는 03 미니 프로젝트에서 백엔드/프론트엔드/Supabase 저장까지 함께 다룹니다.
- 무료 배포 서비스 기반의 간단한 최종 배포는 02 마지막에서 안내하고, 운영 자동화는 07 과정에서 배웁니다.