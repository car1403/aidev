# 03_ch3_openai-vs-llama-comparison

이 챕터에서는 같은 질문을 OpenAI 모델과 로컬 Llama 모델에 보내고 응답 차이를 비교합니다.

## 핵심 개념

- OpenAI 기본 모델은 `gpt-4.1-mini`입니다.
- Llama는 Docker/Ollama로 실행하는 로컬 모델입니다.
- 모델별로 응답 속도, 문체, 정확도, 비용 구조가 달라질 수 있습니다.

## 실행

```powershell
cd C:\aidev\04_llm-agent-orchestration\01_llm-api-and-prompt-basics
.\.venv\Scripts\Activate.ps1
python .\03_ch3_openai-vs-llama-comparison\01_compare-basic-answer.py
python .\03_ch3_openai-vs-llama-comparison\02_compare-prompt-style.py
```

## 기록할 내용

- 두 모델의 응답 길이
- 두 모델의 설명 방식
- 더 이해하기 쉬웠던 응답
- 실습 프로젝트에서 어떤 모델을 우선 사용할지에 대한 이유

