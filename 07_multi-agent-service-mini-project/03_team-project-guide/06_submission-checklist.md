# 06 Submission Checklist

## 필수 파일

```text
README.md
.env.example
Dockerfile
docker-compose.yml
backend/main.py
frontend/app.py
worker/main.py
monitor/app.py
docs/multi-agent-architecture.md
docs/deployment-recovery-report.md
docs/pipeline-result-report.md
docs/test-checklist.md
```

## 멀티 에이전트 아키텍처 설계서 확인

- [ ] 비즈니스 요구사항과 아키텍처 선택 근거가 작성되었습니다.
- [ ] 응답 속도, 결정 일관성, 장애 격리 기준이 설명되었습니다.
- [ ] 각 Agent의 역할과 책임 범위가 정의되었습니다.
- [ ] Planner, Executor, Critic, Memory Keeper 등 역할 의존 관계가 설명되었습니다.
- [ ] 책임 중복이나 공백이 없습니다.
- [ ] Handoff Context가 누락 없이 정의되었습니다.
- [ ] 메시지 큐, 공유 상태, Context 전달 구조가 설명되었습니다.
- [ ] Agent 간 Context 동기화와 협업 일관성 유지 기준이 설명되었습니다.
- [ ] Context 불일치 시 Critic 또는 Feedback Loop가 검증하는 흐름이 있습니다.

## 배포 및 장애 복구 보고서 확인

- [ ] Docker Compose 또는 배포 매니페스트가 작성되었습니다.
- [ ] 서비스 디스커버리, 로드밸런싱, 시크릿 관리가 고려되었습니다.
- [ ] 장애 유형별 감지 메트릭이 수립되었습니다.
- [ ] 자동 복구 스크립트 또는 복구 흐름이 정의되었습니다.
- [ ] 재시작, 재연결, 대체 모델 호출, 캐시 fallback 중 필요한 전략이 포함되었습니다.
- [ ] 수동 개입 없이 복구되는 시나리오 비율이 제시되었습니다.
- [ ] App Runner 또는 ECS로 확장할 때 image, port, env, health check, log 항목이 정리되었습니다.

## 파이프라인 구현 결과 보고서 확인

- [ ] 코드 커밋 -> 빌드 -> 테스트 -> 배포 단계가 표현되었습니다.
- [ ] 각 단계의 입력과 출력이 정의되었습니다.
- [ ] 실패 시 처리 규칙이 정의되었습니다.
- [ ] 테스트 커버리지 기준과 테스트 데이터 관리 방식이 정리되었습니다.
- [ ] 실패 시 블로킹 정책이 명시되었습니다.
- [ ] Slack, Teams, PagerDuty 등 알림 구조가 설명되었습니다.
- [ ] 담당자 할당과 에스컬레이션 기준이 설명되었습니다.
- [ ] 성공/실패/지연 상태별 알림 기준이 작성되었습니다.
- [ ] pipeline 실패 시 block/retry/escalation 기준이 작성되었습니다.

## 실행 검증

- [ ] `.env.example` 작성
- [ ] `.env` 제외 확인
- [ ] `docker compose config` 통과
- [ ] `docker compose up --build` 실행 결과 확인
- [ ] Health Check 결과 작성
- [ ] worker/monitor 로그 확인 결과 작성
- [ ] GitHub Actions 적용 여부 작성
- [ ] AWS 배포 체크리스트 작성
- [ ] 비용/보안 주의 사항 작성
- [ ] 발표 자료 작성
- [ ] `__pycache__` 삭제
