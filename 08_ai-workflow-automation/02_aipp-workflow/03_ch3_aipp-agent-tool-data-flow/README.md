# 03_ch3_aipp-agent-tool-data-flow

Agent, Tool, Data 노드 사이의 입력/출력 흐름을 설계하는 챕터입니다.

## 핵심 질문

- 각 노드는 어떤 데이터를 받아야 하는가?
- 각 노드는 어떤 데이터를 다음 노드로 넘겨야 하는가?
- 어떤 데이터는 Memory에 저장해야 하는가?
- 어떤 결과는 로그로 남겨야 하는가?

## 기본 흐름

```text
Input Data
-> Agent 판단
-> Tool 실행
-> Data 정리
-> Agent 응답 생성
-> 검증
-> Output
```

## 실행

```powershell
cd C:\aidev\08_ai-workflow-automation\02_aipp-workflow
python .\03_ch3_aipp-agent-tool-data-flow\01_agent_tool_data_flow.py
```
