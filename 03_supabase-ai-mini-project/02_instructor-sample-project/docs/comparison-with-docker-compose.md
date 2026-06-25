# Docker Is Covered Later

이 샘플 프로젝트는 Supabase 기반으로 진행합니다.

03 과정에서는 Docker Compose를 사용하지 않습니다. 데이터 저장은 Supabase 클라우드 프로젝트를 사용하고, 로컬 PC에서는 FastAPI와 Streamlit만 Python 가상환경으로 실행합니다.

```text
Streamlit
-> FastAPI
-> Supabase
```

Docker, Docker Compose, AWS, GitHub Actions, 운영 모니터링은 `06_multi-agent-service-ops`에서 학습합니다.

## 이 샘플에서 확인할 기준

```text
가상환경:
C:\aidev\03_supabase-ai-mini-project\.venv

환경변수:
C:\aidev\03_supabase-ai-mini-project\.env

백엔드:
FastAPI + Supabase client

프론트엔드:
Streamlit + httpx
```

이 샘플의 목표는 컨테이너 운영이 아니라, 01/02 과정에서 배운 백엔드와 프론트엔드를 Supabase 데이터 저장 흐름으로 연결하는 것입니다.
