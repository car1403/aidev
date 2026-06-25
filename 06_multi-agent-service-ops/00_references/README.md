# 00 References

이 폴더는 `06_multi-agent-service-ops` 과정의 참고 문서를 모아둔 곳입니다.

06 과정은 Docker Compose, GitHub Actions, AWS, 보안, Auto Healing, 로그와 모니터링처럼 운영 관련 개념이 많이 등장합니다. 실습 중 개념이나 명령어가 헷갈리면 이 폴더의 문서를 먼저 확인합니다.

## 문서 목록

| 문서 | 내용 |
| --- | --- |
| `01_course-big-picture.md` | 06 과정의 전체 그림과 04/05와의 차이 |
| `02_environment-checklist.md` | Python, Docker, Git, AWS 환경 확인 |
| `03_multi-agent-service-map.md` | Multi-Agent 서비스를 backend, worker, monitor로 나누어 보는 방법 |
| `04_docker-compose-and-service-ops.md` | Docker Compose 기본 개념과 자주 쓰는 명령어 |
| `05_aws-deployment-map.md` | ECR, App Runner, ECS, CloudWatch 관계 |
| `06_security-guardrails-overview.md` | Prompt Injection, 정책 검증, Tool 권한 |
| `07_auto-healing-overview.md` | 장애 감지, 재시도, 복구, 검증 흐름 |
| `08_observability-ops-dashboard.md` | 로그, tracing, 운영 대시보드 개념 |
| `09_common-errors-for-beginners.md` | 자주 발생하는 오류와 해결 방법 |
| `10_final-project-roadmap.md` | 99 미니 프로젝트 진행 순서 |
| `11_course-alignment-checklist.md` | 이미지 기준 학습 항목과 폴더 매핑 |

## 읽는 순서

처음에는 아래 순서로 읽는 것이 좋습니다.

```text
01_course-big-picture
-> 02_environment-checklist
-> 04_docker-compose-and-service-ops
-> 03_multi-agent-service-map
-> 06_security-guardrails-overview
-> 07_auto-healing-overview
-> 08_observability-ops-dashboard
```

AWS는 비용이 발생할 수 있으므로 `05_aws-deployment-map.md`를 먼저 읽고, 실제 배포는 안내에 따라 선택적으로 진행합니다.
