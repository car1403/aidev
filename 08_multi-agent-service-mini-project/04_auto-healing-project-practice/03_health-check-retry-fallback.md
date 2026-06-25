# 03. Health Check Retry Fallback

Health Check, Retry, Fallback은 Auto Healing 프로젝트에서 가장 기본이 되는 운영 흐름입니다.

## Health Check

Health Check는 서비스가 정상인지 확인하는 기준입니다.

예시:

```text
GET /health
-> {"status": "ok"}
```

프로젝트에서는 최소한 backend에 `/health`가 있어야 합니다.

## Retry

Retry는 실패한 작업을 다시 시도하는 전략입니다.

설계할 항목:

```text
최대 재시도 횟수
재시도 간격
재시도할 오류 유형
재시도하지 않을 오류 유형
재시도 실패 시 다음 전략
```

예시:

```text
timeout 발생
-> 1초 대기
-> 1차 retry
-> 실패
-> 2초 대기
-> 2차 retry
-> 실패
-> fallback 전환
```

## Fallback

Fallback은 원래 경로가 실패했을 때 대체 경로를 사용하는 전략입니다.

예시:

- 실시간 LLM 호출 실패 시 캐시된 안내 문구 반환
- 외부 API 실패 시 기본 데이터 사용
- worker 자동 복구 실패 시 manual review 상태로 전환
- 정책 위반 가능성이 있으면 실행하지 않고 안전 응답 반환

## 실습 체크리스트

- [ ] `/health` 확인 기준이 있다.
- [ ] Retry 횟수와 간격이 정해져 있다.
- [ ] Fallback 조건이 정해져 있다.
- [ ] 실패한 복구 시도가 로그에 남는다.
- [ ] 복구 성공 여부가 monitor에 표시된다.
- [ ] 위험한 작업은 Guardrail에서 차단된다.
