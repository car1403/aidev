# Worker

worker는 장애 이벤트를 처리하고 Auto Healing 흐름을 실행하는 백그라운드 서비스입니다.

## 담당 역할

- 장애 유형 분류
- 복구 전략 선택
- Retry, Restart, Reconnect, Fallback 흐름 처리
- 복구 결과 검증 요청
- 실행 로그 출력

## 수정할 파일

```text
worker/main.py
```

## 구현할 때 확인할 것

- 장애 유형별 처리 기준이 명확한가?
- 무한 재시도를 하지 않는가?
- 실패 결과도 로그에 남기는가?
- 위험한 작업은 Guardrail 기준에 따라 차단하는가?
- monitor에서 확인할 수 있는 이벤트를 남기는가?
