# 05_ch5_aws-deployment-basic

Docker 기반 AI 서비스를 AWS에 배포할 때 필요한 기본 개념을 학습합니다.

## 이 챕터의 위치

이 챕터는 바로 AWS 배포를 실습하기보다, Docker Compose로 만든 서비스를 AWS 배포 구조로 어떻게 옮기는지 이해하는 단계입니다.

초보자 수업에서는 먼저 로컬 Docker 실행 구조를 완성하고, 그 다음 AWS에서 어떤 서비스가 같은 역할을 하는지 연결합니다.

## 핵심 구성 요소

| 로컬 Docker 개념 | AWS에서 대응되는 개념 |
| --- | --- |
| Docker image | Amazon ECR image |
| docker compose service | ECS Service 또는 EC2 container |
| .env | Secrets Manager, Parameter Store, Task Definition env |
| docker compose logs | CloudWatch Logs |
| healthcheck | ALB Target Health Check, ECS Health Check |

## 초보자용 배포 선택지

| 선택지 | 특징 | 수업에서의 위치 |
| --- | --- | --- |
| App Runner | 컨테이너 웹 서비스를 비교적 간단히 배포 | 첫 AWS 배포 설명에 적합 |
| ECS | 컨테이너 운영을 세밀하게 제어 | 운영 구조 확장에 적합 |
| EC2 | 서버를 직접 관리 | 자유도는 높지만 초보자에게 부담 큼 |

처음에는 App Runner 또는 ECS 중 하나를 선택해 흐름을 이해합니다. 이 과정의 핵심은 특정 AWS 서비스를 외우는 것이 아니라, Docker image가 클라우드에서 어떻게 실행되는지 이해하는 것입니다.

## AWS 배포 전 체크리스트

- Docker 이미지가 로컬에서 빌드되는가?
- 컨테이너가 로컬에서 정상 실행되는가?
- `/health` 엔드포인트가 있는가?
- 환경 변수가 코드에 직접 박혀 있지 않은가?
- 로그가 표준 출력으로 남는가?
- 포트가 명확히 정리되어 있는가?
- AWS Region을 정했는가?
- 예상 비용을 확인했는가?
- 실습 후 삭제할 리소스 목록을 적었는가?

## 선택 실습 1. App Runner 배포 체크리스트

App Runner는 초보자가 컨테이너 기반 웹 서비스를 처음 배포할 때 비교적 단순하게 접근할 수 있는 선택지입니다.

| 항목 | 확인 내용 |
| --- | --- |
| Container image | ECR에 push할 image 이름과 tag를 정했는가? |
| Port | FastAPI backend가 사용하는 port를 알고 있는가? |
| Health check | `/health` endpoint가 200 응답을 반환하는가? |
| Environment variables | `.env` 값을 App Runner 환경변수로 옮길 목록을 정리했는가? |
| Secrets | API Key를 코드가 아니라 Secret/환경변수로 관리하는가? |
| Logs | App Runner 로그를 CloudWatch에서 확인할 수 있는가? |
| Cost cleanup | 실습 후 App Runner Service와 ECR image 삭제 계획이 있는가? |

초보자용 흐름:

```text
1. 로컬에서 docker build
2. 로컬에서 docker run으로 /health 확인
3. ECR repository 생성
4. Docker image를 ECR에 push
5. App Runner에서 ECR image 선택
6. Port와 환경변수 설정
7. 배포 후 App Runner URL로 /health 확인
8. CloudWatch Logs 확인
9. 실습 후 App Runner Service 정리
```

## 선택 실습 2. ECS 배포 체크리스트

ECS는 운영 구조를 더 세밀하게 다룰 수 있지만, App Runner보다 이해할 개념이 많습니다. 06 과정에서는 선택 확장으로 다루는 것이 적절합니다.

| 항목 | 확인 내용 |
| --- | --- |
| Cluster | ECS Cluster를 어떤 이름으로 만들 것인가? |
| Task Definition | image, port, env, CPU, memory를 정의했는가? |
| Service | 몇 개의 task를 실행할지 정했는가? |
| Networking | VPC, Subnet, Security Group을 이해했는가? |
| Load Balancer | 외부 접속이 필요하면 ALB와 Target Group을 설계했는가? |
| Health Check | Target Group 또는 ECS Health Check 경로가 `/health`와 맞는가? |
| Logs | CloudWatch Log Group 이름을 정했는가? |
| IAM | Task 실행 역할과 권한을 확인했는가? |
| Cleanup | Service, Task Definition, Cluster, ALB, Target Group, ECR image 삭제 계획이 있는가? |

초보자용 흐름:

```text
1. 로컬 Docker 실행 확인
2. ECR repository 생성
3. Docker image push
4. ECS Task Definition 작성
5. ECS Service 생성
6. Security Group과 port 확인
7. /health 확인
8. CloudWatch Logs 확인
9. 실습 후 비용이 발생하는 리소스 삭제
```

## AWS CLI 확인

```powershell
aws --version
aws configure
aws sts get-caller-identity
```

`aws sts get-caller-identity`는 현재 어떤 AWS 계정과 권한으로 접속 중인지 확인하는 명령입니다.

## 배포 흐름 예시

```text
1. 로컬에서 docker build
2. 로컬에서 docker run 또는 docker compose up으로 검증
3. /health endpoint 확인
4. Amazon ECR repository 생성
5. Docker image tag 지정
6. Docker image를 ECR에 push
7. App Runner 또는 ECS에서 image 실행
8. 환경변수와 port 설정
9. 외부 URL로 /health 확인
10. CloudWatch Logs 확인
11. 실습 후 리소스 삭제
```

## GitHub Actions와 연결할 때

```text
GitHub push
-> GitHub Actions 실행
-> Docker build
-> ECR login
-> ECR push
-> App Runner 또는 ECS 배포 갱신
```

실제 자동 배포에는 AWS 권한과 GitHub Secrets 설정이 필요합니다. 초보자 수업에서는 먼저 build 검증 workflow를 이해하고, AWS 자동 배포는 강사 안내에 따라 확장합니다.

## 이후 확장

```text
GitHub Actions
-> Docker image build
-> Amazon ECR push
-> ECS service deploy
-> CloudWatch logs/alarms
```

자동 배포까지 확장할 때는 먼저 `GitHub Actions -> Docker build`까지만 성공시키고, 이후 `ECR push -> App Runner/ECS deploy`를 단계별로 추가합니다. 초보자 수업에서는 AWS 권한, 비용, 리소스 삭제 계획을 확인한 뒤 진행합니다.

## 비용과 보안 주의

- AWS 리소스는 실행 중이면 비용이 발생할 수 있습니다.
- 실습 후 App Runner Service, ECS Service, Load Balancer, ECR image, CloudWatch Log Group 등을 정리합니다.
- AWS Access Key를 코드나 README에 적지 않습니다.
- GitHub Actions에 비밀 값이 필요하면 Repository Secrets를 사용합니다.
- 장기 Access Key 대신 OIDC 기반 인증을 사용하는 방식은 이후 고급 단계에서 다룹니다.
