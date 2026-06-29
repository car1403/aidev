# 코드 리뷰 요청 템플릿

코드 리뷰를 요청할 때는 "좋게 고쳐줘"보다 어떤 관점으로 볼지 먼저 정하는 것이 중요합니다.

## 일반 코드 리뷰 요청 템플릿

```text
아래 코드를 리뷰해주세요.

코드 목적:

리뷰 관점:
1. 실행 오류 가능성
2. 요구사항 충족 여부
3. 입력값 검증
4. 변수명과 함수명
5. 중복 코드
6. 초보자가 이해하기 쉬운 구조

출력 형식:
- 반드시 수정할 문제
- 수정하면 좋은 문제
- 지금은 보류해도 되는 문제
- 확인 질문

아직 코드를 수정하지 말고 리뷰 결과만 정리해주세요.
```

## 백엔드 코드 리뷰 요청 템플릿

```text
아래 FastAPI/Supabase/Redis 코드를 리뷰해주세요.

리뷰 대상:

코드 목적:

리뷰 관점:
1. endpoint URL과 HTTP Method가 REST API 기준에 맞는가?
2. Pydantic 요청 모델의 검증 조건이 충분한가?
3. 응답 모델이 실제 반환 데이터와 일치하는가?
4. Supabase insert/select/update/delete 코드에 조건 누락이 없는가?
5. Upstash Redis key, TTL, token 사용이 적절한가?
6. mock-first, Gemini SDK 최소/안내형 예제, OpenAI 선택 사용 흐름이 구분되는가?
7. API key, service role key, Redis token이 노출될 위험은 없는가?
8. 실제 LLM API 호출이 반복문 안에서 과도하게 실행될 가능성은 없는가?
9. `provider`, `model`, `actual_api_called`, `llm_call_mode`로 mock-first와 실제 호출을 구분하는가?
10. 오류 상황에서 HTTPException 또는 명확한 오류 응답이 있는가?
11. 서비스 로그에 필요한 정보는 남기고, 민감 정보는 남기지 않는가?

출력 형식:
- 치명적인 문제
- 수정이 필요한 문제
- 개선하면 좋은 문제
- 확인 질문
- 실행 또는 테스트 방법

아직 코드를 수정하지 말고 리뷰 결과만 정리해주세요.
```
