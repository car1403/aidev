# 02 Role and Schedule

## 팀 역할 예시

- Multi-Agent 아키텍처 설계
- Handoff/Context 설계
- Docker Compose 구성
- backend API 구현
- worker Auto Healing 로직 구현
- frontend/monitor 화면 구현
- 장애 복구 시험
- 파이프라인 결과 보고서 작성
- 발표 자료 정리

## 권장 일정

### Day 1: 아키텍처와 장애 시나리오 설계

- 비즈니스 요구사항 정의
- 장애 시나리오 3개 이상 작성
- Agent 역할과 책임 범위 정의
- Handoff Context 설계
- Docker Compose 서비스 구조 초안 작성
- 멀티 에이전트 아키텍처 설계서 초안 작성

체크포인트:

```text
Agent 역할 4개 이상 정의
Handoff Context 초안 작성
장애 시나리오 3개 이상 작성
Compose 서비스 구조 초안 작성
```

### Day 2: 복구 로직과 서비스 통합

- backend Health Check 구현
- worker 장애 감지와 복구 전략 구현
- monitor 운영 이벤트 표시
- Auto Healing 요청 실행
- 장애 유형별 감지 메트릭 정리
- 배포 및 장애 복구 보고서 초안 작성

체크포인트:

```text
docker compose config 통과
docker compose up --build 성공
Health Check 성공
장애 복구 시나리오 2개 이상 확인
```

### Day 3: 파이프라인과 결과 검증

- 테스트 체크리스트 작성
- 파이프라인 단계 정리
- GitHub Actions 적용 여부 정리
- AWS 배포 후보와 체크리스트 정리
- 알림과 에스컬레이션 기준 작성
- 파이프라인 구현 결과 보고서 작성
- 최종 시연 리허설

체크포인트:

```text
멀티 에이전트 아키텍처 설계서 완성
배포 및 장애 복구 보고서 완성
파이프라인 구현 결과 보고서 완성
3분 시연 가능
```
