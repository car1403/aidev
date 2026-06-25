# AI Development Course

이 저장소는 Python 기초부터 Supabase 기반 AI 서비스, LLM Agent, Docker 기반 서비스 운영, 멀티 에이전트 미니 프로젝트까지 단계적으로 학습하기 위한 과정 자료입니다.

현재 과정은 `01`부터 `07`까지 진행합니다.

## 빠른 바로가기

처음 시작할 때는 아래 문서부터 확인하시면 됩니다.

- [전체 운영 안내](./00_admin/README.md)
- [처음 시작 가이드](./00_admin/03_student-guides/01_getting-started/README.md)
- [GitHub 계정 준비 및 VS Code 설치](./00_admin/03_student-guides/01_getting-started/02_vscode-install-guide.md)
- [VS Code 확장 프로그램과 GitHub Copilot Chat](./00_admin/03_student-guides/01_getting-started/03_vscode-extensions-guide.md)
- [Python 가상환경(.venv)과 pip 사용법](./00_admin/03_student-guides/01_getting-started/05_venv-and-pip-guide.md)
- [Markdown 문서 보기와 작성법](./00_admin/03_student-guides/01_getting-started/06_markdown-preview-guide.md)
- [첫 실행 체크리스트](./00_admin/03_student-guides/01_getting-started/07_first-run-checklist.md)
- [Codex 설치와 로그인 안내](./00_admin/03_student-guides/01_getting-started/08_codex-install-and-login-guide.md)
- [OpenAI 계정과 결제 안내](./00_admin/03_student-guides/01_getting-started/09_openai-account-billing-guide.md)

## 과정 바로가기

| 순서 | 과정 | 핵심 내용 | 바로가기 |
| --- | --- | --- | --- |
| 00 | 운영 안내 | 개발 환경 준비, 문서 보는 법, 과정 진행 기준 | [README](./00_admin/README.md) |
| 01 | Supabase AI Backend | Python, FastAPI, Gemini API, Supabase, Upstash Redis, 백엔드 미니 서비스 | [README](./01_supabase-ai-backend/README.md) / [SETUP](./01_supabase-ai-backend/SETUP.md) |
| 02 | Supabase AI Frontend | Streamlit UI, 챗봇 화면, API 연동, 상태 관리, 프론트엔드 배포 | [README](./02_supabase-ai-frontend/README.md) / [SETUP](./02_supabase-ai-frontend/SETUP.md) |
| 03 | Supabase AI Mini Project | 백엔드, 프론트엔드, Supabase, SSE 스트리밍을 연결한 팀 프로젝트 | [README](./03_supabase-ai-mini-project/README.md) / [SETUP](./03_supabase-ai-mini-project/SETUP.md) |
| 04 | LLM Agent Orchestration | Docker 기반 로컬 LLM 환경, LangGraph, Tool Use, Memory, RAG | [README](./04_llm-agent-orchestration/README.md) / [SETUP](./04_llm-agent-orchestration/SETUP.md) |
| 05 | LLM Agent Mini Project | 단일 Agent 추론, 도구 선택, 자기 성찰, 결과 검증 프로젝트 | [README](./05_llm-agent-mini-project/README.md) / [SETUP](./05_llm-agent-mini-project/SETUP.md) |
| 06 | Multi-Agent Service Ops | Docker Compose, AWS, GitHub Actions, 모니터링, 보안 가드레일 | [README](./06_multi-agent-service-ops/README.md) / [SETUP](./06_multi-agent-service-ops/SETUP.md) |
| 07 | Multi-Agent Service Mini Project | 멀티 에이전트 협업, 장애 복구, 배포 파이프라인 프로젝트 | [README](./07_multi-agent-service-mini-project/README.md) / [SETUP](./07_multi-agent-service-mini-project/SETUP.md) |

## 학습 흐름

1. [00_admin](./00_admin/README.md)에서 개발 환경과 문서 읽는 방법을 먼저 확인합니다.
2. [01_supabase-ai-backend](./01_supabase-ai-backend/README.md)에서 Python, FastAPI, Supabase, Gemini API 기반 백엔드 흐름을 익힙니다.
3. [02_supabase-ai-frontend](./02_supabase-ai-frontend/README.md)에서 Streamlit UI와 백엔드 API 연동을 실습합니다.
4. [03_supabase-ai-mini-project](./03_supabase-ai-mini-project/README.md)에서 백엔드, 프론트엔드, Supabase, SSE 스트리밍을 하나의 프로젝트로 연결합니다.
5. [04_llm-agent-orchestration](./04_llm-agent-orchestration/README.md)부터는 Docker 기반 환경에서 Agent, Tool, Memory, RAG 구조를 다룹니다.
6. [05_llm-agent-mini-project](./05_llm-agent-mini-project/README.md)에서 단일 Agent 프로젝트를 완성합니다.
7. [06_multi-agent-service-ops](./06_multi-agent-service-ops/README.md)에서 Docker Compose, AWS, GitHub Actions, 운영 관측성을 학습합니다.
8. [07_multi-agent-service-mini-project](./07_multi-agent-service-mini-project/README.md)에서 멀티 에이전트 서비스 운영 프로젝트로 마무리합니다.

## 환경 준비 링크

개발 환경 설정은 한 번에 완벽하게 끝내기보다, 필요한 시점에 다시 확인하면서 진행하면 됩니다.

- Python 설치: [01_python-install-guide.md](./00_admin/03_student-guides/01_getting-started/01_python-install-guide.md)
- GitHub 계정과 VS Code 설치: [02_vscode-install-guide.md](./00_admin/03_student-guides/01_getting-started/02_vscode-install-guide.md)
- VS Code 확장 프로그램: [03_vscode-extensions-guide.md](./00_admin/03_student-guides/01_getting-started/03_vscode-extensions-guide.md)
- 터미널 기본 명령어: [04_terminal-basic-guide.md](./00_admin/03_student-guides/01_getting-started/04_terminal-basic-guide.md)
- 가상환경과 pip: [05_venv-and-pip-guide.md](./00_admin/03_student-guides/01_getting-started/05_venv-and-pip-guide.md)
- Markdown 문서 보기: [06_markdown-preview-guide.md](./00_admin/03_student-guides/01_getting-started/06_markdown-preview-guide.md)
- Codex 설치와 로그인: [08_codex-install-and-login-guide.md](./00_admin/03_student-guides/01_getting-started/08_codex-install-and-login-guide.md)

## 주요 기준

- `01`부터 `03`까지는 Supabase 중심으로 진행합니다.
- `04`부터 Docker 기반 로컬 실행 환경을 본격적으로 사용합니다.
- Docker Compose, AWS, GitHub Actions는 [06_multi-agent-service-ops](./06_multi-agent-service-ops/README.md)에서 집중적으로 다룹니다.
- Gemini는 초반 실습의 기본 LLM으로 사용하고, OpenAI 예제는 비교와 확장 학습용으로 유지합니다.
- GitHub Copilot Chat은 VS Code 안에서 AI 보조 개발을 경험하기 위한 도구로 사용합니다.

## 문서 읽는 방법

각 과정 폴더에는 보통 다음 문서가 있습니다.

- `README.md`: 과정 목표, 학습 순서, 챕터 안내
- `SETUP.md`: 설치, 실행, 환경 변수 설정
- `00_references`: 참고 개념, 용어, 보충 자료
- 각 챕터 폴더의 `README.md`: 해당 챕터의 실습 목표와 진행 방법
- `10_labs`, `20_assignments`, `99_*`: 실습, 과제, 미니 프로젝트

필요한 설명을 찾을 때는 이 README의 링크를 먼저 사용하고, 세부 실습은 각 과정의 `README.md`에서 해당 챕터로 이동하시면 됩니다.
