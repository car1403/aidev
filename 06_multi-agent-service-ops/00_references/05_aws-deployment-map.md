# 05. AWS Deployment Map

AWS 배포는 선택 실습입니다. 비용이 발생할 수 있으므로 실제 배포 전에는 구조와 정리 방법을 먼저 이해합니다.

## 기본 배포 흐름

```text
로컬 Docker image build
-> 로컬 container 실행 확인
-> /health 확인
-> ECR에 image push
-> App Runner 또는 ECS에서 image 실행
-> 환경변수와 port 설정
-> CloudWatch Logs 확인
-> 실습 후 리소스 정리
```

## 주요 서비스

| 서비스 | 역할 |
| --- | --- |
| ECR | Docker image 저장소 |
| App Runner | 컨테이너 앱을 비교적 간단하게 배포 |
| ECS | 컨테이너 서비스를 더 세밀하게 운영 |
| CloudWatch | 로그와 지표 확인 |
| IAM | 권한 관리 |
| Secrets Manager | 비밀 값 관리 |
| Parameter Store | 설정 값 관리 |

## App Runner와 ECS 선택 기준

| 방식 | 적합한 경우 |
| --- | --- |
| App Runner | 처음 배포를 배우고 싶을 때, 단순한 웹 서비스 |
| ECS | 여러 컨테이너와 네트워크, 로드밸런서를 더 직접 다루고 싶을 때 |

## 비용 주의

- 실습 후 App Runner Service, ECS Service, Load Balancer, ECR image를 정리합니다.
- CloudWatch Log Group도 남아 있을 수 있습니다.
- AWS Access Key는 코드나 GitHub에 올리지 않습니다.
