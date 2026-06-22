# Test Checklist

## Local Docker Compose

- [ ] `Copy-Item.env.example.env` 실행
- [ ] `docker compose config` 통과
- [ ] `docker compose up --build` 실행 성공
- [ ] backend `/health` 확인
- [ ] frontend 화면 접속
- [ ] monitor 화면 접속
- [ ] worker 로그 확인
- [ ] Auto Healing 요청 실행
- [ ] 이벤트 이력 표시 확인
- [ ] `docker compose down` 정상 종료

## Multi-Agent Architecture

- [ ] 비즈니스 요구사항과 아키텍처 선택 근거 작성
- [ ] 응답 속도, 결정 일관성, 장애 격리 기준 설명
- [ ] Planner, Executor, Critic, Memory Keeper 등 Agent 역할 설명
- [ ] Agent 간 책임 중복 또는 공백 없음
- [ ] Agent 간 Handoff 흐름 설명
- [ ] Handoff Context 필드 설명
- [ ] Agent 간 Context 동기화 기준 설명
- [ ] Context 불일치 시 Critic 또는 Feedback Loop 검증 기준 설명
- [ ] MCP/Tool 연결과 Agent별 권한 설명

## Auto Healing And Recovery

- [ ] 장애 유형 3개 이상 테스트
- [ ] 네트워크, DB, API, LLM, Prompt Injection 중 필요한 장애 감지 기준 작성
- [ ] 복구 전략 2개 이상 확인
- [ ] Retry/Restart/Fallback 기준 설명
- [ ] 복구 결과 검증 기준 설명
- [ ] 자동 복구와 수동 개입 기준 구분
- [ ] 수동 개입 없이 복구되는 시나리오 비율 작성
- [ ] App Runner 또는 ECS로 확장할 때 image, port, env, health check, log 항목 설명

## Pipeline

- [ ] 코드 커밋 -> 빌드 -> 테스트 -> 배포 단계 작성
- [ ] 각 단계의 입력과 출력 작성
- [ ] 실패 시 처리 규칙 작성
- [ ] 테스트 커버리지 기준 작성
- [ ] 테스트 데이터 관리 방식 작성
- [ ] 실패 시 블로킹 정책 작성
- [ ] Slack/Teams/PagerDuty 등 알림 구조 작성
- [ ] 담당자 할당과 에스컬레이션 기준 작성
- [ ] 성공/실패/지연 상태별 알림 기준 작성
- [ ] pipeline 실패 시 block/retry/escalation 기준 작성

## Observability

- [ ] 실행 이벤트 로그 확인
- [ ] trace_id 또는 request_id 기준 추적 가능
- [ ] LangSmith식 trace/run/span 구조 설명
- [ ] 실패한 Agent 실행을 찾는 방법 설명

## Security And Guardrails

- [ ] 보안 Runbook 작성
- [ ] 감사 로그 항목 작성
- [ ] 정책 위반 이벤트 기록 기준 작성
- [ ] Guardrail 입력 검증 기준 작성
- [ ] Guardrail 출력 검증 기준 작성
- [ ] 위험 Tool 실행 제한 기준 작성

## GitHub Actions

- [ ] workflow 파일 위치 확인
- [ ] Python 문법 검사 항목 확인
- [ ] `docker compose config` 검증 항목 확인
- [ ] Docker build 검증 항목 확인

## AWS Deployment Checklist

- [ ] ECR image 저장 전략 작성
- [ ] App Runner 또는 ECS 중 배포 후보 선택
- [ ] 환경변수와 secret 관리 방식 작성
- [ ] `/health` 기반 Health Check 작성
- [ ] CloudWatch Logs 확인 방식 작성
- [ ] 실습 후 삭제할 AWS 리소스 목록 작성
