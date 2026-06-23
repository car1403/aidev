# 05_state-session-and-data

`05_state-session-and-data`는 `04_ai-chatbot-interface`에서 만든 챗봇 UI 뼈대를 실제 서비스 화면처럼 확장하는 단원입니다.

04에서는 사용자 질문 입력, mock 응답 표시, Gemini 선택 실습, 간단한 대화 이력 미리보기까지 다루었습니다. 05에서는 여기서 한 단계 나아가 로그인 상태, access token, Authorization header, 사용자별 대화 이력, 서비스 로그, 캐시, 통합 점검을 다룹니다.

중요한 기준은 다음과 같습니다.

- Streamlit은 Supabase에 직접 접속하지 않습니다.
- Streamlit은 `API_BASE_URL`로 FastAPI 백엔드를 호출합니다.
- Supabase Auth, RLS, DB 저장, Gemini API 호출은 백엔드에서 처리합니다.
- 프론트엔드에는 `SUPABASE_SERVICE_ROLE_KEY`를 절대 두지 않습니다.
- Gemini API key도 실제 서비스 구조에서는 백엔드에 둡니다.
- Docker, Docker Compose, AWS, GitHub Actions 운영 자동화는 `06_multi-agent-service-ops`에서 다룹니다.

## 학습 목표

이 단원을 마치면 다음 내용을 설명하고 직접 구현할 수 있어야 합니다.

- `st.session_state`로 화면 상태를 유지할 수 있다.
- 입력값, 선택값, 임시 작성 중인 질문을 상태로 관리할 수 있다.
- 로그인 성공 응답의 access token을 `st.session_state`에 저장할 수 있다.
- 로그인 여부에 따라 화면을 다르게 표시할 수 있다.
- `Authorization: Bearer ...` header를 만들어 보호된 API를 호출할 수 있다.
- 사용자별 대화 이력을 백엔드 API로 조회하고 화면에 표시할 수 있다.
- 새 대화 메시지를 백엔드 API로 저장하는 흐름을 이해할 수 있다.
- `st.cache_data`를 사용해 반복 조회 성능을 개선할 수 있다.
- 백엔드가 저장한 서비스 로그를 조회하고 서비스 상태를 점검할 수 있다.
- 배포 전 프론트엔드, 백엔드, Supabase 연결 상태를 체크리스트로 확인할 수 있다.

## 학습 순서

```text
00_references
-> 01_streamlit-session-state
-> 02_user-input-state-management
-> 03_auth-token-and-login-state
-> 04_user-data-and-conversation-history
-> 05_frontend-cache-and-performance
-> 06_service-log-and-integration-check
-> 10_labs
-> 20_assignments
```

## 폴더 역할

| 폴더 | 역할 |
| --- | --- |
| `00_references` | 상태 관리, 인증 흐름, 샘플 백엔드 참고 자료를 정리합니다. |
| `01_streamlit-session-state` | `st.session_state`의 기본 사용법을 연습합니다. |
| `02_user-input-state-management` | 입력값, 필터, 단계형 폼, 질문 초안을 상태로 관리합니다. |
| `03_auth-token-and-login-state` | 로그인 응답 token 저장, 로그아웃, Authorization header 구성을 연습합니다. |
| `04_user-data-and-conversation-history` | 사용자 정보와 사용자별 대화 이력을 백엔드 API로 조회하고 저장합니다. |
| `05_frontend-cache-and-performance` | 반복 조회 결과를 캐시하고, 캐시 적용 시 주의할 점을 학습합니다. |
| `06_service-log-and-integration-check` | 서비스 로그 조회, 통합 점검, 무료 배포 전 확인 사항을 정리합니다. |
| `10_labs` | 수업 중 따라 해 보는 종합 실습입니다. |
| `20_assignments` | 수업 후 제출 과제입니다. |

## 백엔드 연결 기준

실제 수업에서는 `01_supabase-ai-backend`의 Supabase 기반 FastAPI API와 연결합니다.

관련 백엔드 단원은 다음과 같습니다.

```text
C:\aidev\01_supabase-ai-backend\06_supabase-db-and-auth\03_fastapi-supabase-integration
C:\aidev\01_supabase-ai-backend\06_supabase-db-and-auth\04_supabase-auth-and-rls
C:\aidev\01_supabase-ai-backend\06_supabase-db-and-auth\05_conversation-history-and-service-logs
C:\aidev\01_supabase-ai-backend\07_backend-service-data-management
```

백엔드 실행 예시는 다음과 같습니다.

```powershell
cd C:\aidev\01_supabase-ai-backend\06_supabase-db-and-auth\03_fastapi-supabase-integration
..\..\.venv\Scripts\Activate.ps1
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

## 보조 샘플 백엔드

백엔드 인증 단원이 아직 준비되지 않았거나 화면 상태 흐름만 빠르게 확인할 때는 05 단원 안의 보조 샘플 백엔드를 사용할 수 있습니다.

```text
00_references\backend-auth-session-sample.py
```

실행 예시는 다음과 같습니다.

```powershell
cd C:\aidev\02_supabase-ai-frontend\05_state-session-and-data\00_references
..\..\.venv\Scripts\Activate.ps1
uvicorn backend-auth-session-sample:app --reload --host 127.0.0.1 --port 8000
```

샘플 백엔드는 Supabase를 대체하는 자료가 아닙니다. 로그인 상태, token 저장, Authorization header 흐름을 연습하기 위한 보조 자료입니다.

## 프론트엔드 실행 예시

```powershell
cd C:\aidev\02_supabase-ai-frontend
.\.venv\Scripts\Activate.ps1
streamlit run .\05_state-session-and-data\03_auth-token-and-login-state\02_login-token-state.py
```

## 04 단원과의 연결

04 단원에서는 챗봇 화면을 먼저 만들었습니다.

```text
질문 입력
-> mock 응답 또는 선택 Gemini 응답 표시
-> 간단한 대화 이력 미리보기
```

05 단원에서는 같은 화면을 실제 서비스 상태 관리 흐름으로 확장합니다.

```text
로그인 상태 관리
-> access token 저장
-> Authorization header로 백엔드 호출
-> 사용자별 대화 이력 조회
-> 새 메시지 저장
-> 서비스 로그 조회
-> 통합 점검
```

## 확인 기준

- 버튼을 누른 뒤 값이 화면 새로고침에도 유지되는가?
- 로그인 성공 후 token이 `st.session_state`에 저장되는가?
- 로그인 여부에 따라 화면이 다르게 보이는가?
- Authorization header가 보호된 API 호출에 포함되는가?
- 사용자별 대화 이력이 화면에 표시되는가?
- 새 메시지 저장 후 다시 조회했을 때 목록이 바뀌는가?
- 캐시 적용 전후의 화면 응답 차이를 설명할 수 있는가?
- 서비스 로그 화면에서 API 호출 결과와 오류 상태를 확인할 수 있는가?
- 배포 전 점검 항목을 기준으로 프론트엔드 준비 상태를 설명할 수 있는가?
