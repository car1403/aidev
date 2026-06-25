# 02 LangGraph CLI Check

이 단계에서는 샘플 Agent 프로젝트를 CLI에서 실행해 LangGraph 흐름이 동작하는지 확인합니다.

## 실행

```powershell
cd C:\aidev\06_llm-agent-mini-project\02_instructor-sample-project
..\.venv\Scripts\Activate.ps1
python -m app.graph
```

## 확인 기준

- 오류 없이 실행되는가?
- Agent State가 단계별로 업데이트되는가?
- Tool 함수가 호출되는가?
- API Key가 없어도 Mock 또는 규칙 기반 응답 흐름을 확인할 수 있는가?

## 이 단계에서 보는 것

Streamlit 화면을 보기 전에 CLI에서 먼저 실행하는 이유는 문제 원인을 찾기 쉽기 때문입니다. CLI에서 동작하지 않는 Agent는 화면에서도 정상 동작하기 어렵습니다.
