# PostgreSQL SQL 요약

PostgreSQL에서 자주 사용하는 SQL 명령어를 정리한 legacy 참고 문서입니다.

Supabase도 PostgreSQL 기반이므로 SQL 개념 자체는 현재 과정에서도 그대로 도움이 됩니다.

## 테이블 생성

```sql
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email TEXT UNIQUE NOT NULL,
  name TEXT NOT NULL,
  password_hash TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## INSERT

```sql
INSERT INTO users (email, name, password_hash)
VALUES ('alice@example.com', 'Alice', 'hashed-password');
```

## SELECT

```sql
SELECT id, email, name, created_at
FROM users
ORDER BY id DESC;
```

## UPDATE

```sql
UPDATE users
SET name = 'Alice Kim'
WHERE id = 1;
```

## DELETE

```sql
DELETE FROM users
WHERE id = 1;
```

## WHERE 조건

```sql
SELECT *
FROM users
WHERE email = 'alice@example.com';
```

## Supabase 과정에서의 연결

현재 과정에서는 직접 `psql`에 접속하기보다 Supabase SQL Editor 또는 Supabase Python SDK를 사용합니다.
