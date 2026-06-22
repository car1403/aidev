# 03_supabase-ai-mini-project

이 과정은 `01_supabase-ai-backend`와 `02_supabase-ai-frontend`에서 배운 내용을 연결해, Supabase 기반 AI 미니 프로젝트를 완성하는 수업입니다.

이 과정은 Supabase 프로젝트, FastAPI, Streamlit을 연결해 작은 AI 서비스를 완성하는 데 집중합니다. Docker, Docker Compose, AWS 기반 운영 배포, GitHub Actions 자동화는 이 과정에서 진행하지 않고 `06_multi-agent-service-ops`에서 다룹니다.

이 과정은 `01_supabase-ai-backend`에서 보강한 FastAPI, LLM API, Supabase, Upstash Redis 기초와 `02_supabase-ai-frontend`에서 보강한 Streamlit UI, API 호출, 로그인 상태, 서비스 로그 조회, 무료 배포 흐름을 하나의 미니 프로젝트로 연결합니다.

01~03 과정의 AI API 실습은 Gemini API를 기본으로 진행합니다. OpenAI API 관련 기존 예제는 삭제하지 않고, 팀의 수준이나 강의 방향에 따라 선택/비교 실습으로 사용할 수 있습니다.

03 과정에서는 팀 프로젝트 결과물을 선택적으로 무료 배포 서비스에 올려 시연할 수 있습니다. **배포는 필수가 아니며, 로컬에서 FastAPI, Streamlit, Supabase가 정상 연동되는 것이 기본 제출 기준입니다.** 배포 흐름은 다음과 같이 정리합니다.

```text
FastAPI 백엔드 -> Render
Redis 캐시/세션/로그 보조 저장소 -> Upstash
Streamlit 프론트엔드 -> Streamlit Community Cloud
Supabase Database/Auth -> Supabase Cloud
```

이 배포는 “운영 자동화”가 아니라 “직접 만든 미니 프로젝트를 외부 URL로 시연해 보는 선택 실습”입니다.

## SSE 스트리밍 통합 실습 안내

Server-Sent Events(SSE) 기반 실시간 AI 응답 스트리밍은 이 과정에서 통합 실습으로 다룹니다.

01 과정에서 배운 FastAPI API 구조와 02 과정에서 배운 Streamlit UI/API 호출 흐름을 연결해, 다음 구조를 구현합니다.

```text
사용자 질문 입력
-> FastAPI SSE 스트리밍 엔드포인트 호출
-> AI 응답 chunk를 Streamlit 화면에 실시간 누적 표시
-> 스트리밍 완료 후 최종 assistant 응답을 Supabase messages 테이블에 저장
```

초보자에게는 SSE와 Supabase의 역할을 분리해서 설명합니다.

```text
SSE: AI 응답을 실시간으로 화면에 보내는 통신 방식
Supabase: 사용자, 대화방, 최종 메시지, 사용 로그를 저장하는 데이터 저장소
```

## 과정 목표

- Supabase 프로젝트를 만들고 URL/key/env 구조를 이해한다.
- Gemini API를 기본 AI 응답 생성 API로 사용하고, OpenAI API는 선택 확장으로 구분한다.
- Supabase PostgreSQL에 테이블을 설계하고 CRUD를 수행한다.
- FastAPI에서 Supabase를 호출하는 API 서버 구조를 만든다.
- Streamlit에서 FastAPI API를 호출하는 화면을 만든다.
- SSE 기반 실시간 AI 응답 스트리밍 구조를 이해하고 구현한다.
- 스트리밍 완료 후 최종 응답을 Supabase에 저장하는 흐름을 설계한다.
- 사용자별 로그, AI 응답, 피드백 데이터를 설계한다.
- API 설계 문서, 화면 설계서, 데이터베이스 설계서, 대시보드 구현 결과물을 프로젝트 산출물로 작성한다.
- 로컬 실행 환경에서 대시보드가 동작하는지 검증한다.
- 시간이 충분한 팀은 무료 배포 환경에서도 선택적으로 시연한다.
- 팀별 미니 프로젝트를 기획, 구현, 테스트, 발표할 수 있다.

## 이번 프로젝트에서 만드는 것

최종 목표는 Supabase, FastAPI, Streamlit을 연결한 **실시간 로그 대시보드 인터페이스**를 완성하는 것입니다.

이번 프로젝트의 기준 주제는 다음과 같습니다.

```text
분야:
웹 서비스 기초 및 AI 백엔드 개발

프로젝트:
실시간 로그 대시보드 인터페이스

진행 방향:
1. 백엔드, DB, UI 통합 아키텍처 구현 및 실행 실습
2. 실시간 데이터 스트리밍을 통한 로그 시각화 대시보드 최종 제작
3. 사용자 피드백 데이터를 반영한 AI 답변 품질 고도화 및 서비스 최적화
```

예시 기능:

- 사용자 요청/질문 로그 저장
- Gemini 기반 AI 응답 결과 저장
- 오류 로그 저장
- 사용자 피드백 저장
- 로그 목록과 상세 조회
- 처리 시간, 응답 상태, 피드백 점수 대시보드 표시
- 선택 확장: SSE 기반 실시간 응답 또는 로그 상태 스트리밍
- 선택 확장: OpenAI API 예제를 활용한 모델별 응답 비교
- 선택 확장: Render, Upstash, Streamlit Community Cloud를 활용한 무료 배포 시연

처음부터 큰 서비스를 만들려고 하기보다, 아래 4가지를 확실히 연결하는 것을 목표로 합니다.

```text
Streamlit 화면
-> FastAPI API
-> Supabase 테이블
-> 로그/AI 응답/피드백 데이터 시각화
```

배포까지 진행하는 팀은 아래 구조까지 연결합니다.

```text
사용자 브라우저
-> Streamlit Community Cloud 프론트엔드
-> Render FastAPI 백엔드
-> Supabase Database/Auth
-> Upstash Redis 선택 사용
```

## 필수 산출물

팀 프로젝트는 아래 4가지 산출물을 기준으로 평가합니다. 단순히 문서 파일을 만드는 것이 아니라, 실제 구현 결과와 서로 맞아야 합니다.

| 산출물 | 핵심 확인 기준 |
| --- | --- |
| API 설계 문서 | 엔드포인트 URL이 리소스 중심으로 일관되게 명명되었는가, HTTP Method가 의미에 맞게 사용되었는가, 표준 에러 응답과 Pydantic 모델이 명확한가 |
| 화면 설계서 | 메인/상세/입력/설정/오류 화면의 와이어프레임이 작성되었는가, 정보 계층 구조와 사용자 액션별 시스템 반응이 정의되었는가 |
| 데이터베이스 설계서 | 3정규화 기준, 논리/물리 ERD, PK/FK, 인덱스, 컬럼 타입/길이/제약조건/기본값/코멘트가 정리되었는가 |
| 대시보드 구현 결과물 | 구현된 대시보드가 로컬 환경에서 동작하며, 로그 수집/조회/시각화와 피드백 반영이 시연 가능한가. 무료 배포 URL은 선택 제출인가 |

### API 설계 문서 세부 기준

- 엔드포인트 URL이 리소스 중심으로 일관되게 명명되었는가?
- HTTP Method `GET`, `POST`, `PUT`, `DELETE`가 의미에 맞게 사용되었는가?
- 표준화된 에러 응답 형식이 정의되었는가?
- HTTP Status Code, 에러 코드, 메시지, 상세 정보가 분리되어 있는가?
- 4xx/5xx 예외 상황별 처리 규칙이 문서화되었는가?
- Request/Response용 Pydantic 모델에 필수/선택 필드, 타입 힌트, 예시값이 명확한가?
- 중첩 JSON은 문자열이 아니라 nested Pydantic 모델 또는 명확한 JSON 구조로 표현되었는가?

### 화면 설계서 세부 기준

- 모든 화면, 즉 메인, 상세, 입력, 설정, 오류 화면의 와이어프레임이 누락 없이 작성되었는가?
- 정보 계층 구조(IA)가 논리적인가?
- 버튼, 입력폼, 테이블, 차트의 스타일, 색상, 폰트, 여백이 전체 화면에서 일관된 디자인 시스템을 따르는가?
- 클릭, 호버, 드래그, 스크롤, 필터 적용, 새로고침 같은 사용자 액션에 대한 시스템 반응이 정의되었는가?
- 화면별 API 호출, 로딩 상태, 오류 메시지, 피드백 표시 방식이 정리되었는가?

### 데이터베이스 설계서 세부 기준

- 테이블이 3정규화(3NF) 기준으로 설계되어 데이터 중복이 최소화되었는가?
- 삽입, 갱신, 삭제 이상현상이 방지되도록 테이블이 나뉘어 있는가?
- 논리 ERD에 엔티티, 속성, 관계, 카디널리티가 포함되었는가?
- 물리 ERD에 테이블명, 컬럼, PK/FK, 인덱스가 포함되었는가?
- 모든 컬럼의 데이터 타입, 길이, 제약조건, 기본값, 코멘트가 명확히 정의되었는가?
- Supabase RLS 적용 여부와 사용자별 접근 제어 방식이 설명되었는가?

### 대시보드 구현 결과물 세부 기준

- 구현된 대시보드가 실행 환경에서 동작하는가?
- 핵심 기능인 로그 수집, 조회, 시각화가 시연 가능한가?
- 사용자 피드백 데이터가 저장되거나 대시보드 지표에 반영되는가?
- AI 답변 품질 개선 방향이 문서화되어 있는가?
- SSE 기반 스트리밍 또는 자동 새로고침 기반 실시간 표시 방식이 설명되어 있는가?
- 로컬 실행 URL이 문서에 정리되어 있는가?
- 무료 배포를 진행한 경우 배포 URL이 추가로 정리되어 있는가?

## 과정 구조

```text
03_supabase-ai-mini-project
├─.venv
├─.gitignore
├─ README.md
├─ SETUP.md
├─.env.example
├─ requirements.txt
├─ 00_references
│ └─ supabase
├─ 01_local-dev-basic
├─ 02_instructor-sample-project
├─ 03_team-project-guide
├─ 04_supabase-project-practice
├─ 05_supabase-sample-assets
└─ 99_team-projects
 ├─ team-template
 └─ supabase-team-template
```

팀 프로젝트를 실제 배포 대상으로 정리할 때는 템플릿 내부 구조를 다음 기준으로 맞춥니다.

```text
team-project
├─ README.md
├─.env.example
├─ backend
│ ├─ main.py
│ └─ requirements.txt
├─ frontend
│ ├─ app.py
│ └─ requirements.txt
├─ docs
│ ├─ project-plan.md
│ ├─ api-spec.md
│ ├─ ui-design.md
│ ├─ supabase-schema.md
│ ├─ streaming-response-design.md
│ ├─ dashboard-result.md
│ ├─ deployment-guide.md
│ └─ test-checklist.md
└─ presentation
 └─ final-presentation.md
```

배포할 때는 `backend`와 `frontend`가 각각 독립적으로 배포될 수 있어야 합니다. 그래서 `backend/requirements.txt`와 `frontend/requirements.txt`를 나누어 둡니다.

## 폴더를 읽는 방법

각 폴더의 역할은 다음과 같습니다.

```text
00_references Supabase, env, RLS, 보안 개념 참고 자료
01_local-dev-basic Supabase env, 로컬 FastAPI/Streamlit 실행 감각을 익히는 예비 실습
02_instructor-sample-project 수업용 Supabase 샘플 프로젝트
03_team-project-guide 팀 프로젝트 운영 가이드
04_supabase-project-practice Supabase 프로젝트와 테이블 준비 실습
05_supabase-sample-assets Supabase 연동 샘플 자료
99_team-projects 팀별 최종 결과물을 만드는 공간
```

초보자는 `00_references`를 전부 외우려고 하지 않아도 됩니다. 먼저 `01_local-dev-basic`에서 Supabase 환경변수, FastAPI 실행, Streamlit 실행 감각을 익히고, 프로젝트를 진행하면서 필요한 참고 자료로 다시 돌아오면 됩니다.

## 현재 구성 기준

- Supabase 프로젝트를 데이터 저장소로 사용합니다.
- FastAPI는 Supabase와 통신하는 백엔드 API 역할을 합니다.
- Streamlit은 FastAPI API를 호출하는 화면 역할을 합니다.
- 팀 프로젝트는 `99_team-projects/supabase-team-template`을 기준으로 시작합니다.
- 무료 배포 시연은 선택 확장으로 다룹니다.
- Docker, Docker Compose, AWS, GitHub Actions 기반 운영 자동화는 06 과정에서 학습합니다.

## 권장 학습 흐름

```text
00_references 읽기
-> 01_local-dev-basic에서 Supabase env와 로컬 FastAPI/Streamlit 실행 감각 확인
-> 04_supabase-project-practice에서 Supabase 프로젝트/테이블/env 준비
-> 05_supabase-sample-assets/sample-learning-log-dashboard 참고
-> 03_team-project-guide로 팀 주제/역할/일정 확정
-> 99_team-projects/supabase-team-template 기반 팀 프로젝트 진행
```

초보자에게는 아래처럼 더 작게 나누어 진행하는 것을 권장합니다.

1. `SETUP.md`를 보고 `.venv`와 `.env`를 준비합니다.
2. `01_local-dev-basic`에서 Supabase 환경변수를 확인하고 FastAPI와 Streamlit을 각각 실행해 봅니다.
3. Supabase 프로젝트를 만들고 URL/key 값을 `.env`에 넣습니다.
4. Gemini API key를 준비하고 `.env`에 `GEMINI_API_KEY`를 넣습니다.
5. Supabase에서 프로젝트에 필요한 테이블을 1개만 먼저 만듭니다.
6. FastAPI에서 Supabase 테이블 데이터를 조회하는 API를 만듭니다.
7. Streamlit에서 FastAPI API를 호출해 화면에 표시합니다.
8. 데이터 추가, 수정, 삭제 기능을 하나씩 붙입니다.
9. Gemini 기반 일반 AI 응답 API를 만든 뒤 SSE 기반 스트리밍 응답 API로 확장합니다.
10. 스트리밍 완료 후 최종 응답과 실행 로그를 Supabase에 저장합니다.
11. AI 응답, 사용자별 로그, 피드백, 대시보드 기능을 선택적으로 확장합니다.
12. 배포를 진행하는 팀은 Render, Upstash, Streamlit Community Cloud 환경변수를 준비합니다.
13. `docs` 폴더의 문서를 채우고 발표 자료를 준비합니다.

## 실행 방식

```text
Supabase: 클라우드 프로젝트 사용
FastAPI: 로컬.venv에서 uvicorn 실행
Streamlit: 로컬.venv에서 streamlit run 실행
.env: Supabase URL/key, GEMINI_API_KEY, API_BASE_URL 관리
Docker: 사용하지 않음. 06_multi-agent-service-ops에서 학습
```

## 선택 배포 실습

03 과정의 기본 목표는 로컬 실행과 Supabase 연동입니다. **배포는 필수가 아닙니다.** 시간이 충분하거나 팀 프로젝트를 외부 URL로 시연하고 싶다면 무료 배포 실습을 선택적으로 진행합니다.

```text
1. Supabase Cloud에 테이블과 RLS 정책 준비
2. GitHub 저장소에 팀 프로젝트 코드 업로드
3. Render에 FastAPI 백엔드 배포
4. Upstash Redis 생성 후 필요한 경우 Render 환경변수에 등록
5. Streamlit Community Cloud에 프론트엔드 배포
6. Streamlit Secrets에 배포된 Render API URL 등록
7. 배포 URL에서 로그 저장, 조회, 대시보드, SSE 또는 새로고침 기능 시연
```

자세한 절차는 다음 문서를 참고합니다.

```text
00_references/08_free-deployment-guide.md
99_team-projects/supabase-team-template/docs/deployment-guide.md
```

직접 기억해야 할 핵심은 다음입니다.

- `.env` 파일은 GitHub에 올리지 않습니다.
- Supabase service role key가 필요하다면 Render 백엔드 환경변수에만 등록합니다.
- Streamlit Community Cloud에는 `API_BASE_URL`처럼 프론트엔드가 알아야 하는 값만 등록합니다.
- `API_BASE_URL`은 로컬에서는 `http://127.0.0.1:8000`, 배포 후에는 Render URL로 바꿉니다.
- Upstash Redis는 선택입니다. 세션, 캐시, 임시 로그, rate limit 같은 기능을 넣을 때 사용합니다.

## 공통 실행 준비

자세한 환경 준비는 [SETUP.md](./SETUP.md)를 참고합니다.

PowerShell 기준 기본 흐름은 다음과 같습니다.

```powershell
cd C:\aidev\03_supabase-ai-mini-project
C:\Users\jeanm\AppData\Local\Programs\Python\Python312\python.exe -m venv.venv
.\.venv\Scripts\Activate.ps1
python --version
pip install -r requirements.txt
Copy-Item.env.example.env
```

이미 `.venv`가 만들어져 있다면 다시 만들 필요는 없습니다. 그때는 아래처럼 활성화부터 시작하면 됩니다.

```powershell
cd C:\aidev\03_supabase-ai-mini-project
.\.venv\Scripts\Activate.ps1
```

이 과정에서는 각 하위 실습 폴더마다 `.venv`를 따로 만들지 않고, `03_supabase-ai-mini-project` 최상위의 `.venv` 하나를 사용합니다.

## 팀 프로젝트 시작 방법

팀 프로젝트는 `99_team-projects\supabase-team-template`을 기준으로 시작합니다. `team-template`도 같은 Supabase 구조를 담은 호환용 템플릿입니다. 팀별로 작업 폴더를 만들 때는 `supabase-team-template`을 복사해서 사용합니다.

```powershell
cd C:\aidev\03_supabase-ai-mini-project
Copy-Item.\99_team-projects\supabase-team-template.\99_team-projects\team-01-learning-chatbot -Recurse
```

팀 이름에 맞게 `team-01-learning-chatbot` 부분만 바꾸면 됩니다.

복사한 뒤에는 아래 문서를 먼저 채웁니다.

```text
docs/project-plan.md 프로젝트 주제, 사용자, 주요 기능
docs/supabase-schema.md Supabase 테이블 설계
docs/api-spec.md FastAPI 엔드포인트 설계
docs/ui-design.md 화면 설계와 사용자 액션 흐름
docs/dashboard-result.md 구현된 대시보드 결과 정리
docs/streaming-response-design.md SSE 스트리밍 응답 설계
docs/test-checklist.md 테스트 체크리스트
presentation/final-presentation.md 발표 자료 초안
```

코드를 먼저 많이 작성하기보다, 테이블과 API를 작은 단위로 정하고 하나씩 실행 확인하는 방식이 좋습니다.

## 백엔드와 프론트엔드 실행 방법

백엔드와 프론트엔드는 PowerShell을 두 개 열어 실행하는 것이 좋습니다.

첫 번째 PowerShell에서는 FastAPI 백엔드를 실행합니다.

```powershell
cd C:\aidev\03_supabase-ai-mini-project\99_team-projects\supabase-team-template\backend
..\..\..\.venv\Scripts\Activate.ps1
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

브라우저에서 아래 주소를 열어 API 문서를 확인합니다.

```text
http://127.0.0.1:8000/docs
```

두 번째 PowerShell에서는 Streamlit 프론트엔드를 실행합니다.

```powershell
cd C:\aidev\03_supabase-ai-mini-project\99_team-projects\supabase-team-template\frontend
..\..\..\.venv\Scripts\Activate.ps1
streamlit run app.py --server.port 8501
```

브라우저에서 아래 주소를 열어 화면을 확인합니다.

```text
http://127.0.0.1:8501
```

서버를 멈출 때는 각 PowerShell에서 `Ctrl + C`를 누릅니다.

## 보안 원칙

- 실제 Supabase key를 코드에 직접 쓰지 않습니다.
- `.env` 파일은 제출하거나 GitHub에 올리지 않습니다.
- `.env.example`만 공유합니다.
- service role key는 FastAPI 같은 서버에서만 사용합니다.
- Streamlit 화면에는 service role key를 넣지 않습니다.
- RLS 정책을 이해하지 않고 실제 서비스를 공개하지 않습니다.

초보자가 특히 헷갈리기 쉬운 기준은 다음과 같습니다.

- `anon key`는 프론트엔드에서 사용할 수 있지만, RLS 정책과 함께 사용해야 안전합니다.
- `service role key`는 강한 권한을 가진 키라서 서버 코드나 로컬 `.env`에서만 사용합니다.
- GitHub에 `.env`를 올리면 키가 노출될 수 있으므로 `.gitignore`에 포함되어야 합니다.
- RLS를 켰다면 테이블에 데이터가 있어도 정책이 없으면 조회가 안 될 수 있습니다.

## 자주 만나는 오류

Supabase 연결 오류가 나오면 `.env` 값이 정확한지 먼저 확인합니다.

```env
SUPABASE_URL=...
SUPABASE_ANON_KEY=...
SUPABASE_SERVICE_ROLE_KEY=...
GEMINI_API_KEY=...
API_BASE_URL=http://127.0.0.1:8000
```

`ModuleNotFoundError`가 나오면 가상환경을 활성화하고 패키지를 다시 설치합니다.

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

FastAPI API가 열리지 않으면 백엔드 서버가 실행 중인지 확인합니다.

```text
http://127.0.0.1:8000/docs
```

Streamlit에서 API 연결 오류가 나오면 `API_BASE_URL`이 실제 FastAPI 주소와 같은지 확인합니다.

포트가 이미 사용 중이면 다른 포트를 사용합니다.

```powershell
uvicorn main:app --reload --port 8001
streamlit run app.py --server.port 8502
```

## 최종 목표

이 과정을 마친 뒤 다음을 설명하고 구현할 수 있어야 합니다.

```text
Supabase 프로젝트와 Python 앱은 어떻게 연결되는가?
FastAPI를 거쳐 Supabase를 호출하는 방식과 Streamlit이 직접 Supabase를 호출하는 방식은 무엇이 다른가?
사용자별 로그, AI 응답, 피드백 데이터는 어떻게 안전하게 저장하고 조회하는가?
팀 프로젝트를 어떻게 문서화하고 발표할 것인가?
```

## 03 과정에서 하지 않는 것

다음 내용은 이 과정의 필수 범위가 아닙니다.

- Docker로 PostgreSQL 컨테이너 실행
- Redis 컨테이너 실행
- Docker Compose로 전체 서비스를 묶기
- AWS 기반 운영 배포
- GitHub Actions 기반 CI/CD

위 내용은 `06_multi-agent-service-ops`에서 운영 관점으로 학습합니다. 단, Render, Upstash, Streamlit Community Cloud를 활용한 무료 배포 시연은 03 팀 프로젝트의 선택 확장으로 진행할 수 있습니다.

## 커리큘럼 점검

이미지 기준 항목이 프로젝트로 연결되는 방식은 아래와 같습니다.

| 이미지 기준 | 03 과정 반영 위치 | 상태 |
| --- | --- | --- |
| 백엔드, DB, UI 통합 아키텍처 구현 및 실행 실습 | `01_local-dev-basic`, `02_instructor-sample-project`, `99_team-projects/supabase-team-template` | 포함 |
| 실시간 데이터 스트리밍을 통한 로그 시각화 대시보드 최종 제작 | `04_supabase-project-practice/05_sse-streaming-ai-response`, `99_team-projects/*/streaming_response_design.md` | 포함 |
| 사용자 피드백 데이터를 반영한 AI 답변 품질 고도화 및 서비스 최적화 | `docs/dashboard-result.md`, `docs/test-checklist.md`, `feedback` 테이블 설계 | 포함 |
| API 설계 문서 | `docs/api-spec.md` | 포함/보강 |
| 화면 설계서 | `docs/ui-design.md` | 포함/보강 |
| 데이터베이스 설계서 | `docs/supabase-schema.md` | 포함/보강 |
| 대시보드 구현 결과물 | `docs/dashboard-result.md`, `frontend/app.py`, 선택 배포 URL | 포함/보강 |
| 선택 배포 실습 | `00_references/08_free-deployment-guide.md`, `docs/deployment-guide.md` | 선택 확장. 필수 제출 아님 |

수업 운영 시 처음부터 완성도 높은 대시보드를 요구하기보다, 아래 순서로 작게 성공하도록 안내합니다.

```text
1. 로그 1개를 Supabase에 저장한다.
2. 저장된 로그를 FastAPI로 조회한다.
3. Streamlit 화면에 로그 목록을 표시한다.
4. 로그 수, 오류 수, 평균 처리 시간 같은 지표를 추가한다.
5. 사용자 피드백을 저장한다.
6. AI 응답 품질 개선 방향을 문서화한다.
7. SSE 또는 자동 새로고침으로 실시간성을 추가한다.
8. 로컬 실행 환경에서 최종 대시보드를 시연한다.
9. 시간이 충분한 팀은 무료 배포 환경에서 추가 시연한다.
```



