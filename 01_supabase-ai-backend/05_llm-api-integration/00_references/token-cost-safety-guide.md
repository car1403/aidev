# Token Cost Safety Guide

LLM API는 사용량에 따라 비용이 발생할 수 있습니다.

## token

Token은 모델이 텍스트를 처리하는 단위입니다.

```text
입력 token
-> 사용자가 보낸 질문, system prompt, 이전 대화

출력 token
-> 모델이 생성한 답변
```

## 비용이 늘어나는 경우

```text
긴 질문을 보냄
긴 문서를 통째로 보냄
이전 대화를 계속 누적함
max_tokens를 크게 설정함
반복문 안에서 API를 여러 번 호출함
```

## 수업 중 안전 기준

```text
실제 API key가 없으면 mock 예제로 실습합니다.
실제 호출 전 API key와 결제 상태를 확인합니다.
반복문으로 실제 API를 대량 호출하지 않습니다.
과제에는 실제 key를 제출하지 않습니다.
.env 파일은 GitHub에 올리지 않습니다.
```
