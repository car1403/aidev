# 01_ch1_openai-api-basic

이 챕터에서는 OpenAI API를 Python에서 처음 호출하는 흐름을 배웁니다.

## 핵심 개념

- `.env` 파일에서 `OPENAI_API_KEY`와 `OPENAI_MODEL`을 읽습니다.
- 기본 모델은 `gpt-4.1-mini`를 사용합니다.
- API Key가 없을 때 예제가 어떻게 안전하게 종료되는지 확인합니다.
- 메시지 스타일을 바꾸면 응답이 어떻게 달라지는지 살펴봅니다.

## 실행

```powershell
cd C:\aidev\04_llm-agent-orchestration\01_llm-api-and-prompt-basics
.\.venv\Scripts\Activate.ps1
python .\01_ch1_openai-api-basic\01_check-env.py
python .\01_ch1_openai-api-basic\02_openai-basic-response.py
python .\01_ch1_openai-api-basic\03_openai-message-style.py
```

## 확인 질문

- 환경 변수는 왜 코드에 직접 적지 않을까요?
- `gpt-4.1-mini`는 어떤 실습에 적합할까요?
- API 호출 실패 시 학생은 무엇을 먼저 확인해야 할까요?

