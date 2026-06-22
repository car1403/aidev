# Deployment And Recovery Report

이 문서는 배포 및 장애 복구 보고서입니다.

## 1. Deployment Manifest

Docker Compose 또는 선택 확장 배포 매니페스트의 핵심 구조를 정리합니다.

| Service | Role | Port | Health Check | Secret Required |
| --- | --- | --- | --- | --- |
| backend | API, health check | 8000 | `/health` | yes/no |
| frontend | user UI | 8801 | - | yes/no |
| worker | auto healing worker | - | log check | yes/no |
| monitor | ops dashboard | 8802 | - | yes/no |

선택 확장으로 App Runner, ECS, Kubernetes를 검토하는 경우 아래 항목도 정리합니다.

```text
배포 후보:
이미지 저장소:
서비스 디스커버리 방식:
로드밸런싱 방식:
시크릿 관리 방식:
로그 수집 위치:
```

## 2. Service Discovery And Load Balancing

```text
서비스 디스커버리 방식:
로드밸런싱 방식:
시크릿 관리 방식:
```

초보자 프로젝트에서는 Docker Compose 기준으로 먼저 작성하고, AWS로 확장한다면 App Runner 또는 ECS 기준을 추가합니다.

| 항목 | Docker Compose | App Runner | ECS |
| --- | --- | --- | --- |
| 서비스 실행 | compose service | App Runner service | ECS service/task |
| 이미지 | local build | ECR image | ECR image |
| 환경변수 | `.env` | service env/secrets | task definition env/secrets |
| Health Check | `/health` | health check path | target group/ECS health check |
| Logs | compose logs | CloudWatch Logs | CloudWatch Logs |

## 3. Failure Detection Matrix

| Failure Type | Detection Metric | Example | Severity |
| --- | --- | --- | --- |
| Network Timeout | timeout count | API 응답 지연 | |
| Connection Lost | connection error | DB 연결 끊김 | |
| DB Exhaustion | slow query, pool usage | 연결 풀 고갈 | |
| API 5xx | status code | 외부 API 장애 | |
| Rate Limit | 429 count | API 호출 제한 | |
| LLM Hallucination | validation mismatch | Tool 결과와 답변 불일치 | |
| Token Limit | token error | 컨텍스트 초과 | |
| Prompt Injection | policy violation | 시스템 지시 무시 유도 | |

감지 메트릭은 "장애가 난 것 같다"가 아니라 숫자 또는 명확한 조건으로 작성합니다.

```text
예:
- 5분 동안 timeout 3회 이상
- /health 3회 연속 실패
- API 5xx 비율 20% 초과
- LLM 응답과 Tool 결과 불일치
- Prompt Injection 키워드 또는 정책 위반 탐지
```

## 4. Auto Recovery Strategy

| Failure Type | Auto Recovery | Manual Escalation | Expected Recovery Without Manual Intervention |
| --- | --- | --- | --- |
| Network Timeout | retry | repeated timeout | |
| Connection Lost | reconnect | reconnect failed | |
| API 5xx | fallback API/model | repeated 5xx | |
| Rate Limit | backoff, cache fallback | limit 지속 | |
| LLM Hallucination | validation retry | unsafe output | |

복구 흐름은 아래 전략 중 프로젝트에 필요한 것을 선택합니다.

```text
Retry:
Restart:
Reconnect:
Fallback API:
Fallback model:
Cache fallback:
Human escalation:
```

## 5. Recovery Scripts Or Commands

```text
재시작:
재연결:
대체 모델 호출:
캐시 fallback:
```

## 6. Recovery Result

| Scenario | Success | Recovery Time | Manual Intervention | Notes |
| --- | --- | --- | --- | --- |
| | | | | |

시나리오별로 수동 개입 없이 복구되었는지 표시합니다.

## 7. Summary

```text
자동 복구 가능한 시나리오 수:
전체 시나리오 수:
자동 복구 비율:
```
