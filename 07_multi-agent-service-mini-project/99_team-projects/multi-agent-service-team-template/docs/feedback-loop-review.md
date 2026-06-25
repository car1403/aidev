# Feedback Loop Review

복구 실패 후 재시도와 개선 흐름을 정리합니다.

## 1. Feedback Loop 흐름

```text
복구 실행
-> Health Check
-> 성공 여부 판단
-> 실패 원인 기록
-> 재시도 또는 fallback
-> 최종 결과 보고
```

## 2. 재시도 기준

```text
최대 재시도 횟수:
재시도 간격:
재시도할 오류:
재시도하지 않을 오류:
fallback 전환 조건:
manual review 전환 조건:
```

## 3. 개선 기록

| 실행 | 실패 원인 | 수정 전략 | 결과 |
| --- | --- | --- | --- |
| 1차 | timeout | retry | 실패 |
| 2차 | timeout | fallback | 성공 |

## 4. 확인 기준

- 실패 결과가 로그에 남는가?
- 같은 실패를 무한 반복하지 않는가?
- fallback 또는 manual review 기준이 있는가?
- 최종 결과가 monitor에 표시되는가?
