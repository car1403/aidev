# Codex Review Log

Codex를 활용해 코드 설명, 디버깅, 리팩토링, 코드 리뷰, 보안/비용 점검을 진행한 기록을 작성합니다.

Codex 응답을 그대로 붙이지 않습니다. 어떤 요청을 했고, 어떤 제안을 받아들였고, 어떤 제안은 보류했는지 직접 판단한 내용을 함께 기록합니다.

## 기록 양식

```text
날짜:
리뷰 대상 파일:
사용한 요청문:
Codex가 지적한 내용:
내가 동의한 내용:
실제 수정한 내용:
수정 후 실행 결과:
보류한 내용과 이유:
배운 점:
```

## 필수 리뷰 관점

- FastAPI endpoint 구조
- Pydantic 요청/응답 모델
- Supabase 테이블명과 컬럼명
- LLM API mock-first/실제 호출 구분
- Gemini SDK 기본 사용 흐름
- Gemini SDK 안내형 예제 사용 흐름
- OpenAI 선택 사용 흐름
- Upstash Redis 사용 시 key와 TTL
- 서비스 로그 저장 흐름
- 보안과 비용 위험

## Codex 요청 예시

```text
아래 FastAPI/Supabase 코드를 리뷰해주세요.

리뷰 관점:
1. endpoint URL과 HTTP Method가 적절한가?
2. Pydantic 요청/응답 모델이 충분한가?
3. Supabase 테이블명과 컬럼명이 일치하는가?
4. 서비스 로그에 민감 정보가 들어갈 가능성이 있는가?
5. mock-first 호출, Gemini SDK 최소/안내형 호출, OpenAI 선택 호출이 구분되어 있는가?
6. provider, model, actual_api_called, llm_call_mode 기준이 문서와 코드에 일치하는가?
7. 최종 프로젝트 제출 전 반드시 수정할 부분은 무엇인가?

아직 코드를 수정하지 말고 리뷰 결과만 정리해주세요.
```
