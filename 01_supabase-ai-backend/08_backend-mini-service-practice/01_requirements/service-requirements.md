# Service Requirements

이 문서는 `AI 질문 응답 백엔드 미니 서비스`의 요구사항 정의서입니다.

요구사항 정의서는 구현 전에 작성하는 기준 문서입니다. 이 문서를 기준으로 API 설계, Supabase 테이블 설계, FastAPI 구현, 로그 저장 방식을 결정합니다.

## 1. 서비스 이름

```text
AI 질문 응답 백엔드 미니 서비스
```

## 2. 서비스 목적

사용자가 질문을 보내면 백엔드 API가 질문을 검증하고 AI 답변을 생성한 뒤, 질문과 답변 기록을 저장합니다. 또한 API 처리 결과를 서비스 로그로 남겨서 나중에 오류 원인과 실행 흐름을 확인할 수 있게 합니다.

## 3. 사용자 시나리오

```text
1. 사용자가 자신의 user_id와 질문을 API로 보냅니다.
2. FastAPI 서버가 입력값을 검증합니다.
3. 서버가 사용자 프로필 또는 기본 사용자 정보를 확인합니다.
4. 서버가 mock-first 함수로 답변을 생성합니다.
5. 서버가 질문과 답변을 Supabase에 저장합니다.
6. 서버가 처리 결과를 service_logs에 저장합니다.
7. 서버가 사용자에게 JSON 응답을 반환합니다.
```

## 4. 필수 기능 요구사항

| 번호 | 기능 | 설명 | 완료 기준 |
| --- | --- | --- | --- |
| F-01 | 서버 상태 확인 | 서버가 실행 중인지 확인합니다. | `GET /health`가 정상 응답을 반환합니다. |
| F-02 | 질문 등록 | 사용자 질문을 API로 받습니다. | `POST /questions` 형태의 API가 요청을 받습니다. |
| F-03 | 입력값 검증 | `user_id`, `question` 값을 검증합니다. | 빈 값이나 너무 긴 질문에 오류를 반환합니다. |
| F-04 | AI 답변 생성 | mock-first 함수로 답변을 생성합니다. | 외부 API 없이도 답변 문자열이 생성됩니다. |
| F-05 | 질문/답변 저장 | 질문과 답변을 저장합니다. | Supabase 저장 구조와 연결될 수 있습니다. |
| F-06 | 기록 조회 | 저장된 질문/답변 목록을 조회합니다. | 사용자별 기록 조회 API를 설계합니다. |
| F-07 | 서비스 로그 저장 | 성공/실패/오류 기록을 남깁니다. | `event_type`, `message`, `metadata`가 저장됩니다. |
| F-08 | 오류 응답 표준화 | 오류를 일정한 JSON 구조로 반환합니다. | 오류 응답에 `code`, `message`가 포함됩니다. |

## 5. 선택 기능 요구사항

| 번호 | 기능 | 설명 |
| --- | --- | --- |
| O-01 | Gemini SDK 연동 | mock-first 이후 실제 LLM 연동이 필요할 때 Gemini SDK를 사용합니다. |
| O-02 | OpenAI API 비교 | 기존 OpenAI 예제는 선택 비교용으로 유지합니다. |
| O-03 | Upstash Redis 캐시 | 반복 질문에 대한 짧은 캐시를 적용할 수 있습니다. |
| O-04 | 요청 제한 | 짧은 시간 동안 너무 많은 요청을 막기 위해 Redis 카운터를 사용할 수 있습니다. |

## 6. 데이터 요구사항

| 데이터 | 저장 위치 | 필수 여부 | 설명 |
| --- | --- | --- | --- |
| 사용자 프로필 | Supabase | 필수 | 사용자 id, 표시 이름, 선호 언어, 학습 수준 |
| 질문 | Supabase | 필수 | 사용자가 입력한 질문 |
| AI 답변 | Supabase | 필수 | mock-first 또는 Gemini SDK가 만든 답변 |
| 서비스 로그 | Supabase | 필수 | API 성공/실패, 오류, 처리 시간 |
| 캐시 | Upstash Redis | 선택 | 짧은 시간 재사용할 응답 |
| 요청 제한 상태 | Upstash Redis | 선택 | 사용자별 요청 횟수 카운터 |

## 7. 입력값 검증 기준

| 입력값 | 기준 | 오류 예시 |
| --- | --- | --- |
| `user_id` | 빈 문자열이면 안 됩니다. | `user_id_required` |
| `question` | 빈 문자열이면 안 됩니다. | `question_required` |
| `question` 길이 | 최대 길이를 넘으면 안 됩니다. 예: 500자 | `question_too_long` |
| 요청 JSON | 필요한 필드가 있어야 합니다. | `invalid_request_body` |

## 8. 오류 응답 기준

오류 응답은 항상 같은 구조를 사용합니다.

```json
{
  "ok": false,
  "error": {
    "code": "question_required",
    "message": "질문 내용은 비어 있을 수 없습니다."
  }
}
```

## 9. 서비스 로그 기준

서비스 로그에는 운영 확인에 필요한 정보만 저장합니다.

| 항목 | 예시 |
| --- | --- |
| `event_type` | `question_created`, `api_error`, `validation_error` |
| `message` | `질문 답변 생성 성공` |
| `metadata` | 요청 경로, 처리 시간, user_id, 오류 코드, provider, model, actual_api_called, llm_call_mode |

민감 정보는 로그에 저장하지 않습니다.

```text
저장하면 안 되는 값:
- API Key
- 비밀번호
- access token
- refresh token
- 개인 식별 정보 전체 원문
```

## 10. 제외 범위

이번 미니 서비스에서는 다음 내용을 깊게 구현하지 않습니다.

| 제외 항목 | 이유 |
| --- | --- |
| SSE 실시간 스트리밍 | 백엔드/프론트엔드/Supabase 저장을 함께 보아야 하므로 `03_supabase-ai-mini-project`에서 다룹니다. |
| 프론트엔드 화면 | 이번 단원은 API 중심입니다. 화면은 `02_supabase-ai-frontend`와 `03_supabase-ai-mini-project`에서 다룹니다. |
| Docker 배포 | Docker는 `04_llm-agent-orchestration` 이후 본격적으로 사용합니다. |
| Docker Compose, AWS 배포 | `06_multi-agent-service-ops`에서 다룹니다. |
| 운영 대시보드 | 서비스 운영 관점의 모니터링은 이후 과정에서 다룹니다. |

## 11. 다음 단계에서 설계할 API 후보

| Method | URL | 목적 |
| --- | --- | --- |
| GET | `/health` | 서버 상태 확인 |
| POST | `/questions` | 질문 등록 및 답변 생성 |
| GET | `/questions` | 질문/답변 목록 조회 |
| GET | `/questions/{question_id}` | 특정 질문/답변 상세 조회 |
| POST | `/service-logs` | 서비스 로그 저장 |

## 12. 완료 체크리스트

- [ ] 서비스 목적이 한 문장으로 설명되어 있다.
- [ ] 필수 기능과 선택 기능이 구분되어 있다.
- [ ] Supabase에 저장할 데이터가 정리되어 있다.
- [ ] Upstash Redis가 필요한 경우와 필요하지 않은 경우가 구분되어 있다.
- [ ] 입력값 검증 기준이 정리되어 있다.
- [ ] 오류 응답 형식이 정리되어 있다.
- [ ] 서비스 로그에 남길 항목이 정리되어 있다.
- [ ] 제외 범위가 명확하다.
- [ ] 다음 단계에서 설계할 API 후보가 정리되어 있다.
