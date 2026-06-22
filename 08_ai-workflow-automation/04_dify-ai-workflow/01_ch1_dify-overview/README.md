# 01_ch1_dify-overview

Dify의 전체 구조와 AI 앱 설계 관점을 이해하는 챕터입니다.

## 핵심 질문

- Dify는 어떤 종류의 AI 앱을 만들 수 있는가?
- Chatbot, Chatflow, Workflow는 어떻게 다른가?
- Knowledge는 어떤 역할을 하는가?
- Dify 앱을 외부 자동화 도구와 어떻게 연결할 수 있는가?

## Dify 앱 구성 요소

```text
App
-> Prompt / Instruction
-> Model
-> Knowledge
-> Tool
-> Workflow Nodes
-> API
-> Logs
```

## 예제 실행

```powershell
cd C:\aidev\08_ai-workflow-automation\04_dify-ai-workflow
python.\01_ch1_dify-overview\01_dify_app_map.py
```
