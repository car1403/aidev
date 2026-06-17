# SETUP

`09_ai-workflow-mini-project` 과정의 실습 환경 설정 문서입니다.

09 과정은 08에서 배운 AIPP, n8n, Dify 기반 AI 워크플로우 자동화 내용을 하나의 팀 미니 프로젝트로 정리하는 단계입니다. 따라서 환경 준비도 단순히 Python만 준비하는 것이 아니라, 샘플 실행, 도구 선택, 팀 프로젝트 시작, 최종 시연까지 이어지도록 준비합니다.

## 1. 수업 전 준비물

수업을 시작하기 전에 아래 항목을 확인합니다.

```text
[ ] Windows PC
[ ] VS Code 또는 Cursor
[ ] Python 3.11 이상
[ ] PowerShell
[ ] Chrome 또는 Edge 브라우저
[ ] Docker Desktop
[ ] OpenAI API Key 또는 강사가 제공한 실습용 API Key
[ ] AIPP 계정 또는 강사가 제공한 실습 계정
[ ] n8n 로컬 실행 환경
[ ] Dify 계정 또는 강사가 제공한 실습 환경
```

09 과정에서는 모든 팀이 AIPP, n8n, Dify를 모두 완성할 필요는 없습니다. 다만 팀 프로젝트에서 최소 1개 이상의 도구를 선택하고, 그 도구를 왜 선택했는지 설명할 수 있어야 합니다.

## 2. 작업 위치로 이동

PowerShell을 열고 과정 폴더로 이동합니다.

```powershell
cd C:\aidev\09_ai-workflow-mini-project
```

현재 위치 확인:

```powershell
Get-Location
```

결과가 아래와 비슷하면 정상입니다.

```text
C:\aidev\09_ai-workflow-mini-project
```

## 3. Python 버전 확인

```powershell
python --version
pip --version
```

권장 버전은 Python 3.11 이상입니다.

Python 명령이 동작하지 않으면 다음을 확인합니다.

```text
Python이 설치되어 있는가?
설치할 때 Add python.exe to PATH를 체크했는가?
PowerShell을 다시 열었는가?
```

## 4. 가상환경 준비

09 과정은 최상위 폴더의 `.venv` 하나를 사용합니다. 하위 폴더마다 `.venv`를 새로 만들지 않습니다.

이미 `.venv`가 있으면 활성화합니다.

```powershell
.\.venv\Scripts\Activate.ps1
```

명령줄 앞에 `(.venv)`가 보이면 정상입니다.

```text
(.venv) PS C:\aidev\09_ai-workflow-mini-project>
```

만약 `.venv`가 없다면 한 번만 생성합니다.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

PowerShell 실행 정책 오류가 나오면 아래 명령을 실행한 뒤 PowerShell을 다시 엽니다.

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

## 5. Python 패키지 설치

가상환경이 활성화된 상태에서 패키지를 설치합니다.

```powershell
pip install -r requirements.txt
```

설치가 끝났는지 간단히 확인합니다.

```powershell
python .\01_local-dev-basic\01_python-env-check\01_check_python_env.py
```

## 6. 환경변수 파일 만들기

최상위 `.env.example`을 복사해 `.env`를 만듭니다.

```powershell
Copy-Item .env.example .env
```

`.env`에는 실제 API Key와 도구 주소를 입력합니다.

```env
API_BASE_URL=http://127.0.0.1:8900
OPENAI_API_KEY=your-openai-api-key
OPENAI_MODEL=gpt-4.1-mini
AIPP_API_KEY=your-aipp-api-key
N8N_BASE_URL=http://localhost:5678
DIFY_API_KEY=your-dify-api-key
DIFY_BASE_URL=http://localhost
```

주의:

```text
.env 파일은 GitHub에 올리지 않습니다.
API Key는 코드, README, 발표 자료에 직접 적지 않습니다.
개인정보나 회사 내부 문서는 실습용 더미 데이터로 대체합니다.
```

## 7. 강사 샘플 프로젝트 실행

강사 샘플은 FastAPI backend와 Streamlit frontend로 구성되어 있습니다. PowerShell을 두 개 열어 실행하는 것을 권장합니다.

### 7.1 Backend 실행

첫 번째 PowerShell:

```powershell
cd C:\aidev\09_ai-workflow-mini-project
.\.venv\Scripts\Activate.ps1
cd .\02_instructor-sample-project
Copy-Item .env.example .env
uvicorn backend.main:app --reload --host 127.0.0.1 --port 8900
```

브라우저에서 확인합니다.

```text
Backend health: http://127.0.0.1:8900/health
API docs      : http://127.0.0.1:8900/docs
```

### 7.2 Frontend 실행

두 번째 PowerShell:

```powershell
cd C:\aidev\09_ai-workflow-mini-project
.\.venv\Scripts\Activate.ps1
cd .\02_instructor-sample-project
streamlit run frontend/app.py --server.port 8901
```

브라우저에서 확인합니다.

```text
Frontend: http://127.0.0.1:8901
```

서버를 멈출 때는 각 PowerShell에서 `Ctrl + C`를 누릅니다.

## 8. 강사 샘플에서 확인할 내용

샘플을 실행한 뒤 학생은 아래를 확인합니다.

```text
[ ] 문의 입력 화면이 열리는가?
[ ] 정상 문의를 입력했을 때 결과가 나오는가?
[ ] 긴급 문의를 입력했을 때 긴급 처리 흐름이 보이는가?
[ ] backend /docs에서 API 구조를 확인했는가?
[ ] docs/aipp-workflow-plan.md를 읽었는가?
[ ] docs/n8n-workflow-plan.md를 읽었는가?
[ ] docs/dify-workflow-plan.md를 읽었는가?
[ ] docs/ops-quality-checklist.md를 읽었는가?
```

## 9. n8n이 필요한 팀을 위한 준비

n8n을 사용하는 팀은 Docker Desktop을 실행한 뒤 n8n을 시작합니다.

```powershell
docker run -d `
  --name n8n-ai-workflow `
  -p 5678:5678 `
  -v n8n-data:/home/node/.n8n `
  n8nio/n8n:latest
```

접속 주소:

```text
http://localhost:5678
```

중지:

```powershell
docker stop n8n-ai-workflow
```

다시 시작:

```powershell
docker start n8n-ai-workflow
```

n8n 팀은 최소한 다음 흐름을 설계합니다.

```text
Webhook Trigger
-> IF
-> HTTP Request
-> Respond to Webhook
-> Execution Log 확인
```

## 10. Dify가 필요한 팀을 위한 준비

Dify를 사용하는 팀은 Dify Cloud 또는 강사가 제공한 Dify 환경을 먼저 사용합니다.

확인할 항목:

```text
[ ] 새 앱 생성
[ ] 모델 선택
[ ] System Prompt 작성
[ ] Knowledge 생성
[ ] 문서 업로드
[ ] Knowledge 연결 후 테스트
[ ] API Access 또는 API Key 확인
```

Dify self-host는 Docker Compose가 필요하므로 선택 실습으로 진행합니다. Docker Compose와 배포 운영은 `06_multi-agent-service-ops`에서 더 자세히 다룹니다.

## 11. AIPP가 필요한 팀을 위한 준비

AIPP를 사용하는 팀은 실제 구현보다 워크플로우 설계와 노드 구조를 명확히 정리하는 것이 중요합니다.

확인할 항목:

```text
[ ] 새 프로젝트 또는 워크플로우 생성
[ ] 입력값 정의
[ ] LLM 또는 Agent 노드 정의
[ ] Tool 또는 Knowledge 연결 여부 정의
[ ] 조건 분기 정의
[ ] 출력 결과 정의
[ ] 실행 로그 또는 검토 단계 정의
```

## 12. 팀 프로젝트 시작

팀 프로젝트는 템플릿을 복사해서 시작합니다.

```powershell
cd C:\aidev\09_ai-workflow-mini-project
Copy-Item .\99_team-projects\ai-workflow-team-template .\99_team-projects\team-01-tech-support-workflow -Recurse
```

팀명에 맞게 `team-01-tech-support-workflow` 부분을 바꿔도 됩니다.

복사한 뒤 먼저 작성할 문서:

```text
docs/project-plan.md
docs/workflow-design.md
docs/ops-quality-plan.md
docs/test-checklist.md
presentation/final-presentation.md
```

## 13. 팀 프로젝트 진행 순서

```text
1. 업무 시나리오 선택
2. 사용자와 문제 정의
3. Trigger, Condition, Action 설계
4. AIPP, n8n, Dify 중 사용할 도구 선택
5. 샘플 backend/frontend 실행
6. 팀 프로젝트에 필요한 코드 또는 문서 수정
7. 테스트 체크리스트 작성
8. 오류 처리와 fallback 정리
9. 최종 발표 자료 작성
10. 시연 리허설
```

## 14. 자주 만나는 오류

### `ModuleNotFoundError`

```powershell
cd C:\aidev\09_ai-workflow-mini-project
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### backend 접속이 안 됨

확인할 것:

```text
uvicorn이 실행 중인가?
포트 8900을 다른 프로그램이 사용 중이지 않은가?
브라우저 주소가 http://127.0.0.1:8900/health 인가?
```

### frontend 접속이 안 됨

확인할 것:

```text
streamlit이 실행 중인가?
포트 8901을 다른 프로그램이 사용 중이지 않은가?
API_BASE_URL이 backend 주소와 맞는가?
```

### n8n 접속이 안 됨

```powershell
docker ps
docker logs n8n-ai-workflow
```

### Dify 응답이 기대와 다름

확인할 것:

```text
System Prompt가 명확한가?
Knowledge가 앱에 연결되어 있는가?
문서 인덱싱이 완료되었는가?
테스트 질문이 문서 내용과 관련 있는가?
```

## 15. 최종 제출 전 확인

```text
[ ] README에 실행 방법이 적혀 있다.
[ ] .env.example은 있고 실제 .env는 제외했다.
[ ] 프로젝트 주제와 사용자 문제가 명확하다.
[ ] Trigger, Condition, Action 흐름이 있다.
[ ] AIPP, n8n, Dify 중 최소 1개 이상의 활용 방식이 있다.
[ ] FastAPI/Streamlit 시연 또는 설계 문서가 있다.
[ ] 오류 처리와 fallback이 있다.
[ ] 테스트 체크리스트가 작성되어 있다.
[ ] 발표 자료에 시연 순서가 있다.
```
