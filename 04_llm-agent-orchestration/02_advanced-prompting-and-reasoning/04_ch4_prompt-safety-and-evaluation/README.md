# 04_ch4_prompt-safety-and-evaluation

이 챕터에서는 Prompt Injection을 이해하고 프롬프트 버전별 품질을 비교합니다.

## 핵심 개념

- Prompt Injection은 사용자가 시스템 지시문을 무시하게 만들려는 공격입니다.
- 입력 검증은 위험한 요청을 먼저 걸러내는 과정입니다.
- 프롬프트 버전 평가는 어떤 프롬프트가 더 안정적인지 비교하는 과정입니다.

## 실행

```powershell
cd C:\aidev\04_llm-agent-orchestration\02_advanced-prompting-and-reasoning
.\.venv\Scripts\Activate.ps1
python .\04_ch4_prompt-safety-and-evaluation\01_prompt-injection-defense.py
python .\04_ch4_prompt-safety-and-evaluation\02_prompt-version-evaluation.py
```

## 확인 질문

- 사용자의 입력을 그대로 믿으면 어떤 문제가 생길까요?
- 프롬프트 품질은 어떤 기준으로 평가할 수 있을까요?

