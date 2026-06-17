# FastAPI DB 연동 패턴

## 기본 분리

```text
main.py
database.py
repositories
services
schemas
```

## 역할

- `database.py`: DB 연결 생성
- `schemas`: 요청/응답 모델
- `repositories`: SQL 실행
- `services`: 비즈니스 로직
- `main.py`: API 라우팅

초급 단계에서는 `main.py` 안에 작성해도 되지만, 프로젝트에서는 역할별로 분리합니다.

