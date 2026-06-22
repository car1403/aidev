# Sample Tech Support Workflow

수업용 샘플 기술 지원 자동화 워크플로우입니다.

외부 AI API 없이 규칙 기반으로 동작하지만, 구조는 실제 AI Workflow 프로젝트처럼 구성했습니다.

## 구조

```text
sample-tech-support-workflow
├─ README.md
├─.env.example
├─ requirements.txt
├─ backend
│ ├─ main.py
│ ├─ workflow.py
│ └─ schemas.py
├─ frontend
│ └─ app.py
└─ docs
 ├─ aipp-workflow-plan.md
 ├─ n8n-workflow-plan.md
 ├─ dify-workflow-plan.md
 ├─ ops-quality-checklist.md
 └─ demo-script.md
```

## 실행

```powershell
cd C:\aidev\08_ai-workflow-automation\99_mini-project\sample-tech-support-workflow
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item.env.example.env
```

Backend:

```powershell
uvicorn backend.main:app --reload --host 127.0.0.1 --port 8900
```

Frontend:

```powershell
streamlit run frontend/app.py --server.port 8901
```

## API

```text
GET /health
POST /analyze
GET /events
GET /metrics
```

## 샘플 문의

```text
프리미엄 고객입니다. AI 서비스 응답이 너무 느리고 장애가 의심됩니다. 빠르게 확인해 주세요.
```
