# Python PostgreSQL 연결

이 과정에서는 `psycopg`를 사용해 PostgreSQL에 연결합니다.

## 설치

```powershell
pip install "psycopg[binary]"
```

## 연결 예시

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

## 환경변수 권장

실제 프로젝트에서는 DB 비밀번호를 코드에 직접 작성하지 않습니다.

```env
DATABASE_URL=postgresql://aidev:aidev1234@localhost:5432/aidev_db
```

