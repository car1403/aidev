# 01 Multi-Agent Collaboration

이 단원은 단일 Agent와 Multi-Agent 구조를 비교하고, 역할 기반 Agent 분리, Supervisor/Router, Handoff, Context 동기화, Feedback Loop를 학습합니다.

06 과정 전체에서는 Docker, AWS, CI/CD, 모니터링까지 다루지만, 이 단원에서는 먼저 여러 Agent가 어떤 책임으로 나뉘고 어떻게 협업하는지를 이해하는 데 집중합니다.

## 학습 목표

- 단일 Agent와 Multi-Agent 구조의 차이를 설명합니다.
- 역할(Role) 기반으로 Agent 책임을 나눕니다.
- Supervisor 또는 Router가 작업을 어떻게 분배하는지 이해합니다.
- 여러 Agent 결과를 하나의 최종 결과로 통합합니다.
- Agent 간 Handoff와 Context 공유 구조를 설계합니다.
- Agent 간 Context 동기화와 협업 일관성 유지 기준을 설계합니다.
- Agent 실행 결과를 검증하고 Feedback Loop를 구성합니다.

## 폴더 구조

```text
01_multi-agent-collaboration
├─ 01_single-vs-multi-agent
├─ 02_role-based-agent-design
├─ 03_supervisor-router-workflow
├─ 04_distributed-agent-collaboration
├─ 05_handoff-context-mcp
├─ 06_feedback-loop-result-review
├─ 10_labs
└─ 20_assignments
```

## 진행 흐름

```text
단일 Agent와 Multi-Agent 비교
-> Agent 역할 분리
-> Supervisor/Router 설계
-> 분산 협업 결과 통합
-> Handoff와 Context 공유
-> Context 동기화와 Feedback Loop
```

## 실행 준비

```powershell
cd C:\aidev\06_multi-agent-service-ops
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r .\requirements.txt
```

## 실행 예시

```powershell
cd C:\aidev\06_multi-agent-service-ops\01_multi-agent-collaboration
python .\01_single-vs-multi-agent\01_single-agent-vs-multi-agent.py
python .\02_role-based-agent-design\01_role-based-agent-design.py
python .\03_supervisor-router-workflow\01_supervisor-router-workflow.py
python .\04_distributed-agent-collaboration\01_distributed-agent-collaboration.py
python .\05_handoff-context-mcp\01_handoff_context_mcp.py
python .\06_feedback-loop-result-review\01_feedback_loop_result_review.py
```

## Agent 간 Context 동기화 기준

Multi-Agent 구조에서는 한 Agent의 결과가 다음 Agent의 판단 기준이 됩니다. 따라서 Agent 간 Context가 서로 다르게 해석되면 작업 결과가 흔들릴 수 있습니다.

| 기준 | 설명 |
| --- | --- |
| 공통 `request_id` | 모든 Agent가 같은 요청을 처리하고 있음을 확인합니다. |
| `shared_context` | 서비스명, 장애 유형, 사용자 요청, 제약 조건처럼 공통으로 필요한 정보를 유지합니다. |
| `handoff_summary` | 다음 Agent에게 필요한 요약만 전달합니다. |
| `previous_result` | 이전 Agent가 어떤 판단을 했는지 기록합니다. |
| `feedback_loop` | 결과가 기준을 통과하지 못하면 원인을 기록하고 재시도 또는 fallback합니다. |

## Docker Compose와의 연결

이 단원에서 나누는 Agent 역할은 02 단원에서 Docker Compose 서비스 구조로 확장됩니다.

```text
supervisor -> backend
diagnosis/recovery/validation -> worker
result/status -> monitor
```

따라서 01 단원은 클라우드 배포 전에 서비스 내부 역할을 설계하는 단계라고 보면 됩니다.
