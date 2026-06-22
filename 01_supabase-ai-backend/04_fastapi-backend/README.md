# 04_fastapi-backend

Python으로 웹 API 서버를 만드는 FastAPI 백엔드 개발 단원입니다.

`01_python-basic`과 `02_python-advanced`에서 익힌 Python 문법, 함수, 모듈, 객체지향 개념을 실제 API 서버 개발로 연결합니다.

## 학습 목표

- FastAPI 프로젝트를 만들고 실행할 수 있다.
- HTTP Method, Path Parameter, Query Parameter, Request Body를 이해할 수 있다.
- Pydantic 모델로 요청 데이터를 검증할 수 있다.
- Response Model과 표준 응답 구조를 설계할 수 있다.
- FastAPI의 `Depends`를 사용해 공통 로직을 분리할 수 있다.
- 비동기 엔드포인트와 외부 API 호출 구조를 이해할 수 있다.
- HTTPException, 전역 Exception Handler, Middleware, CORS, Swagger UI, 간단한 테스트 흐름을 익힐 수 있다.
- 메모리 저장소 기반 CRUD API를 만들고 이후 Supabase 저장 구조로 확장할 준비를 할 수 있다.

## 학습 순서

```text
00_references
-> 01_ch1_fastapi-project-setup
-> 02_ch2_routing-and-request
-> 03_ch3_pydantic-and-response
-> 04_ch4_async-and-external-api
-> 05_ch5_error-handling-and-testing
-> 10_labs
-> 20_assignments
```

## 실행 기본 명령

먼저 과정 루트에서 가상환경을 활성화합니다.

```powershell
cd C:\aidev\01_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

FastAPI 서버는 `app = FastAPI()`가 있는 파일을 기준으로 실행합니다.

```powershell
uvicorn main:app --reload
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## 예제 실행 방법

각 챕터의 예제 파일명은 학습 순서를 보여주기 위해 번호와 하이픈을 포함할 수 있습니다. 실제 서버 실행에서는 import가 쉬운 `main.py`, `solution.py`, `starter.py` 같은 파일명을 사용하는 것을 권장합니다.

### Lab 01 실행

```powershell
cd C:\aidev\01_supabase-ai-backend\04_fastapi-backend\10_labs\lab01_hello-fastapi
uvicorn solution:app --reload
```

확인:

```text
http://127.0.0.1:8000/health
http://127.0.0.1:8000/docs
```

PowerShell에서 직접 확인:

```powershell
Invoke-RestMethod http://127.0.0.1:8000/health
```

기대 결과:

```json
{
 "status": "ok"
}
```

### Path/Query Parameter 확인

```powershell
cd C:\aidev\01_supabase-ai-backend\04_fastapi-backend\10_labs\lab02_path-query-params
uvicorn solution:app --reload
```

확인:

```powershell
Invoke-RestMethod http://127.0.0.1:8000/users/1
Invoke-RestMethod "http://127.0.0.1:8000/search?keyword=python&limit=5"
```

### Request Body 확인

```powershell
cd C:\aidev\01_supabase-ai-backend\04_fastapi-backend\10_labs\lab03_request-body-validation
uvicorn solution:app --reload
```

Swagger UI에서 `POST /users`를 열고 다음 JSON을 입력합니다.

```json
{
 "name": "Alice",
 "email": "alice@example.com",
 "age": 25
}
```

확인할 것:

- 정상 요청은 200 응답을 반환한다.
- 필드를 누락하거나 타입을 틀리게 보내면 422 오류가 발생한다.

### Depends, Exception Handler, Middleware 확인

```powershell
cd C:\aidev\01_supabase-ai-backend\04_fastapi-backend\05_ch5_error-handling-and-testing
uvicorn dependency_injection_depends:app --reload
```

확인:

```powershell
Invoke-RestMethod "http://127.0.0.1:8000/me?token=student-token"
Invoke-RestMethod "http://127.0.0.1:8000/admin?token=student-token"
```

`Depends`는 여러 API에서 반복되는 인증, 설정 확인, DB 연결 준비 같은 공통 작업을 함수로 분리할 때 사용합니다.

전역 예외 처리 예제:

```powershell
uvicorn global_exception_handler:app --reload
```

확인:

```powershell
Invoke-RestMethod http://127.0.0.1:8000/items/999
```

Middleware와 CORS 예제:

```powershell
uvicorn 02_middleware-cors:app --reload
```

확인할 것:

- 모든 요청에 공통 처리를 끼워 넣는 구조가 Middleware입니다.
- 브라우저에서 다른 주소의 API를 호출할 때 CORS 설정이 필요합니다.

### Response Model 확인

```powershell
cd C:\aidev\01_supabase-ai-backend\04_fastapi-backend\10_labs\lab04_response-model
uvicorn solution:app --reload
```

확인:

```powershell
Invoke-RestMethod http://127.0.0.1:8000/users/1
```

확인할 것:

- 응답에 `id`, `name`만 포함된다.
- 내부 데이터의 `password`는 응답에서 제외된다.

### Async API 확인

```powershell
cd C:\aidev\01_supabase-ai-backend\04_fastapi-backend\10_labs\lab05_async-external-api
uvicorn solution:app --reload
```

확인:

```powershell
Invoke-RestMethod "http://127.0.0.1:8000/mock-external?keyword=fastapi"
```

### In Memory CRUD API 확인

```powershell
cd C:\aidev\01_supabase-ai-backend\04_fastapi-backend\10_labs\lab06_in-memory-crud-api
uvicorn solution:app --reload
```

Swagger UI에서 아래 순서로 확인합니다.

```text
GET /memos
POST /memos
GET /memos/{memo_id}
PUT /memos/{memo_id}
DELETE /memos/{memo_id}
```

이 실습은 Supabase 연결 전 단계입니다. 서버 메모리에 데이터를 저장하므로 서버를 재시작하면 데이터가 초기화됩니다.

### Mini API Server 확인

```powershell
cd C:\aidev\01_supabase-ai-backend\04_fastapi-backend\10_labs\lab99_mini-api-server
uvicorn solution:app --reload
```

확인할 것:

```text
GET /health
GET /notes
POST /notes
GET /notes/{note_id}
```

이 실습은 FastAPI 단원의 마무리용 작은 API 서버입니다.

## 실행 검증 체크리스트

- [ ] 가상환경이 활성화되어 있다.
- [ ] `uvicorn` 실행 시 오류가 없다.
- [ ] 브라우저에서 `/docs`가 열린다.
- [ ] `/health` 또는 실습 API가 정상 응답한다.
- [ ] Swagger UI에서 요청/응답을 확인했다.
- [ ] 잘못된 요청을 보냈을 때 422 또는 404 등 오류 응답을 확인했다.

## 자주 발생하는 문제

### `Error loading ASGI app`

실행한 파일명과 앱 변수명을 확인합니다.

```powershell
uvicorn solution:app --reload
```

위 명령은 `solution.py` 파일 안에 `app = FastAPI()`가 있어야 동작합니다.

### 포트 8000이 이미 사용 중인 경우

기존 서버를 `Ctrl + C`로 종료하거나 다른 포트를 사용합니다.

```powershell
uvicorn solution:app --reload --port 8001
```

### 422 오류가 발생하는 경우

Pydantic 모델이 요구하는 JSON 형식과 실제 요청이 맞지 않는 상태입니다. Swagger UI의 Request body 예시와 모델 필드를 비교합니다.

## 다음 단원 연결

이 단원 이후 `06_supabase-db-and-auth`에서 Supabase 테이블, Auth, RLS, 대화 이력, 서비스 로그 저장 구조를 FastAPI에 연결합니다.

Redis는 `06_supabase-db-and-auth`에서 Upstash Redis를 사용해 캐시와 TTL 개념을 먼저 다룹니다. Docker 기반 Redis 운영과 로컬 PostgreSQL 운영은 `C:\aidev\06_multi-agent-service-ops`에서 본격적으로 다룹니다.

