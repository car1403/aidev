# 01 Course Big Picture

`06_multi-agent-service-ops`는 04와 05에서 배운 LLM Agent를 실제 서비스 운영 구조로 확장하는 과정입니다.

## 전체 흐름

```text
멀티 에이전트 협업 설계
-> Docker 기반 서비스 패키징
-> Docker Compose 기반 멀티 서비스 실행
-> AI 보안과 가드레일 적용
-> Auto Healing 워크플로우 설계
-> 로그, 추적, 운영 대시보드 구성
-> 미니 프로젝트 통합
```

## 왜 이 과정이 필요한가?

Agent 하나를 로컬에서 실행하는 것과 운영 가능한 AI 서비스를 만드는 것은 다릅니다.

운영 가능한 AI 서비스에는 다음이 필요합니다.

- 여러 Agent의 역할 분리
- API 서버와 Worker 분리
- Docker 기반 실행 환경
- 서비스 상태 확인
- 장애 대응 흐름
- 보안 정책과 권한 제어
- 로그와 실행 이력 관리
- 배포와 운영 자동화

## 최종적으로 만들 구조

```text
backend: 사용자 요청과 Agent 실행 API
frontend: 사용자 또는 운영자 화면
worker: 백그라운드 Agent 작업 실행
monitor: 상태, 로그, 이벤트 확인 화면
```

이 구조는 Docker Compose로 로컬에서 먼저 실행하고, 나중에 AWS 같은 클라우드로 확장할 수 있습니다.
