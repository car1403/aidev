# 01 Multi-Agent Collaboration

이 단원은 단일 Agent와 Multi-Agent 구조를 비교하고, 역할 기반 Agent 분리, Supervisor/Router 기반 작업 분배, 분산 협업 구조를 학습합니다.

06 과정 전체에서는 Docker, Docker Compose, AWS, CI/CD, 모니터링까지 다루지만, 01 단원에서는 먼저 서비스 안에서 여러 Agent가 어떤 역할로 나뉘고 어떻게 협업하는지 이해하는 데 집중합니다.

## 이 단원의 목표

- 단일 Agent와 Multi-Agent 구조의 차이를 설명할 수 있다.
- 역할(Role) 기반으로 Agent 책임을 나눌 수 있다.
- Supervisor 또는 Router가 작업을 어떻게 분배하는지 이해한다.
- 여러 Agent 결과를 하나의 최종 응답으로 통합할 수 있다.
- Agent 간 Handoff와 Context 공유 구조를 설계할 수 있다.
- Agent 간 Context 동기화와 협업 일관성 유지 기준을 설계할 수 있다.
- Agent 실행 결과를 검증하고 Feedback Loop를 설계할 수 있다.
- 이후 Docker Compose 서비스 구조로 확장할 수 있는 Agent 경계를 설계한다.

## 학습 순서

```text
01_ch1_single-vs-multi-agent
-> 02_ch2_role-based-agent-design
-> 03_ch3_supervisor-router-workflow
-> 04_ch4_distributed-agent-collaboration
-> 05_ch5_handoff-context-mcp
-> 06_ch6_feedback-loop-result-review
-> 10_labs
-> 20_assignments
```

## 환경 준비

06 과정의 공통 `.venv`를 사용합니다.

```powershell
cd C:\aidev\06_multi-agent-service-ops
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

설치가 끝나면 01 단원 폴더로 이동합니다.

```powershell
cd C:\aidev\06_multi-agent-service-ops\01_multi-agent-collaboration
```

##.env 설정

01 단원 예제는 기본적으로 Mock Agent로 동작하므로 API Key 없이도 실행할 수 있습니다.

LLM 호출을 확장하려면 상위 폴더에서 `.env.example`을 `.env`로 복사합니다.

```powershell
cd C:\aidev\06_multi-agent-service-ops
Copy-Item.env.example.env
```

`.env` 파일에는 실제 키를 넣습니다.

```env
OPENAI_API_KEY=your-openai-api-key
OPENAI_MODEL=gpt-4.1-mini
```

중요: `.env` 파일은 GitHub에 올리지 않습니다.

## Docker와 어떻게 연결되는가?

01 단원에서는 Docker를 직접 실행하지 않아도 됩니다. 다만 이 단원에서 나누는 Agent 역할은 02 단원의 Docker Compose 서비스 분리로 이어집니다.

예를 들어 01에서 아래처럼 역할을 나누면:

```text
planner_agent: 요청 분석과 계획 수립
research_agent: 자료 검색과 근거 수집
executor_agent: 작업 실행
reviewer_agent: 결과 검증
supervisor_agent: 전체 흐름 조정
```

02 단원에서는 이를 아래처럼 서비스로 나눌 수 있습니다.

```text
backend service: API 요청 수신
worker service: Agent 작업 실행
monitor service: 실행 상태 추적
frontend service: 운영 화면 표시
```

## AWS와 어떻게 연결되는가?

01 단원의 Agent 설계는 나중에 AWS 배포 시 서비스 경계를 정하는 기준이 됩니다.

- 어떤 Agent가 API 서버 안에서 실행되는가?
- 어떤 Agent는 백그라운드 worker로 분리해야 하는가?
- 어떤 실행 로그를 CloudWatch 같은 운영 로그로 남길 것인가?
- 장애 발생 시 어떤 Agent 작업을 재시도할 것인가?

즉, 01 단원은 클라우드 배포 전에 서비스 내부 구조를 설계하는 단계입니다.

## Agent 간 Context 동기화 기준

Multi-Agent 구조에서는 한 Agent의 결과가 다음 Agent의 판단 기준이 됩니다. 따라서 Agent 간 Context가 서로 다르게 해석되면 협업 결과가 흔들릴 수 있습니다.

수업에서는 아래 기준을 확인합니다.

| 기준 | 설명 |
| --- | --- |
| 공통 request_id | 모든 Agent가 같은 요청을 처리하고 있음을 확인합니다. |
| shared_context | 서비스명, 장애 유형, 사용자 요청, 제약 조건처럼 공통으로 필요한 정보를 유지합니다. |
| handoff_summary | 다음 Agent에게 필요한 요약만 전달합니다. |
| previous_result | 이전 Agent가 어떤 판단을 했는지 기록합니다. |
| consistency_check | Agent 간 결과가 서로 충돌하지 않는지 검증합니다. |
| feedback_loop | 불일치가 있으면 원인을 기록하고 재시도 또는 fallback합니다. |

이 기준은 `05_ch5_handoff-context-mcp`와 `06_ch6_feedback-loop-result-review`에서 실습합니다.

## 실행 예제

```powershell
python.\01_ch1_single-vs-multi-agent\01_single-agent-vs-multi-agent.py
python.\02_ch2_role-based-agent-design\01_role-based-agent-design.py
python.\03_ch3_supervisor-router-workflow\01_supervisor-router-workflow.py
python.\04_ch4_distributed-agent-collaboration\01_distributed-agent-collaboration.py
python.\05_ch5_handoff-context-mcp\01_handoff_context_mcp.py
python.\06_ch6_feedback-loop-result-review\01_feedback_loop_result_review.py
```
