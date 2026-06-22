# 01_local-dev-basic

이 단원은 Supabase 미니 프로젝트를 로컬 Python 환경에서 실행하는 기본 방법을 학습합니다.

`03_supabase-ai-mini-project`에서는 Docker로 PostgreSQL이나 Redis를 실행하지 않습니다. Supabase 클라우드 프로젝트를 데이터 저장소로 사용하고, 개인 PC에서는 FastAPI와 Streamlit만 실행합니다. Docker, Docker Compose, AWS 배포, 운영 자동화는 `06_multi-agent-service-ops`에서 학습합니다.

## 학습 목표

- `.env`에 Supabase 연결 값을 준비할 수 있다.
- FastAPI를 로컬 Python 환경에서 실행할 수 있다.
- Streamlit을 로컬 Python 환경에서 실행할 수 있다.
- Streamlit, FastAPI, Supabase의 연결 구조를 설명할 수 있다.
- 백엔드와 프론트엔드를 각각 다른 PowerShell에서 실행할 수 있다.

## 학습 순서

```text
01_supabase-env-check
-> 02_local-fastapi
-> 03_local-streamlit
-> 04_local-full-stack
```

## 핵심 실행 방식

```text
Supabase: 클라우드 프로젝트 사용
FastAPI: uvicorn으로 로컬 실행
Streamlit: streamlit run으로 로컬 실행
.env: Supabase URL/key와 API_BASE_URL 관리
```

## 수업 참여자가 꼭 기억할 점

- Supabase 테이블은 Supabase 화면 또는 SQL Editor에서 준비합니다.
- FastAPI는 Supabase에 저장/조회 요청을 보냅니다.
- Streamlit은 FastAPI API를 호출해서 화면에 결과를 표시합니다.
- service role key는 프론트엔드 화면에 넣지 않습니다.
