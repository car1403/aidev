# 02_instructor-sample-project

수업 중 함께 실행하는 일정 조정 에이전트 샘플 프로젝트입니다.

이 샘플은 실제 캘린더 API를 사용하지 않습니다. 초보자 수업에서는 먼저 Mock 일정 데이터를 사용해 에이전트 흐름을 이해합니다. 이후 팀 프로젝트에서 Google Calendar, Notion, 로컬 파일 저장, 04 방식의 pgvector docker run 등으로 확장할 수 있습니다.

## 기능

- 사용자 요청 분석
- 참석자 일정 조회
- 가능한 시간대 계산
- 일정 제안 메시지 생성
- LangGraph 상태 흐름 실행
- Streamlit 화면에서 에이전트 실행

## 구조

```text
02_instructor-sample-project
├─ README.md
├─.env.example
├─ requirements.txt
├─ app
│ ├─ __init__.py
│ ├─ graph.py
│ ├─ mock_data.py
│ ├─ schemas.py
│ └─ tools.py
├─ frontend
│ └─ streamlit_app.py
└─ docs
 ├─ agent-flow.md
 ├─ tool-spec.md
 └─ test-checklist.md
```

## 설치

이 과정은 상위 폴더의 `.venv`를 사용합니다.

```powershell
cd C:\aidev\05_llm-agent-mini-project
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item.env.example.env
```

## 실행 1. CLI에서 그래프 실행

```powershell
cd C:\aidev\05_llm-agent-mini-project\02_instructor-sample-project
..\.venv\Scripts\Activate.ps1
python -m app.graph
```

## 실행 2. Streamlit UI 실행

```powershell
streamlit run.\frontend\streamlit_app.py --server.port 8701
```

브라우저에서 확인합니다.

```text
http://127.0.0.1:8701
```

## API Key 없이 실행할 때

OpenAI API Key가 없으면 샘플은 규칙 기반 메시지를 생성합니다.

API Key가 있으면 LLM이 더 자연스러운 일정 제안 메시지를 생성합니다.

## 학습 포인트

- 에이전트 상태를 어떻게 설계하는가?
- 도구 실행 결과를 state에 어떻게 저장하는가?
- 조건 분기 없이도 기본 업무 흐름을 어떻게 만들 수 있는가?
- LLM 호출을 어디에 넣는 것이 좋은가?
