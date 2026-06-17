# 01_ch1_prompt-design-patterns

이 챕터에서는 좋은 프롬프트를 만들기 위한 기본 패턴을 배웁니다.

## 핵심 개념

- Role은 LLM이 맡을 역할입니다.
- Instruction은 LLM이 수행할 작업입니다.
- Context는 답변에 필요한 배경 정보입니다.
- Few-shot은 원하는 답변 예시를 먼저 보여주는 방식입니다.

## 실행

```powershell
cd C:\aidev\04_llm-agent-orchestration\02_advanced-prompting-and-reasoning
.\.venv\Scripts\Activate.ps1
python .\01_ch1_prompt-design-patterns\01_role-and-context-prompt.py
python .\01_ch1_prompt-design-patterns\02_few-shot-style-prompt.py
```

## 확인 질문

- 역할을 명확히 주면 응답이 어떻게 달라지나요?
- 예시를 제공하면 왜 답변 형식이 안정될까요?

