# Backend Mock

`backend_mock`은 `99_final-frontend-project`에서 프론트엔드 UX 실습을 안정적으로 진행하기 위한 제공용 mock backend입니다.

이 backend는 Supabase Auth, Gemini API, Upstash Redis를 사용하지 않습니다. 기본 저장소는 메모리이며, 서버를 재시작하면 회원, 대화 기록, 서비스 로그가 초기화됩니다.

## 언제 사용하나요?

수강생이 Streamlit 화면을 만들 때는 먼저 `backend_mock`을 사용합니다.

- 회원가입/로그인 화면 만들기
- `access_token`을 `st.session_state`에 저장하기
- `Authorization: Bearer ...` header 보내기
- 챗봇 UI와 대화 기록 UI 만들기
- 서비스 로그를 표로 표시하기

실제 Supabase/Gemini/Redis 연결은 같은 프로젝트의 `backend_service`에서 선택/심화로 진행합니다.

## 폴더 구조

```text
backend_mock
├─ README.md
├─ requirements.txt
├─ app
│  ├─ main.py
│  ├─ core
│  │  ├─ config.py
│  │  └─ security.py
│  ├─ routers
│  │  ├─ auth_router.py
│  │  ├─ chat_router.py
│  │  └─ log_router.py
│  ├─ schemas
│  │  ├─ auth_schema.py
│  │  ├─ chat_schema.py
│  │  └─ log_schema.py
│  └─ services
│     ├─ auth_service.py
│     ├─ chat_service.py
│     ├─ log_service.py
│     └─ memory_store.py
└─ tests
   └─ test_backend_api.py
```

## 실행 방법

```powershell
cd C:\aidev\03_supabase-ai-frontend\99_final-frontend-project\backend_mock
C:\aidev\03_supabase-ai-frontend\.venv\Scripts\Activate.ps1
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## 제공 API

| Method | URL | 설명 |
| --- | --- | --- |
| GET | `/health` | backend 실행 상태 확인 |
| POST | `/auth/signup` | 수업용 회원가입 |
| POST | `/auth/signin` | 수업용 로그인과 mock access token 발급 |
| POST | `/auth/signout` | 현재 token 로그아웃 |
| GET | `/me` | 현재 로그인 사용자 정보 조회 |
| POST | `/chat` | mock AI 답변 생성과 대화 기록 저장 |
| GET | `/conversations` | 현재 사용자 대화 기록 조회 |
| GET | `/service-logs` | 현재 사용자 서비스 로그 조회 |

## 테스트

```powershell
cd C:\aidev\03_supabase-ai-frontend\99_final-frontend-project\backend_mock
C:\aidev\03_supabase-ai-frontend\.venv\Scripts\Activate.ps1
pytest tests -q
```
