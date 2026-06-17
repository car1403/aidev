# SETUP

`03_supabase-ai-mini-project` 실행 환경 설정 안내입니다.

이 문서는 학생이 수업 시간에 그대로 따라 할 수 있도록 작성했습니다. 이 과정은 Supabase 프로젝트를 데이터 저장소로 사용하고, 로컬 PC에서는 FastAPI와 Streamlit을 Python 가상환경으로 실행합니다.

Docker, Docker Compose, AWS 배포는 여기서 설정하지 않습니다. 해당 내용은 `06_multi-agent-service-ops`에서 다룹니다.

처음 수업을 시작할 때는 `README.md`와 `00_references`를 먼저 읽고, 프로젝트 목표, 필수 산출물, SSE 학습 범위, Supabase key 보안 기준을 확인합니다.

## 1. 작업 위치로 이동

```powershell
cd C:\aidev\03_supabase-ai-mini-project
```

현재 위치를 확인합니다.

```powershell
Get-Location
```

## 2. 가상환경 만들기

```powershell
C:\Users\jeanm\AppData\Local\Programs\Python\Python312\python.exe -m venv .venv
```

이미 `.venv`가 있다면 다시 만들 필요가 없습니다.

## 3. 가상환경 활성화

```powershell
.\.venv\Scripts\Activate.ps1
```

정상적으로 활성화되었는지 확인합니다.

```powershell
python --version
pip --version
```

## 4. 패키지 설치

```powershell
pip install -r requirements.txt
```

## 5. 환경 변수 파일 만들기

```powershell
Copy-Item .env.example .env
```

`.env` 파일에 Supabase와 API 값을 입력합니다.

```env
SUPABASE_URL=https://your-project-ref.supabase.co
SUPABASE_ANON_KEY=your-supabase-anon-key
SUPABASE_SERVICE_ROLE_KEY=your-supabase-service-role-key
GEMINI_API_KEY=your-gemini-api-key
GEMINI_MODEL=gemini-2.5-flash-lite
OPENAI_API_KEY=your-openai-api-key
OPENAI_MODEL=gpt-4.1-mini
API_BASE_URL=http://127.0.0.1:8000
```

주의할 점은 다음과 같습니다.

- `.env` 파일은 GitHub에 올리지 않습니다.
- `SUPABASE_SERVICE_ROLE_KEY`는 FastAPI 같은 백엔드에서만 사용합니다.
- Streamlit 화면에는 service role key를 넣지 않습니다.
- 03 미니 프로젝트의 기본 AI API는 Gemini API로 진행합니다.
- Gemini 무료 범위와 호출 제한은 수업 시점의 공식 화면에서 확인합니다.
- OpenAI API key는 기존 OpenAI 예제를 활용한 선택/비교 실습 때만 사용합니다.
- 학생에게 제출받을 때도 `.env` 대신 `.env.example`만 확인합니다.

## 6. Supabase 준비

1. Supabase 프로젝트를 생성합니다.
2. Project URL, anon key, service role key를 확인합니다.
3. SQL Editor에서 프로젝트에 필요한 테이블을 생성합니다.
4. Auth를 사용할 경우 회원가입과 로그인 정책을 확인합니다.
5. RLS를 켠 경우 select, insert, update, delete 정책을 테스트합니다.

샘플 테이블 안내는 다음 문서를 참고합니다.

```text
05_supabase-sample-assets/sample-learning-log-dashboard/docs/setup-supabase.md
99_team-projects/supabase-team-template/docs/supabase-schema.md
```

## 7. 환경 변수 확인

```powershell
cd C:\aidev\03_supabase-ai-mini-project
.\.venv\Scripts\Activate.ps1
python .\01_local-dev-basic\01_supabase-env-check\01_check_env.py
```

## 8. FastAPI 실행 예시

```powershell
cd C:\aidev\03_supabase-ai-mini-project\99_team-projects\supabase-team-template\backend
..\..\..\.venv\Scripts\Activate.ps1
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

브라우저에서 API 문서를 확인합니다.

```text
http://127.0.0.1:8000/docs
```

## 9. Streamlit 실행 예시

새 PowerShell을 하나 더 열고 실행합니다.

```powershell
cd C:\aidev\03_supabase-ai-mini-project\99_team-projects\supabase-team-template\frontend
..\..\..\.venv\Scripts\Activate.ps1
streamlit run app.py --server.port 8501
```

브라우저에서 화면을 확인합니다.

```text
http://127.0.0.1:8501
```

## 10. 팀 프로젝트 권장 순서

```text
1. README.md와 00_references 읽기
2. 주제 선정
3. API 설계 문서 초안 작성
4. 화면 설계서 초안 작성
5. 데이터베이스 설계서 초안 작성
6. Supabase 테이블 생성
7. RLS 정책 확인
8. FastAPI API 작성
9. Streamlit 화면 작성
10. SSE 또는 자동 새로고침 기반 실시간 표시 방식 선택
11. 통합 테스트
12. 대시보드 구현 결과물과 발표 자료 작성
```

## 11. Docker 학습 위치

03 과정에서는 Docker를 사용하지 않습니다.

Docker, Docker Compose, AWS, GitHub Actions, 운영 모니터링은 다음 과정에서 다룹니다.

```text
C:\aidev\06_multi-agent-service-ops
```
