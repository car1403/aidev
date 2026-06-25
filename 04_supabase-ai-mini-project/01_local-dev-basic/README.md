# 01_local-dev-basic

이 단원은 Supabase 미니 프로젝트를 로컬 Python 환경에서 실행하는 기본 방법을 학습합니다.

`04_supabase-ai-mini-project`에서는 Docker로 PostgreSQL이나 Redis를 실행하지 않습니다. Supabase 클라우드 프로젝트를 데이터 저장소로 사용하고, 개인 PC에서는 FastAPI와 Streamlit만 실행합니다. Docker, Docker Compose, AWS 배포, 운영 자동화는 `07_multi-agent-service-ops`에서 학습합니다.

이 단원은 `02_supabase-ai-backend`와 `03_supabase-ai-frontend`에서 배운 실행 방식을 하나로 연결하는 준비 단계입니다.

```text
02_supabase-ai-backend
-> FastAPI, Supabase, Gemini, Upstash Redis 기초

03_supabase-ai-frontend
-> Streamlit 화면, API 호출, 상태 표시, 서비스 로그 조회

04_supabase-ai-mini-project
-> FastAPI + Streamlit + Supabase를 하나의 미니 프로젝트로 통합
```

## 실행 환경 기준

이 단원에서는 하위 폴더마다 `.venv`를 새로 만들지 않습니다.

```text
C:\aidev\04_supabase-ai-mini-project\.venv
```

위 공통 가상환경 하나를 사용합니다.

환경변수도 아래 파일을 기준으로 사용합니다.

```text
C:\aidev\04_supabase-ai-mini-project\.env
```

즉, `C:\aidev\.env`, `02_supabase-ai-backend\.env`, `03_supabase-ai-frontend\.env`를 사용하는 구조가 아닙니다. 각 과정은 자기 폴더의 `.env`를 기준으로 실행합니다.

## 학습 목표

- `.env`에 Supabase 연결 값을 준비할 수 있다.
- FastAPI를 로컬 Python 환경에서 실행할 수 있다.
- Streamlit을 로컬 Python 환경에서 실행할 수 있다.
- Streamlit, FastAPI, Supabase의 연결 구조를 설명할 수 있다.
- 백엔드와 프론트엔드를 각각 다른 PowerShell에서 실행할 수 있다.
- 프론트엔드에는 Supabase `service_role` key나 LLM API key를 넣지 않는 이유를 설명할 수 있다.
- 04 과정에서 Gemini가 기본 LLM이고 OpenAI는 선택/비교 실습이라는 기준을 설명할 수 있다.

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
LLM: Gemini 기본, OpenAI 선택 비교
Redis: 필요하면 Upstash Redis를 선택 사용
```

## 핵심 요약

- Supabase 테이블은 Supabase 화면 또는 SQL Editor에서 준비합니다.
- FastAPI는 Supabase에 저장/조회 요청을 보냅니다.
- Streamlit은 FastAPI API를 호출해서 화면에 결과를 표시합니다.
- service role key는 프론트엔드 화면에 넣지 않습니다.
- Gemini API key는 백엔드에서 사용하는 값입니다. Streamlit 화면 코드에 직접 넣지 않습니다.
- 배포는 필수가 아닙니다. 기본 제출 기준은 로컬에서 FastAPI, Streamlit, Supabase가 정상 연결되는 것입니다.
