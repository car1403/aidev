# 05 Observability and Ops Dashboard

이 단원은 AI 서비스와 Multi-Agent 시스템의 실행 상태를 관찰하고 운영 대시보드로 확인하는 방법을 학습합니다.

Observability는 단순히 로그를 출력하는 것이 아닙니다. 서비스가 어떤 요청을 받았고, 어떤 Agent가 실행되었고, 어떤 Tool이 호출되었고, 어디서 실패했는지 추적할 수 있게 만드는 운영 역량입니다.

## 이 단원의 목표

- 서비스 로그와 이벤트 이력을 구조화해서 남길 수 있다.
- Agent 실행 흐름을 Trace 단위로 추적할 수 있다.
- LangSmith 같은 실행 추적 도구에서 trace/run/span을 어떻게 보는지 이해한다.
- Streamlit으로 간단한 운영 대시보드를 만들 수 있다.
- 실행 상태를 `pending`, `running`, `success`, `failed`로 관리할 수 있다.
- Docker Compose와 AWS 운영 환경에서 로그와 모니터링이 어떻게 연결되는지 이해한다.

## 학습 순서

```text
01_ch1_logging-and-event-history
-> 02_ch2_tracing-and-monitoring
-> 03_ch3_ops-dashboard-streamlit
-> 04_ch4_execution-status-management
-> 10_labs
-> 20_assignments
```

## 환경 준비

```powershell
cd C:\aidev\06_multi-agent-service-ops
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
cd.\05_observability-and-ops-dashboard
```

## 관찰해야 할 정보

운영 환경에서는 최소한 아래 정보를 남기는 것이 좋습니다.

```text
요청 ID
사용자 요청 요약
Agent 이름
Tool 이름
실행 시작/종료 시간
성공/실패 상태
오류 메시지
복구 조치 여부
```

## Docker와 연결

Docker Compose에서는 로그와 상태를 아래 명령으로 확인합니다.

```powershell
docker compose ps
docker compose logs backend
docker compose logs -f worker
docker stats
```

05 단원에서 만든 구조는 나중에 monitor 서비스나 Streamlit 운영 대시보드로 확장됩니다.

## AWS와 연결

AWS에서는 운영 관찰 정보가 다음 서비스와 연결됩니다.

| 로컬 개념 | AWS 연결 예시 |
| --- | --- |
| print/logging | CloudWatch Logs |
| event history | DynamoDB, RDS, S3, CloudWatch Logs Insights |
| tracing | X-Ray, OpenTelemetry, LangSmith |
| dashboard | CloudWatch Dashboard, Streamlit admin UI |
| alarm | CloudWatch Alarm, SNS |

## 실행 예제

```powershell
python.\01_ch1_logging-and-event-history\01_event-history-logger.py
python.\02_ch2_tracing-and-monitoring\01_trace-agent-execution.py
python.\02_ch2_tracing-and-monitoring\02_langsmith_trace_mapping.py
streamlit run.\03_ch3_ops-dashboard-streamlit\01_ops-dashboard.py --server.port 8803
python.\04_ch4_execution-status-management\01_execution-status-manager.py
```
