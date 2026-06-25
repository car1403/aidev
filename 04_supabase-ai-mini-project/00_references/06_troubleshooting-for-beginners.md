# Troubleshooting for Beginners

03 과정에서 자주 만나는 오류와 확인 방법입니다.

## 1. FastAPI가 실행되지 않는 경우

확인할 것:

1. 가상환경을 활성화했는가?
2. `pip install -r requirements.txt`를 실행했는가?
3. `backend` 폴더에서 명령을 실행했는가?
4. 8000 포트가 이미 사용 중은 아닌가?

```powershell
netstat -ano | findstr :8000
```

## 2. Streamlit이 실행되지 않는 경우

확인할 것:

1. `frontend` 폴더에서 명령을 실행했는가?
2. Streamlit이 설치되어 있는가?
3. 8501 포트가 이미 사용 중은 아닌가?

```powershell
streamlit run app.py --server.port 8501
```

## 3. Supabase 연결이 안 되는 경우

먼저 `.env` 값을 확인합니다.

```env
SUPABASE_URL=https://your-project-ref.supabase.co
SUPABASE_ANON_KEY=your-supabase-anon-key
SUPABASE_SERVICE_ROLE_KEY=your-supabase-service-role-key
API_BASE_URL=http://127.0.0.1:8000
```

확인할 것:

1. `SUPABASE_URL`에 오타가 없는가?
2. `SUPABASE_ANON_KEY`가 현재 프로젝트의 key인가?
3. `SUPABASE_SERVICE_ROLE_KEY`를 백엔드에서만 사용하는가?
4. `.env` 파일을 실행 위치에서 읽을 수 있는가?

## 4. Supabase 테이블이 없다는 오류

Supabase SQL Editor 또는 Table Editor에서 테이블을 만들었는지 확인합니다.

03 과정에서는 실습 위치에 따라 사용하는 테이블이 다릅니다.

```text
01_local-dev-basic, 02_instructor-sample-project
-> learning_logs

03_supabase-and-sse-practice, 99_team-projects/team-template
-> service_logs, messages, feedbacks
```

테이블 설계 예시는 다음 문서를 참고합니다.

```text
03_supabase-and-sse-practice/01_supabase-project-and-schema/03_team-project-base-schema.sql
05_project-templates/sql/supabase-base-schema.sql
99_team-projects/team-template/docs/supabase-schema.md
```

## 5. RLS 때문에 데이터가 안 보이는 경우

Supabase Table Editor에는 데이터가 있는데 Python 앱에서 안 보이면 RLS 정책을 확인합니다.

초보자 실습에서는 먼저 아래 순서로 확인합니다.

1. RLS가 켜져 있는가?
2. select 정책이 있는가?
3. insert 정책이 있는가?
4. 현재 사용하는 key와 정책 조건이 맞는가?

자세한 내용은 다음 문서를 참고합니다.

```text
00_references/supabase/04_rls-for-beginners.md
00_references/supabase/08_rls-troubleshooting-checklist.md
```

## 6. 프론트엔드에서 백엔드를 못 찾는 경우

Streamlit의 `API_BASE_URL`이 아래 주소인지 확인합니다.

```text
http://127.0.0.1:8000
```

백엔드가 먼저 실행되어 있어야 합니다.

## 7. Docker 관련 질문이 나오는 경우

03 과정에서는 Docker로 DB나 Redis를 실행하지 않습니다. Docker, Docker Compose, AWS 배포, 운영 자동화는 `07_multi-agent-service-ops`에서 다룹니다.

## 8. 오류 기록 템플릿

```text
오류가 난 위치:
실행한 명령:
오류 메시지:
확인한 내용:
해결 방법:
```