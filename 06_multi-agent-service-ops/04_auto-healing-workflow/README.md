# 04 Auto Healing Workflow

이 단원은 장애가 발생했을 때 AI 서비스가 스스로 상태를 진단하고, 재시도·재시작·대체 경로 같은 복구 절차를 수행한 뒤 결과를 검증하는 Auto Healing 워크플로우를 학습합니다.

Auto Healing은 단순히 `restart` 명령을 실행하는 것이 아닙니다. 장애 유형을 분류하고, 안전한 복구 조치를 선택하고, 조치 결과를 확인하고, 실패하면 다음 대응 경로로 넘어가는 운영 흐름입니다.

## 이 단원의 목표

- 서비스 장애 유형을 분류할 수 있다.
- Health Check 결과를 바탕으로 장애 여부를 판단할 수 있다.
- Retry, Restart, Fallback 같은 복구 전략을 구분할 수 있다.
- Auto Healing 파이프라인을 단계별로 설계할 수 있다.
- 복구 결과를 검증하고 운영 로그로 남길 수 있다.
- Docker Compose와 AWS 운영 환경에서 Auto Healing이 어떻게 확장되는지 이해한다.

## 학습 순서

```text
01_ch1_failure-scenarios
-> 02_ch2_health-check-retry-restart
-> 03_ch3_recovery-pipeline
-> 04_ch4_recovery-result-validation
-> 10_labs
-> 20_assignments
```

## 환경 준비

04 단원 예제는 외부 API 없이 실행됩니다.

```powershell
cd C:\aidev\06_multi-agent-service-ops
.\.venv\Scripts\Activate.ps1
cd .\04_auto-healing-workflow
```

## Auto Healing 기본 흐름

```text
서비스 상태 확인
-> 장애 유형 분류
-> 복구 전략 선택
-> 복구 조치 실행
-> 결과 검증
-> 로그 기록
```

## Docker와 연결

Docker Compose 환경에서는 다음 명령과 개념으로 이어집니다.

```text
docker compose ps
docker compose logs backend
docker compose restart backend
healthcheck
restart policy
```

처음에는 Python Mock 예제로 흐름을 이해하고, 이후 99 미니 프로젝트에서 실제 Docker Compose 서비스와 연결할 수 있습니다.

## AWS와 연결

AWS에서는 Auto Healing 개념이 다음 기능으로 확장됩니다.

| Auto Healing 개념 | AWS 연결 예시 |
| --- | --- |
| Health Check | ALB Target Health Check, ECS Health Check |
| Restart | ECS Service가 Task 재시작 |
| Logs | CloudWatch Logs |
| Alarm | CloudWatch Alarm |
| Fallback | 다른 Target Group, 대체 서비스, 수동 승인 |

## 실행 예제

```powershell
python .\01_ch1_failure-scenarios\01_failure-scenario-classifier.py
python .\02_ch2_health-check-retry-restart\01_health-check-retry-restart.py
python .\03_ch3_recovery-pipeline\01_auto-healing-pipeline.py
python .\04_ch4_recovery-result-validation\01_recovery-result-validation.py
```
