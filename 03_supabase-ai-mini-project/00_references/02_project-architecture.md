# Project Architecture

03 과정의 미니 프로젝트는 Supabase, FastAPI, Streamlit을 연결하는 구조로 진행합니다.

```text
Streamlit Frontend
-> FastAPI Backend
-> Supabase Database/Auth
-> Gemini API 또는 데이터 처리 로직
```

Docker, Docker Compose, 로컬 PostgreSQL 컨테이너, Redis 컨테이너는 이 과정의 기본 실행 방식이 아닙니다. 해당 내용은 `06_multi-agent-service-ops`에서 서비스 운영 관점으로 학습합니다.

## Frontend

Streamlit은 사용자가 보는 화면입니다.

역할:

- 학습 로그 또는 대화 메시지 입력
- 데이터 목록과 대시보드 표시
- 상태 변경 버튼 제공
- FastAPI API 호출
- 로그인 상태와 화면 상태 관리

## Backend

FastAPI는 요청 검증과 API 응답을 담당합니다.

역할:

- 요청 데이터 검증
- Supabase 테이블에 데이터 저장
- Supabase 테이블에서 데이터 조회
- AI API 호출이 필요한 경우 서버 쪽에서 처리
- 프론트엔드에 JSON 응답 반환

## Supabase

Supabase는 프로젝트의 데이터 저장과 인증 기반을 담당합니다.

예시 테이블:

- `learning_logs`: 학습 기록
- `conversations`: 사용자별 대화 이력
- `usage_logs`: 사용 로그
- `profiles`: 사용자 프로필

Supabase에서 특히 확인할 것:

- Project URL
- anon key
- service role key
- Table Editor
- SQL Editor
- Auth
- RLS 정책

## AI API

03 과정에서는 Gemini API를 기본 AI API로 사용합니다. Gemini API는 FastAPI 백엔드에서 호출하고, Streamlit은 FastAPI 응답만 표시하는 구조로 진행합니다.

기존 OpenAI API 예제는 삭제하지 않고 선택/비교 실습으로 유지합니다. 팀 프로젝트에서 OpenAI를 사용하려면 비용과 API 결제 구조를 별도로 확인한 뒤 진행합니다.

AI API key는 화면 코드에 직접 쓰지 않고 `.env`에서 읽습니다. 가능하면 FastAPI 백엔드에서 AI API를 호출하고, Streamlit은 FastAPI의 응답만 표시하도록 구성합니다.

## 로컬 실행에서의 주소

이 과정에서는 FastAPI와 Streamlit을 로컬 PC에서 실행합니다.

```text
FastAPI: http://127.0.0.1:8000
Streamlit: http://127.0.0.1:8501
Supabase: 클라우드 프로젝트 URL 사용
```

프론트엔드가 백엔드를 호출할 때는 보통 다음 주소를 사용합니다.

```text
http://127.0.0.1:8000
```

이 값은 `.env`의 `API_BASE_URL`에 저장합니다.
