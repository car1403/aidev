# 01_ch1_aipp-overview

AIPP 기반 AI 워크플로우의 큰 그림을 이해하는 챕터입니다.

## 핵심 질문

- AIPP 같은 워크플로우 도구는 어떤 문제를 해결하는가?
- AI 자동화 흐름은 어떤 노드로 구성되는가?
- LLM 노드와 Tool 노드는 어떻게 다르게 설계해야 하는가?
- 결과 검증과 로그 기록은 왜 필요한가?

## 기본 구조

```text
Start
-> Input
-> Classify
-> Retrieve
-> Generate
-> Validate
-> Notify
-> Log
```

## 실행

```powershell
cd C:\aidev\08_ai-workflow-automation\02_aipp-workflow
python.\01_ch1_aipp-overview\01_aipp_workflow_concept.py
```
