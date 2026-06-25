# Docker Is Covered Later

이 통합 실습은 Supabase 기반으로 진행합니다.

04 과정에서는 Docker Compose를 사용하지 않습니다. 데이터 저장은 Supabase 클라우드 프로젝트를 사용하고, 로컬 PC에서는 FastAPI와 Streamlit만 실행합니다.

```text
Streamlit
-> FastAPI
-> Supabase
```

Docker, Docker Compose, AWS, GitHub Actions, 운영 모니터링은 `07_multi-agent-service-ops`에서 학습합니다.

## 왜 여기서는 Docker Compose를 쓰지 않나요?

04 과정의 목표는 운영 환경 구성이 아니라 백엔드, 프론트엔드, Supabase, SSE 스트리밍이 실제로 연결되는 흐름을 이해하는 것입니다.

Docker Compose는 여러 서비스를 한 번에 실행하고 운영하는 데 유용하지만, 처음 통합 프로젝트를 만들 때는 아래 흐름을 먼저 눈으로 확인하는 것이 더 중요합니다.

```text
사용자 입력
-> Streamlit 화면
-> FastAPI API 호출
-> Supabase 저장
-> 응답 표시
```

서비스 운영, 장애 대응, 배포 자동화는 07 과정에서 별도 주제로 확장합니다.
