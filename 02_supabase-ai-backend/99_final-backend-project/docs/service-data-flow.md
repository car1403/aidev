# Service Data Flow

최종 프로젝트에서 데이터가 어떤 순서로 이동하는지 작성합니다.

데이터 흐름을 먼저 정리하면 API, Supabase 테이블, 서비스 로그, Redis 선택 기능의 역할을 명확히 나눌 수 있습니다.

## 기본 흐름

```text
사용자 요청
-> FastAPI 요청 검증
-> mock-first 또는 Gemini SDK 호출
-> Supabase mini_questions 테이블에 질문/답변 저장
-> Supabase mini_service_logs 테이블에 서비스 로그 저장
-> JSON 응답 반환
```

## `POST /questions` 흐름 예시

```text
POST /questions 요청
-> QuestionCreate Pydantic 모델 검증
-> question 빈 값 여부 확인
-> mock-first 또는 Gemini SDK로 답변 생성
-> mini_questions 테이블에 question/answer/provider/model/actual_api_called/llm_call_mode 저장
-> mini_service_logs 테이블에 success 로그 저장
-> { ok: true, item: ... } 응답 반환
```

## 오류 발생 흐름 예시

```text
잘못된 요청
-> Pydantic 또는 직접 검증에서 오류 확인
-> mini_service_logs 테이블에 error 로그 저장
-> { ok: false, error: ... } 응답 반환
```

## Upstash Redis 선택 흐름

Redis를 사용할 경우 아래 중 하나를 선택해 작성합니다.

```text
응답 캐시:
사용자 질문 hash
-> Redis 캐시 조회
-> 캐시 hit이면 LLM 호출 없이 응답
-> 캐시 miss이면 LLM 호출 후 TTL과 함께 저장

요청 횟수 제한:
user_id 또는 IP 기준 key 생성
-> Redis count 증가
-> TTL 내 요청 횟수 초과 시 오류 응답
```

## 작성할 내용

```text
1. 사용자가 보내는 데이터:
2. FastAPI가 검증하는 항목:
3. LLM 호출 방식:
   - mock-first:
   - Gemini SDK:
   - REST 보충:
   - OpenAI 선택:
4. Supabase에 저장하는 테이블:
5. 서비스 로그에 저장하는 내용:
6. Upstash Redis를 사용하는 경우:
7. 오류 발생 시 흐름:
```
