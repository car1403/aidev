# 06_ch6_feedback-loop-result-review

Agent 실행 결과를 검증하고, 품질이 낮거나 실패한 경우 재시도하는 Feedback Loop 구조를 학습합니다.

## 학습 목표

- Agent 결과 검증이 왜 필요한지 이해합니다.
- 응답 품질 점수를 기준으로 retry, revise, escalate를 결정할 수 있습니다.
- Feedback Loop를 무한 반복하지 않도록 최대 재시도 횟수를 설계할 수 있습니다.
- 결과 검증 정보를 운영 로그와 Observability 구조로 연결할 수 있습니다.

## 기본 흐름

```text
Agent 실행
-> 결과 검증
-> 품질 기준 통과
   -> 최종 응답
-> 품질 기준 실패
   -> 피드백 생성
   -> 재시도
   -> 다시 검증
-> 반복 실패
   -> 사람 검토 또는 fallback
```

## 실행 예제

```powershell
cd C:\aidev\06_multi-agent-service-ops\01_multi-agent-collaboration
python .\06_ch6_feedback-loop-result-review\01_feedback_loop_result_review.py
```

## 운영 관점

Feedback Loop는 품질 개선에 유용하지만, 운영 환경에서는 반드시 제한이 필요합니다.

```text
최대 재시도 횟수
재시도 비용
응답 지연 시간
실패 시 fallback
검증 로그
```

이 정보는 05 단원의 Observability, 04 단원의 Auto Healing과 연결됩니다.
