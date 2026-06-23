# Python PostgreSQL 연결

Python에서 로컬 PostgreSQL에 직접 연결하는 legacy 참고 문서입니다.

현재 과정에서는 Supabase SDK를 사용하므로 `psycopg` 직접 연결은 필수로 진행하지 않습니다.

## 패키지 설치

```powershell
pip install "psycopg[binary]"
```

## 직접 연결 예시

```python
import psycopg


conn = psycopg.connect(
    host="localhost",
    port=5432,
    dbname="aidev_db",
    user="aidev",
    password="aidev1234",
)
```

## 환경변수 사용 권장

실제 프로젝트에서는 DB 비밀번호를 코드에 직접 적지 않습니다.

```env
DATABASE_URL=postgresql://aidev:aidev1234@localhost:5432/aidev_db
```

## 현재 과정에서의 대응

Supabase 과정에서는 아래 환경변수를 사용합니다.

```env
SUPABASE_URL=...
SUPABASE_ANON_KEY=...
SUPABASE_SERVICE_ROLE_KEY=...
```

Supabase 방식은 DB 서버 주소, 인증, API 접근을 Supabase가 관리해 주기 때문에 초반 학습 난이도가 낮습니다.
