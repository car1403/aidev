# 04 Test Checklist

## 실행 환경

- [ ] `docker compose config` 통과
- [ ] `docker compose up --build` 실행 성공
- [ ] backend health check 성공
- [ ] frontend 화면 접속
- [ ] monitor 화면 접속
- [ ] worker 로그 확인
- [ ] `docker compose down` 정상 종료

## Multi-Agent 협업

- [ ] Agent 역할 4개 이상 정의
- [ ] Agent별 책임 범위와 의존 관계 설명
- [ ] Agent 간 Handoff/Context 전달 구조 확인
- [ ] Agent 간 Context 동기화 기준 확인
- [ ] Context 불일치 시 Feedback Loop 기준 확인
- [ ] 중복 책임 또는 공백 없음
- [ ] MCP/Tool 연결과 Agent별 권한 설명

## 장애 복구

- [ ] 장애 유형 3개 이상 테스트
- [ ] 장애 유형별 감지 메트릭 정의
- [ ] 복구 전략 2개 이상 테스트
- [ ] Retry/Restart/Fallback 중 필요한 전략 확인
- [ ] 자동 복구 시나리오와 수동 개입 시나리오 구분
- [ ] 복구 결과 검증 기준 확인
- [ ] Guardrail 또는 위험 명령 제한 확인

## 파이프라인

- [ ] 코드 커밋 -> 빌드 -> 테스트 -> 배포 단계 설명
- [ ] 단위/통합 테스트 기준 설명
- [ ] 실패 시 블로킹 정책 설명
- [ ] 선택 사항: GitHub Actions build check 설명
- [ ] 선택 사항: AWS 배포 체크리스트 작성
- [ ] 선택 사항: App Runner/ECS 배포 후보와 체크리스트 설명
- [ ] 알림과 에스컬레이션 기준 설명

## 문서

- [ ] 멀티 에이전트 아키텍처 설계서 작성
- [ ] 배포 및 장애 복구 보고서 작성
- [ ] 파이프라인 구현 결과 보고서 작성
- [ ] 발표 자료 작성
