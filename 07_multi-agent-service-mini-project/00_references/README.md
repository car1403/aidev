# 00 References

`07_multi-agent-service-mini-project`를 시작하기 전에 확인하는 참고 자료입니다.

07의 목표는 06에서 배운 운영형 Multi-Agent 구조를 실제 미니 프로젝트 산출물로 바꾸는 것입니다. 따라서 이 폴더의 문서는 개념 설명뿐 아니라 프로젝트 설계, 실행, 제출 기준을 함께 확인하는 기준서로 사용합니다.

## 읽는 순서

1. [01_project-big-picture.md](./01_project-big-picture.md)
2. [02_auto-healing-scenario.md](./02_auto-healing-scenario.md)
3. [03_docker-compose-service-map.md](./03_docker-compose-service-map.md)
4. [04_team-project-checklist.md](./04_team-project-checklist.md)
5. [05_github-actions-and-aws-submission-guide.md](./05_github-actions-and-aws-submission-guide.md)
6. [06_project-alignment-checklist.md](./06_project-alignment-checklist.md)

## 문서별 역할

| 문서 | 역할 |
| --- | --- |
| `01_project-big-picture.md` | Auto Healing Multi-Agent 프로젝트의 전체 흐름을 이해합니다. |
| `02_auto-healing-scenario.md` | 장애 유형, 복구 전략, Feedback Loop 예시를 확인합니다. |
| `03_docker-compose-service-map.md` | backend, frontend, worker, monitor 서비스 구조를 확인합니다. |
| `04_team-project-checklist.md` | 팀 구성, 역할, 산출물, 시연 기준을 확인합니다. |
| `05_github-actions-and-aws-submission-guide.md` | GitHub Actions와 AWS 선택 확장 기준을 확인합니다. |
| `06_project-alignment-checklist.md` | 06 보강 내용과 07 프로젝트 산출물이 일치하는지 확인합니다. |

## 핵심 기준

07 최종 프로젝트는 아래 네 가지가 동시에 보여야 합니다.

```text
1. Multi-Agent 협업 구조
2. Docker Compose 기반 서비스 실행
3. Auto Healing과 결과 검증
4. 운영 로그, 감사 로그, 보안 가드레일
```

GitHub Actions와 AWS 실제 배포는 필수가 아니지만, 운영형 서비스로 확장할 수 있는 체크리스트는 문서에 포함하는 것을 권장합니다.
