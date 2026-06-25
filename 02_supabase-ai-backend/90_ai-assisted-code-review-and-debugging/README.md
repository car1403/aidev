# 90_ai-assisted-code-review-and-debugging

이 단원에서는 Codex를 활용해 Python과 AI 백엔드 코드를 설명받고, 생성하고, 디버깅하고, 리뷰하는 방법을 학습합니다.

핵심은 Codex에게 코드를 대신 맡기는 것이 아닙니다. 요구사항을 명확히 설명하고, Codex의 답변을 검토하고, 실행 결과로 확인하며, 오류와 보안 위험을 함께 줄이는 개발 습관을 만드는 것입니다.

## 학습 목표

- Codex에게 명확한 개발 요청을 작성할 수 있다.
- 생성된 코드를 읽고 요구사항과 비교할 수 있다.
- 오류 메시지와 실행 결과를 바탕으로 디버깅을 요청할 수 있다.
- 동작을 유지하면서 리팩토링을 요청할 수 있다.
- 코드 리뷰 결과를 치명도별로 분류할 수 있다.
- FastAPI, Pydantic, Supabase, Upstash Redis, LLM API 코드에서 자주 발생하는 문제를 점검할 수 있다.
- API key, service role key, Redis token 같은 민감 정보가 노출되지 않았는지 확인할 수 있다.
- Gemini SDK 기본 사용 흐름, REST 보충 예제, OpenAI 선택 사용 흐름을 구분하고 비용 위험을 점검할 수 있다.
- `08_backend-mini-service-practice`에서 만든 미니 서비스를 Codex와 함께 종합 리뷰할 수 있다.

## 학습 순서

```text
00_references
-> 01_codex-basic-usage
-> 02_prompting-for-code
-> 03_debugging-with-codex
-> 04_refactoring-with-codex
-> 05_code-review-with-codex
-> 06_backend-security-review-with-codex
-> 07_supabase-redis-debugging-with-codex
-> 08_mini-service-review-with-codex
-> 10_labs
-> 20_assignments
```

## 폴더 구성

```text
90_ai-assisted-code-review-and-debugging
├─ 00_references
├─ 01_codex-basic-usage
├─ 02_prompting-for-code
├─ 03_debugging-with-codex
├─ 04_refactoring-with-codex
├─ 05_code-review-with-codex
├─ 06_backend-security-review-with-codex
├─ 07_supabase-redis-debugging-with-codex
├─ 08_mini-service-review-with-codex
├─ 10_labs
└─ 20_assignments
```

## 학습 운영 원칙

1. Codex에게 요청하기 전에 먼저 문제를 자기 말로 정리합니다.
2. 한 번에 큰 기능을 요청하지 않고 작은 단위로 나눕니다.
3. 생성된 코드는 반드시 직접 읽고 실행합니다.
4. 오류가 나면 에러 메시지, 실행 명령, 기대 결과를 함께 전달합니다.
5. 최종 결과물에는 본인이 이해한 설명과 직접 확인한 실행 결과를 포함합니다.
6. 실제 API key, token, 비밀번호는 Codex 요청문이나 문서에 붙여 넣지 않습니다.

## AI 도구 선택 기준

| 상황 | 추천 도구 | 이유 |
| --- | --- | --- |
| 현재 폴더의 코드를 직접 수정해야 함 | Codex | 로컬 파일을 읽고 수정하며 실행 검증까지 연결하기 좋습니다. |
| 긴 문서나 요구사항을 요약해야 함 | NotebookLM, Claude | 문서 기반 정리와 긴 맥락 분석에 활용하기 좋습니다. |
| 최신 공식 문서나 출처가 필요함 | Perplexity AI, 공식 문서 | 검색 결과와 출처를 함께 확인할 수 있습니다. |
| 코드 리뷰 관점을 넓히고 싶음 | Codex, Claude Code | 실행 안정성, 보안, 가독성 관점의 비교 리뷰에 활용합니다. |
| 개념을 쉬운 말로 다시 듣고 싶음 | ChatGPT, Claude, Gemini | 초보자 수준 설명, 예시, 비유를 요청하기 좋습니다. |

핵심은 AI 답변을 많이 받는 것이 아니라, 답변을 검증하고 현재 코드에 맞게 적용하는 것입니다.

## 다른 단원과의 연결

- `01_python-basic`: 기초 문법 설명, 오류 원인 분석, 작은 함수 생성
- `02_python-advanced`: 함수 분리, 모듈화, 객체지향 리팩토링
- `04_fastapi-backend`: API 구조 생성, 테스트, 오류 해결
- `05_llm-api-integration`: mock-first, Gemini SDK 기본 호출, REST 보충 호출, OpenAI 선택 호출 구분, 비용/토큰/예외 처리 점검
- `06_supabase-db-and-auth`: Supabase 연동 코드 검토, Auth/RLS, Upstash Redis 세션과 캐시 점검
- `07_backend-service-data-management`: 사용자 프로필, 대화 이력, 서비스 로그 설계 리뷰
- `08_backend-mini-service-practice`: 미니 서비스 전체 코드 리뷰와 개선
- `03_supabase-ai-frontend`: Streamlit 화면 흐름, 사용자 경험, API 연동 피드백

## 백엔드 코드 리뷰 관점

이 단원 후반부에서는 앞에서 만든 실제 예제를 기준으로 Codex에게 다음 관점의 리뷰를 요청합니다.

| 관점 | 확인할 내용 |
| --- | --- |
| 실행 안정성 | import 오류, 실행 위치, 가상환경, 패키지 누락 |
| FastAPI 구조 | endpoint URL, HTTP Method, Pydantic 검증, 오류 응답 |
| Supabase 저장 | 테이블명, 컬럼명, `.eq(...)` 조건, insert/update/delete 결과 확인 |
| LLM API | Gemini SDK 기본 사용, REST 보충 예제, OpenAI 선택 사용, mock-first/실제 호출 구분, 비용 발생 가능성 |
| Upstash Redis | token 노출 여부, key 설계, TTL 설정, rate limit 적용 |
| 보안 | `.env` 관리, service role key 노출 방지, 로그 민감 정보 제거 |
| 미니 서비스 | 요구사항 충족, 응답 형식 통일, 서비스 로그 저장 여부 |

## AI 답변 검증 체크리스트

- 답변이 현재 파일 구조와 맞는가?
- 코드가 실행되는가?
- 테스트 또는 최소 실행 검증을 했는가?
- API key, service role key, Redis token이 노출되지 않았는가?
- 외부 API 호출 비용을 제한하는 장치가 있는가?
- Supabase 테이블명과 컬럼명이 실제 스키마와 맞는가?
- Upstash Redis key에 TTL이 필요한 경우 설정되어 있는가?
- 초보자가 이해하기 어려운 부분에는 설명이나 주석이 있는가?

## 추천 리뷰 요청 예시

```text
08_backend-mini-service-practice/04_implementation-guide/main_mock.py를 리뷰해주세요.

리뷰 관점:
1. FastAPI endpoint 구조가 실습 요구사항과 맞는가?
2. Pydantic 검증이 충분한가?
3. 서비스 로그가 필요한 정보를 담고 있는가?
4. mock-first 구현에서 Supabase 구현으로 넘어갈 때 주의할 점은 무엇인가?
5. 초보자가 이해하기 어려운 부분이 있으면 설명해주세요.

아직 코드를 수정하지 말고 리뷰 결과만 정리해주세요.
```
