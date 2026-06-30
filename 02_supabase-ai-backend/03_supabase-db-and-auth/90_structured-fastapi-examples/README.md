# 90. Structured FastAPI Examples

이 폴더는 `03_supabase-db-and-auth`의 `00`~`06`을 마친 뒤 참고하는 구조화 예제 모음입니다.

본문에서는 개념과 최소 실행 흐름을 작게 배웠습니다. 이 폴더에서는 같은 내용을 실제 프로젝트에 가까운 FastAPI 구조로 나누어 봅니다.

처음 학습할 때 반드시 모두 실행해야 하는 필수 실습은 아닙니다. 나중에 프로젝트를 만들 때 “폴더를 어떻게 나누면 좋을까?”를 다시 확인하는 참고 자료로 사용합니다.

## 예제 목록

| 순서 | 예제 | 연결 내용 |
|---|---|---|
| 1 | `01_notes-api-with-supabase` | Supabase 테이블 CRUD를 FastAPI 구조로 분리 |
| 2 | `02_simple-chat-log-api` | 질문/답변 로그를 Supabase에 저장 |
| 3 | `03_cached-ai-answer-api` | Upstash Redis TTL 캐시 |
| 4 | `04_auth-jwt-profile-api` | Supabase Auth, JWT, Bearer token, RLS SQL |
| 5 | `05_integrated-ai-backend-api` | Auth, DB 저장, Redis 캐시, Gemini 선택 호출을 하나로 연결 |

## 공통 구조

각 예제는 최대한 같은 구조를 사용합니다.

```text
example-name
├─ README.md
├─ .env.example
├─ schema.sql
├─ app
│  ├─ main.py
│  ├─ core
│  ├─ routers
│  ├─ schemas
│  └─ services
└─ tests
```

`schema.sql`이 없는 예제는 Supabase 테이블 없이 Redis만 사용합니다.

## 테이블 이름 기준

90번 예제는 본문 실습 데이터와 섞이지 않도록 `ex90_` prefix를 사용합니다.

```text
ex90_notes
ex90_simple_chat_logs
ex90_profiles
ex90_user_chat_logs
```

## 실행 전 공통 준비

```powershell
cd C:\aidev\02_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

각 예제 폴더의 `.env.example`을 참고해 `.env`를 만듭니다. 실제 key 값은 GitHub, README, 제출 문서에 올리지 않습니다.

## 학습 기준

이 폴더에서 가장 중요한 것은 기능의 양이 아니라 코드의 위치입니다.

```text
main.py:
  FastAPI 앱 생성과 router 연결

routers:
  URL, HTTP Method, status code

schemas:
  요청/응답 Pydantic 모델

services:
  Supabase, Redis, Auth 같은 외부 서비스 호출

core:
  환경변수와 공통 설정
```

처음에는 `01`부터 순서대로 보는 것을 권장합니다.

`05_integrated-ai-backend-api`는 기본값으로 mock 답변을 사용합니다. `.env`에서 `USE_GEMINI=true`로 바꾸면 Gemini SDK 호출 흐름까지 확인할 수 있습니다.
