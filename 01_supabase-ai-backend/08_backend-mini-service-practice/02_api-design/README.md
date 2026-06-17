# 02. API Design

Endpoint URL, HTTP Method, 요청/응답 모델, 오류 응답 형식을 설계합니다.

## API 목록

| Method | URL | 설명 |
| --- | --- | --- |
| GET | `/health` | 서버 상태를 확인합니다. |
| POST | `/qa` | 질문을 보내고 AI 답변을 생성합니다. |
| GET | `/qa` | 저장된 질문/답변 목록을 조회합니다. |
| GET | `/qa/{item_id}` | 질문/답변 1개를 조회합니다. |
| GET | `/service-logs` | 서비스 로그 목록을 조회합니다. |

## 오류 응답 기준

| 상황 | Status Code | 설명 |
| --- | --- | --- |
| 질문이 비어 있음 | 422 | Pydantic 검증 오류 |
| 질문/답변 id가 없음 | 404 | 해당 데이터가 없음 |
| Supabase 설정 누락 | 500 | 서버 환경 설정 문제 |
| 저장 실패 | 500 | 외부 저장소 처리 실패 |
