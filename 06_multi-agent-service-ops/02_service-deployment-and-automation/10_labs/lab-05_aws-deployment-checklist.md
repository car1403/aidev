# Lab 05. AWS Deployment Checklist

## 목표

Docker Compose 서비스를 AWS 배포 구조로 옮기기 전에 필요한 항목을 점검합니다.

## 작성할 것

- 이미지 이름
- 필요한 포트
- 환경 변수 목록
- Health Check URL
- 로그 확인 위치
- 배포 대상 후보: EC2, ECS, App Runner 중 하나

## 배포 전 확인 질문

- 로컬에서 `docker build`가 성공했는가?
- 로컬에서 `docker run` 또는 `docker compose up`으로 서비스가 실행되는가?
- `/health`가 정상 응답을 반환하는가?
- CloudWatch에서 확인해야 할 로그 이름을 정했는가?
- AWS 비용이 발생할 수 있는 리소스를 알고 있는가?
- 실습 후 삭제할 리소스를 목록으로 적었는가?

## 배포 후 확인 질문

- 외부 URL에서 `/health`가 정상 응답을 반환하는가?
- 환경변수가 누락되지 않았는가?
- API Key나 Access Key가 로그에 출력되지 않는가?
- 오류가 발생했을 때 CloudWatch Logs에서 원인을 찾을 수 있는가?
- 실습 후 App Runner, ECS, ECR, Load Balancer, CloudWatch Log Group 정리 계획이 있는가?
