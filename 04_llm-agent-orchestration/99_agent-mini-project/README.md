# 99 Agent Mini Project

이 폴더는 04 과정에서 배운 내용을 하나의 미니 프로젝트로 통합하는 단계입니다.

학생은 Prompt, Tool Calling, RAG 또는 Memory, LangGraph State Flow를 사용해 일정 조정 Agent를 만들고 실행 결과를 확인합니다.

## 프로젝트 목표

- Agent가 해결할 문제를 명확히 정의합니다.
- StateGraph의 Node, Edge, State를 설계합니다.
- 필요한 Tool을 Python 함수로 구현합니다.
- Tool 선택, Tool 호출, 결과 검증, Retry 또는 Fallback 흐름을 만듭니다.
- Streamlit 화면 또는 CLI에서 Agent 실행 결과를 확인합니다.
- 최종 발표에서 설계 의도와 테스트 결과를 설명합니다.

## 폴더 구성

```text
99_agent-mini-project
├─ sample-schedule-agent
│  ├─ .env.example
│  ├─ requirements.txt
│  ├─ app
│  │  ├─ graph.py
│  │  ├─ mock_data.py
│  │  ├─ schemas.py
│  │  └─ tools.py
│  └─ frontend
│     └─ streamlit_app.py
└─ team-template
   ├─ backend
   │  ├─ agent_state.py
   │  ├─ graph.py
   │  ├─ requirements.txt
   │  └─ tools.py
   └─ frontend
      └─ app.py
```

## 강사 샘플 실행

```powershell
cd C:\aidev\04_llm-agent-orchestration\99_agent-mini-project\sample-schedule-agent
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
python -m app.graph
```

Streamlit 화면으로 확인하려면 다음 명령을 실행합니다.

```powershell
streamlit run .\frontend\streamlit_app.py --server.port 8601
```

## 팀 템플릿 실행

```powershell
cd C:\aidev\04_llm-agent-orchestration\99_agent-mini-project\team-template
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r .\backend\requirements.txt
python .\backend\graph.py
streamlit run .\frontend\app.py --server.port 8602
```

## 산출물 기준

학생 팀은 최종 발표에서 다음 내용을 설명할 수 있어야 합니다.

- Agent가 해결하려는 문제
- State 필드 설계
- Node와 Edge 흐름
- Tool 목록과 입력/출력
- Memory 또는 RAG 사용 여부
- Retry, Fallback, Reflection 전략
- 실행 화면과 테스트 결과
- 개선 전후 비교 또는 한계점

## 수업 중 확인 질문

- 이 Agent는 어떤 문제를 해결하나요?
- Tool이 2개 이상 필요한 이유는 무엇인가요?
- Agent가 잘못 판단했을 때 어떻게 다시 시도하나요?
- State에 불필요한 정보가 너무 많이 들어가지는 않았나요?
- 최종 사용자에게 보여줄 결과는 충분히 이해하기 쉬운가요?

