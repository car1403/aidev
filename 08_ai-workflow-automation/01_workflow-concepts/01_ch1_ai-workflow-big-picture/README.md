# 01_ch1_ai-workflow-big-picture

AI 워크플로우의 전체 구조를 이해하는 챕터입니다.

## 핵심 질문

- AI 워크플로우는 일반 자동화와 무엇이 다른가?
- 업무 요청을 어떤 단계로 나누어야 하는가?
- LLM은 전체 흐름 중 어느 위치에서 사용되는가?
- 도구 실행, 결과 검증, 로그 기록은 왜 필요한가?

## 기본 흐름

```text
Trigger
-> Input
-> Classify
-> Retrieve
-> Generate
-> Validate
-> Action
-> Log
```

## 실행

```powershell
cd C:\aidev\08_ai-workflow-automation\01_workflow-concepts
python .\01_ch1_ai-workflow-big-picture\01_ai_workflow_map.py
```

## 학습 포인트

- 워크플로우는 한 번에 코딩하지 않고 단계로 나눈다.
- 각 단계의 입력과 출력을 명확히 해야 한다.
- AI가 필요한 단계와 규칙 기반으로 처리할 단계를 구분한다.
- 운영 단계에서는 실행 기록이 반드시 필요하다.
