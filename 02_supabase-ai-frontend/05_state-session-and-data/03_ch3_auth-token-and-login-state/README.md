# 03_ch3_auth-token-and-login-state

로그인 API 응답 token을 Streamlit 상태에 저장하고 화면 흐름을 분기하는 방법을 학습합니다.

이 챕터는 Supabase Auth를 직접 호출하는 프론트엔드 수업이 아닙니다. Supabase Auth는 `01_supabase-ai-backend`에서 처리하고, 프론트엔드는 백엔드 로그인 API를 호출한 뒤 응답으로 받은 token을 `st.session_state`에 저장합니다.

## 학습 목표

- 로그인 폼을 만들 수 있다.
- 로그인 API에 사용자 정보 또는 테스트 계정 정보를 POST 요청으로 보낼 수 있다.
- 로그인 성공 응답의 token을 `st.session_state`에 저장할 수 있다.
- 로그인 상태와 로그아웃 상태에 따라 화면을 다르게 표시할 수 있다.
- Authorization header를 사용해 보호된 API를 호출할 수 있다.

## 예제 파일

```text
01_login-form.py
02_login-token-state.py
03_logout-flow.py
04_authorization-header.py
```

## 기본 백엔드 연결

실제 수업에서는 다음 백엔드 흐름과 연결합니다.

```text
C:\aidev\01_supabase-ai-backend\06_supabase-db-and-auth\04_ch4_supabase-auth-and-rls
```

API 서버는 아래처럼 실행합니다.

```powershell
cd C:\aidev\01_supabase-ai-backend\06_supabase-db-and-auth\03_ch3_fastapi-supabase-integration
..\..\.venv\Scripts\Activate.ps1
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

## 보조 샘플 백엔드 실행

백엔드 인증 단원이 아직 준비되지 않았을 때는 아래 샘플을 사용해 token 저장 흐름만 확인할 수 있습니다.

```powershell
cd C:\aidev\02_supabase-ai-frontend\05_state-session-and-data\00_references
..\..\.venv\Scripts\Activate.ps1
uvicorn backend-auth-session-sample:app --reload --host 127.0.0.1 --port 8000
```

샘플 실습 계정은 다음과 같습니다.

```text
student / 1234
```

## 프론트엔드 실행 예시

```powershell
cd C:\aidev\02_supabase-ai-frontend
.\.venv\Scripts\Activate.ps1
streamlit run.\05_state-session-and-data\03_ch3_auth-token-and-login-state\02_login-token-state.py
```

## 확인할 내용

- 올바른 계정으로 로그인하면 token이 저장되는가?
- 잘못된 계정으로 로그인하면 실패 메시지가 표시되는가?
- 로그아웃 버튼을 누르면 token이 제거되는가?
- `/api/me` 호출 시 `Authorization: Bearer...` 헤더가 포함되는가?
- 인증 실패 시 사용자에게 이해 가능한 메시지가 표시되는가?

## 보안 메모

프론트엔드에는 Supabase service role key를 저장하지 않습니다. 서비스 권한이 큰 키는 백엔드에서만 사용해야 합니다.
