# 06. Project Alignment Checklist

이 문서는 07 프로젝트가 06 보강 내용과 이미지 기준에 맞게 구성되었는지 확인하는 체크리스트입니다.

## Multi-Agent 협업

- [ ] 단일 Agent와 Multi-Agent 구조의 차이를 설명할 수 있는가?
- [ ] Agent별 역할이 명확한가?
- [ ] Supervisor 또는 Router 역할이 있는가?
- [ ] Handoff 시 전달되는 Context가 정의되어 있는가?
- [ ] Agent 간 Context 동기화 기준이 있는가?
- [ ] Feedback Loop가 설계되어 있는가?

## 서비스 운영

- [ ] Docker Compose로 여러 서비스를 실행하는가?
- [ ] backend, frontend, worker, monitor 역할이 분리되어 있는가?
- [ ] Health Check가 있는가?
- [ ] 서비스 로그를 확인할 수 있는가?
- [ ] monitor 화면에서 운영 상태를 볼 수 있는가?

## Auto Healing

- [ ] 장애 유형이 2개 이상 정의되어 있는가?
- [ ] 장애별 감지 기준이 있는가?
- [ ] Retry, Restart, Reconnect, Fallback 중 2개 이상을 설명할 수 있는가?
- [ ] 복구 후 검증 단계가 있는가?
- [ ] 복구 실패 시 다음 조치가 정의되어 있는가?

## 보안과 Guardrails

- [ ] Prompt Injection 방어 기준이 있는가?
- [ ] 위험한 Tool 실행 제한 기준이 있는가?
- [ ] 민감 정보가 로그에 남지 않게 설계했는가?
- [ ] 정책 위반 이벤트를 감사 로그로 남기는가?
- [ ] Guardrails 검증 문서가 있는가?

## GitHub Actions와 AWS

- [ ] GitHub Actions 자동 검증 기준이 정리되어 있는가?
- [ ] `docker compose config`를 자동 검증할 수 있는가?
- [ ] Docker image build 검증 기준이 있는가?
- [ ] AWS 배포 확장 구조를 설명할 수 있는가?
- [ ] App Runner와 ECS 선택 기준을 설명할 수 있는가?
- [ ] CloudWatch 로그 확인 방법을 설명할 수 있는가?

## 최종 제출

- [ ] README만 보고 실행할 수 있는가?
- [ ] 필수 산출물 3종이 작성되었는가?
- [ ] 테스트 체크리스트가 작성되었는가?
- [ ] 발표 시나리오가 정리되었는가?
- [ ] `.env`, `.venv`, API Key가 커밋되지 않았는가?
