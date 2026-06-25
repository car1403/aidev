# 02 Instructor Sample Project

이 폴더는 05 과정에서 먼저 실행해 보는 일정 조정 Agent 샘플 프로젝트입니다.

실제 Calendar API는 사용하지 않습니다. 처음에는 Mock 일정 데이터를 사용해 Agent의 기본 흐름을 이해합니다. 이후 팀 프로젝트에서 필요하면 Google Calendar, Notion, 로컬 파일, pgvector RAG/Memory 같은 기능으로 확장할 수 있습니다.

## 이 샘플에서 확인할 것

- 사용자 요청을 Agent State에 저장하는 방법
- 참석자와 회의 시간을 추출하는 방법
- Python Tool 함수로 Mock 일정 데이터를 조회하는 방법
- LangGraph Node를 순서대로 실행하는 방법
- OpenAI API Key가 없을 때 규칙 기반 메시지로 대체하는 방법
- Streamlit 화면에서 요청과 응답을 확인하는 방법

## 구조

```text
02_instructor-sample-project
├─ .env.example
├─ README.md
├─ requirements.txt
├─ app
│  ├─ __init__.py
│  ├─ graph.py
│  ├─ mock_data.py
│  ├─ schemas.py
│  └─ tools.py
├─ docs
│  ├─ agent-flow.md
│  ├─ test-checklist.md
│  └─ tool-spec.md
└─ frontend
   └─ streamlit_app.py
```

## 실행 준비

05 과정은 최상위 `.venv`를 사용합니다.

```powershell
cd C:\aidev\05_llm-agent-mini-project
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

샘플 프로젝트 폴더 안의 `.env.example`을 `.env`로 복사합니다.

```powershell
cd C:\aidev\05_llm-agent-mini-project\02_instructor-sample-project
Copy-Item .env.example .env
```

OpenAI API Key가 없다면 `.env`의 기본값을 그대로 두어도 됩니다. 이 경우 규칙 기반 메시지 생성 흐름으로 실행됩니다.

## 실행 1. CLI에서 Agent 실행

```powershell
cd C:\aidev\05_llm-agent-mini-project\02_instructor-sample-project
..\.venv\Scripts\Activate.ps1
python -m app.graph
```

CLI 실행에서는 화면 없이 Agent 흐름만 확인합니다. 문제가 생겼을 때 가장 먼저 확인하기 좋은 실행 방식입니다.

## 실행 2. Streamlit UI 실행

```powershell
streamlit run .\frontend\streamlit_app.py --server.port 8701
```

브라우저에서 아래 주소를 엽니다.

```text
http://127.0.0.1:8701
```

## 학습 포인트

- Agent State를 어떻게 설계하는가?
- Tool 실행 결과를 State에 어떻게 저장하는가?
- 조건 분기 없이도 기본 업무 흐름을 어디까지 만들 수 있는가?
- LLM 호출은 어느 Node에 넣는 것이 좋은가?
- API Key가 없는 환경에서도 Mock data로 최소 흐름을 확인할 수 있는가?

## 다음 단계

샘플을 실행한 뒤에는 아래 문서를 읽습니다.

- `docs/agent-flow.md`: Graph 흐름과 State 필드
- `docs/tool-spec.md`: Tool 함수의 역할과 입출력
- `docs/test-checklist.md`: 실행 전후 확인 항목
