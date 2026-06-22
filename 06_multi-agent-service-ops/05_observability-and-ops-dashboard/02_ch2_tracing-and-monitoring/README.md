# 02_ch2_tracing-and-monitoring

Agent 실행 흐름을 Trace 단위로 추적하는 방법을 학습합니다.

## Trace란?

Trace는 하나의 요청이 여러 단계와 Agent를 거치며 실행되는 전체 흐름입니다.

```text
request_id
-> supervisor_agent
-> ops_agent
-> tool_call
-> reviewer_agent
-> final_response
```

## Monitoring과 차이

- Logging: 무슨 일이 일어났는지 기록
- Tracing: 하나의 요청이 어떤 경로로 흘렀는지 추적
- Monitoring: 현재 서비스 상태와 지표를 관찰

## 실행

```powershell
python.\02_ch2_tracing-and-monitoring\01_trace-agent-execution.py
```
