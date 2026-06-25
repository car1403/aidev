# Database Design

최종 프로젝트에서 사용할 Supabase 테이블, 컬럼, 관계, 권한 기준을 작성합니다.

이 프로젝트는 `05_backend-mini-service-practice`와 연결되므로 기본 테이블 이름은 `mini_questions`, `mini_service_logs`를 기준으로 정리합니다. 프로젝트 상황에 따라 이름을 바꿀 수 있지만, API 문서와 Python 코드의 이름은 반드시 일치해야 합니다.

## 필수 테이블

```text
mini_questions
-> 사용자 질문과 AI 답변 저장

mini_service_logs
-> API 처리 성공/실패와 오류 로그 저장
```

## 선택 테이블

```text
profiles
-> 사용자 프로필 저장

feedback
-> AI 답변 평가 저장

conversations / messages
-> 여러 메시지를 대화방 단위로 관리할 때 사용
```

## `mini_questions` 설계 예시

| 컬럼 | 타입 | 설명 |
| --- | --- | --- |
| id | uuid 또는 text | 질문 고유 ID |
| user_id | text | 사용자 식별 값 |
| question | text | 사용자 질문 |
| answer | text | AI 응답 |
| provider | text | LLM 제공자, 기본값은 `gemini` |
| model | text | 사용한 모델명 |
| actual_api_called | boolean | 실제 외부 LLM API 호출 여부 |
| llm_call_mode | text | `mock-first`, `gemini-sdk`, `gemini-rest`, `openai-optional` 등 호출 방식 |
| created_at | timestamptz | 생성 시각 |

## `mini_service_logs` 설계 예시

| 컬럼 | 타입 | 설명 |
| --- | --- | --- |
| id | uuid 또는 text | 로그 고유 ID |
| event_type | text | 이벤트 종류 |
| status | text | success 또는 error |
| message | text | 로그 메시지 |
| metadata | jsonb | endpoint, provider, model, actual_api_called, llm_call_mode, item_id 등 부가 정보 |
| created_at | timestamptz | 생성 시각 |

## 작성할 내용

각 테이블마다 아래 항목을 작성합니다.

```text
테이블 목적:
컬럼 목록:
Primary Key:
Foreign Key:
Index:
RLS 적용 여부:
사용하는 API:
```

## 설계 체크리스트

- [ ] API 문서의 필드와 테이블 컬럼이 일치합니다.
- [ ] 질문/응답 데이터와 서비스 로그가 분리되어 있습니다.
- [ ] mock-first 응답과 실제 Gemini SDK 응답을 구분할 수 있는 컬럼 기준이 있습니다.
- [ ] `created_at`이 있어 최신순 조회가 가능합니다.
- [ ] 로그의 `metadata`에는 민감 정보가 들어가지 않습니다.
- [ ] 사용자별 데이터라면 `user_id` 또는 `owner_id` 기준을 고려했습니다.
- [ ] RLS 적용 여부를 문서에 기록했습니다.
