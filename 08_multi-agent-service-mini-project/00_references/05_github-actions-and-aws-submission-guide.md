# 05. GitHub Actions And AWS Submission Guide

07에서 GitHub Actions와 AWS 실제 배포는 필수가 아닙니다. 다만 운영형 서비스 프로젝트이므로, 자동 검증과 배포 확장 가능성을 문서에 정리하는 것을 권장합니다.

## GitHub Actions 권장 검증

최소 검증 흐름:

```text
push 또는 pull request
-> Python 문법 검사
-> docker compose config
-> Docker image build
```

확인할 파일:

```text
.github/workflows/docker-compose-check.yml
```

workflow가 저장소에서 실행되려면 `.github/workflows` 폴더가 GitHub 저장소 최상위에 있어야 합니다.

## GitHub Actions에 포함하면 좋은 항목

- Python 문법 검사
- Docker Compose 문법 검사
- Docker image build
- 테스트 명령 실행
- 실패 시 로그 확인

## AWS 배포 선택지

| 선택지 | 특징 | 07에서의 위치 |
| --- | --- | --- |
| App Runner | 컨테이너 기반 웹 서비스를 비교적 쉽게 배포 | 선택 실습 또는 배포 설계 문서 |
| ECS | 여러 컨테이너와 운영 설정을 세밀하게 관리 | 확장 설계 문서 |
| ECR | Docker image 저장소 | App Runner/ECS 배포 전 단계 |
| CloudWatch | 로그와 모니터링 | 운영 로그 확인 기준 |

## AWS 배포 문서에 들어갈 내용

- 어떤 서비스를 AWS에 올릴 것인가?
- Docker image는 어디에 저장할 것인가?
- 환경변수와 secret은 어떻게 관리할 것인가?
- Health Check path는 무엇인가?
- 로그는 어디에서 확인할 것인가?
- 실습 후 어떤 리소스를 삭제할 것인가?

## 비용 주의

AWS 리소스는 실행 중이면 비용이 발생할 수 있습니다. 실제 배포를 진행했다면 아래 항목을 반드시 확인합니다.

- App Runner service 삭제
- ECS service/task/cluster 삭제
- Load Balancer 삭제
- ECR image 삭제
- CloudWatch Log Group 삭제
- 사용하지 않는 IAM Access Key 비활성화
