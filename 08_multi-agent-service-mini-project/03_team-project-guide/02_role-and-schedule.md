# 02. Role And Schedule

프로젝트는 역할을 먼저 정하고 시작하면 훨씬 안정적으로 진행됩니다.

## 팀 구성

권장 팀 구성은 4~5명입니다.

| 역할 | 주요 책임 | 결과물 |
| --- | --- | --- |
| API 담당 | backend API, Health Check, 장애 이벤트 모델 | `backend/main.py`, backend 설명 |
| Worker 담당 | 장애 분류, 복구 전략, Feedback Loop | `worker/main.py`, 복구 흐름 문서 |
| UI/Monitor 담당 | frontend, monitor 화면 구성 | `frontend/app.py`, `monitor/app.py` |
| Docker/CI 담당 | Docker Compose, GitHub Actions 검증 | `docker-compose.yml`, workflow |
| 문서/QA 담당 | 산출물 문서, 테스트 체크리스트, 발표 흐름 | `docs/*.md` |

## 일정 예시

| 순서 | 작업 |
| --- | --- |
| 1 | 샘플 프로젝트 실행 |
| 2 | 주제와 장애 유형 결정 |
| 3 | Agent 역할과 Context 설계 |
| 4 | backend/worker 기본 구현 |
| 5 | frontend/monitor 화면 구현 |
| 6 | Docker Compose 통합 실행 |
| 7 | 테스트 체크리스트 작성 |
| 8 | 발표 시나리오 정리 |

## 회의 때 확인할 질문

- 오늘 수정할 파일은 무엇인가?
- 현재 막힌 부분은 무엇인가?
- Docker Compose 실행은 정상인가?
- Health Check는 통과하는가?
- 문서와 코드가 같은 구조를 설명하고 있는가?
