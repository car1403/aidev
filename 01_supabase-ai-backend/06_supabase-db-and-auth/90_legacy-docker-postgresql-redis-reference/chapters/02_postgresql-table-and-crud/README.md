# 02_postgresql-table-and-crud

로컬 PostgreSQL에서 테이블을 만들고 CRUD를 실행하는 legacy 참고 챕터입니다.

현재 과정에서는 Supabase SQL Editor와 Supabase Python SDK로 같은 개념을 학습합니다.

## 핵심 개념

- `CREATE TABLE`: 테이블 생성
- `INSERT`: 데이터 추가
- `SELECT`: 데이터 조회
- `UPDATE`: 데이터 수정
- `DELETE`: 데이터 삭제

## 현재 과정에서의 대응

| Legacy SQL 작업 | 현재 과정 위치 |
|---|---|
| 테이블 생성 | `00_references/supabase-schema.sql` |
| Python CRUD | `02_supabase-table-and-crud` |
| API CRUD | `03_fastapi-supabase-integration` |

## 참고 관점

Supabase도 내부적으로 PostgreSQL을 사용합니다. 따라서 SQL의 기본 개념은 동일하지만, 현재 과정에서는 서버 설치와 운영을 Supabase에 맡기고 API와 서비스 설계에 집중합니다.
