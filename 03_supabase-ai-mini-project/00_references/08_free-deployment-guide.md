# 08_free-deployment-guide

이 문서는 `03_supabase-ai-mini-project` 팀 프로젝트를 무료 배포 서비스에 올려 시연하는 방법을 설명합니다.

03 과정의 기본 목표는 Supabase, FastAPI, Streamlit을 로컬에서 연결해 미니 프로젝트를 완성하는 것입니다. **배포는 필수가 아닙니다.** 배포는 팀 프로젝트 결과물을 외부 URL로 보여주기 위한 선택 확장입니다.

수업 제출 기준은 다음처럼 구분합니다.

```text
필수:
로컬에서 FastAPI + Streamlit + Supabase 연동 시연

선택:
Render + Upstash + Streamlit Community Cloud 무료 배포 시연
```

## 1. 배포 전체 구조

```text
사용자 브라우저
-> Streamlit Community Cloud
-> Render FastAPI 백엔드
-> Supabase Database/Auth
-> Upstash Redis 선택 사용
```

서비스별 역할은 다음과 같습니다.

| 서비스 | 역할 |
| --- | --- |
| Supabase | 사용자, 대화, 로그, 피드백 데이터를 저장합니다. Auth와 RLS도 여기서 관리합니다. |
| Render | FastAPI 백엔드 서버를 외부에서 호출할 수 있게 배포합니다. |
| Streamlit Community Cloud | Streamlit 프론트엔드 화면을 외부 URL로 배포합니다. |
| Upstash | Redis를 서버 설치 없이 사용합니다. 세션, 캐시, 임시 로그, rate limit 등에 선택적으로 사용합니다. |
| GitHub | Render와 Streamlit Community Cloud가 배포할 코드를 가져오는 저장소입니다. |

## 2. 배포용 프로젝트 구조

팀 프로젝트 폴더는 아래 구조를 권장합니다.

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

`backend`와 `frontend`를 나누는 이유는 배포 서비스가 서로 다르기 때문입니다.

```text
backend -> Render에서 실행
frontend -> Streamlit Community Cloud에서 실행
```

## 3. 환경변수 기준

로컬에서는 `.env` 파일을 사용합니다.

```env
SUPABASE_URL=https://your-project-id.supabase.co
SUPABASE_ANON_KEY=your-anon-key
SUPABASE_SERVICE_ROLE_KEY=your-service-role-key-if-needed
API_BASE_URL=http://127.0.0.1:8000
UPSTASH_REDIS_REST_URL=
UPSTASH_REDIS_REST_TOKEN=
```

배포할 때는 `.env` 파일을 GitHub에 올리지 않고, 각 배포 서비스의 환경변수 메뉴에 값을 넣습니다.

| 값 | 어디에 등록하나요? | 설명 |
| --- | --- | --- |
| `SUPABASE_URL` | Render | 백엔드가 Supabase에 접속할 때 사용합니다. |
| `SUPABASE_ANON_KEY` | Render | 백엔드가 Supabase API를 호출할 때 사용합니다. |
| `SUPABASE_SERVICE_ROLE_KEY` | Render | 필요한 경우에만 사용합니다. 프론트엔드에는 절대 넣지 않습니다. |
| `UPSTASH_REDIS_REST_URL` | Render | Redis를 선택 사용하는 경우 등록합니다. |
| `UPSTASH_REDIS_REST_TOKEN` | Render | Redis를 선택 사용하는 경우 등록합니다. |
| `API_BASE_URL` | Streamlit Community Cloud | 프론트엔드가 호출할 Render 백엔드 URL입니다. |

## 4. 배포 전 로컬 확인

배포는 선택이지만, 배포하기 전에는 반드시 로컬에서 먼저 확인합니다.

첫 번째 PowerShell에서 백엔드를 실행합니다.

```powershell
cd C:\aidev\03_supabase-ai-mini-project\99_team-projects\supabase-team-template\backend
..\..\..\.venv\Scripts\Activate.ps1
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

브라우저에서 확인합니다.

```text
http://127.0.0.1:8000/health
http://127.0.0.1:8000/docs
```

두 번째 PowerShell에서 프론트엔드를 실행합니다.

```powershell
cd C:\aidev\03_supabase-ai-mini-project\99_team-projects\supabase-team-template\frontend
..\..\..\.venv\Scripts\Activate.ps1
streamlit run app.py --server.port 8501
```

브라우저에서 확인합니다.

```text
http://localhost:8501
```

## 5. GitHub 저장소 준비

초보자는 전체 `C:\aidev` 폴더를 GitHub에 올리지 않는 것이 좋습니다. 배포할 팀 프로젝트 폴더만 별도 저장소로 정리합니다.

예시:

```text
my-supabase-mini-project
├─ backend
├─ frontend
├─ docs
├─ presentation
├─ README.md
└─.env.example
```

주의:

- `.env`는 올리지 않습니다.
- `.env.example`은 올립니다.
- `.venv`는 올리지 않습니다.
- `__pycache__`는 올리지 않습니다.

## 6. Render에 FastAPI 백엔드 배포

Render에서는 FastAPI 백엔드를 Web Service로 배포합니다.

1. Render에 로그인합니다.
2. `New`를 누릅니다.
3. `Web Service`를 선택합니다.
4. GitHub 저장소를 연결합니다.
5. 팀 프로젝트 저장소를 선택합니다.
6. Root Directory에 `backend`를 입력합니다.
7. Build Command를 입력합니다.

```text
pip install -r requirements.txt
```

8. Start Command를 입력합니다.

```text
uvicorn main:app --host 0.0.0.0 --port $PORT
```

Render에서는 포트를 `8000`으로 고정하지 않고 `$PORT`를 사용합니다.

9. Environment Variables에 백엔드용 값을 등록합니다.

```env
SUPABASE_URL=본인 Supabase URL
SUPABASE_ANON_KEY=본인 Supabase anon key
SUPABASE_SERVICE_ROLE_KEY=필요한 경우만 등록
UPSTASH_REDIS_REST_URL=선택
UPSTASH_REDIS_REST_TOKEN=선택
```

10. 배포가 끝나면 Render URL을 확인합니다.

```text
https://your-service-name.onrender.com
```

11. 브라우저에서 확인합니다.

```text
https://your-service-name.onrender.com/health
https://your-service-name.onrender.com/docs
```

## 7. Upstash Redis 준비

Upstash Redis는 선택입니다. 03 프로젝트에서 Redis를 반드시 써야 하는 것은 아닙니다.

사용하면 좋은 경우:

- 사용자별 임시 세션을 저장할 때
- 자주 조회되는 대시보드 요약값을 캐싱할 때
- 짧은 시간 동안의 실행 로그를 임시 저장할 때
- API 호출 제한(rate limit)을 구현할 때

준비 순서:

1. Upstash에 로그인합니다.
2. Redis Database를 생성합니다.
3. Free plan을 선택합니다.
4. REST API 영역에서 `UPSTASH_REDIS_REST_URL`과 `UPSTASH_REDIS_REST_TOKEN`을 복사합니다.
5. Render 백엔드 환경변수에 등록합니다.

프론트엔드에는 Upstash token을 넣지 않습니다.

## 8. Streamlit Community Cloud에 프론트엔드 배포

1. Streamlit Community Cloud에 로그인합니다.
2. `Create app` 또는 `New app`을 선택합니다.
3. GitHub 저장소를 선택합니다.
4. Branch를 선택합니다.
5. Main file path에 아래 값을 입력합니다.

```text
frontend/app.py
```

6. Secrets 또는 Advanced settings에 프론트엔드용 값을 등록합니다.

```toml
API_BASE_URL = "https://your-service-name.onrender.com"
```

7. 배포 후 생성된 URL을 확인합니다.

```text
https://your-app-name.streamlit.app
```

8. 배포된 화면에서 다음 기능을 확인합니다.

- 로그 생성
- 로그 목록 조회
- 대시보드 지표 표시
- 피드백 저장
- SSE 또는 자동 새로고침 기반 실시간 표시

## 9. 배포 후 제출할 정보

배포를 진행한 팀은 `docs/dashboard-result.md`와 `docs/deployment-guide.md`에 다음 정보를 기록합니다. 배포를 진행하지 않은 팀은 로컬 실행 URL과 시연 결과만 기록하면 됩니다.

```text
Render Backend URL:
Streamlit Frontend URL:
Supabase Project URL:
Upstash 사용 여부:
배포 확인 날짜:
배포 중 발생한 오류:
해결 방법:
```

## 10. 자주 만나는 오류

### Streamlit에서 백엔드 연결 실패

확인할 것:

```text
API_BASE_URL이 Render URL인가?
Render /health가 브라우저에서 열리는가?
백엔드 CORS 설정이 되어 있는가?
```

### Render에서 서버가 켜지지 않음

확인할 것:

```text
Root Directory가 backend인가?
Build Command가 pip install -r requirements.txt인가?
Start Command가 uvicorn main:app --host 0.0.0.0 --port $PORT인가?
requirements.txt에 fastapi, uvicorn, supabase가 있는가?
```

### Supabase 연결 실패

확인할 것:

```text
SUPABASE_URL이 정확한가?
SUPABASE_ANON_KEY가 정확한가?
테이블 이름이 코드와 같은가?
RLS 정책 때문에 조회/저장이 막힌 것은 아닌가?
```

### GitHub에 key가 올라감

즉시 해야 할 일:

```text
1. Supabase 또는 Upstash에서 노출된 key를 재발급합니다.
2. GitHub에서 key가 포함된 파일을 제거합니다.
3..gitignore에.env가 포함되어 있는지 확인합니다.
4. 앞으로는.env.example만 공유합니다.
```

## 11. 06 과정과의 차이

03에서의 배포는 무료 서비스를 활용한 시연용 선택 배포입니다. 필수 제출 조건은 아닙니다.

06에서는 다음을 별도로 학습합니다.

```text
Docker Compose
AWS 배포
GitHub Actions CI/CD
서비스 모니터링
Auto Healing
운영 로그와 장애 대응
```

따라서 03에서는 “팀 프로젝트를 URL로 보여줄 수 있다”를 목표로 하고, 운영 자동화와 장애 대응은 06에서 다룹니다.
