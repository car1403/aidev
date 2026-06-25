# Backend

backend는 FastAPI 기반 API 서버입니다.

## 담당 역할

- `/health` Health Check 제공
- 장애 이벤트 입력 API 제공
- 복구 결과 조회 API 제공
- worker나 monitor가 사용할 데이터 제공

## 수정할 파일

```text
backend/main.py
```

## 구현할 때 확인할 것

- `/health`가 항상 빠르게 응답하는가?
- 장애 이벤트 입력 데이터가 명확한가?
- 응답 형식이 일정한가?
- 오류가 발생했을 때 상태 코드와 메시지가 명확한가?
- monitor나 frontend가 호출할 API 주소가 정리되어 있는가?
