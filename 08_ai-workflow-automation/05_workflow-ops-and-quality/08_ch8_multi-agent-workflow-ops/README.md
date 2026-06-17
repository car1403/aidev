# 08_ch8_multi-agent-workflow-ops

Multi-Agent 기반 AI 워크플로우를 운영 관점에서 설계하는 챕터입니다.

08 과정은 AIPP, n8n, Dify 같은 노코드/로코드 도구 중심이지만, 복잡한 업무에서는 여러 Agent가 역할을 나누어 협업하는 구조가 필요합니다.

## 학습 목표

- Multi-Agent 협업 구조를 워크플로우 도구 관점으로 설계할 수 있습니다.
- 역할별 Agent의 입력, 출력, 책임을 정의할 수 있습니다.
- Agent 간 결과 전달과 품질 검증 흐름을 설계할 수 있습니다.
- 실행 로그와 운영 대시보드에서 Agent별 상태를 추적할 수 있습니다.

## 기본 구조

```text
Supervisor Agent
-> Classifier Agent
-> RAG Agent
-> Answer Agent
-> Review Agent
-> Ops Assistant
```

## 실행 예제

```powershell
cd C:\aidev\08_ai-workflow-automation\05_workflow-ops-and-quality
python .\08_ch8_multi-agent-workflow-ops\01_multi_agent_workflow_ops.py
```
