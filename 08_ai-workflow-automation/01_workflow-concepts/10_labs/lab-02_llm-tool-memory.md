# Lab 02. LLM, Tool, Memory 역할 구분

## 목표

AI 워크플로우에서 LLM, Tool, Memory가 각각 맡아야 할 일을 구분합니다.

## 준비

```powershell
cd C:\aidev\08_ai-workflow-automation\01_workflow-concepts
python .\02_ch2_llm-tool-memory-workflow\01_llm_tool_memory_flow.py
```

## 할 일

아래 작업을 LLM, Tool, Memory 중 어디에 배치해야 하는지 분류합니다.

```text
1. 고객 문의 유형 분류
2. 주문 번호로 결제 내역 조회
3. 이전 문의 이력 확인
4. 답변 문장 생성
5. 슬랙 알림 전송
6. 사용자 선호 언어 확인
7. 답변의 위험 표현 검토
```

## 결과물

```text
LLM:
Tool:
Memory:
이유:
```

## 추가 실습

`01_llm_tool_memory_flow.py`에서 `user_message` 값을 바꾸고 분류 결과가 어떻게 달라지는지 확인합니다.
