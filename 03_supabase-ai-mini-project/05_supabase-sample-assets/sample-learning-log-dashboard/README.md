# Sample Learning Log Dashboard

Supabase 기반 학습 로그 대시보드 샘플 프로젝트입니다.

이 프로젝트는 `03_supabase-ai-mini-project\02_instructor-sample-project`의 학습 로그 대시보드를 Supabase 방식으로 다시 구현합니다.

## 구조

```text
sample-learning-log-dashboard
├─ README.md
├─.env.example
├─ backend
│ ├─ main.py
│ └─ requirements.txt
├─ frontend
│ ├─ app.py
│ └─ requirements.txt
└─ docs
 ├─ setup-supabase.md
 ├─ api-test-guide.md
 └─ comparison-with-docker-compose.md
```

## 실행 준비

Supabase SQL Editor에서 다음 테이블이 필요합니다.

```text
public.learning_logs
```

테이블 SQL은 다음 문서를 참고합니다.

```text
docs\setup-supabase.md
```

`.env.example`을 복사해 `.env`를 만들고 실제 값을 입력합니다.

```powershell
Copy-Item.env.example.env
```

## Backend 실행

```powershell
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

확인:

```text
http://127.0.0.1:8000/health
http://127.0.0.1:8000/docs
```

## Frontend 실행

```powershell
cd frontend
pip install -r requirements.txt
streamlit run app.py
```

확인:

```text
http://127.0.0.1:8501
```

## 주의사항

- 이 샘플은 Docker Compose를 사용하지 않습니다.
- DB는 Supabase 클라우드 PostgreSQL을 사용합니다.
- 실제 key는 코드나 README에 작성하지 않습니다.

