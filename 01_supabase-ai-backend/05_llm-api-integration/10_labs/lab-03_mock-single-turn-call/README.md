# Lab 03. Single-turn mock 호출

Single-turn 호출은 사용자의 질문 하나에 대해 AI가 한 번 답하는 구조입니다.

이 실습에서는 실제 Gemini API를 호출하지 않고, 요청 구조를 만든 뒤 mock 응답을 반환합니다. 이렇게 하면 비용 없이 LLM 연동 흐름을 먼저 이해할 수 있습니다.

## 학습 목표

- 사용자 질문과 메모 컨텍스트를 하나의 프롬프트로 정리합니다.
- mock 응답에 `provider`, `model`, `actual_api_called`를 포함합니다.
- 응답 토큰 수를 대략적으로 계산해 사용량 구조를 이해합니다.

## 실행

```powershell
cd C:\aidev\01_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
python .\05_llm-api-integration\10_labs\lab-03_mock-single-turn-call\starter.py
```
