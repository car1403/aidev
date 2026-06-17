# 01_ch1_failure-scenarios

서비스 장애 유형을 분류하는 방법을 학습합니다.

## 장애 유형 예시

| 장애 유형 | 설명 | 대응 예시 |
| --- | --- | --- |
| `unhealthy` | Health Check 실패 | 재시도 후 재시작 |
| `timeout` | 응답 지연 | 재시도 또는 timeout 조정 |
| `dependency_error` | 외부 API/DB 연결 실패 | 대체 경로 또는 알림 |
| `permission_error` | 권한 부족 | Secret/IAM/환경 변수 확인 |
| `unknown` | 원인 불명 | 로그 수집 후 수동 확인 |

## 실행

```powershell
cd C:\aidev\06_multi-agent-service-ops\04_auto-healing-workflow
..\.venv\Scripts\Activate.ps1
python .\01_ch1_failure-scenarios\01_failure-scenario-classifier.py
```
