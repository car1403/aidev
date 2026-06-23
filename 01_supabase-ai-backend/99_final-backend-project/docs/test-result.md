# Test Result

Swagger UI, API 요청, Supabase 저장 결과, 오류 처리 테스트 결과를 작성합니다.

테스트 결과는 "실행했다"가 아니라 "어떤 명령 또는 화면에서 어떤 결과를 확인했는가"를 남기는 문서입니다.

## 테스트 항목

| 항목 | 확인 내용 | 결과 |
| --- | --- | --- |
| 서버 실행 | `GET /health`가 200을 반환하는가? | |
| 질문 생성 | `POST /questions`가 201 또는 200을 반환하는가? | |
| 질문 목록 | `GET /questions`가 목록을 반환하는가? | |
| 단건 조회 | `GET /questions/{question_id}`가 1개 데이터를 반환하는가? | |
| 로그 조회 | `GET /service-logs`가 로그 목록을 반환하는가? | |
| Supabase 저장 | `mini_questions` 테이블에 데이터가 저장되는가? | |
| 서비스 로그 | `mini_service_logs` 테이블에 성공/실패 로그가 저장되는가? | |
| LLM 호출 상태 | `provider`, `model`, `actual_api_called`, `llm_call_mode`가 응답/DB/로그에서 일치하는가? | |
| 오류 응답 | 빈 질문 또는 잘못된 요청에서 오류 응답이 반환되는가? | |
| 보안 | API key, token이 응답과 로그에 노출되지 않는가? | |

## 실행 명령 기록

```text
실행 위치:

실행 명령:

확인 URL:

확인 결과:
```

## Supabase 확인 기록

```text
확인한 테이블:

저장된 컬럼:

예상한 값:

실제 저장된 값:

문제 여부:
```

## 오류 테스트 기록

```text
테스트 상황:

보낸 요청:

예상 오류:

실제 오류:

수정 필요 여부:
```
