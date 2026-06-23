# 코드 리뷰 요청 템플릿

```text
아래 코드를 리뷰해줘.

리뷰 관점:
1. 실행 오류 가능성
2. 요구사항 충족 여부
3. 변수명과 함수명
4. 중복 코드
5. 예외 처리
6. 초급자가 이해하기 쉬운 구조

출력 형식:
- 수정이 필요한 부분
- 이유
- 개선 예시
```

## 백엔드 코드 리뷰 요청 템플릿

```text
아래 FastAPI/Supabase 코드를 리뷰해줘.

리뷰 관점:
1. endpoint URL과 HTTP Method가 REST API 기준에 맞는가?
2. Pydantic 요청 모델의 검증 조건이 충분한가?
3. Supabase insert/select/update/delete 코드에 조건 누락이 없는가?
4. API key, service role key, Redis token이 노출될 위험은 없는가?
5. 실제 LLM API 호출이 반복문 안에서 과도하게 실행될 가능성은 없는가?
6. 오류 상황에서 HTTPException 또는 명확한 오류 응답이 있는가?
7. 서비스 로그에 필요한 정보는 남기고, 민감 정보는 남기지 않는가?

출력 형식:
- 치명적인 문제
- 수정하면 좋은 문제
- 초보자가 이해해야 할 개념
- 개선 예시 코드
```


