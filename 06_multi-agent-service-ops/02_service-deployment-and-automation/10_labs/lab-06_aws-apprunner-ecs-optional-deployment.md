# Lab 06. AWS App Runner / ECS Optional Deployment

## 목표

Docker Compose로 실행한 AI 서비스를 AWS 배포 구조로 옮길 때 App Runner와 ECS 중 어떤 방식을 선택할지 비교하고, 배포 전후 체크리스트를 작성합니다.

이 Lab은 비용과 권한 설정이 필요할 수 있으므로 **선택 실습**입니다. 수업 안내 없이 실제 리소스를 만들기보다, 먼저 체크리스트를 작성하고 배포 흐름을 설명할 수 있는 것을 목표로 합니다.

## 1. App Runner를 선택하는 경우

App Runner는 컨테이너 웹 서비스를 비교적 단순하게 배포할 때 적합합니다.

작성할 것:

```text
1. ECR repository 이름
2. Docker image tag
3. 서비스 port
4. Health Check path
5. 필요한 환경변수
6. CloudWatch Logs 확인 위치
7. 실습 후 삭제할 리소스
```

확인 질문:

- App Runner가 어떤 image를 실행하는가?
- `/health` 경로가 올바르게 설정되어 있는가?
- API Key는 코드가 아니라 환경변수로 들어가는가?
- 배포 후 CloudWatch Logs를 어디에서 보는가?

## 2. ECS를 선택하는 경우

ECS는 더 세밀한 컨테이너 운영이 필요할 때 적합합니다.

작성할 것:

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

확인 질문:

- Task Definition에서 image, port, env가 맞게 설정되었는가?
- 외부 접속이 필요하면 Load Balancer와 Target Group이 필요한가?
- Health Check path가 backend의 `/health`와 맞는가?
- ECS Service가 실패하면 CloudWatch Logs에서 어떤 정보를 확인할 것인가?

## 3. App Runner와 ECS 비교

| 기준 | App Runner | ECS |
| --- | --- | --- |
| 난이도 | 낮음 | 중간 이상 |
| 초보자 첫 배포 | 적합 | 조금 복잡함 |
| 운영 제어 | 제한적 | 세밀함 |
| 여러 컨테이너 구성 | 제한적 | 유리함 |
| 네트워크 제어 | 단순 | VPC, Subnet, Security Group 이해 필요 |
| 추천 위치 | 첫 클라우드 배포 흐름 이해 | 운영 구조 확장 실습 |

## 4. 제출할 내용

- App Runner 또는 ECS 중 하나를 선택한 이유
- 배포 전 체크리스트
- 배포 후 확인 체크리스트
- 비용과 보안 주의 사항
- 실습 후 리소스 삭제 계획
