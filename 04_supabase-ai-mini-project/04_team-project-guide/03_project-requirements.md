# 03 Project Requirements

Supabase 기반 AI 미니 프로젝트의 필수 요구사항입니다.

이번 프로젝트는 단순한 챗봇 화면만 만드는 것이 아니라, 사용자 요청과 AI 응답이 서비스 안에서 어떤 로그로 남고, 그 로그를 어떻게 조회하고 시각화하는지까지 구현합니다.

## 필수 구현 범위

필수 구현 범위는 아래 4가지입니다.

```text
1. FastAPI 백엔드 API
2. Supabase 테이블 저장/조회
3. Streamlit 대시보드 화면
4. 필수 산출물 4종 정리
```

SSE 스트리밍, 무료 배포, OpenAI 비교 호출은 선택 확장입니다.

## 1. FastAPI 백엔드

- 최소 5개 이상의 API 엔드포인트를 구현합니다.
- 엔드포인트 URL은 리소스 중심으로 일관되게 이름 붙입니다.
- HTTP Method를 의미에 맞게 사용합니다.
- 입력 검증을 위해 Pydantic 모델을 사용합니다.
- Request/Response 모델에 필수/선택 필드, 타입 힌트, 예시값을 정의합니다.
- Supabase service role key는 백엔드에서만 사용합니다.
- Gemini API를 기본 LLM으로 사용합니다.
- OpenAI API는 선택/비교 실습으로만 사용합니다.

권장 API 예시:

```text
GET  /health
GET  /api/logs
POST /api/logs
GET  /api/logs/{log_id}
POST /api/feedbacks
POST /api/chat
POST /api/chat/stream
```

## 2. Streamlit 화면

- `API_BASE_URL`을 기준으로 FastAPI API를 호출합니다.
- 실시간 로그 대시보드 화면을 구현합니다.
- 로그 등록 또는 사용자 질문 입력 화면을 구현합니다.
- 로그 목록, 상세, 필터, 통계 표시 기능을 포함합니다.
- API 호출 결과를 화면에 표시합니다.
- 오류 발생 시 사용자에게 안내 메시지를 표시합니다.
- SSE를 적용하는 경우 응답 chunk 또는 로그 상태가 화면에 누적 표시되도록 구성합니다.

권장 화면 예시:

```text
메인 대시보드
로그 등록/질문 입력 화면
로그 상세 조회 화면
피드백 입력 화면
오류/빈 데이터 안내 화면
```

## 3. Supabase 데이터베이스

- 실제 `.env`는 제출하지 않습니다.
- 테이블은 3정규형(3NF)을 기준으로 중복을 줄여 설계합니다.
- 논리 ERD와 물리 ERD를 문서에 정리합니다.
- 모든 컬럼의 데이터 타입, 길이, 제약조건, 기본값, 설명을 작성합니다.
- PK/FK, 인덱스, NOT NULL, UNIQUE, CHECK 같은 제약조건을 필요한 곳에 정의합니다.
- RLS를 사용하는 경우 정책 설명과 테스트 결과를 포함합니다.
- anon key와 service role key 사용 위치를 구분합니다.

권장 테이블 예시:

```text
profiles
conversations
messages
service_logs
feedbacks
```

## 4. AI 기능

- 사용자 질문 또는 로그 내용을 입력받고 AI 응답을 반환합니다.
- Gemini API를 기본 AI 응답 생성 API로 사용합니다.
- 프롬프트 설계 의도를 README 또는 docs에 설명합니다.
- 사용자 피드백 데이터를 AI 응답 품질 개선에 어떻게 사용할지 문서화합니다.
- 응답 생성 중 loading, spinner, status를 표시합니다.
- 선택 확장: Server-Sent Events(SSE) 기반 실시간 응답 스트리밍을 구현합니다.

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
피드백 데이터 표시
```

## 6. 보안 기준

- `.env`는 GitHub에 올리지 않습니다.
- `.env.example`에는 실제 key 대신 변수 이름과 예시값만 넣습니다.
- `SUPABASE_SERVICE_ROLE_KEY`는 FastAPI에서만 사용합니다.
- Streamlit에는 service role key를 넣지 않습니다.
- API key, 비밀번호, 토큰을 로그에 남기지 않습니다.
- Docker/PostgreSQL/Redis 직접 실행은 이 과정의 요구사항이 아닙니다.
- Docker, Docker Compose, AWS 배포는 `07_multi-agent-service-ops`에서 학습합니다.

## 7. 필수 산출물

```text
docs/api-spec.md
docs/ui-design.md
docs/supabase-schema.md
docs/dashboard-result.md
```

각 문서는 아래 기준을 충족해야 합니다.

```text
API 설계 문서:
엔드포인트 URL, HTTP Method, 표준 에러 응답, Pydantic Request/Response 모델

화면 설계서:
메인/상세/입력/설정/오류 화면, 와이어프레임, 사용자 액션별 시스템 반응

데이터베이스 스키마 설계서:
3NF 기준, 논리/물리 ERD, PK/FK, 인덱스, 컬럼 타입/제약조건/기본값/코멘트

대시보드 구현 결과물:
로컬 실행 또는 배포 환경에서 로그 수집/조회/시각화가 시연 가능한 결과
```

## 8. 선택 보조 산출물

아래 문서는 팀 상황에 따라 작성합니다. 작성하지 않아도 03 과정의 필수 산출물에는 포함되지 않습니다.

```text
docs/project-plan.md
docs/test-checklist.md
docs/streaming-response-design.md
docs/deployment-guide.md
presentation/final-presentation.md
```

## 9. 03 실습과의 연결

아래 기능은 `03_supabase-and-sse-practice`에서 단계적으로 연습한 뒤 팀 프로젝트에 적용합니다.

```text
01_supabase-project-and-schema
02_fastapi-supabase-api
03_streamlit-dashboard-ui
04_service-log-and-feedback
05_sse-streaming-ai-response
```
