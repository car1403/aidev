# 03 Multi-Agent Service Map

Multi-Agent 서비스는 여러 Agent가 각자 역할을 나누어 협업하는 구조입니다.

## 기본 Agent 역할

```text
supervisor_agent: 전체 요청 분석과 작업 분배
planner_agent: 실행 계획 수립
ops_agent: 서비스 상태 확인과 복구 조치 판단
security_agent: 보안 정책과 권한 확인
reviewer_agent: 결과 검증과 품질 확인
monitor_agent: 실행 이력과 상태 추적
```

## 서비스 구조와 Agent 연결

| 서비스 | 역할 | 연결되는 Agent |
| --- | --- | --- |
| backend | API 요청 수신, Supervisor 실행 | supervisor_agent, planner_agent |
| worker | 오래 걸리는 작업, 복구 조치 실행 | ops_agent, security_agent |
| monitor | 실행 상태와 로그 표시 | monitor_agent, reviewer_agent |
| frontend | 사용자 요청 입력과 결과 표시 | 사용자 UI |

## 설계할 때 중요한 질문

- 어떤 Agent가 요청을 먼저 받는가?
- 어떤 Agent가 Tool을 실행할 수 있는가?
- 어떤 Agent는 조회만 가능한가?
- 여러 Agent 결과를 누가 합치는가?
- 실패하면 누가 재시도하거나 운영자에게 넘기는가?
