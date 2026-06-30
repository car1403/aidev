# 90_ai-assisted-code-review-and-debugging

이 단원은 `01_fastapi-backend`, `02_llm-api-integration`, `03_supabase-db-and-auth`를 진행하면서 만난 오류를 Codex와 함께 분석하고, 코드 리뷰 결과를 정리하는 마무리 단원입니다.

새로운 큰 기능을 만드는 단원이 아니라, 앞에서 만든 코드를 더 안전하게 읽고 고치는 방법을 연습합니다.

## 학습 목표

- 오류 메시지를 실행 명령, 위치, 기대 결과와 함께 정리할 수 있습니다.
- Codex에게 코드를 수정시키기 전에 먼저 원인 분석을 요청할 수 있습니다.
- FastAPI, LLM API, Supabase, Redis 실습에서 자주 나오는 오류를 분류할 수 있습니다.
- API key, JWT, service role key, Redis token 같은 민감 정보가 노출되지 않았는지 확인할 수 있습니다.
- 최종 프로젝트 전에 코드 리뷰 체크리스트를 사용해 위험 지점을 점검할 수 있습니다.

## 진행 순서

```text
01_debugging-playbook.md
-> 02_code-review-checklist.md
-> 03_prompt-recipes.md
-> 10_labs
-> templates
```

## 가장 중요한 원칙

Codex에게 오류를 물어볼 때 실제 API key, JWT, service role key, Redis token, 비밀번호를 붙여 넣지 않습니다.

대신 아래처럼 값을 가려서 전달합니다.

```text
GEMINI_API_KEY=***
SUPABASE_SERVICE_ROLE_KEY=***
Authorization: Bearer ***
```

## 단원별 점검 관점

| 앞 단원 | 점검할 내용 |
| --- | --- |
| `01_fastapi-backend` | import 오류, 실행 위치, `uvicorn` 명령, 404/405, Pydantic 검증 오류 |
| `02_llm-api-integration` | `.env` 위치, API key 누락, Gemini 503, 모델명 오류, 실제 호출과 mock 호출 구분 |
| `03_supabase-db-and-auth` | Supabase URL/key, 테이블명/컬럼명, Auth 로그인, Bearer token, RLS 접근 오류, Redis token/TTL |
| `99_final-backend-project` | 요구사항 충족, API 응답 형식, 저장 흐름, 보안/비용 점검, Swagger 테스트 결과 |

## 수업에서 사용하는 최소 흐름

1. 오류가 난 명령어를 복사합니다.
2. 전체 Traceback 또는 응답 메시지를 복사합니다.
3. 민감 정보가 있으면 `***`로 바꿉니다.
4. `templates/error-report-template.md` 형식으로 정리합니다.
5. Codex에게 “수정하지 말고 원인부터 설명해 달라”고 요청합니다.
6. 제안이 맞는지 파일과 실행 결과로 확인합니다.
7. 필요한 경우에만 작은 범위로 수정합니다.

## 제출 산출물

필수 산출물은 길지 않아도 됩니다.

```text
1. 오류 분석 기록 1개
2. 코드 리뷰 요청 기록 1개
3. 수정 후 재실행 결과 1개
```

선택 산출물:

```text
보안/비용 점검표
리팩토링 전후 비교
최종 프로젝트 사전 리뷰 기록
```
