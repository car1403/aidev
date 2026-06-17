# LangSmith Tracing Plan

LangSmith식 trace/run/span 관점으로 Multi-Agent 실행 추적 계획을 작성합니다.

실제 LangSmith 연동은 선택 사항입니다. 이 문서는 어떤 정보를 추적해야 하는지 설계하는 용도입니다.

## 1. Trace 구조

```text
trace_id
-> supervisor_agent
   -> diagnosis_agent
      -> health_check_tool
   -> recovery_agent
      -> restart_or_fallback_tool
   -> validation_agent
   -> reporter_agent
```

## 2. Run 정보

```text
run_id:
parent_run_id:
name:
run_type:
inputs:
outputs:
status:
duration_ms:
error:
```

## 3. 추적할 메타데이터

```text
request_id:
user_id:
service_name:
agent_name:
tool_name:
attempt_count:
recovery_action:
final_status:
```

## 4. 민감 정보 마스킹

```text
LangSmith 또는 외부 추적 도구에 저장하면 안 되는 정보:
마스킹할 필드:
저장 가능한 요약 정보:
```

## 5. 운영 활용

```text
실패한 Agent 실행 찾기:
느린 Tool 호출 찾기:
재시도 횟수 많은 요청 찾기:
정책 위반 이벤트와 연결하기:
```
