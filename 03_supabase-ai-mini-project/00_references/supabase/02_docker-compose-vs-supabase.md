# 02 Supabase First, Docker Later

03 과정에서는 Supabase를 먼저 사용합니다.

Docker Compose도 중요한 기술이지만, 03 미니 프로젝트의 목표는 데이터베이스 운영보다 서비스 기능을 빠르게 완성하는 것입니다. 그래서 Supabase 프로젝트를 만들고, FastAPI와 Streamlit을 연결하는 흐름에 집중합니다.

## 03 과정에서 사용하는 방식

```text
Streamlit
-> FastAPI
-> Supabase Database/Auth
```

개인 PC에서는 다음만 실행합니다.

```text
FastAPI: uvicorn
Streamlit: streamlit run
```

## Docker를 지금 하지 않는 이유

초보자가 처음부터 Docker까지 함께 다루면 오류 원인을 구분하기 어렵습니다.

예를 들어 화면이 안 열릴 때 다음 중 무엇이 문제인지 동시에 확인해야 합니다.

- Python 가상환경 문제
- FastAPI 실행 문제
- Streamlit 실행 문제
- API 주소 문제
- 컨테이너 실행 문제
- 컨테이너 네트워크 문제

03 과정에서는 이 복잡도를 줄이고 Supabase 기반 서비스 구현에 집중합니다.

## Docker는 어디에서 배우는가?

Docker, Docker Compose, AWS, GitHub Actions, 운영 모니터링은 `06_multi-agent-service-ops`에서 다룹니다.

03에서 만든 미니 프로젝트를 나중에 06 과정의 운영 지식과 연결하면, 같은 서비스가 개발 단계에서 운영 단계로 확장되는 흐름을 이해할 수 있습니다.
