# 05 AWS Deployment Map

이 문서는 06 과정에서 다루는 Docker 기반 서비스를 AWS로 확장할 때의 큰 그림을 설명합니다.

## 로컬과 AWS 대응 관계

| 로컬 Docker 개념 | AWS 대응 예시 |
| --- | --- |
| Docker image | Amazon ECR |
| Docker container | ECS Task, EC2 Container |
| docker compose service | ECS Service |
| .env | Parameter Store, Secrets Manager |
| container logs | CloudWatch Logs |
| healthcheck | ALB Target Health Check, ECS Health Check |
| GitHub Actions | CI/CD 자동 빌드와 배포 |

## 초보자가 먼저 이해할 것

AWS 배포를 바로 시작하기 전에 아래가 먼저 되어야 합니다.

- 로컬에서 Docker 이미지가 빌드되는가?
- Docker Compose로 서비스가 실행되는가?
- `/health` 엔드포인트가 있는가?
- 환경 변수가 코드에 직접 들어가 있지 않은가?
- 로그가 표준 출력으로 남는가?
- AWS Region을 정했는가?
- 예상 비용과 삭제할 리소스를 확인했는가?

## 첫 배포 후보

```text
App Runner:
- 컨테이너 기반 웹 서비스를 비교적 간단히 배포
- 초보자 첫 배포 흐름 설명에 적합

ECS:
- 여러 컨테이너와 로드밸런서, Auto Scaling을 더 세밀하게 운영
- Docker Compose 서비스 구조를 AWS 운영 구조로 확장할 때 적합

EC2:
- 서버를 직접 관리
- 자유도는 높지만 OS, 보안, 네트워크 관리 책임이 큼
```

## 이후 확장 흐름

```text
Dockerfile 작성
-> docker compose로 로컬 검증
-> GitHub Actions로 build 확인
-> ECR에 이미지 push
-> ECS 또는 EC2에 배포
-> CloudWatch Logs/Alarm으로 운영 확인
```

## 비용과 보안

- AWS 리소스는 실행 중이면 비용이 발생합니다.
- 실습 후 사용하지 않는 서비스와 이미지를 삭제합니다.
- Access Key는 코드, README, 발표 자료, GitHub Actions 로그에 노출하지 않습니다.
- GitHub Actions에서 AWS 인증이 필요하면 Secrets 또는 OIDC 기반 인증을 사용합니다.
