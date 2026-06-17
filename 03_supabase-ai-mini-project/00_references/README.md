# 00_references

이 폴더는 `03_supabase-ai-mini-project`를 진행할 때 필요한 참고 자료를 모아 둔 곳입니다.

03 과정에서는 Supabase 클라우드 프로젝트를 데이터 저장소로 사용하고, FastAPI와 Streamlit은 로컬 Python 가상환경에서 실행합니다. Docker, Docker Compose, AWS 배포, 운영 자동화는 이 과정에서 진행하지 않고 `06_multi-agent-service-ops`에서 학습합니다.

## 먼저 확인할 기준

03 과정의 최종 프로젝트는 Supabase, FastAPI, Streamlit을 연결한 **실시간 로그 대시보드 인터페이스**입니다.

학생은 이 폴더의 참고 자료를 보면서 다음 산출물을 준비합니다.

| 산출물 | 확인할 내용 |
| --- | --- |
| API 설계 문서 | URL, HTTP Method, 표준 에러 응답, Pydantic Request/Response 모델 |
| 화면 설계서 | 화면 목록, 와이어프레임, 사용자 액션, 로딩/오류/피드백 표시 |
| 데이터베이스 설계서 | 테이블, ERD, PK/FK, 인덱스, 컬럼 타입, RLS 기준 |
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

1. `README.md`에서 03 과정의 목표와 산출물을 확인합니다.
2. `mini-project-deliverables-guide.md`에서 API, 화면, 데이터베이스, 대시보드 산출물 기준을 확인합니다.
3. `01_local-run-first-look.md`에서 로컬 실행 흐름을 확인합니다.
4. `02_project-architecture.md`에서 FastAPI, Streamlit, Supabase의 역할을 구분합니다.
5. `04_env-port-guide.md`에서 `.env`와 포트 설정을 확인합니다.
6. `03_common-commands.md`에서 자주 쓰는 실행 명령어를 확인합니다.
7. `05_api-supabase-flow.md`에서 API와 Supabase 데이터 흐름을 확인합니다.
8. `06_troubleshooting-for-beginners.md`에서 자주 만나는 오류 해결 방법을 확인합니다.
9. `07_project-workflow-tips.md`에서 팀 프로젝트 진행 순서를 확인합니다.
10. `08_free-deployment-guide.md`에서 무료 배포 시연 흐름을 확인합니다.
11. `supabase` 폴더의 보안/RLS 자료를 확인합니다.

## 수업에서 사용하는 방법

강사와 학생은 수업 시작 시 이 폴더를 함께 열고, 오늘 실습에서 필요한 참고 문서만 선택해서 봅니다.

처음부터 모든 문서를 외울 필요는 없습니다. 실습 중 막히는 지점이 생기면 이 폴더로 돌아와서 환경 변수, 포트, Supabase 흐름, 산출물 기준을 다시 확인하면 됩니다.
