# Message Format Guide

LLM API는 보통 message 목록을 사용해 대화를 표현합니다.

## role

| role | 의미 |
| --- | --- |
| system | 모델의 역할과 규칙을 정합니다. |
| user | 사용자의 질문입니다. |
| assistant | 모델이 이전에 답변한 내용입니다. |

## 싱글턴 예시

```python
messages = [
 {"role": "system", "content": "You are a helpful backend tutor."},
 {"role": "user", "content": "FastAPI가 무엇인가요?"},
]
```

## 멀티턴 예시

```python
messages = [
 {"role": "system", "content": "You are a helpful backend tutor."},
 {"role": "user", "content": "FastAPI가 무엇인가요?"},
 {"role": "assistant", "content": "Python 웹 API 프레임워크입니다."},
 {"role": "user", "content": "그럼 Swagger는 어떤 역할인가요?"},
]
```

## 초보자가 기억할 점

멀티턴은 모델이 자동으로 기억하는 것이 아니라, 우리가 이전 대화를 다시 보내는 구조입니다.

