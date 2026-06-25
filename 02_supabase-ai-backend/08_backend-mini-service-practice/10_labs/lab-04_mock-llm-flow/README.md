# Lab 04. Mock LLM Flow

## 목표

실제 LLM API를 호출하기 전에 mock-first 함수로 답변 생성 흐름을 이해합니다.

## 확인 파일

```text
../04_implementation-guide/llm_mock.py
```

## 확인할 내용

- `generate_mock_answer()` 함수가 어떤 값을 받나요?
- 함수가 실제 외부 API를 호출하나요?
- mock 함수를 먼저 사용하는 이유는 무엇인가요?
- 나중에 Gemini SDK를 연결한다면 어느 위치를 바꾸면 될까요?

## 정리할 내용

mock-first 함수와 실제 Gemini SDK 호출 함수의 차이를 적어 봅니다.
