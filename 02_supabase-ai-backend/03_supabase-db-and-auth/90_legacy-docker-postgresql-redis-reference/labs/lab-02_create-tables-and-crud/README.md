# Lab 02 - PostgreSQL 테이블 생성과 CRUD

로컬 PostgreSQL 컨테이너 안에서 테이블을 만들고 CRUD를 실행하는 legacy lab입니다.

## 목표

- SQL로 테이블을 생성합니다.
- `INSERT`, `SELECT`, `UPDATE`, `DELETE`를 실행합니다.
- SQL 결과를 직접 확인합니다.

## 참고 SQL

```sql
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  email TEXT NOT NULL UNIQUE
);

INSERT INTO users (name, email)
VALUES ('Aidev User', 'aidev@example.com');

SELECT * FROM users;
```

## 현재 과정에서의 대응

현재 과정에서는 Supabase SQL Editor와 `supabase-schema.sql`을 사용합니다.
