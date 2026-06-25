# 06_llm-agent-mini-project

`06_llm-agent-mini-project`는 `05_llm-agent-orchestration`에서 배운 LangGraph, Tool Use, Agent 상태 관리, 오류 감지와 자기 성찰 흐름을 팀 미니 프로젝트로 정리하는 과정입니다.

이 과정의 목표는 단일 Agent가 사용자 요청을 분석하고, 필요한 Tool을 선택하고, 오류를 감지한 뒤 재시도 또는 fallback을 수행하는 구조를 구현하고 문서화하는 것입니다.

## 핵심 기준

- 처음에는 Mock data와 로컬 실행으로 Agent 흐름을 완성합니다.
- OpenAI API, Ollama, pgvector 기반 장기 기억은 선택 확장입니다.
- Docker와 배포는 필수가 아니며, 운영 확장은 `07_multi-agent-service-ops`에서 다룹니다.
- 코드만 제출하지 않고 Agent 설계와 시험 결과를 문서로 설명합니다.

## 필수 산출물

| 산출물 | 파일 예시 | 핵심 확인 기준 |
| --- | --- | --- |
| 에이전트 아키텍처 설계서 | `docs/agent-architecture.md` | StateGraph의 Node, Edge, 상태 필드, Tool 호출 흐름이 명확한가 |
| 에이전트 시험 결과 보고서 | `docs/agent-test-report.md` | 오류 감지, 재시도, fallback, 성능 비교, 개선 전후 결과가 정리되었는가 |

테스트 체크리스트, 발표 자료, Docker 실행 가이드, 장기 기억 설계서는 선택 보조 산출물입니다.

## 과정 구조

```text
06_llm-agent-mini-project
├─ README.md
├─ SETUP.md
├─ .env.example
├─ requirements.txt
├─ 00_references
├─ 01_local-dev-basic
├─ 02_instructor-sample-project
├─ 03_team-project-guide
├─ 04_agent-project-practice
├─ 05_llm-agent-sample-assets
└─ 99_team-projects
```

## 권장 진행 순서

1. [SETUP.md](./SETUP.md)를 보고 `.venv`, 패키지, 선택 API Key를 준비합니다.
2. [00_references](./00_references/README.md)에서 프로젝트 큰 그림과 체크리스트를 확인합니다.
3. [01_local-dev-basic](./01_local-dev-basic/README.md)에서 Python, LangGraph, Streamlit 실행 상태를 확인합니다.
4. [02_instructor-sample-project](./02_instructor-sample-project/README.md)를 실행해 일정 조정 Agent 예제를 확인합니다.
5. [03_team-project-guide](./03_team-project-guide/README.md)에서 팀 주제와 산출물 기준을 정리합니다.
6. [04_agent-project-practice](./04_agent-project-practice/README.md)에서 Agent 설계와 시험 흐름을 작성합니다.
7. [99_team-projects](./99_team-projects/README.md)의 팀 템플릿으로 최종 프로젝트를 진행합니다.

## 빠른 실행

```powershell
cd C:\aidev\06_llm-agent-mini-project
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
```

VS Code에서 `C:\aidev\06_llm-agent-mini-project` 폴더 자체를 열면 `.vscode/settings.json` 설정에 따라 새 터미널에서 `.venv`가 자동 활성화됩니다.
