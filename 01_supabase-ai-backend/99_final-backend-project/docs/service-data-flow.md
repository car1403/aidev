# Service Data Flow

최종 프로젝트에서 데이터가 어떤 순서로 이동하는지 작성합니다.

## 기본 흐름

```text
사용자 요청
-> FastAPI 요청 검증
-> mock LLM 또는 실제 LLM API 호출
-> Supabase에 질문/답변 저장
-> Supabase에 서비스 로그 저장
-> JSON 응답 반환
```

## 작성할 내용

```text
1. 사용자가 보내는 데이터:
2. FastAPI가 검증하는 항목:
3. LLM 호출 방식:
4. Supabase에 저장하는 테이블:
5. 서비스 로그에 저장하는 내용:
6. Upstash Redis를 사용하는 경우:
7. 오류 발생 시 흐름:
```

## 예시

```text
POST /qa 요청
-> QaCreate 모델로 question 빈 값 검증
-> generate_mock_answer 함수로 답변 생성
-> qa_items 테이블에 question/answer/model 저장
-> service_logs 테이블에 qa.created 로그 저장
-> {"item":...} 응답 반환
```
