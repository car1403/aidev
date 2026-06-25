# 02_fastapi-supabase-api

이 단계에서는 FastAPI가 Supabase와 통신하는 백엔드 API 역할을 하도록 구성합니다.

Streamlit 화면에서 Supabase key를 직접 다루기보다, Streamlit은 FastAPI API를 호출하고 FastAPI가 Supabase에 접근하는 구조를 권장합니다. 이 구조는 key 보안, 오류 처리, 로그 저장, AI API 연동을 한곳에서 관리하기 쉽습니다.

## 학습 목표

- FastAPI에서 Supabase client를 초기화할 수 있습니다.
- 사용자, 대화, 메시지, 로그 데이터를 API로 조회하거나 저장할 수 있습니다.
- Swagger UI에서 API를 테스트할 수 있습니다.
- API 오류를 표준화된 형식으로 응답할 수 있습니다.

## 권장 API 구조

```text
GET  /health
GET  /api/conversations
POST /api/conversations
GET  /api/conversations/{conversation_id}/messages
POST /api/conversations/{conversation_id}/messages
POST /api/service-logs
POST /api/feedbacks
```

## FastAPI가 맡는 역할

```text
Streamlit 요청 받기
-> 요청 데이터 검증
-> Supabase에 데이터 조회/저장
-> 오류 발생 시 표준 오류 응답 반환
-> 필요하면 서비스 로그 저장
```

## 실습 파일

- [01_api-design.md](./01_api-design.md)
- [02_crud-endpoints.md](./02_crud-endpoints.md)
- [03_api-test-checklist.md](./03_api-test-checklist.md)

## 체크리스트

- [ ] `/health` API가 정상 응답한다.
- [ ] Swagger UI에서 API 목록을 확인했다.
- [ ] 메시지 저장 API를 테스트했다.
- [ ] 로그 저장 API를 테스트했다.
- [ ] Supabase 오류 발생 시 화면에 보여줄 수 있는 메시지를 정리했다.
