# 01. Project Big Picture

07 프로젝트는 **Multi-Agent 기반 Auto Healing 서비스**를 만드는 미니 프로젝트입니다.

장애가 발생하면 하나의 함수가 모든 일을 처리하는 것이 아니라, 여러 Agent가 역할을 나누어 판단합니다.

```text
Supervisor Agent
-> Diagnosis Agent
-> Recovery Agent
-> Validation Agent
-> Reporter Agent
```

## 전체 구조

```text
사용자 또는 시스템이 장애 이벤트 입력
-> backend가 장애 이벤트 수신
-> worker가 장애 유형 분석
-> Agent들이 복구 전략 선택
-> Health Check로 복구 여부 확인
-> monitor가 실행 상태와 로그 표시
-> docs에 설계와 결과 정리
```

## 서비스 구성

| 서비스 | 역할 |
| --- | --- |
| backend | 장애 이벤트 API, Health Check, 복구 결과 조회 |
| frontend | 장애 이벤트 입력과 결과 확인 화면 |
| worker | 장애 분석, 복구 전략 선택, 자동 복구 시뮬레이션 |
| monitor | 운영 로그, 복구 상태, 감사 로그 표시 |

## 중요한 설계 기준

프로젝트에서 가장 중요한 것은 “Agent가 많다”가 아니라 “역할과 책임이 분리되어 있다”입니다.

확인할 기준:

- 어떤 Agent가 어떤 판단을 하는가?
- Agent 간 중복 책임이 없는가?
- Handoff 시 어떤 Context가 전달되는가?
- 장애 복구가 실패했을 때 Feedback Loop가 있는가?
- 위험한 작업은 Guardrail로 제한되는가?
- 실행 결과가 로그와 대시보드에 남는가?

## 06과의 연결

06에서 배운 내용은 07에서 아래처럼 연결됩니다.

| 06 내용 | 07 적용 |
| --- | --- |
| Multi-Agent 협업 | Agent 역할과 업무 인계 설계 |
| Docker Compose | 여러 서비스를 한 번에 실행 |
| Auto Healing | 장애 감지와 복구 전략 구현 |
| Observability | 실행 로그와 대시보드 구성 |
| 보안/Guardrails | 위험 작업 제한과 정책 위반 추적 |
| GitHub Actions | Compose와 build 자동 검증 |
| AWS | 배포 확장 체크리스트 작성 |
