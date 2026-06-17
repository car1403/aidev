# 05 GitHub Actions and AWS Submission Guide

이 문서는 07 팀 미니 프로젝트에서 GitHub Actions와 AWS 배포 체크리스트를 어떻게 제출물에 반영할지 설명합니다.

07의 필수 목표는 Docker Compose 기반 Auto Healing Multi-Agent 서비스를 완성하는 것입니다. GitHub Actions와 AWS 실제 배포는 선택 항목이지만, 운영형 프로젝트를 설명하려면 최소한의 설계와 체크리스트는 포함하는 것이 좋습니다.

## GitHub Actions 제출 기준

GitHub Actions를 적용하는 팀은 아래 항목을 확인합니다.

```text
workflow 파일 위치:
.github/workflows/docker-compose-check.yml

검증 항목:
- Python 문법 검사
- docker compose config
- Docker image build
```

팀 템플릿에는 예시 workflow가 포함되어 있습니다.

```text
99_team-projects/multi-agent-service-team-template/.github/workflows/docker-compose-check.yml
```

실제 GitHub 저장소에서 자동 실행하려면 저장소 최상위 `.github/workflows` 아래에 위치해야 합니다.

## AWS 배포 체크리스트

실제 AWS 배포를 하지 않더라도 아래 항목을 문서로 정리합니다.

```text
1. Docker image를 어디에 저장할 것인가?       예: Amazon ECR
2. 어떤 AWS 서비스로 실행할 것인가?            예: App Runner 또는 ECS
3. 환경변수와 secret은 어떻게 관리할 것인가?   예: Secrets Manager, Parameter Store
4. Health Check 경로는 무엇인가?               예: /health
5. 로그는 어디서 볼 것인가?                    예: CloudWatch Logs
6. 장애 감지는 어떻게 할 것인가?               예: Health Check, Alarm
7. 실습 후 어떤 리소스를 삭제할 것인가?         예: Service, image, log group
```

## App Runner와 ECS 선택 기준

| 기준 | App Runner | ECS |
| --- | --- | --- |
| 난이도 | 낮음 | 중간 이상 |
| 첫 배포 적합성 | 초보자 첫 클라우드 배포 설명에 적합 | 운영 구조 확장 설명에 적합 |
| 운영 제어 | 제한적 | 세밀함 |
| 여러 서비스 구성 | 단일 웹 서비스에 적합 | backend, worker, monitor 등 확장에 적합 |
| 주요 체크 항목 | image, port, env, health check, log | cluster, task definition, service, security group, ALB, log |

## App Runner 체크리스트

```text
1. ECR repository 이름
2. Docker image tag
3. 서비스 port
4. Health Check path
5. 필요한 환경변수
6. CloudWatch Logs 확인 위치
7. 실습 후 삭제할 리소스
```

## ECS 체크리스트

```text
1. ECS Cluster 이름
2. Task Definition 이름
3. Container image URI
4. Container port
5. CPU/Memory 설정
6. Security Group inbound rule
7. Load Balancer 사용 여부
8. CloudWatch Log Group 이름
9. 실습 후 삭제할 리소스
```

## 비용과 보안 주의

- AWS 리소스는 실행 중이면 비용이 발생할 수 있습니다.
- AWS Access Key는 코드, README, 발표 자료, GitHub Actions 로그에 노출하지 않습니다.
- GitHub Actions에서 비밀 값이 필요하면 Repository Secrets를 사용합니다.
- 실습 후 App Runner, ECS Service, Load Balancer, ECR image, CloudWatch Log Group을 정리합니다.

## 발표에 포함하면 좋은 내용

```text
Docker Compose 서비스 구조
Auto Healing 장애 대응 흐름
Health Check와 로그 확인 방법
GitHub Actions로 자동 검증하는 항목
AWS로 배포한다면 사용할 서비스와 이유
비용과 보안 주의 사항
```
