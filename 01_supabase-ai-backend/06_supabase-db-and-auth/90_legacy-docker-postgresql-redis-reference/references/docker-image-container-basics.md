# Docker image와 container 기초

## 핵심 개념

- image: 실행에 필요한 파일과 설정이 담긴 템플릿
- container: image를 실행한 실제 프로세스
- port mapping: 컨테이너 내부 포트를 PC 포트에 연결
- environment variable: 컨테이너 실행 시 전달하는 설정값

## 자주 쓰는 명령

```powershell
docker pull postgres
docker images
docker ps
docker ps -a
docker logs aidev-postgres
docker stop aidev-postgres
docker start aidev-postgres
docker rm aidev-postgres
```

## 수업 원칙

이 단원에서는 단일 컨테이너 실행을 먼저 익힙니다. `docker compose`는 여러 서비스를 한 번에 실행해야 하는 프로젝트 통합 단계에서 사용합니다.

