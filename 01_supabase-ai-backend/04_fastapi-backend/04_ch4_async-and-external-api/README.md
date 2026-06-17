# 04_ch4_async-and-external-api

비동기 엔드포인트와 외부 API 호출 구조를 학습합니다.

이 챕터는 이후 LLM API, Supabase, SSE 스트리밍으로 확장하기 위한 준비 단계입니다.

## 예제 파일

```text
01_async-endpoint.py
02_external-api-structure.py
03_ai-api-call-placeholder.py
04_streaming-response.py
```

## 학습 기준

- `async def`와 `await`의 기본 의미를 이해합니다.
- 외부 API 호출 실패를 `HTTPException`으로 바꾸는 흐름을 봅니다.
- 실제 LLM API 호출 전, placeholder 함수로 전체 구조를 먼저 이해합니다.
- StreamingResponse는 기초만 확인하고, SSE 기반 AI 응답 스트리밍 통합은 `03_supabase-ai-mini-project`에서 다룹니다.

