# 03 Project Requirements

Supabase 기반 AI 미니 프로젝트 필수 요구사항입니다.

이번 프로젝트의 기준 주제는 **실시간 로그 대시보드 인터페이스**입니다. 단순한 챗봇 화면만 만드는 것이 아니라, 사용자 요청과 AI 응답이 서비스 안에서 어떤 로그로 남고, 그 로그를 어떻게 조회하고 시각화하는지까지 구현합니다.

## 1. Backend

- FastAPI 사용
- 최소 5개 이상의 API 엔드포인트 구현
- 엔드포인트 URL은 리소스 중심으로 일관되게 명명
- HTTP Method는 의미에 맞게 사용
- 입력 검증을 위한 Pydantic 모델 사용
- Request/Response 모델에 필수/선택 필드, 타입 힌트, 예시값 정의
- 표준화된 에러 응답 형식 사용
- Supabase service role key는 백엔드에서만 사용
- 사용자 요청, AI 응답, 사용 로그, 피드백 데이터 중 필요한 데이터를 Supabase에 저장
- SSE 기반 실시간 응답 또는 로그 스트리밍은 선택 확장 기능으로 구현하거나 설계 문서에 반영

권장 API 예시:

```text
GET    /health
GET    /api/logs
POST   /api/logs
GET    /api/logs/{log_id}
PUT    /api/logs/{log_id}
DELETE /api/logs/{log_id}
GET    /api/dashboard/summary
POST   /api/feedback
POST   /api/chat
POST   /api/chat/stream
```

## 2. Frontend

- Streamlit 사용
- 실시간 로그 대시보드 화면 구현
- 로그 등록 또는 사용자 질문 입력 화면 구현
- 로그 목록, 상세, 필터, 통계 표시 기능 포함
- API 호출 결과를 화면에 표시
- 버튼, 입력폼, 테이블, 차트의 스타일과 배치가 전체 화면에서 일관되도록 구성
- 오류 발생 시 사용자에게 안내 메시지 표시
- SSE를 적용하는 경우 응답 chunk 또는 로그 상태가 화면에 실시간으로 누적 표시되도록 구현
- 로그인 상태 또는 사용자 식별 상태를 사용할 경우 `st.session_state`로 관리

권장 화면 예시:

```text
메인 대시보드
로그 등록/질문 입력 화면
로그 상세 조회 화면
피드백 입력 화면
오류/빈 데이터 안내 화면
설정 화면
```

## 3. Supabase

- Supabase 프로젝트 사용
- `.env.example` 포함
- 실제 `.env`는 제출하지 않음
- 테이블은 3정규화(3NF)를 기준으로 중복을 줄여 설계
- 논리 ERD와 물리 ERD를 문서에 정리
- 모든 컬럼의 데이터 타입, 길이, 제약조건, 기본값, 설명 작성
- PK/FK, 인덱스, NOT NULL, UNIQUE, CHECK 같은 제약조건을 필요한 곳에 정의
- RLS를 사용할 경우 정책 설명과 테스트 결과 포함
- anon key와 service role key 사용 위치를 구분

권장 테이블 예시:

```text
profiles
log_events
ai_responses
feedback
dashboard_metrics
```

## 4. AI 기능

- 사용자 질문 또는 로그 내용을 입력받고 AI 응답을 반환
- 프롬프트 설계 의도를 README 또는 docs에 설명
- 사용자 피드백 데이터를 AI 답변 품질 개선에 어떻게 활용할지 문서화
- 응답 생성 중 loading/spinner/status 표시
- 선택 확장: Server-Sent Events(SSE) 기반 실시간 응답 스트리밍 구현
- SSE 적용 시 최종 assistant 응답을 Supabase에 저장
- SSE 적용 시 스트리밍 실패 상황에 대한 fallback 메시지와 로그 기록 기준 작성

## 5. 대시보드 기능

대시보드는 이번 프로젝트의 핵심 결과물입니다.

필수 기능:

```text
로그 생성 또는 수집
로그 목록 조회
로그 상세 조회
로그 상태/유형/시간 기준 필터
집계 지표 표시
차트 또는 테이블 기반 시각화
피드백 데이터 표시 또는 저장
```

가능하면 아래 기능도 포함합니다.

```text
최근 로그 자동 새로고침
오류 로그 강조
AI 응답 품질 점수 또는 사용자 만족도 표시
처리 시간 평균 표시
```

## 6. 실행 방식

- Supabase는 클라우드 프로젝트 사용
- FastAPI는 로컬 `.venv`에서 `uvicorn`으로 실행
- Streamlit은 로컬 `.venv`에서 `streamlit run`으로 실행
- Docker/PostgreSQL/Redis 직접 실행은 이 과정의 요구사항이 아님
- Docker, Docker Compose, AWS 배포는 `06_multi-agent-service-ops`에서 학습

## 7. 문서 필수 항목

```text
README.md
.env.example
backend/requirements.txt
frontend/requirements.txt
docs/project-plan.md
docs/api-spec.md
docs/ui-design.md
docs/supabase-schema.md
docs/dashboard-result.md
docs/streaming-response-design.md
docs/test-checklist.md
presentation/final-presentation.md
```
