# 02_llm-api-integration

이 단원은 FastAPI 백엔드에서 LLM API를 호출하는 기본 흐름을 다룹니다. 비용과 API Key 오류를 줄이기 위해 mock-first 방식으로 시작하고, 이후 Gemini SDK, Gemini REST 보충 예제, OpenAI 선택 비교 순서로 확장합니다.

## 학습 순서

1. [01_llm-api-concepts](./01_llm-api-concepts/README.md)에서 LLM API 요청/응답 구조를 이해합니다.
2. [02_api-key-and-billing](./02_api-key-and-billing/README.md)에서 API Key, 비용, 호출 제한을 확인합니다.
3. [03_single-turn-call](./03_single-turn-call/README.md)에서 단일 요청/응답 흐름을 실습합니다.
4. [04_multi-turn-call](./04_multi-turn-call/README.md)에서 대화 이력과 multi-turn 호출을 확인합니다.
5. [05_fastapi-llm-endpoint](./05_fastapi-llm-endpoint/README.md)에서 FastAPI 엔드포인트로 연결합니다.

## 기준

- 02~04 과정의 기본 LLM은 Gemini입니다.
- OpenAI 예제는 선택/비교 실습으로 유지합니다.
- 실제 API Key는 `.env`에만 넣고 GitHub에 올리지 않습니다.
