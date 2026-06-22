# 01 Local Run First Look

이 과정에서는 프로젝트를 로컬 Python 실행 방식으로 진행합니다.

## 로컬 실행이란?

FastAPI와 Streamlit을 Docker 이미지로 만들지 않고, 개인 PC의 Python 가상환경에서 직접 실행하는 방식입니다. 데이터 저장소는 로컬 컨테이너가 아니라 Supabase 클라우드 프로젝트를 사용합니다.

```text
FastAPI -> uvicorn으로 실행
Streamlit -> streamlit run으로 실행
Supabase -> 클라우드 프로젝트 사용
```

## 왜 먼저 로컬 실행을 배우는가?

초보자는 먼저 프로그램이 어떻게 연결되는지 눈으로 확인해야 합니다.

로컬 실행을 사용하면 다음을 쉽게 볼 수 있습니다.

- 백엔드 서버가 어느 포트에서 실행되는지
- 프론트엔드가 어떤 주소로 백엔드를 호출하는지
- `.env` 값이 어디에서 사용되는지
- Supabase 테이블 조회/저장이 어느 API에서 일어나는지
- 오류가 백엔드에서 난 것인지, 프론트엔드에서 난 것인지

## 06 과정과의 관계

03 과정에서는 Supabase, FastAPI, Streamlit을 로컬 Python 방식으로 연결합니다.

Docker, Docker Compose, AWS, GitHub Actions, 운영 모니터링은 `06_multi-agent-service-ops`에서 서비스 운영 관점으로 학습합니다.
