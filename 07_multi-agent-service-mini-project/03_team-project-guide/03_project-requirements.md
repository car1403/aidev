# 03 Project Requirements

이번 프로젝트의 기준 주제는 **에러 자가 치유(Auto Healing) 워크플로우**입니다.

단순히 Docker Compose 서비스를 실행하는 것이 아니라, 여러 Agent가 장애를 분류하고, 복구 전략을 선택하고, 복구 결과를 검증하며, 파이프라인과 알림까지 운영 흐름으로 연결하는 프로젝트입니다.

## 1. 필수 구현

- Docker Compose 실행 구조
- backend, frontend, worker, monitor 중 3개 이상 서비스
- 장애 유형 3개 이상
- Agent 역할 4개 이상
- Agent 간 Handoff/Context 구조
- Auto Healing 판단 로직
- 장애 유형별 복구 로직
- 복구 결과 검증과 Feedback Loop
- Health Check 또는 상태 확인 API
- 운영 이벤트 로그
- 감사 로그 또는 정책 위반 추적 항목
- 위험 명령 제한 또는 Guardrail 검증 기준
- `docker compose config` 통과
- README 실행 방법

## 2. 멀티 에이전트 아키텍처 설계서 필수 항목

```text
docs/multi-agent-architecture.md
```

아래 항목을 반드시 작성합니다.

- 아키텍처 구조가 비즈니스 요구사항에 맞게 선택되었는가?
- 응답 속도, 결정 일관성, 장애 격리 같은 선택 근거가 문서화되었는가?
- 각 Agent의 역할과 책임 범위가 정의되었는가?
- Planner, Executor, Critic, Memory Keeper 같은 역할의 의존 관계가 명확한가?
- Agent 간 책임 중복이나 공백이 없는가?
- Agent 간 Handoff 시 Context가 누락 없이 전달되는가?
- 메시지 큐, 공유 상태, Handoff Context 중 어떤 방식을 사용할지 설명되었는가?

## 3. 배포 및 장애 복구 보고서 필수 항목

```text
docs/deployment-recovery-report.md
```

아래 항목을 반드시 작성합니다.

- 멀티 컨테이너(Pod/Service) 배포 매니페스트가 작성되었는가?
- 서비스 디스커버리, 로드밸런싱, 시크릿 관리가 포함되었는가?
- 네트워크 타임아웃, 연결 끊김, DB 고갈, API 5xx/Rate Limit, LLM hallucination/token limit, Prompt Injection 같은 장애 유형별 감지 메트릭이 수립되었는가?
- 장애 유형별 자동 복구 스크립트가 정의되었는가?
- 재시작, 재연결, 대체 모델 호출, 캐시 fallback 같은 복구 전략이 포함되었는가?
- 수동 개입 없이 복구되는 시나리오 비율이 제시되었는가?

## 4. 파이프라인 구현 결과 보고서 필수 항목

```text
docs/pipeline-result-report.md
```

아래 항목을 반드시 작성합니다.

- 코드 커밋 -> 빌드 -> 테스트 -> 배포의 전체 단계가 다이어그램으로 표현되었는가?
- 보안 스캔 적용 여부가 정리되었는가?
- 각 단계의 입력과 출력이 정의되었는가?
- 실패 시 처리 규칙이 정의되었는가?
- 단위/통합 테스트 커버리지 기준이 명시되었는가?
- 테스트 데이터 관리 방식이 설명되었는가?
- 실패 시 블로킹 정책이 명시되었는가?
- 성공/실패/지연 결과가 Slack, Teams, PagerDuty 등으로 알림되는 구조가 설명되었는가?
- 장애 발생 시 담당자 할당과 에스컬레이션이 설정되었는가?

## 5. 선택 구현

- Tool 권한 제어
- 보안/가드레일 정책
- MCP/Tool 연결 설계
- LangSmith식 trace/run/span 추적 계획
- 보안 운영 Runbook
- Guardrails AI 통합 검증 설계
- AWS 배포 체크리스트
- GitHub Actions build check
- CloudWatch 로그 설계
- 비용/보안 정리
