# 06_backend-security-review-with-codex

FastAPI, LLM API, Supabase, Upstash Redis 코드에서 보안과 비용 위험을 점검하는 단원입니다.

## 학습 목표

- API key와 token이 코드나 로그에 노출되지 않았는지 확인합니다.
- 실제 LLM API 호출이 비용을 과도하게 발생시키지 않는지 점검합니다.
- Supabase service role key를 안전하게 사용하는 기준을 설명합니다.
- Codex에게 보안 리뷰를 요청할 때 어떤 관점을 지정해야 하는지 익힙니다.

## 리뷰 대상 예시

```text
05_llm-api-integration
06_supabase-db-and-auth
08_backend-mini-service-practice
```

## Codex 요청 예시

```text
아래 코드를 보안과 비용 관점에서 리뷰해줘.

중점 확인:
1. API key나 token이 출력되는 부분이 있는가?
2. 실제 LLM API 호출이 반복문에서 과도하게 실행될 수 있는가?
3. Supabase service role key가 프론트엔드에 노출될 가능성이 있는가?
4. 로그 metadata에 민감 정보가 들어갈 수 있는가?
5. 초보자가 수정할 수 있는 방식으로 개선안을 제안해줘.
```

## 수업 진행 팁

먼저 mock 예제는 안전하다는 점을 확인합니다. 그 다음 실제 API 호출 파일을 보며 비용이 발생할 수 있는 위치를 표시합니다.

