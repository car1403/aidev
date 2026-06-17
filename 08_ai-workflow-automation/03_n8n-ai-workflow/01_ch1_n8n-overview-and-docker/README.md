# 01_ch1_n8n-overview-and-docker

n8n의 기본 개념과 Docker 실행 방법을 학습하는 챕터입니다.

## 핵심 질문

- n8n은 어떤 자동화 문제를 해결하는가?
- n8n의 노드는 어떤 역할을 하는가?
- Docker로 n8n을 실행하면 어떤 장점이 있는가?
- AI 워크플로우에서 n8n은 어느 위치에 들어가는가?

## n8n 기본 구조

```text
Trigger Node
-> Data Processing Node
-> Condition Node
-> External API Node
-> Response / Notification Node
```

## Docker 실행

```powershell
docker run -it --rm `
  --name n8n-ai-workflow `
  -p 5678:5678 `
  -v n8n-data:/home/node/.n8n `
  n8nio/n8n:latest
```

접속 주소:

```text
http://localhost:5678
```

## 예제 실행

```powershell
cd C:\aidev\08_ai-workflow-automation\03_n8n-ai-workflow
python .\01_ch1_n8n-overview-and-docker\01_n8n_node_map.py
```
