# Test Checklist

최종 제출 전에 아래 항목을 확인합니다.

## Local Docker Compose

- [ ] `Copy-Item .env.example .env`를 실행했다.
- [ ] `docker compose config`가 통과했다.
- [ ] `docker compose up --build`로 서비스가 실행되었다.
- [ ] backend `/health`가 정상 응답한다.
- [ ] frontend 화면에 접속할 수 있다.
- [ ] monitor 화면에 접속할 수 있다.
- [ ] worker 로그를 확인할 수 있다.
- [ ] 장애 이벤트 예시를 실행했다.
- [ ] 이벤트 이력이 화면 또는 로그에 표시된다.
- [ ] `docker compose down`으로 정상 종료했다.

## Multi-Agent Architecture

- [ ] 비즈니스 요구사항과 아키텍처 선택 근거를 작성했다.
- [ ] 응답 속도, 결정 일관성, 장애 격리 기준을 설명했다.
- [ ] Agent 역할을 3개 이상 정의했다.
- [ ] Agent 간 책임 중복이나 공백이 없는지 확인했다.
- [ ] Agent 간 Handoff 흐름을 설명했다.
- [ ] Handoff Context 필드를 설명했다.
- [ ] Agent 간 Context 동기화 기준을 설명했다.
- [ ] Context 불일치 시 Critic 또는 Feedback Loop 검증 기준을 설명했다.
- [ ] MCP/Tool 연결과 Agent별 권한을 설명했다.

## Auto Healing And Recovery

- [ ] 장애 유형을 2개 이상 테스트했다.
- [ ] 네트워크, API, LLM, Prompt Injection 중 필요한 장애 감지 기준을 작성했다.
- [ ] 복구 전략을 2개 이상 확인했다.
- [ ] Retry, Restart, Reconnect, Fallback 기준을 설명했다.
- [ ] 복구 결과 검증 기준을 설명했다.
- [ ] 자동 복구와 수동 확인 전환 기준을 구분했다.
- [ ] 복구 실패 시 다음 조치를 설명했다.

## Pipeline

- [ ] 코드 커밋 -> 빌드 -> 테스트 -> 배포 흐름을 작성했다.
- [ ] 각 단계의 입력과 출력을 작성했다.
- [ ] 실패 시 처리 규칙을 작성했다.
- [ ] 테스트 데이터 관리 방식을 작성했다.
- [ ] 실패 시 block/retry/escalation 기준을 작성했다.
- [ ] Slack/Teams/PagerDuty 같은 알림 구조를 선택 확장으로 설명했다.

## Observability

- [ ] 실행 이벤트 로그를 확인했다.
- [ ] `incident_id` 또는 `request_id` 기준으로 추적할 수 있다.
- [ ] LangSmith식 trace/run/span 구조를 설명했다.
- [ ] 실패한 Agent 실행을 찾는 방법을 설명했다.
- [ ] monitor 화면에서 서비스 상태를 확인했다.

## Security And Guardrails

- [ ] 보안 Runbook을 작성했다.
- [ ] 감사 로그 항목을 작성했다.
- [ ] 정책 위반 이벤트 기록 기준을 작성했다.
- [ ] Guardrail 입력 검증 기준을 작성했다.
- [ ] Guardrail 출력 검증 기준을 작성했다.
- [ ] 위험 Tool 실행 제한 기준을 작성했다.
- [ ] 민감 정보가 로그에 남지 않게 했다.

## GitHub Actions

- [ ] workflow 파일 위치를 확인했다.
- [ ] Python 문법 검사 항목을 확인했다.
- [ ] `docker compose config` 검증 항목을 확인했다.
- [ ] Docker build 검증 항목을 확인했다.

## AWS Deployment Checklist

- [ ] ECR image 저장 전략을 작성했다.
- [ ] App Runner 또는 ECS 중 배포 후보를 선택했다.
- [ ] 환경변수와 secret 관리 방식을 작성했다.
- [ ] `/health` 기반 Health Check를 작성했다.
- [ ] CloudWatch Logs 확인 방식을 작성했다.
- [ ] 실습 후 삭제할 AWS 리소스 목록을 작성했다.
