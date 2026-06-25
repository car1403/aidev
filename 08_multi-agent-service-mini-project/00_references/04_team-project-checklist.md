# 04. Team Project Checklist

이 문서는 최종 프로젝트를 진행할 때 확인할 체크리스트입니다.

## 팀 구성

권장 팀 구성은 4~5명입니다.

| 역할 | 담당 내용 |
| --- | --- |
| API 담당 | backend API, Health Check, 장애 이벤트 처리 |
| Worker 담당 | 장애 감지, 복구 전략, Feedback Loop |
| UI/Monitor 담당 | frontend, monitor, 운영 로그 화면 |
| Docker/CI 담당 | Docker Compose, GitHub Actions, 실행 검증 |
| 문서/QA 담당 | 필수 산출물 3종 정리, 선택적으로 테스트 체크리스트와 발표 자료 작성 |

인원이 적으면 한 사람이 여러 역할을 맡을 수 있습니다. 중요한 것은 누가 어떤 파일과 산출물을 책임지는지 명확히 하는 것입니다.

## 시작 전 체크리스트

- [ ] Docker Desktop이 실행되는가?
- [ ] `docker compose version`이 출력되는가?
- [ ] 샘플 프로젝트의 `docker compose config`가 통과하는가?
- [ ] 팀 프로젝트 폴더를 복사했는가?
- [ ] `.env.example`을 `.env`로 복사했는가?
- [ ] 프로젝트 주제와 장애 시나리오를 정했는가?
- [ ] Agent 역할을 나누었는가?
- [ ] 필수 산출물 파일을 열어 작성 위치를 확인했는가?

## 필수 산출물 체크리스트

- [ ] `docs/multi-agent-architecture.md`
- [ ] `docs/deployment-recovery-report.md`
- [ ] `docs/pipeline-result-report.md`

## 선택 보조 산출물 체크리스트

- [ ] `docs/test-checklist.md`
- [ ] `docs/handoff-context-design.md`
- [ ] `docs/feedback-loop-review.md`
- [ ] `docs/security-runbook.md`
- [ ] `docs/audit-policy-log.md`
- [ ] `docs/guardrails-validation.md`
- [ ] `docs/langsmith-tracing-plan.md`

## 시연 체크리스트

- [ ] backend `/health`가 정상 응답한다.
- [ ] frontend 화면이 열린다.
- [ ] monitor 화면이 열린다.
- [ ] 장애 이벤트를 입력할 수 있다.
- [ ] worker 로그에 장애 처리 흐름이 보인다.
- [ ] 복구 결과가 monitor에 표시된다.
- [ ] 실패 시 fallback 또는 manual review 상태가 표시된다.
- [ ] 보안 제한 규칙이 설명되어 있다.

## 제출 전 확인

- [ ] `.env`가 커밋되지 않았다.
- [ ] `.venv`가 커밋되지 않았다.
- [ ] API Key나 AWS Key가 문서에 적혀 있지 않다.
- [ ] `docker compose config` 결과가 정상이다.
- [ ] README만 보고 실행할 수 있다.
- [ ] 프로젝트 산출물과 시연 흐름이 일치한다.
