# 01. Course Big Picture

06 과정의 핵심은 **AI Agent 코드를 운영 가능한 서비스 구조로 확장하는 것**입니다.

04와 05에서 만든 Agent 코드는 로컬에서 잘 동작하는 데 초점이 있었습니다. 06에서는 이 코드를 여러 서비스로 나누고, 컨테이너로 실행하고, 장애와 보안과 로그를 함께 다룹니다.

## 04, 05, 06 연결

```text
04_llm-agent-orchestration
-> Agent, Tool, RAG, Memory, LangGraph 원리

05_llm-agent-mini-project
-> 단일 Agent 미니 프로젝트 구현

06_multi-agent-service-ops
-> Multi-Agent 서비스를 Docker Compose, CI/CD, AWS, 보안, Auto Healing, 모니터링으로 확장
```

## 06의 핵심 질문

- 여러 Agent는 어떤 역할로 나뉘는가?
- Agent 간에는 어떤 Context를 넘기는가?
- 서비스를 Docker image로 어떻게 패키징하는가?
- backend, frontend, worker, monitor는 Docker Compose에서 어떻게 함께 실행되는가?
- 장애가 발생하면 어떻게 감지하고 복구하는가?
- 운영 로그와 trace를 어떻게 남기는가?
- GitHub Actions는 어떤 검증을 자동으로 해주는가?
- AWS로 옮길 때 image, port, env, log는 어떻게 연결되는가?

## 최종 목표

06을 마치면 아래 구조를 설명하고 실행할 수 있어야 합니다.

```text
사용자 요청
-> frontend
-> backend
-> supervisor agent
-> diagnosis/recovery/validation agent
-> worker
-> logs/events
-> monitor dashboard
```
