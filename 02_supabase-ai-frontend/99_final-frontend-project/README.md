# 99_final-frontend-project

이 폴더는 `02_supabase-ai-frontend`의 마지막 실습입니다. 직접 Streamlit 화면을 만들고, FastAPI 백엔드 API를 호출하고, 서비스 로그를 확인한 뒤, 무료 배포 서비스에 올려보는 흐름을 간단한 예제로 경험합니다.

## 최종 실습 주제

```text
개인화 AI 챗봇 서비스 통합 구현
서비스 로그 수집
최종 배포 실습
```

무료 배포 서비스는 다음 흐름으로 사용합니다.

```text
FastAPI 백엔드 -> Render
Redis 캐시/세션 -> Upstash
Streamlit 프론트엔드 -> Streamlit Community Cloud
```

이 실습은 운영 자동화 과정이 아닙니다. Docker, Docker Compose, AWS, GitHub Actions 기반 운영 자동화는 `06_multi-agent-service-ops`에서 더 깊게 다룹니다.

## 이 폴더에서 배우는 것

- Streamlit으로 개인화 챗봇 화면을 구성합니다.
- `API_BASE_URL`을 사용해 FastAPI 백엔드를 호출합니다.
- 사용자 이름, 질문, AI 응답, 서비스 로그를 화면에서 확인합니다.
- 백엔드가 남긴 로그를 프론트엔드에서 조회합니다.
- Render, Upstash, Streamlit Community Cloud 배포 흐름을 초보자 기준으로 따라갑니다.
- 이 예제를 `03_supabase-ai-mini-project`의 팀 프로젝트로 확장하는 방법을 이해합니다.

## 폴더 구조

```text
99_final-frontend-project
├─ README.md
├─ SETUP.md
├─.env.example
├─ backend
│ ├─ main.py
│ └─ requirements.txt
├─ frontend
│ ├─ app.py
│ ├─ requirements.txt
│ └─ pages
│ ├─ 01_chatbot.py
│ ├─ 02_chat_history.py
│ ├─ 03_service_logs.py
│ └─ 04_deployment_check.py
└─ docs
 ├─ free-deployment-guide.md
 ├─ connect-to-03-mini-project.md
 └─ final-checklist.md
```

## 실행 순서

처음에는 로컬에서 백엔드와 프론트엔드를 각각 실행합니다.

```text
1..env 파일 준비
2. FastAPI 백엔드 실행
3. Streamlit 프론트엔드 실행
4. 챗봇 질문 전송
5. 대화 이력과 서비스 로그 확인
6. 배포 가이드에 따라 Render, Upstash, Streamlit Community Cloud 배포
```

자세한 로컬 실행 방법은 [SETUP.md](./SETUP.md)를 먼저 봅니다.

배포는 [docs/free-deployment-guide.md](./docs/free-deployment-guide.md)를 따라 진행합니다.

## 03 미니 프로젝트와의 연결

이 폴더는 `03_supabase-ai-mini-project`의 축소판입니다.

```text
02 최종 예제
-> Streamlit 화면
-> FastAPI API 호출
-> 대화 이력과 서비스 로그 확인
-> 무료 배포 흐름 체험

03 미니 프로젝트
-> Supabase 테이블 설계
-> 사용자/대화/로그/피드백 저장
-> SSE 기반 실시간 응답 스트리밍
-> API 설계 문서, 화면 설계서, DB 설계서, 대시보드 산출물 작성
```

즉, 02에서는 “프론트엔드가 백엔드를 호출하는 감각”을 익히고, 03에서는 같은 흐름을 Supabase와 팀 프로젝트 산출물까지 확장합니다.

