# 02 LangGraph CLI Check

수업용 샘플 프로젝트를 CLI에서 실행해 LangGraph 흐름이 동작하는지 확인합니다.

```powershell
cd C:\aidev\05_llm-agent-mini-project\02_instructor-sample-project
..\.venv\Scripts\Activate.ps1
python -m app.graph
```

확인할 것:

- 에러 없이 실행되는가?
- Agent State가 단계별로 업데이트되는가?
- API Key가 없을 때 Mock 또는 규칙 기반 응답이 나오는가?
