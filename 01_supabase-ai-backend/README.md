# 01_supabase-ai-backend

Python, FastAPI, Supabase, Gemini API를 중심으로 AI 백엔드 개발을 학습하는 과정 폴더입니다.

이 과정은 이미지 기준의 **웹 서비스 기초 및 AI 백엔드 개발** 중에서 백엔드에 해당하는 내용을 담당합니다. 화면 UI, SSE 스트리밍 통합, 최종 배포는 `02_supabase-ai-frontend`, `03_supabase-ai-mini-project`, `06_multi-agent-service-ops`와 역할을 나누어 진행합니다.

## 과정 목표

- AI 리터러시와 Vibe Coding의 기본 태도를 이해합니다.
- Python 개발환경, `.venv`, `pip`, `requirements.txt`를 사용할 수 있습니다.
- Python 기본 문법과 고급 문법을 단계적으로 학습합니다.
- Git/GitHub로 코드 변경 이력을 관리하고, Codex로 문서와 커밋 메시지를 개선할 수 있습니다.
- FastAPI로 REST API 서버를 만들고 Swagger UI에서 검증할 수 있습니다.
- Pydantic으로 요청/응답 데이터를 검증할 수 있습니다.
- Gemini API를 기본 LLM 실습 모델로 사용하고, API key, 토큰, 무료 범위/과금, 싱글턴/멀티턴 호출 차이를 이해합니다.
- OpenAI API 예제는 삭제하지 않고 선택/비교 실습용으로 유지합니다.
- Supabase 프로젝트, 테이블, Auth, RLS, service role key의 역할을 이해합니다.
- 사용자 정보, 대화 이력, 서비스 로그를 Supabase에 저장하는 백엔드 흐름을 설계합니다.
- Upstash Redis를 사용해 캐시, TTL, 임시 세션 상태, 요청 횟수 제한의 기본 흐름을 이해합니다.

## 처음 시작하는 순서

처음에는 아래 순서대로 진행하면 됩니다.

1. `SETUP.md`를 보고 `01_supabase-ai-backend` 폴더에 `.venv`를 만듭니다.
2. PowerShell에서 `.venv`를 활성화합니다.
3. `pip install -r requirements.txt`로 공통 패키지를 설치합니다.
4. `00_references`를 읽고 수업 전체 방향과 API key 보안 기준을 확인합니다.
5. `01_python-basic`부터 순서대로 예제 파일을 실행합니다.
6. 각 단원의 `10_labs`는 수업 중 실습으로, `20_assignments`는 개인 과제로 진행합니다.

이 과정에서는 각 단원마다 `.venv`를 따로 만들지 않고, `01_supabase-ai-backend` 최상위의 `.venv` 하나를 사용합니다.

## 과정 구조

```text
01_supabase-ai-backend
├─.venv
├─.gitignore
├─.env.example
├─ requirements.txt
├─ README.md
├─ SETUP.md
├─ 00_references
├─ 01_python-basic
├─ 02_python-advanced
├─ 03_git-github-and-vibe-coding
├─ 04_fastapi-backend
├─ 05_llm-api-integration
├─ 06_supabase-db-and-auth
├─ 07_backend-service-data-management
├─ 08_backend-mini-service-practice
├─ 90_ai-assisted-code-review-and-debugging
└─ 99_final-backend-project
```

## 폴더를 읽는 방법

각 단원은 보통 다음 흐름으로 구성됩니다.

```text
README.md 단원 설명과 학습 순서
00_references 개념 정리, 참고 자료, 보충 설명
01_... 첫 번째 개념 예제
02_... 두 번째 개념 예제
10_labs 수업 중 직접 따라 하는 실습
20_assignments 혼자 풀어 보는 과제
99_... 단원 마무리 미니 프로젝트
```

숫자가 낮은 폴더부터 순서대로 진행하면 됩니다.

## 단원 요약

| 단원 | 역할 |
| --- | --- |
| `00_references` | AI 리터러시, Vibe Coding, AI 도구 비교, 프롬프트 작성, 답변 검증, API key 보안 기준을 이해합니다. |
| `01_python-basic` | 변수, 자료형, 입출력, 조건문, 반복문, 함수, 파일/JSON 기초를 학습합니다. |
| `02_python-advanced` | 함수 심화, 모듈/패키지, 예외 처리, OOP, 테스트, 프로젝트 구조를 학습합니다. |
| `03_git-github-and-vibe-coding` | Git/GitHub, 커밋/브랜치, README/문서 작성, Codex 활용 흐름을 학습합니다. |
| `04_fastapi-backend` | FastAPI, REST API, HTTP Method, Pydantic, async, Swagger/Postman 테스트를 학습합니다. |
| `05_llm-api-integration` | Gemini API를 기본으로 LLM API, 토큰/과금, 파라미터, 싱글턴/멀티턴 호출, FastAPI 연동을 학습합니다. OpenAI 예제는 선택 비교용으로 유지합니다. |
| `06_supabase-db-and-auth` | RDBMS, ERD, SQL 기초, Supabase 프로젝트, 테이블, CRUD, Auth, RLS, Upstash Redis 캐시/TTL을 학습합니다. |
| `07_backend-service-data-management` | 사용자 정보, 대화 이력, 서비스 로그, 피드백 데이터를 백엔드 관점에서 설계합니다. |
| `08_backend-mini-service-practice` | FastAPI, Supabase, LLM API를 작은 백엔드 서비스로 묶어 봅니다. |
| `90_ai-assisted-code-review-and-debugging` | Codex를 활용한 코드 설명, 디버깅, 리팩토링, 코드 리뷰를 연습합니다. |
| `99_final-backend-project` | 01 과정의 최종 백엔드 프로젝트를 진행합니다. |

## 공통 실행 준비

자세한 환경 준비는 [SETUP.md](./SETUP.md)를 참고합니다.

PowerShell 기준 기본 흐름은 다음과 같습니다.

```powershell
cd C:\aidev\01_supabase-ai-backend
C:\Users\jeanm\AppData\Local\Programs\Python\Python312\python.exe -m venv.venv
.\.venv\Scripts\Activate.ps1
python --version
pip install -r requirements.txt
```

이미 `.venv`가 만들어져 있다면 다시 만들 필요는 없습니다.

```powershell
cd C:\aidev\01_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
```

활성화가 잘 되면 PowerShell 줄 앞에 `(.venv)`가 표시됩니다.

## 예제 실행 방법

Python 예제는 최상위 폴더에서 아래처럼 실행할 수 있습니다.

```powershell
cd C:\aidev\01_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
python.\01_python-basic\01_python-start\01_hello_python.py
python.\02_python-advanced\01_function-advanced\01_args_kwargs.py
```

FastAPI 예제는 보통 예제 파일이 있는 폴더로 이동한 뒤 실행합니다.

```powershell
cd C:\aidev\01_supabase-ai-backend\04_fastapi-backend\10_labs\lab01_hello-fastapi
uvicorn solution:app --reload
```

브라우저에서 `http://127.0.0.1:8000/docs`를 열면 Swagger 문서를 확인할 수 있습니다. 서버를 멈출 때는 PowerShell에서 `Ctrl + C`를 누릅니다.

## Supabase, Upstash Redis, Docker 학습 기준

이 과정은 Supabase를 기준으로 진행합니다. Supabase는 데이터베이스, 인증, API 기능을 관리형 서비스로 제공하므로 초반에는 서버 운영보다 백엔드 개발 흐름에 집중할 수 있습니다.

Redis는 로컬에 직접 설치하거나 Docker로 실행하지 않고, 관리형 Redis 서비스인 Upstash Redis를 사용합니다. 이렇게 하면 초보자는 Redis 서버 운영보다 캐시, TTL, 세션 보조, 요청 제한 같은 백엔드 기능의 의미를 먼저 이해할 수 있습니다.

```text
Supabase
-> 오래 보관할 데이터
-> 사용자 정보, 대화 이력, 서비스 로그, 피드백

Upstash Redis
-> 짧게 보관할 임시 데이터
-> 캐시, TTL, 중복 요청 방지, 요청 횟수 제한, 임시 세션 상태
```

이 과정에서 하는 것:

1. Python 기초와 고급 문법을 학습합니다.
2. FastAPI로 API 서버를 만듭니다.
3. Gemini API 호출 흐름과 비용/토큰 개념을 이해합니다.
4. Supabase 프로젝트를 만들고 테이블을 설계합니다.
5. FastAPI에서 Supabase에 데이터를 저장하고 조회합니다.
6. Supabase Auth와 RLS로 사용자별 접근 제어를 이해합니다.
7. 대화 이력과 서비스 로그를 Supabase 테이블에 저장합니다.
8. Upstash Redis로 TTL 기반 캐시와 간단한 요청 횟수 제한을 실습합니다.

이 과정에서 하지 않는 것:

```text
Streamlit/React 화면 설계
SSE 기반 실시간 화면 표시
Docker로 PostgreSQL 직접 실행
Docker로 Redis 직접 실행
Docker Compose 기반 서비스 운영
AWS 배포
운영 모니터링과 Auto Healing
```

위 내용은 각각 `02_supabase-ai-frontend`, `03_supabase-ai-mini-project`, `06_multi-agent-service-ops`에서 다룹니다.

## SSE 스트리밍 학습 위치 안내

Server-Sent Events(SSE) 기반 AI 응답 스트리밍은 `03_supabase-ai-mini-project`에서 백엔드, 프론트엔드, Supabase 저장 흐름을 함께 연결하는 통합 실습으로 다룹니다.

정리하면 아래와 같습니다.

- `01_supabase-ai-backend`: FastAPI 기본 구조, async, 요청/응답 모델, Supabase 저장 흐름 학습
- `02_supabase-ai-frontend`: Streamlit 화면 구성과 API 호출 학습
- `03_supabase-ai-mini-project`: SSE 기반 실시간 응답 표시와 Supabase 최종 메시지 저장 통합 실습

## 커리큘럼 반영 점검

| 이미지 기준 항목 | 반영 위치 | 상태 |
| --- | --- | --- |
| AI 리터러시, Python 개발환경, `.venv`, 변수/자료형/입출력 | `00_references`, `01_python-basic` | 포함 |
| 조건문, 반복문, 함수, 모듈/패키지 | `01_python-basic`, `02_python-advanced` | 포함 |
| OOP, 예외 처리, 코드 개선/리팩토링 | `02_python-advanced`, `90_ai-assisted-code-review-and-debugging` | 포함 |
| Git/GitHub, 커밋/브랜치, AI 활용 문서 작성 | `03_git-github-and-vibe-coding` | 추가 |
| FastAPI, HTTP Method, REST API endpoint | `04_fastapi-backend` | 포함 |
| Pydantic 요청/응답 검증 | `04_fastapi-backend` | 포함 |
| async/await, 외부 API 연동 | `04_fastapi-backend` | 포함 |
| Swagger/Postman 테스트 | `04_fastapi-backend` | 포함 |
| LLM API, Gemini API 기본, OpenAI API 선택 비교, 토큰/과금, 파라미터 | `05_llm-api-integration` | 추가 |
| 싱글턴/멀티턴 호출, FastAPI LLM 연동 | `05_llm-api-integration` | 추가 |
| RDBMS, ERD, SQL, Supabase 프로젝트 | `06_supabase-db-and-auth` | 포함/보강 |
| Supabase Auth, RLS, 사용자별 접근 제어 | `06_supabase-db-and-auth` | 포함 |
| 사용자 정보, 대화 이력, 서비스 로그 | `07_backend-service-data-management` | 추가 |
| Redis 세션/TTL | `06_supabase-db-and-auth/06_ch6_upstash-redis-cache-and-session` | Upstash Redis로 포함 |
| Docker 기반 Redis 운영 | `06_multi-agent-service-ops` | 01에서는 제외 |
| Streamlit/React UI | `02_supabase-ai-frontend` | 01에서는 제외 |
| 배포 실습 | `03_supabase-ai-mini-project`, `06_multi-agent-service-ops` | 01에서는 제외 |

## 자주 만나는 오류

`python` 명령을 찾을 수 없다고 나오면 Python 설치 경로를 확인합니다.

```powershell
py --version
python --version
```

`.venv` 활성화가 막히면 PowerShell 실행 정책 문제일 수 있습니다.

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

패키지 import 오류가 나오면 가상환경이 활성화되어 있는지 확인한 뒤 다시 설치합니다.

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

FastAPI 서버 실행 중 포트가 이미 사용 중이면 다른 서버가 켜져 있을 수 있습니다. 기존 서버를 `Ctrl + C`로 종료하거나 다른 포트를 사용합니다.

```powershell
uvicorn solution:app --reload --port 8001
```
