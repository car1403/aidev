# 08 Observability and Ops Dashboard

Observability는 서비스 내부에서 무슨 일이 일어나는지 확인할 수 있게 만드는 운영 구조입니다.

## Logging, Tracing, Monitoring 차이

| 개념 | 의미 |
| --- | --- |
| Logging | 발생한 이벤트를 기록 |
| Tracing | 하나의 요청이 어떤 단계로 흘렀는지 추적 |
| Monitoring | 현재 상태와 지표를 관찰 |

## 운영 대시보드에 보여줄 정보

- 서비스 상태
- Health Check 결과
- 최근 이벤트 로그
- Agent 실행 이력
- 실패 이벤트 수
- Auto Healing 조치 결과

## Docker와 연결

```powershell
docker compose ps
docker compose logs backend
docker compose logs -f worker
```

## AWS와 연결

- CloudWatch Logs
- CloudWatch Dashboard
- CloudWatch Alarm
- AWS X-Ray 또는 OpenTelemetry
- SNS 알림
