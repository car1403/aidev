# Lab 05. LangSmith Tracing Practice

## 목표

LangSmith 기반 실행 추적이 어떤 정보를 기록하는지 이해하고, Multi-Agent 실행 흐름을 trace/run/span 관점으로 정리합니다.

이 실습은 외부 LangSmith API를 호출하지 않고 Mock 데이터로 먼저 구조를 이해합니다. 실제 LangSmith 연동은 API Key, 프로젝트 설정, SDK 버전에 따라 달라질 수 있으므로 강사 안내에 따라 선택 실습으로 진행합니다.

## 실습

```powershell
cd C:\aidev\06_multi-agent-service-ops\05_observability-and-ops-dashboard
python .\02_ch2_tracing-and-monitoring\02_langsmith_trace_mapping.py
```

## LangSmith에서 관찰하는 정보

```text
project_name
trace_id
run_id
parent_run_id
run_type
inputs
outputs
latency
error
tags
metadata
```

## Multi-Agent Trace 예시

```text
trace_id
-> supervisor_agent
   -> ops_agent
      -> health_check_tool
   -> reviewer_agent
```

## 실제 LangSmith 연동 시 체크리스트

```text
[ ] LangSmith 계정 또는 실습 프로젝트 준비
[ ] LANGSMITH_API_KEY 준비
[ ] LANGSMITH_PROJECT 이름 결정
[ ] trace에 남길 입력/출력 범위 결정
[ ] 민감 정보 마스킹 기준 작성
[ ] 실패한 run을 어떻게 찾을지 기준 작성
```

## 확인 질문

- Logging과 Tracing의 차이는 무엇인가?
- Agent가 여러 개일 때 parent_run_id가 왜 중요한가?
- LangSmith에 저장하면 안 되는 민감 정보는 무엇인가?
- 실행 추적 결과를 Auto Healing과 어떻게 연결할 수 있는가?
