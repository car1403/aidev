# 01_ch1_logging-and-event-history

서비스 실행 이벤트를 구조화해서 기록하는 방법을 학습합니다.

## 왜 구조화 로그가 필요한가?

그냥 문자열만 출력하면 나중에 검색과 분석이 어렵습니다.

좋은 로그는 아래 값을 포함합니다.

- event_id
- service_name
- agent_name
- event_type
- status
- message
- created_at

## 실행

```powershell
cd C:\aidev\06_multi-agent-service-ops\05_observability-and-ops-dashboard
..\.venv\Scripts\Activate.ps1
python.\01_ch1_logging-and-event-history\01_event-history-logger.py
```
