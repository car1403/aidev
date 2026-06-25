# 01 Local Dev Basic

이 폴더는 팀 프로젝트를 시작하기 전에 로컬 실행 환경이 준비되었는지 확인하는 곳입니다.

06 과정에서는 처음부터 복잡한 기능을 붙이지 않습니다. 먼저 아래 세 가지가 되는지 확인합니다.

```text
Python 가상환경 활성화
-> LangGraph 기반 샘플 Agent CLI 실행
-> Streamlit 화면 실행
```

## 구성

```text
01_local-dev-basic
├─ README.md
├─ 01_python-env-check
│  └─ README.md
├─ 02_langgraph-cli-check
│  └─ README.md
└─ 03_streamlit-ui-check
   └─ README.md
```

## 권장 순서

1. Python과 `.venv`를 확인합니다.
2. `02_instructor-sample-project`의 LangGraph CLI 예제를 실행합니다.
3. 같은 샘플 프로젝트를 Streamlit 화면으로 실행합니다.

## 완료 기준

- PowerShell에서 `(.venv)`가 보입니다.
- `python -m app.graph` 명령이 오류 없이 실행됩니다.
- `http://127.0.0.1:8701`에서 Streamlit 화면이 열립니다.
- OpenAI API Key가 없어도 Mock 기반 최소 흐름을 확인할 수 있습니다.
