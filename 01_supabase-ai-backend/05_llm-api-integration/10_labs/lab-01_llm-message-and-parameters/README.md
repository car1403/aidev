# Lab 01. LLM 메시지와 파라미터 정리

LLM API를 호출하기 전에 가장 먼저 알아야 할 것은 **어떤 메시지를 어떤 설정값과 함께 보낼지**입니다.

이 실습에서는 실제 API를 호출하지 않습니다. 대신 Gemini API나 OpenAI API에 보낼 수 있는 메시지 구조와 파라미터를 Python 딕셔너리로 만들어 봅니다.

## 학습 목표

- `system`, `user`, `assistant` 역할의 의미를 구분합니다.
- 사용자의 질문과 메모 컨텍스트를 하나의 요청 구조로 정리합니다.
- `temperature`, `top_p`, `max_tokens`가 응답에 어떤 영향을 주는지 설명합니다.
- 01~03 과정의 기본 모델을 `gemini-2.5-flash-lite`로 정리합니다.

## 실행

```powershell
cd C:\aidev\01_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
python .\05_llm-api-integration\10_labs\lab-01_llm-message-and-parameters\starter.py
```

## 확인 질문

1. 사용자의 질문만 보내는 것과 메모 컨텍스트를 함께 보내는 것은 어떤 차이가 있나요?
2. `temperature` 값을 낮추면 어떤 종류의 답변이 더 잘 나오나요?
3. 이 구조를 나중에 Supabase에 저장한다면 어떤 필드를 저장하면 좋을까요?
