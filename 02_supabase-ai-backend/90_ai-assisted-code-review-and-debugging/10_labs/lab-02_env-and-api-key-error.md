# Lab 02. Env and API Key Error

## 목표

Gemini/OpenAI 호출 전에 `.env` 위치와 key 이름을 확인합니다.

## 확인할 것

- `.env`가 현재 예제에서 읽는 위치에 있는가?
- 변수 이름이 문서와 같은가?
- 실제 key를 코드에 직접 적지 않았는가?
- Gemini 503은 코드 오류가 아니라 일시적인 서버 수요 문제일 수 있는가?

## Codex 질문 예시

```text
Gemini API 호출에 실패했습니다.

오류:
503 UNAVAILABLE 또는 API key 관련 오류

확인한 것:
GEMINI_API_KEY는 .env에 있고, 실제 값은 보안상 가렸습니다.

요청:
가능한 원인과 다음 확인 순서를 알려주세요.
```
