# 02. Auto Healing Scenario

Auto Healing은 장애가 발생했을 때 시스템이 스스로 감지하고, 원인을 분류하고, 복구 전략을 선택하고, 결과를 검증하는 흐름입니다.

07에서는 실제 운영 환경을 완벽히 재현하기보다, 장애 대응 흐름을 작은 서비스로 구현하고 문서화하는 것을 목표로 합니다.

## 장애 시나리오 예시

| 장애 유형 | 감지 기준 | 복구 전략 | 검증 방법 |
| --- | --- | --- | --- |
| API 5xx | backend 응답 코드가 500번대 | 재시도, fallback 응답 | `/health` 재확인 |
| Timeout | 응답 시간이 기준보다 김 | 재시도, timeout 값 조정 | 재요청 결과 확인 |
| Rate Limit | 외부 API가 429 응답 | 대기 후 재시도, 캐시 사용 | 성공 응답 여부 확인 |
| LLM 응답 오류 | 빈 응답, 형식 오류 | 프롬프트 조정, 대체 모델 호출 | 응답 형식 재검증 |
| Prompt Injection | 위험 지시문 감지 | 요청 차단, 감사 로그 기록 | 정책 위반 로그 확인 |
| Worker 실패 | worker 로그 오류, 작업 중단 | 재시작, 큐 재처리 | worker 상태 확인 |

## 기본 Auto Healing 흐름

```text
1. 장애 이벤트 수집
2. 장애 유형 분류
3. 영향 범위 판단
4. 복구 전략 선택
5. 복구 실행 또는 시뮬레이션
6. Health Check 재확인
7. 성공/실패 기록
8. 실패 시 Feedback Loop 수행
```

## Agent별 역할 예시

| Agent | 맡는 일 |
| --- | --- |
| Supervisor | 전체 흐름을 조율하고 다음 Agent를 선택합니다. |
| Diagnosis | 장애 원인과 유형을 분석합니다. |
| Recovery | 복구 전략을 선택합니다. |
| Validation | 복구 결과를 검증합니다. |
| Reporter | 최종 결과를 정리합니다. |
| Guardrail | 위험한 복구 작업과 정책 위반 가능성을 확인합니다. |

## Feedback Loop 기준

복구 실패 시에는 같은 작업을 무한 반복하지 않습니다. 아래 기준이 필요합니다.

```text
최대 재시도 횟수
재시도 간격
fallback 조건
수동 확인 전환 조건
실패 로그 기록 기준
```

예시:

```text
timeout 장애 발생
-> retry 2회
-> 실패 시 fallback 응답 사용
-> health check 실패 시 manual_review 상태로 전환
-> monitor에 실패 이벤트 표시
```
