# 03. Project Requirements

07 프로젝트의 최소 요구사항입니다.

## 필수 기능

- Docker Compose로 backend, frontend, worker, monitor를 실행합니다.
- backend에 `/health` 엔드포인트가 있어야 합니다.
- 장애 이벤트를 입력하거나 시뮬레이션할 수 있어야 합니다.
- 장애 유형을 2개 이상 정의합니다.
- 복구 전략을 2개 이상 정의합니다.
- Agent 역할을 3개 이상 나눕니다.
- 복구 결과를 검증하는 단계가 있어야 합니다.
- monitor에서 운영 이벤트를 확인할 수 있어야 합니다.

## 필수 산출물

- `docs/multi-agent-architecture.md`
- `docs/deployment-recovery-report.md`
- `docs/pipeline-result-report.md`

위 3가지가 07 과정의 필수 산출물입니다. `docs/test-checklist.md`, 보안/감사/Guardrails 문서, LangSmith 추적 계획, 발표 자료는 선택 보조 산출물입니다.

## 선택 확장

- GitHub Actions build check
- AWS App Runner 또는 ECS 배포 체크리스트
- LangSmith식 실행 추적 계획
- Guardrails 검증 문서
- 감사 로그와 정책 위반 추적

## 완료 기준

```text
README만 보고 실행할 수 있다.
docker compose config가 통과한다.
docker compose up --build로 서비스가 실행된다.
장애 이벤트가 처리된다.
결과가 로그와 화면에 표시된다.
필수 산출물이 작성되어 있다.
```
