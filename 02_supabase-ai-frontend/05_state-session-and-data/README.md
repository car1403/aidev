# 05_state-session-and-data

Streamlit 앱에서 상태, 로그인 정보, 사용자별 데이터, 대화 이력, 캐시를 관리하는 단원입니다.

이 단원은 `01_supabase-ai-backend`의 `06_supabase-db-and-auth`, `07_backend-service-data-management`와 연결됩니다. Supabase Auth와 RLS는 백엔드와 Supabase 프로젝트에서 처리하고, 프론트엔드는 로그인 상태를 화면에서 유지하며 보호된 API를 호출하는 역할을 담당합니다.

## 학습 목표

- `st.session_state`로 화면 상태를 유지할 수 있다.
- 입력값과 선택값을 상태로 관리할 수 있다.
- 로그인 응답 token을 저장하고 화면 흐름을 분기할 수 있다.
- Authorization header로 인증이 필요한 API를 호출할 수 있다.
- 사용자별 데이터와 대화 이력을 조회하고 표시할 수 있다.
- `st.cache_data`로 반복 조회 비용을 줄일 수 있다.
- 백엔드가 저장한 서비스 로그를 조회하고 UI-백엔드-데이터 연결 상태를 점검할 수 있다.

## 학습 순서

```text
01_ch1_streamlit-session-state
-> 02_ch2_user-input-state-management
-> 03_ch3_auth-token-and-login-state
-> 04_ch4_user-data-and-conversation-history
-> 05_ch5_frontend-cache-and-performance
-> 06_ch6_service-log-and-integration-check
-> 10_labs
-> 20_assignments
```

## 백엔드 연결 기준

실제 수업에서는 다음 백엔드 단원과 연결합니다.

```text
C:\aidev\01_supabase-ai-backend\06_supabase-db-and-auth\04_ch4_supabase-auth-and-rls
C:\aidev\01_supabase-ai-backend\06_supabase-db-and-auth\05_ch5_conversation-history-and-service-logs
C:\aidev\01_supabase-ai-backend\07_backend-service-data-management
```

그리고 API 서버 실행은 Supabase 연동 FastAPI 단원을 기준으로 합니다.

```powershell
cd C:\aidev\01_supabase-ai-backend\06_supabase-db-and-auth\03_ch3_fastapi-supabase-integration
..\..\.venv\Scripts\Activate.ps1
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

## 보조 샘플 백엔드

프론트엔드 상태 관리 개념만 빠르게 확인할 때는 이 폴더의 샘플 백엔드를 사용할 수 있습니다.

```text
00_references\backend-auth-session-sample.py
```

실행 예시:

```powershell
cd C:\aidev\02_supabase-ai-frontend\05_state-session-and-data\00_references
..\..\.venv\Scripts\Activate.ps1
uvicorn backend-auth-session-sample:app --reload --host 127.0.0.1 --port 8000
```

샘플 백엔드는 Supabase를 대체하는 것이 아니라, 로그인 상태와 Authorization header 흐름을 연습하기 위한 보조 자료입니다.

## 프론트엔드 실행 예시

```powershell
cd C:\aidev\02_supabase-ai-frontend
.\.venv\Scripts\Activate.ps1
streamlit run.\05_state-session-and-data\03_ch3_auth-token-and-login-state\02_login-token-state.py
```

## 실행 확인 기준

- 버튼을 누른 뒤 값이 화면 새로고침에도 유지된다.
- 로그인 성공 후 token이 `st.session_state`에 저장된다.
- 로그인 여부에 따라 화면이 다르게 보인다.
- Authorization header가 필요한 API 호출에 포함된다.
- 사용자별 대화 이력이 화면에 표시된다.
- 캐시 적용 전후의 흐름을 설명할 수 있다.
- 서비스 로그 조회 화면에서 API 호출 결과와 오류 상태를 확인할 수 있다.
- 배포 전 점검 항목을 기준으로 프론트엔드 준비 상태를 설명할 수 있다.

## 핵심 요약

- Supabase Auth 검증은 백엔드에서 처리합니다.
- Streamlit은 token을 저장하고 API 요청에 header로 붙이는 역할을 합니다.
- 사용자별 데이터 접근 제어는 Supabase RLS와 백엔드 로직이 함께 담당합니다.
- 서비스 로그 저장은 백엔드가 담당하고, Streamlit은 로그 조회와 상태 확인 화면을 담당합니다.
- Docker 실행과 배포는 `06_multi-agent-service-ops`에서 학습합니다.
