# 03_ch3_reasoning-and-react-basics

이 챕터에서는 LLM이 문제를 단계적으로 처리하는 흐름을 학습합니다.

## 핵심 개념

- Plan은 먼저 해결 순서를 정리하는 단계입니다.
- Act는 실제 행동 또는 도구 호출에 해당하는 단계입니다.
- Review는 결과를 검토하고 수정하는 단계입니다.
- ReAct는 Reasoning과 Action을 번갈아 사용하는 패턴입니다.

## 실행

```powershell
cd C:\aidev\04_llm-agent-orchestration\02_advanced-prompting-and-reasoning
.\.venv\Scripts\Activate.ps1
python .\03_ch3_reasoning-and-react-basics\01_plan-act-review-pattern.py
python .\03_ch3_reasoning-and-react-basics\02_react-style-without-tools.py
```

## 확인 질문

- 바로 답변하는 것과 계획을 세운 뒤 답변하는 것은 무엇이 다른가요?
- ReAct에서 Action은 어떤 역할을 하나요?

