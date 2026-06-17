# 04. Folder Map

이 문서는 `C:\aidev` 폴더 구조를 설명합니다.

## 최상위 구조

```text
C:\aidev
├─ 00_admin
├─ 01_supabase-ai-backend
├─ 02_supabase-ai-frontend
├─ 03_supabase-ai-mini-project
├─ 04_llm-agent-orchestration
├─ 05_llm-agent-mini-project
├─ 06_multi-agent-service-ops
├─ 07_multi-agent-service-mini-project
├─ 08_ai-workflow-automation
└─ 09_ai-workflow-mini-project
```

## 과정 폴더 공통 구조

대부분의 과정 폴더는 아래와 비슷한 구조를 가집니다.

```text
README.md
SETUP.md
requirements.txt
.env.example
.venv
00_references
01_...
02_...
10_labs
20_assignments
99_mini-project 또는 99_team-projects
```

## 파일 의미

| 파일/폴더 | 의미 |
| --- | --- |
| `README.md` | 가장 먼저 읽는 설명서 |
| `SETUP.md` | 환경 설정 안내 |
| `requirements.txt` | 설치할 Python 패키지 목록 |
| `.env.example` | 환경변수 예시 파일 |
| `.env` | 실제 키를 넣는 개인 파일, 제출하지 않음 |
| `.venv` | Python 가상환경, 제출하지 않음 |
| `00_references` | 개념 참고 자료 |
| `10_labs` | 수업 중 실습 |
| `20_assignments` | 혼자 풀 과제 |
| `99_*` | 미니 프로젝트 또는 팀 프로젝트 |

## 주의할 폴더

아래 폴더는 GitHub에 올리지 않거나 제출하지 않습니다.

```text
.venv
.env
__pycache__
```
