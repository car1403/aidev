# 01. Notes API With Supabase

`learning_notes` CRUD 흐름을 실제 프로젝트 구조처럼 나누어 보는 예제입니다.

본문의 `02_supabase-table-and-crud`, `03_fastapi-supabase-integration`을 구조화한 버전입니다.

## 이 예제에서 배우는 것

- FastAPI 코드를 `main`, `router`, `schema`, `service`, `config`로 나누는 방법
- Supabase 테이블 CRUD를 service 함수로 분리하는 방법
- 본문 실습 테이블과 섞이지 않도록 `ex90_notes` 테이블을 사용하는 방법

## 1. Supabase 테이블 만들기

Supabase SQL Editor에서 이 폴더의 `schema.sql`을 실행합니다.

```text
C:\aidev\02_supabase-ai-backend\03_supabase-db-and-auth\90_structured-fastapi-examples\01_notes-api-with-supabase\schema.sql
```

## 2. 환경변수 준비

`.env.example`을 참고해 같은 폴더에 `.env`를 만듭니다.

```text
SUPABASE_URL=...
SUPABASE_SERVICE_ROLE_KEY=...
```

## 3. 서버 실행

```powershell
cd C:\aidev\02_supabase-ai-backend\03_supabase-db-and-auth\90_structured-fastapi-examples\01_notes-api-with-supabase
..\..\..\.venv\Scripts\Activate.ps1
uvicorn app.main:app --reload --host 127.0.0.1 --port 8011
```

Swagger UI:

```text
http://127.0.0.1:8011/docs
```

## 확인할 endpoint

| Method | URL | 설명 |
|---|---|---|
| GET | `/health` | 서버와 환경변수 상태 확인 |
| GET | `/notes` | 노트 목록 조회 |
| POST | `/notes` | 노트 생성 |
| GET | `/notes/{note_id}` | 노트 1개 조회 |
| PUT | `/notes/{note_id}` | 노트 수정 |
| DELETE | `/notes/{note_id}` | 노트 삭제 |

## 테스트

```powershell
python -m pytest -s
```

테스트는 외부 Supabase를 호출하지 않고 앱의 기본 라우트가 준비되었는지만 확인합니다.
