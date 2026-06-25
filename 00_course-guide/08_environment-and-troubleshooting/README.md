# 08_environment-and-troubleshooting

환경 설정과 오류 해결 자료입니다.

처음 설치 안내는 `03_student-guides/01_getting-started`에서 봅니다. 이 폴더는 설치나 실행 중 문제가 생겼을 때 확인합니다.

## 문서 목록

```text
01_python-install-check.md
02_venv-troubleshooting.md
03_powershell-policy-guide.md
04_fastapi-errors.md
05_streamlit-errors.md
06_supabase-errors.md
07_docker-errors-for-later-courses.md
08_common-error-messages.md
09_codex-account-and-billing-troubleshooting.md
```

## 막힘 지점별 빠른 링크

| 막히는 지점 | 먼저 볼 문서 |
| --- | --- |
| Supabase 프로젝트 생성, RLS, service role key 구분 | [06_supabase-errors.md](./06_supabase-errors.md), [02 Supabase Backend SETUP](../../02_supabase-ai-backend/SETUP.md), [env-and-secret-management.md](../../02_supabase-ai-backend/03_supabase-db-and-auth/00_references/env-and-secret-management.md) |
| Gemini/OpenAI API key, 비용, 호출 제한 | [OpenAI 계정과 결제 안내](../03_student-guides/01_getting-started/09_openai-account-billing-guide.md), [Codex/OpenAI 문제 해결](./09_codex-account-and-billing-troubleshooting.md), [API key and billing](../../02_supabase-ai-backend/02_llm-api-integration/02_api-key-and-billing/README.md) |
| Streamlit에서 백엔드 연결 실패 | [05_streamlit-errors.md](./05_streamlit-errors.md), [03 Supabase Frontend SETUP](../../03_supabase-ai-frontend/SETUP.md), [04_fastapi-errors.md](./04_fastapi-errors.md) |
| LangGraph 상태 흐름 이해가 어려움 | [05 LLM Agent README](../../05_llm-agent-orchestration/README.md), [LangGraph state flow](../../05_llm-agent-orchestration/06_langgraph-state-flow/README.md), [common errors for beginners](../../05_llm-agent-orchestration/00_references/07_common-errors-for-beginners.md) |
| Docker Compose, 포트 충돌, `.env` 위치 | [07_docker-errors-for-later-courses.md](./07_docker-errors-for-later-courses.md), [07 Service Ops SETUP](../../07_multi-agent-service-ops/SETUP.md), [Docker Compose multi service](../../07_multi-agent-service-ops/02_service-deployment-and-automation/02_docker-compose-multi-service/README.md) |
| GitHub Actions/AWS 선택 실습의 비용 리스크 | [07 Service Ops SETUP](../../07_multi-agent-service-ops/SETUP.md), [AWS deployment checklist](../../07_multi-agent-service-ops/02_service-deployment-and-automation/10_labs/lab-05_aws-deployment-checklist.md), [optional AWS deployment](../../07_multi-agent-service-ops/02_service-deployment-and-automation/10_labs/lab-06_aws-apprunner-ecs-optional-deployment.md) |

## 오류를 해결하는 기본 순서

오류가 나오면 바로 코드를 고치기보다 아래 순서로 확인합니다.

```text
1. 현재 폴더 위치가 맞는지 확인한다.
2..venv가 활성화되어 있는지 확인한다.
3. 필요한 패키지를 설치했는지 확인한다.
4..env 파일이 필요한 실습인지 확인한다.
5. 오류 메시지를 처음 줄부터 끝까지 읽는다.
6. 오류 메시지 전체를 복사해 진행 중인 화면을 공유한다.
```

Codex, OpenAI 계정, 결제, API Key 관련 문제는 `09_codex-account-and-billing-troubleshooting.md`를 먼저 확인합니다.
