# 00. References

이 문서는 `08_backend-mini-service-practice`에서 계속 참고하는 미니 서비스 설계 기준입니다.

이번 단원은 백엔드의 작은 완성형 흐름을 만드는 단계입니다. 요구사항, API 설계, Supabase 스키마, FastAPI 구현, 서비스 로그를 서로 연결해서 봅니다.

## 미니 서비스 설계 순서

작은 서비스를 만들 때는 아래 순서로 확인합니다.

```text
1. 어떤 문제를 해결하는가?
2. 어떤 API가 필요한가?
3. 요청 데이터와 응답 데이터는 어떤 모양인가?
4. 어떤 데이터를 Supabase에 저장해야 하는가?
5. 어떤 상황에서 오류가 발생할 수 있는가?
6. 서비스 로그에는 무엇을 남겨야 하는가?
7. mock 구현과 실제 연동 구현을 어떻게 나눌 것인가?
```

## mock 먼저 구현하는 이유

처음부터 Supabase와 실제 LLM API를 모두 연결하면 오류 원인을 찾기 어렵습니다.

그래서 이 단원은 다음 순서로 진행합니다.

```text
mock-first + 메모리 저장소
-> FastAPI endpoint 구조 확인
-> Supabase 테이블 준비
-> Supabase 저장 코드 연결
-> Gemini SDK 연동은 이후 확장
```

이렇게 하면 API 구조, 데이터 저장 구조, 외부 API 호출 구조를 단계별로 이해할 수 있습니다.

앞 단원인 `05_llm-api-integration`에서는 `mock-first -> Gemini SDK 기본 구현 -> REST 보충 -> OpenAI 선택 비교` 흐름으로 LLM 호출을 정리했습니다. 이 미니 서비스에서는 그 흐름을 저장 구조에 반영하기 위해 `provider`, `model`, `actual_api_called`, `llm_call_mode` 값을 함께 다룹니다.

## API 이름 기준

이번 단원에서는 아래 API 이름을 표준으로 사용합니다.

| Method | URL | 설명 |
| --- | --- | --- |
| GET | `/health` | 서버 상태 확인 |
| POST | `/questions` | 질문 등록 및 mock 답변 생성 |
| GET | `/questions` | 질문/답변 목록 조회 |
| GET | `/questions/{question_id}` | 질문/답변 상세 조회 |
| POST | `/service-logs` | 서비스 로그 저장 |
| GET | `/service-logs` | 서비스 로그 목록 조회 |

## 테이블 이름 기준

| 테이블 | 저장 데이터 | 설명 |
| --- | --- | --- |
| `mini_questions` | 질문/답변 기록 | 사용자 질문, AI 답변, provider, 모델명, 호출 여부, 생성 시간 |
| `mini_service_logs` | 서비스 로그 | API 성공/실패, 오류, metadata |

## 요청/응답 기준

정상 응답은 `ok: true`를 포함합니다.

```json
{
  "ok": true,
  "item": {
    "id": "question-001"
  }
}
```

목록 응답은 `items`를 사용합니다.

```json
{
  "ok": true,
  "items": []
}
```

오류 응답은 `error.code`, `error.message`를 포함합니다.

```json
{
  "ok": false,
  "error": {
    "code": "question_not_found",
    "message": "질문 기록을 찾을 수 없습니다."
  }
}
```

## Supabase와 Upstash Redis 역할 구분

| 데이터 | 저장 위치 | 이유 |
| --- | --- | --- |
| 질문/답변 기록 | Supabase | 나중에 다시 조회해야 하는 영구 데이터 |
| 서비스 로그 | Supabase | 오류 분석과 실행 흐름 확인에 필요한 운영 데이터 |
| 반복 질문 응답 캐시 | Upstash Redis 선택 | 짧은 시간 재사용하면 되는 임시 데이터 |
| 요청 제한 카운터 | Upstash Redis 선택 | 일정 시간이 지나면 사라져도 되는 카운터 데이터 |

이번 단원에서는 Supabase 저장 흐름을 중심으로 진행합니다. Upstash Redis는 선택 확장 기준으로만 언급합니다.

## 로그 설계 기준

서비스 로그에는 아래 정보를 저장할 수 있습니다.

| 항목 | 예시 |
| --- | --- |
| `event_type` | `question_created`, `validation_error`, `storage_error` |
| `message` | `질문 답변 생성 성공` |
| `metadata` | `user_id`, `question_id`, `endpoint`, `duration_ms`, `provider`, `model`, `actual_api_called`, `llm_call_mode` |

로그에 저장하지 않아야 하는 값:

```text
API Key
비밀번호
access token
refresh token
민감한 개인정보 원문
```

## 점검 체크리스트

| 항목 | 확인 질문 |
| --- | --- |
| 요구사항 | 서비스 목적과 필수 기능이 설명되어 있나요? |
| API | `/questions`와 `/service-logs` 기준으로 설계되어 있나요? |
| 스키마 | `mini_questions`, `mini_service_logs`가 설계되어 있나요? |
| mock 구현 | Supabase 없이 API 흐름을 먼저 확인할 수 있나요? |
| Supabase 구현 | 실제 테이블에 질문과 로그가 저장되나요? |
| 오류 처리 | 잘못된 요청과 저장 실패를 구분할 수 있나요? |
| 보안 | 민감 정보가 로그나 제출 자료에 포함되지 않나요? |

## 관련 폴더

- `01_requirements`: 요구사항 정의
- `02_api-design`: API 설계
- `03_supabase-schema`: Supabase 테이블 설계
- `04_implementation-guide`: FastAPI 구현
- `10_labs`: 단계별 실습
- `20_assignments`: 산출물 과제
