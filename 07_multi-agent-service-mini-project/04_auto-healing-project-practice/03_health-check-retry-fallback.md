# 03 Health Check Retry Fallback

```text
Health Check
-> Retry
-> Restart
-> Fallback
-> Escalate
```

각 단계에서 어떤 로그를 남길지 정리합니다.

## Feedback Loop 추가 설계

복구 조치가 끝난 뒤 바로 성공으로 판단하지 않고, 결과를 검증한 뒤 필요하면 다시 시도합니다.

```text
Health Check
-> Retry
-> Restart
-> Result Review
-> Feedback
-> Retry Again
-> Fallback
-> Escalate
```

## 작성할 것

```text
복구 성공 기준:
복구 실패 기준:
검증 Agent:
최대 재시도 횟수:
재시도 중단 조건:
fallback 조건:
사람 검토로 넘길 조건:
로그에 남길 정보:
```

## 확인 질문

- 복구 명령이 실행되었다는 것과 실제 복구가 되었다는 것은 어떻게 다른가?
- 재시도는 몇 번까지 허용할 것인가?
- 반복 실패 시 운영자는 어떤 정보를 받아야 하는가?
