# Test Checklist

## API

- [ ] `GET /health`가 동작합니다.
- [ ] `GET /api/logs`가 동작합니다.
- [ ] `POST /api/logs`가 동작합니다.
- [ ] `GET /api/logs/{log_id}`가 동작합니다.
- [ ] `PUT /api/logs/{log_id}` 또는 수정 API가 동작합니다.
- [ ] `DELETE /api/logs/{log_id}` 또는 삭제 API가 동작합니다.
- [ ] `GET /api/dashboard/summary`가 동작합니다.
- [ ] 에러 응답 형식이 통일되어 있습니다.
- [ ] Pydantic 검증 오류가 사용자에게 이해 가능하게 처리됩니다.
- [ ] API 설계 문서의 URL/Method와 실제 FastAPI 코드가 일치합니다.
- [ ] Request/Response 예시가 Swagger UI 또는 테스트 결과와 일치합니다.

## Supabase

- [ ] Supabase table이 존재합니다.
- [ ] PK/FK 관계가 문서와 일치합니다.
- [ ] 필수 컬럼에 NOT NULL이 적용되어 있습니다.
- [ ] 필요한 인덱스가 고려되어 있습니다.
- [ ] 실제 key가 제출 파일에 포함되지 않았습니다.
- [ ] 논리 ERD와 물리 ERD가 문서에 포함되어 있습니다.
- [ ] 컬럼 타입, 길이, 제약조건, 기본값, 설명이 문서화되어 있습니다.

## Frontend

- [ ] Streamlit page가 열립니다.
- [ ] Streamlit이 FastAPI를 호출합니다.
- [ ] 로그 목록이 표시됩니다.
- [ ] 대시보드 요약 지표가 표시됩니다.
- [ ] 차트 또는 테이블 시각화가 표시됩니다.
- [ ] 필터 또는 새로고침 기능이 동작합니다.
- [ ] 오류 상황 안내 메시지가 표시됩니다.
- [ ] 메인/상세/입력/설정/오류 화면 중 구현 범위가 문서와 일치합니다.
- [ ] 사용자 액션별 시스템 반응이 화면에서 확인됩니다.

## AI And Feedback

- [ ] AI 응답 API가 동작합니다.
- [ ] 사용자 피드백 저장이 동작합니다.
- [ ] 피드백 데이터가 대시보드 또는 문서에 반영됩니다.
- [ ] SSE backend `/api/chat/stream` 또는 자동 새로고침 기반 실시간 표시가 동작합니다.
- [ ] Streamlit UI가 chunk 또는 최신 로그 상태를 실시간성 있게 표시합니다.
- [ ] Final assistant response save flow is documented.
- [ ] Streaming error fallback is documented.

## Deployment Or Demo

- [ ] 로컬 실행 URL이 `dashboard-result.md`에 기록되어 있습니다.
- [ ] 무료 배포는 필수가 아니라 선택 확장임을 팀원이 설명할 수 있습니다.
- [ ] 배포를 진행한 경우에만 `docs/deployment-guide.md`가 작성되어 있습니다.
- [ ] 배포를 진행한 경우에만 Render 백엔드 URL의 `/health`가 정상 응답합니다.
- [ ] 배포를 진행한 경우에만 Render 백엔드 URL의 `/docs`가 열립니다.
- [ ] 배포를 진행한 경우에만 Streamlit Community Cloud URL이 열립니다.
- [ ] 배포를 진행한 경우에만 Streamlit Secrets의 `API_BASE_URL`이 Render 백엔드 URL을 가리킵니다.
- [ ] Upstash Redis를 사용하는 경우에만 REST URL과 Token이 Render 환경변수에만 등록되어 있습니다.
- [ ] `.env` 파일이 GitHub에 올라가지 않았습니다.
- [ ] `SUPABASE_SERVICE_ROLE_KEY`가 프론트엔드 또는 Streamlit Secrets에 들어가지 않았습니다.
- [ ] 발표 시연 순서가 문서화되어 있습니다.
- [ ] 주요 오류와 해결 방법이 문서화되어 있습니다.
