# 02. API Design

이 폴더에서는 `01_requirements`에서 정리한 요구사항을 FastAPI 엔드포인트 설계로 바꿉니다.

API 설계는 “어떤 주소로 요청을 받을지”, “어떤 데이터를 받을지”, “어떤 데이터를 돌려줄지”, “오류가 났을 때 어떤 형식으로 알려줄지”를 정하는 단계입니다.

## 이번 단계의 목표

- URL과 HTTP Method를 리소스 중심으로 정리합니다.
- 요청 JSON과 응답 JSON의 모양을 미리 정합니다.
- 정상 응답과 오류 응답 형식을 구분합니다.
- 다음 단계인 `03_supabase-schema`에서 필요한 저장 데이터를 확인합니다.
- `04_implementation-guide`의 Pydantic 모델과 FastAPI 코드로 옮길 수 있는 기준을 만듭니다.

## API 설계 원칙

| 원칙 | 설명 |
| --- | --- |
| URL은 명사 중심으로 작성 | `/questions`, `/service-logs`처럼 리소스 이름을 사용합니다. |
| HTTP Method는 의미에 맞게 사용 | 조회는 `GET`, 생성은 `POST`를 사용합니다. |
| 요청/응답 구조를 먼저 정리 | 코드를 작성하기 전에 JSON 형태를 먼저 확인합니다. |
| 오류 응답을 통일 | 어떤 오류든 `ok`, `error.code`, `error.message` 형식을 유지합니다. |
| mock 구현과 실제 저장 구현을 분리 | 처음에는 mock API로 구조를 확인하고, 이후 Supabase로 연결합니다. |

## API 목록

| Method | URL | 설명 | 필수 여부 |
| --- | --- | --- | --- |
| GET | `/health` | 서버 상태를 확인합니다. | 필수 |
| POST | `/questions` | 질문을 등록하고 AI 답변을 생성합니다. | 필수 |
| GET | `/questions` | 저장된 질문/답변 목록을 조회합니다. | 필수 |
| GET | `/questions/{question_id}` | 질문/답변 1개를 조회합니다. | 필수 |
| POST | `/service-logs` | 서비스 로그를 저장합니다. | 선택 |
| GET | `/service-logs` | 서비스 로그 목록을 조회합니다. | 선택 |

## 응답 형식 기준

정상 응답은 항상 `ok: true`를 포함합니다.

단일 데이터 응답:

```json
{
  "ok": true,
  "item": {
    "id": "question-001",
    "user_id": "student01",
    "question": "FastAPI에서 Pydantic은 왜 사용하나요?",
    "answer": "요청 데이터 검증과 응답 구조 정의를 쉽게 하기 위해 사용합니다.",
    "model": "mock-teacher"
  }
}
```

목록 데이터 응답:

```json
{
  "ok": true,
  "items": [
    {
      "id": "question-001",
      "user_id": "student01",
      "question": "FastAPI에서 Pydantic은 왜 사용하나요?",
      "answer": "요청 데이터 검증과 응답 구조 정의를 쉽게 하기 위해 사용합니다.",
      "model": "mock-teacher"
    }
  ]
}
```

오류 응답:

```json
{
  "ok": false,
  "error": {
    "code": "question_required",
    "message": "질문 내용은 비어 있을 수 없습니다."
  }
}
```

## API별 설계 문서

상세 API 설계는 [api-design.md](./api-design.md)에 정리합니다.

이 문서에서는 다음 내용을 확인할 수 있습니다.

- `GET /health`
- `POST /questions`
- `GET /questions`
- `GET /questions/{question_id}`
- `POST /service-logs`
- `GET /service-logs`
- 공통 오류 응답 기준
- HTTP Status Code 기준

## 다음 단계 연결

API 설계가 끝나면 `03_supabase-schema`에서 실제 저장 테이블을 설계합니다.

```text
API 요청 데이터
-> Pydantic 모델
-> Supabase 테이블 컬럼
-> FastAPI 엔드포인트 구현
```

예를 들어 `POST /questions` 요청에 `user_id`, `question`, `model`이 필요하다면 Supabase 테이블에도 질문 기록을 저장할 컬럼이 필요합니다.
