# 04. Folder Map

이번 과정의 기본 폴더 구조입니다.

```text
C:\aidev
├─ 00_admin
├─ 01_supabase-ai-backend
├─ 02_supabase-ai-frontend
├─ 03_supabase-ai-mini-project
├─ 04_llm-agent-orchestration
├─ 05_llm-agent-mini-project
├─ 06_multi-agent-service-ops
└─ 07_multi-agent-service-mini-project
```

## 폴더별 역할

| 폴더 | 역할 |
| --- | --- |
| `00_admin` | 과정 안내, 설치, 체크리스트, 평가, 템플릿 |
| `01_supabase-ai-backend` | Python/FastAPI/Supabase 백엔드 |
| `02_supabase-ai-frontend` | Streamlit 프론트엔드 |
| `03_supabase-ai-mini-project` | Supabase 기반 통합 미니 프로젝트 |
| `04_llm-agent-orchestration` | LLM Agent, RAG, Tool, Memory |
| `05_llm-agent-mini-project` | 단일 Agent 미니 프로젝트 |
| `06_multi-agent-service-ops` | Multi-Agent 운영, Docker Compose, AWS, GitHub Actions |
| `07_multi-agent-service-mini-project` | Multi-Agent Auto Healing 미니 프로젝트 |

## GitHub에 올리지 않는 것

```text
.env
.venv
__pycache__
실제 API Key
AWS Access Key
개인정보가 포함된 데이터
```
