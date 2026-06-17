# Feedback Loop Review

복구 결과 검증과 재시도 Feedback Loop를 설계합니다.

## 1. 기본 흐름

```text
장애 감지
-> 복구 전략 선택
-> 복구 실행
-> 결과 검증
-> 성공이면 종료
-> 실패하면 피드백 생성
-> 재시도
-> 반복 실패 시 fallback 또는 사람 검토
```

## 2. 검증 기준

```text
복구 성공 기준:
복구 실패 기준:
검증 Agent:
검증 Tool:
최대 재시도 횟수:
재시도 중단 조건:
```

## 3. Feedback 항목

```text
실패 원인:
보강할 조치:
다음 재시도 전략:
fallback 조건:
운영자 알림 조건:
```

## 4. 로그 항목

```text
request_id
attempt_count
recovery_action
review_score
review_result
feedback
final_status
```
