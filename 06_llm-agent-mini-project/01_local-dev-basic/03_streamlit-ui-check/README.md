# 03 Streamlit UI Check

이 단계에서는 샘플 Agent 프로젝트를 Streamlit 화면에서 실행합니다.

## 실행

```powershell
cd C:\aidev\06_llm-agent-mini-project\02_instructor-sample-project
..\.venv\Scripts\Activate.ps1
streamlit run .\frontend\streamlit_app.py --server.port 8701
```

브라우저에서 아래 주소를 엽니다.

```text
http://127.0.0.1:8701
```

## 확인 기준

- 입력창에 일정 요청을 입력할 수 있는가?
- Agent 응답이 화면에 표시되는가?
- 디버깅용 State 또는 실행 로그를 확인할 수 있는가?
- 서버 종료는 PowerShell에서 `Ctrl + C`로 할 수 있는가?

## 포트가 이미 사용 중일 때

8701 포트가 이미 사용 중이면 다른 포트를 사용합니다.

```powershell
streamlit run .\frontend\streamlit_app.py --server.port 8703
```
