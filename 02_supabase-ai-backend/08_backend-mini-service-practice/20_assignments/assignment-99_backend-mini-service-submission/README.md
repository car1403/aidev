# Assignment 99. Backend Mini Service Submission

## 목표

`08_backend-mini-service-practice`의 최종 산출물을 한 번에 점검합니다.

## 최종 제출 구성

아래 항목을 정리합니다.

```text
1. 요구사항 요약
2. API 설계 문서
3. Supabase 테이블 설계 문서
4. mock 서버 실행 결과
5. Supabase 서버 실행 결과
6. 서비스 로그 확인 결과
7. 코드 리뷰 및 수정 기록
8. 개선 아이디어
```

## 최종 점검표

| 점검 항목 | 완료 |
| --- | --- |
| 요구사항이 정리되어 있다. | [ ] |
| API가 `/questions` 기준으로 설계되어 있다. | [ ] |
| Supabase 테이블이 `mini_questions`, `mini_service_logs` 기준으로 설계되어 있다. | [ ] |
| mock 서버 실행 결과가 있다. | [ ] |
| Supabase 서버 실행 결과가 있다. | [ ] |
| 질문 생성과 조회가 동작한다. | [ ] |
| 서비스 로그가 저장된다. | [ ] |
| `provider`, `model`, `actual_api_called`, `llm_call_mode` 기준이 문서와 코드에 반영되어 있다. | [ ] |
| 오류 발생 시 원인을 확인할 수 있다. | [ ] |
| 민감 정보가 제출 자료에 포함되지 않았다. | [ ] |

## 개선 아이디어 예시

- 실제 Gemini SDK를 연결해 mock-first 답변을 교체합니다.
- 반복 질문에 Upstash Redis 캐시를 적용합니다.
- 사용자 인증을 붙이고 user_id를 Supabase Auth와 연결합니다.
- SSE 스트리밍은 `04_supabase-ai-mini-project`에서 통합 실습으로 확장합니다.
