# Backend Service

`backend_service`는 `99_final-frontend-project`에서 실제 서비스 연결과 배포 실습을 할 때 사용하는 FastAPI 백엔드입니다.

프론트엔드가 호출하는 API 주소와 응답 구조는 `backend_mock`과 최대한 동일하게 유지합니다. 그래서 Streamlit 앱은 `API_BASE_URL`만 바꾸면 mock backend에서 service backend로 전환할 수 있습니다.

## 언제 사용하나요?

| 구분 | 사용 시점 |
| --- | --- |
| `backend_mock` | 프론트 화면, 로그인 상태, 챗봇 UI, 대화 기록 UI를 빠르게 만들 때 |
| `backend_service` | Supabase Auth, Supabase DB, Gemini API, Upstash Redis, Render 배포까지 연결할 때 |

수업 시간이 부족하면 `backend_mock`만 필수로 진행하고, `backend_service`는 선택/심화 또는 참고 자료로 다룹니다.

## 폴더 구조

```text
backend_service
├─ README.md
├─ requirements.txt
├─ .env.example
├─ schema.sql
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
│     ├─ cache_service.py
│     ├─ chat_service.py
│     ├─ gemini_service.py
│     ├─ log_service.py
│     └─ supabase_service.py
└─ tests
   └─ test_service_app_routes.py
```

## 준비 순서

1. Supabase 프로젝트를 만들고 `schema.sql`을 SQL Editor에서 실행합니다.
2. Supabase Auth에서 이메일 가입 방식을 확인합니다.
3. Gemini API key를 준비합니다.
4. 선택 사항으로 Upstash Redis REST URL/TOKEN을 준비합니다.
5. `.env.example`을 참고해 `.env`를 만듭니다.

## 실행 방법

```powershell
cd C:\aidev\03_supabase-ai-frontend\99_final-frontend-project\backend_service
C:\aidev\03_supabase-ai-frontend\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
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
| POST | `/auth/signup` | Supabase Auth 회원가입, 사용자 정보 반환 |
| POST | `/auth/signin` | Supabase Auth 로그인과 access token 발급 |
| POST | `/auth/signout` | 현재 token 로그아웃 |
| GET | `/me` | 현재 로그인 사용자 정보 조회 |
| POST | `/chat` | Gemini 응답 생성, 선택형 Redis 캐시, Supabase 대화 기록 저장 |
| GET | `/conversations` | 현재 사용자 대화 기록 조회 |
| GET | `/service-logs` | 현재 사용자 서비스 로그 조회 |

## 이메일 인증 주의

Supabase Auth에서 `Confirm email`이 켜져 있으면 회원가입 직후 바로 로그인되지 않을 수 있습니다.

이 경우 수강생은 다음 순서로 진행합니다.

1. `/auth/signup`으로 회원가입합니다.
2. 이메일함에서 인증 메일을 확인합니다.
3. 인증 링크를 누른 뒤 `/auth/signin`으로 로그인합니다.

수업 중 인증 메일 대기가 길어지면 Supabase Auth 설정에서 이메일 인증을 잠시 끄고 진행할 수 있습니다.

## 테스트

이 테스트는 Supabase/Gemini를 실제 호출하지 않고, FastAPI route가 로드되는지만 확인합니다.

```powershell
cd C:\aidev\03_supabase-ai-frontend\99_final-frontend-project\backend_service
C:\aidev\03_supabase-ai-frontend\.venv\Scripts\Activate.ps1
pytest tests -q
```

## 배포 참고

Render 배포 시 시작 명령은 다음과 같습니다.

```text
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

환경변수는 Render의 Environment 메뉴에 등록합니다. `SUPABASE_SERVICE_ROLE_KEY`, `GEMINI_API_KEY`, `UPSTASH_REDIS_REST_TOKEN`은 프론트엔드나 GitHub에 올리지 않습니다.
