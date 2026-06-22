# FastAPI 기본 프로젝트 구조

처음에는 `main.py` 하나로 시작합니다.

```text
project
└─ main.py
```

하지만 기능이 늘어나면 파일을 역할별로 나누는 것이 좋습니다.

```text
app
├─ main.py
├─ routers
│  └─ memo_router.py
├─ schemas
│  └─ memo_schema.py
├─ services
│  └─ memo_service.py
└─ tests
   └─ test_memo_api.py
```

## 폴더 역할

```text
main.py:
  FastAPI 앱을 만들고 서버의 시작점을 담당합니다.

routers:
  /memos, /users 같은 API 주소를 기능별로 나누어 둡니다.

schemas:
  Pydantic 모델을 둡니다. 요청 데이터와 응답 데이터의 모양을 정의합니다.

services:
  실제 처리 로직을 둡니다. 예를 들어 메모 생성, 질문 검증, 외부 API 호출 같은 작업입니다.

tests:
  API가 예상대로 동작하는지 확인하는 테스트 코드를 둡니다.
```

## 이 단원에서는 어디까지 하나요?

이번 첫 단원에서는 `main.py` 하나로 시작합니다.

```text
main.py
-> app = FastAPI()
-> @app.get("/")
-> @app.get("/health")
```

라우터, 스키마, 서비스 분리는 이후 Request Body, Pydantic, CRUD API를 배우면서 천천히 확장합니다.
