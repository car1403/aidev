# 04_supabase-ai-mini-project

`04_supabase-ai-mini-project`는 `02_supabase-ai-backend`와 `03_supabase-ai-frontend`에서 배운 FastAPI, Streamlit, Supabase, Gemini API 흐름을 하나의 팀 프로젝트로 연결하는 과정입니다.

이 과정의 기본 목표는 로컬 환경에서 FastAPI 백엔드, Streamlit 프론트엔드, Supabase 데이터베이스가 함께 동작하는 AI 서비스 미니 프로젝트를 완성하는 것입니다. Docker, GitHub Actions, AWS 배포는 필수가 아니며 `07_multi-agent-service-ops`에서 본격적으로 다룹니다.

## 핵심 기준

- 기본 LLM은 Gemini입니다.
- OpenAI 예제는 선택/비교 실습으로 유지합니다.
- SSE 스트리밍과 무료 배포는 선택 확장입니다.
- 기본 제출 기준은 로컬에서 FastAPI, Streamlit, Supabase 연결이 정상 동작하는 것입니다.
- 실제 `.env`와 API Key는 제출하지 않습니다.

## 필수 산출물

| 산출물 | 파일 예시 | 핵심 확인 기준 |
| --- | --- | --- |
| API 설계 문서 | `docs/api-spec.md` | 엔드포인트 URL, HTTP Method, 요청/응답 모델, 에러 응답 기준이 명확한가 |
| 화면 설계서 | `docs/ui-design.md` | 메인, 상세, 입력, 설정, 에러 화면과 사용자 액션 흐름이 정리되었는가 |
| 데이터베이스 설계서 | `docs/supabase-schema.md` | 테이블, 컬럼, 타입, 제약조건, 관계, 인덱스 전략이 설명되었는가 |
| 대시보드 구현 결과물 | 실행 화면 또는 `docs/dashboard-result.md` | 로그 수집, 조회, 시각화가 로컬 실행 환경에서 확인 가능한가 |

나머지 프로젝트 계획서, 테스트 체크리스트, SSE 설계서, 배포 가이드, 발표 자료는 선택 보조 산출물입니다.

## 과정 구조

```text
04_supabase-ai-mini-project
├─ README.md
├─ SETUP.md
├─ .env.example
├─ requirements.txt
├─ 00_references
├─ 01_local-dev-basic
├─ 02_instructor-sample-project
├─ 03_supabase-and-sse-practice
├─ 04_team-project-guide
├─ 05_project-templates
└─ 99_team-projects
```

## 권장 진행 순서

1. [SETUP.md](./SETUP.md)를 보고 `.venv`, `.env`, 패키지를 준비합니다.
2. [00_references](./00_references/README.md)에서 프로젝트 기준과 보안 주의 사항을 확인합니다.
3. [01_local-dev-basic](./01_local-dev-basic/README.md)에서 Supabase, FastAPI, Streamlit 로컬 실행을 점검합니다.
4. [02_instructor-sample-project](./02_instructor-sample-project/README.md)로 샘플 구조를 확인합니다.
5. [03_supabase-and-sse-practice](./03_supabase-and-sse-practice/README.md)에서 Supabase 연결, 서비스 로그, 선택 SSE 흐름을 실습합니다.
6. [04_team-project-guide](./04_team-project-guide/README.md)에서 팀 주제와 필수 산출물을 정리합니다.
7. [99_team-projects](./99_team-projects/README.md)의 템플릿을 기반으로 최종 프로젝트를 진행합니다.

## 빠른 실행

```powershell
cd C:\aidev\04_supabase-ai-mini-project
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
```

VS Code에서 `C:\aidev\04_supabase-ai-mini-project` 폴더 자체를 열면 `.vscode/settings.json` 설정에 따라 새 터미널에서 `.venv`가 자동 활성화됩니다.
