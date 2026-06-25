# SETUP

`06_llm-agent-mini-project`의 로컬 실행 준비 문서입니다.

## 1. 작업 위치

```powershell
cd C:\aidev\06_llm-agent-mini-project
```

## 2. Python 가상환경 만들기

이 과정은 최상위 `.venv` 하나를 사용합니다. 팀 템플릿 하위 폴더마다 별도 `.venv`를 만들지 않습니다.

```powershell
python -m venv .venv
```

이미 `.venv`가 있다면 다시 만들 필요는 없습니다.

## 3. 가상환경 활성화

```powershell
.\.venv\Scripts\Activate.ps1
```

PowerShell 앞에 `(.venv)`가 보이면 활성화된 상태입니다.

VS Code에서 `C:\aidev\06_llm-agent-mini-project` 폴더 자체를 열면 `.vscode/settings.json` 설정에 따라 새 터미널에서 `.venv`가 자동 활성화됩니다. `C:\aidev` 루트를 열면 이 설정이 적용되지 않을 수 있습니다.

## 4. 패키지 설치

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 5. 환경변수 파일 만들기

```powershell
Copy-Item .env.example .env
```

OpenAI API Key가 없어도 Mock data 기반 Agent 흐름은 일부 실행할 수 있습니다. 실제 LLM 호출을 진행할 때만 `.env`에 값을 넣습니다.

```env
OPENAI_API_KEY=
OPENAI_MODEL=gpt-4.1-mini
```

Ollama와 pgvector는 선택 확장입니다.

## 6. 샘플 프로젝트 실행

```powershell
cd C:\aidev\06_llm-agent-mini-project\02_instructor-sample-project
..\.venv\Scripts\Activate.ps1
Copy-Item .env.example .env
python -m app.graph
```

Streamlit UI가 있는 예제는 해당 README의 실행 명령을 따릅니다.

## 7. 제출 전 확인

- [ ] 에이전트 아키텍처 설계서를 작성했다.
- [ ] 에이전트 시험 결과 보고서를 작성했다.
- [ ] Tool 선택, 오류 감지, 재시도 또는 fallback 흐름을 설명할 수 있다.
- [ ] `.env`와 API Key를 제출하지 않았다.
- [ ] Docker, 장기 기억, 발표 자료는 선택 보조 산출물로 구분했다.
