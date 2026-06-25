# 00_references

이 폴더는 `04_supabase-ai-mini-project`를 진행할 때 필요한 참고 자료를 모아 둔 곳입니다.

03 과정은 Supabase, FastAPI, Streamlit을 연결해 실시간 로그 대시보드 형태의 미니 프로젝트를 완성하는 과정입니다. Docker, Docker Compose, AWS 배포, GitHub Actions 자동화는 이 과정에서 필수로 진행하지 않고 `07_multi-agent-service-ops`에서 다룹니다.

## 먼저 확인할 기준

03 과정의 최종 프로젝트는 아래 구조를 기준으로 진행합니다.

```text
Streamlit 화면
-> FastAPI API
-> Supabase Database/Auth
-> Gemini API 기본 사용
```

OpenAI API는 선택/비교 실습으로 유지합니다. 무료 배포는 선택 확장입니다.

## 산출물 기준

팀 프로젝트는 아래 4가지 필수 산출물을 기준으로 정리합니다. 나머지 문서와 발표 자료는 선택 보조 산출물입니다.

| 산출물 | 확인할 내용 |
| --- | --- |
| API 설계 문서 | URL, HTTP Method, 표준 에러 응답, Pydantic Request/Response 모델 |
| 화면 설계서 | 화면 목록, 와이어프레임, 사용자 액션, 로딩/오류/피드백 표시 |
| 데이터베이스 스키마 설계서 | 테이블, ERD, PK/FK, 인덱스, 컬럼 타입, RLS 기준 |
| 대시보드 구현 결과물 | 로그 수집, 조회, 시각화, 피드백 반영, SSE 또는 자동 새로고침 |

## 참고 자료 목록

```text
00_references
├─ README.md
├─ 01_local-run-first-look.md
├─ 02_project-architecture.md
├─ 03_common-commands.md
├─ 04_env-port-guide.md
├─ 05_api-supabase-flow.md
├─ 06_troubleshooting-for-beginners.md
├─ 07_project-workflow-tips.md
├─ 08_free-deployment-guide.md
├─ mini-project-deliverables-guide.md
└─ supabase
```

## 읽는 순서

1. [README.md](../README.md)에서 03 과정의 목표와 산출물을 확인합니다.
2. [SETUP.md](../SETUP.md)에서 `.venv`, 패키지 설치, `.env` 준비 방법을 확인합니다.
3. [01_local-run-first-look.md](./01_local-run-first-look.md)에서 로컬 실행 흐름을 이해합니다.
4. [02_project-architecture.md](./02_project-architecture.md)에서 FastAPI, Streamlit, Supabase의 역할을 구분합니다.
5. [04_env-port-guide.md](./04_env-port-guide.md)에서 환경변수와 포트 기준을 확인합니다.
6. [03_common-commands.md](./03_common-commands.md)에서 자주 쓰는 명령어를 확인합니다.
7. [05_api-supabase-flow.md](./05_api-supabase-flow.md)에서 API와 Supabase 데이터 흐름을 확인합니다.
8. [mini-project-deliverables-guide.md](./mini-project-deliverables-guide.md)에서 산출물 작성 기준을 확인합니다.
9. [06_troubleshooting-for-beginners.md](./06_troubleshooting-for-beginners.md)에서 자주 만나는 오류 해결 방법을 확인합니다.
10. [07_project-workflow-tips.md](./07_project-workflow-tips.md)에서 프로젝트 진행 순서를 확인합니다.
11. [08_free-deployment-guide.md](./08_free-deployment-guide.md)에서 선택 배포 흐름을 확인합니다.
12. [supabase](./supabase) 폴더에서 key, RLS, Supabase 화면 사용법을 확인합니다.

## 기억할 점

처음부터 모든 문서를 외우려고 하지 않아도 됩니다. 실습 중에 막히는 지점이 생기면 이 폴더로 돌아와서 필요한 문서를 다시 확인하면 됩니다.
