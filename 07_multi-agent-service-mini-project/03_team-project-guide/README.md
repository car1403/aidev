# 03 Team Project Guide

팀별 Auto Healing Multi-Agent Service 프로젝트 진행 문서입니다.

이번 미니 프로젝트의 기준 주제는 **에러 자가 치유(Auto Healing) 워크플로우**입니다. `06_multi-agent-service-ops`에서 배운 Multi-Agent 협업, Docker Compose, GitHub Actions, AWS 배포 설계, 모니터링, 장애 복구 흐름을 하나의 운영형 미니 프로젝트로 묶습니다.

## 프로젝트 큰 방향

```text
1. 에이전트 협업 시나리오 및 구조 설계
2. 장애 유형별 복구 로직 및 자동화 파이프라인 구현
3. 협업 기반 실행 흐름 통합 구현
4. 서비스 배포 및 결과 검증
```

## 필수 산출물

| 산출물 | 설명 |
| --- | --- |
| 멀티 에이전트 아키텍처 설계서 | Agent 역할, 책임, 의존 관계, Handoff, Context 공유 구조를 정리 |
| 배포 및 장애 복구 보고서 | Docker Compose, 장애 감지, 자동 복구, 수동 개입 기준을 정리 |
| 파이프라인 구현 결과 보고서 | 코드 커밋부터 빌드, 테스트, 배포, 알림까지의 CI/CD 흐름을 정리 |

## 문서 목록

```text
01_topic-selection.md
02_role-and-schedule.md
03_project-requirements.md
04_test-checklist.md
05_final-presentation.md
06_submission-checklist.md
```

## 제출 전 확인할 것

- 아키텍처 구조가 비즈니스 요구사항에 맞게 선택되었는가?
- 각 Agent의 역할과 책임 범위가 중복 없이 정의되었는가?
- Agent 간 작업 전달 시 Context가 누락 없이 전달되는가?
- Docker Compose 배포 매니페스트가 작성되었는가?
- 서비스 디스커버리, 로드밸런싱, 시크릿 관리가 고려되었는가?
- 장애 유형별 감지 메트릭과 복구 전략이 정리되었는가?
- 커밋, 빌드, 테스트, 배포, 알림 파이프라인 흐름이 문서화되었는가?
