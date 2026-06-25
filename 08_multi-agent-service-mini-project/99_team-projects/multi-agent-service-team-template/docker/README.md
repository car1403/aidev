# Docker

이 폴더는 Docker Compose 운영 기준을 설명하는 문서 공간입니다.

실제 Compose 파일은 템플릿 루트의 `docker-compose.yml`입니다.

## 확인할 파일

```text
Dockerfile
docker-compose.yml
.env.example
```

## 실행 흐름

```powershell
Copy-Item .env.example .env
docker compose config
docker compose up --build
docker compose ps
docker compose logs worker
docker compose down
```

## Compose에서 확인할 것

- 서비스 이름이 명확한가?
- 포트가 충돌하지 않는가?
- `.env`가 연결되어 있는가?
- backend healthcheck가 있는가?
- frontend와 monitor가 backend에 의존하는가?
- worker 로그를 확인할 수 있는가?

## AWS 확장 시 확인할 것

- Docker image 이름
- ECR 저장 전략
- App Runner 또는 ECS 선택 기준
- 환경변수와 secret 관리
- CloudWatch Logs 연결
- 실습 후 리소스 삭제 계획
