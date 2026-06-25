# LangSmith Tracing Plan

LangSmith를 실제로 연동하지 않더라도, 실행 추적을 어떤 단위로 볼지 설계합니다.

## 1. 추적 단위

| 단위 | 의미 |
| --- | --- |
| trace | 하나의 장애 처리 전체 흐름 |
| run | Agent 하나의 실행 |
| span | Tool 호출, API 요청, Health Check 같은 세부 작업 |

## 2. Trace 예시

```text
trace: inc-001
├─ run: Supervisor Agent
├─ run: Diagnosis Agent
│  └─ span: log read
├─ run: Recovery Agent
│  └─ span: retry request
├─ run: Validation Agent
│  └─ span: health check
└─ run: Reporter Agent
```

## 3. 기록할 정보

- `incident_id`
- Agent 이름
- 입력 Context
- 선택한 Tool
- 실행 결과
- 오류 메시지
- 실행 시간
- 최종 상태

## 4. 확인 기준

- 실패한 Agent를 찾을 수 있는가?
- 시간이 오래 걸린 단계가 보이는가?
- 같은 장애가 반복되는지 확인할 수 있는가?
- 복구 전략 개선에 사용할 수 있는가?
