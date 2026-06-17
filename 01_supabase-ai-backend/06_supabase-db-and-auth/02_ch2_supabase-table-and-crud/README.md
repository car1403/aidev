# 02_ch2_supabase-table-and-crud

이 단원은 Supabase Table Editor 또는 SQL Editor에서 테이블을 만들고, Python에서 CRUD를 실행하는 단계입니다.

## 학습 목표

- 사용자/대화/로그 테이블의 기본 구조를 설계합니다.
- Supabase SQL Editor에서 테이블을 생성합니다.
- Python Supabase client로 데이터를 생성, 조회, 수정, 삭제합니다.
- insert/select/update/delete가 각각 어떤 SQL 개념과 연결되는지 이해합니다.

## 추천 테이블

초보자는 먼저 `learning_notes` 테이블 하나로 시작합니다.

```sql
create table if not exists learning_notes (
  id uuid primary key default gen_random_uuid(),
  title text not null,
  content text not null,
  created_at timestamptz not null default now()
);
```

이후 프로젝트에서 다음 테이블로 확장합니다.

```text
profiles          사용자 프로필
conversations     대화 세션
messages          대화 메시지
service_logs      서비스 실행 로그
```

## 실행 예시

```powershell
cd C:\aidev\01_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
python .\06_supabase-db-and-auth\02_ch2_supabase-table-and-crud\01_learning_notes_crud.py
```

실행 전 Supabase에 `learning_notes` 테이블이 있어야 합니다.

## CRUD와 SQL 대응 관계

| Python Supabase 코드 | SQL 관점 | 의미 |
| --- | --- | --- |
| `.insert({...})` | `insert into` | 새 데이터를 저장합니다. |
| `.select("*")` | `select` | 저장된 데이터를 조회합니다. |
| `.update({...}).eq("id", note_id)` | `update ... where` | 특정 데이터를 수정합니다. |
| `.delete().eq("id", note_id)` | `delete ... where` | 특정 데이터를 삭제합니다. |

초보자에게 중요한 기준은 `eq("id", note_id)` 같은 조건입니다. 수정/삭제를 할 때 조건을 빠뜨리면 여러 데이터가 한꺼번에 바뀔 수 있으므로 항상 어떤 행을 대상으로 하는지 먼저 확인합니다.

## 수업 진행 팁

1. Supabase Table Editor에서 빈 테이블을 먼저 보여줍니다.
2. Python 파일을 실행해 데이터가 추가되는 것을 확인합니다.
3. Supabase 화면을 새로고침해 행이 생겼는지 확인합니다.
4. update 실행 후 제목이 바뀌는지 확인합니다.
5. delete 실행 후 실습용 데이터가 삭제되는지 확인합니다.
