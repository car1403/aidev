# Lab 01. Docker로 n8n 실행

## 목표

Docker로 n8n을 실행하고 브라우저에서 접속합니다.

## 실행

```powershell
docker run -it --rm `
 --name n8n-ai-workflow `
 -p 5678:5678 `
 -v n8n-data:/home/node/.n8n `
 n8nio/n8n:latest
```

## 확인

브라우저에서 접속합니다.

```text
http://localhost:5678
```

## 체크리스트

```text
[ ] Docker Desktop이 실행 중인가?
[ ] 5678 포트로 접속되는가?
[ ] n8n 첫 화면이 열리는가?
[ ] 워크플로우 생성 화면에 접근할 수 있는가?
```
