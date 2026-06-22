# 05. Docker And Local Tools

## 왜 Docker를 쓰는가?

AI 워크플로우 도구는 여러 서비스와 데이터를 함께 사용합니다.

Docker를 사용하면 로컬 PC에 복잡하게 직접 설치하지 않고 컨테이너로 실행할 수 있습니다.

```text
Docker Image: 실행 환경 템플릿
Docker Container: 실제 실행 중인 서비스
Docker Volume: 컨테이너가 삭제되어도 남는 데이터 저장소
Docker Compose: 여러 컨테이너를 함께 실행하는 설정
```

## n8n 실행 예시

```powershell
docker run -it --rm `
 --name n8n-ai-workflow `
 -p 5678:5678 `
 -v n8n-data:/home/node/.n8n `
 n8nio/n8n:latest
```

접속:

```text
http://localhost:5678
```

## Dify 실행 흐름

Dify self-host는 Docker Compose 기반으로 실행하는 흐름이 일반적입니다.

```powershell
git clone https://github.com/langgenius/dify.git
cd dify\docker
Copy-Item.env.example.env
docker compose up -d
```

접속:

```text
http://localhost/install
```

## 주의

```text
n8n과 Dify는 버전에 따라 설치 세부 방식이 달라질 수 있습니다.
실제 설치 전 공식 문서를 확인합니다.
Docker Volume에는 설정과 데이터가 남습니다.
포트 충돌이 나면 실행 포트를 바꿔야 합니다.
```

## 자주 쓰는 명령

```powershell
docker ps
docker ps -a
docker logs 컨테이너이름
docker stop 컨테이너이름
docker rm 컨테이너이름
docker volume ls
```
