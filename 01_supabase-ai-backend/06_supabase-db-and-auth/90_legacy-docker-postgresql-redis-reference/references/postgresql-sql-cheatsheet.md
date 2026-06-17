# PostgreSQL SQL 요약

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

