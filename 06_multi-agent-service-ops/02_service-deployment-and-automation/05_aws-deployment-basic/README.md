# 05 AWS Deployment Basic

이 실습은 Docker 기반 AI 서비스를 AWS로 배포할 때 필요한 기본 흐름을 정리합니다.

AWS 실습은 비용이 발생할 수 있으므로 선택 실습으로 진행합니다.

## 기본 배포 흐름

```text
Docker image build
-> local container 실행 확인
-> /health 확인
-> ECR에 image push
-> App Runner 또는 ECS에서 image 실행
-> 환경변수와 port 설정
-> CloudWatch Logs 확인
-> 리소스 정리
```

## 주요 서비스

| 서비스 | 역할 |
| --- | --- |
| ECR | Docker image 저장 |
| App Runner | 컨테이너 웹 서비스를 간단히 배포 |
| ECS | 컨테이너 서비스를 세밀하게 운영 |
| CloudWatch | 로그와 지표 확인 |
| IAM | 권한 관리 |
| Secrets Manager | 비밀 값 관리 |

## 배포 전 체크리스트

- [ ] 로컬 Docker build 성공
- [ ] 로컬 container 실행 성공
- [ ] `/health` 정상 응답
- [ ] 필요한 환경변수 정리
- [ ] 포트 번호 확인
- [ ] 로그 확인 위치 정리
- [ ] 실습 후 리소스 삭제 계획 확인
