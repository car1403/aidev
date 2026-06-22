# 02_ch2_llm-tool-memory-workflow

AI 워크플로우 안에서 LLM, Tool, Memory가 어떤 역할을 하는지 학습하는 챕터입니다.

## 핵심 개념

```text
LLM: 텍스트 이해, 분류, 요약, 생성, 판단
Tool: 외부 API, 데이터 조회, 파일 처리, 알림 전송
Memory: 이전 대화, 사용자 정보, 실행 이력, 선호도
```

## 왜 분리해서 이해해야 하나?

LLM이 모든 일을 직접 처리하는 구조는 운영하기 어렵습니다.

예를 들어 사용자의 주문 상태를 확인하려면 LLM이 상상해서 답하면 안 됩니다. 주문 DB를 조회하는 Tool을 호출해야 합니다.

```text
사용자 질문
-> LLM이 필요한 작업 판단
-> Tool로 실제 데이터 조회
-> Memory에서 사용자 맥락 확인
-> LLM이 최종 답변 생성
```

## 실행

```powershell
cd C:\aidev\08_ai-workflow-automation\01_workflow-concepts
python.\02_ch2_llm-tool-memory-workflow\01_llm_tool_memory_flow.py
```

## 학습 포인트

- LLM은 판단과 생성에 강하다.
- Tool은 실제 작업 수행에 필요하다.
- Memory는 개인화와 연속성을 만든다.
- 운영 가능한 워크플로우는 각 역할을 분리해서 설계해야 한다.
