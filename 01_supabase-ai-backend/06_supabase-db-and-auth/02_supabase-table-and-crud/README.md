# 02. Supabase 테이블과 CRUD

이 챕터에서는 Supabase에 테이블을 만들고, Python 코드에서 CRUD를 실행합니다.

CRUD는 백엔드 개발에서 가장 기본이 되는 데이터 처리 흐름입니다.

```text
Create: 데이터 생성
Read: 데이터 조회
Update: 데이터 수정
Delete: 데이터 삭제
```

이 과정에서는 먼저 `learning_notes` 테이블 하나로 시작합니다. 사용자, 대화 이력, 서비스 로그처럼 복잡한 테이블은 이후 챕터에서 단계적으로 확장합니다.

## 학습 목표

- Supabase Table Editor와 SQL Editor의 역할을 이해합니다.
- `learning_notes` 테이블을 생성합니다.
- Python Supabase client로 insert/select/update/delete를 실행합니다.
- CRUD 코드가 SQL의 어떤 명령과 연결되는지 이해합니다.
- 수정/삭제 시 조건을 반드시 지정해야 하는 이유를 이해합니다.

## Supabase에서 테이블 만드는 방법

Supabase Dashboard에서 다음 메뉴로 이동합니다.

```text
SQL Editor
-> New query
```

아래 SQL을 붙여 넣고 실행합니다.

```sql
create table if not exists learning_notes (
  id uuid primary key default gen_random_uuid(),
  title text not null,
  content text not null,
  created_at timestamptz not null default now()
);
```

## 컬럼 설명

| 컬럼 | 타입 | 의미 |
| --- | --- | --- |
| `id` | `uuid` | 각 메모를 구분하는 고유 ID입니다. |
| `title` | `text` | 메모 제목입니다. |
| `content` | `text` | 메모 내용입니다. |
| `created_at` | `timestamptz` | 데이터가 생성된 시간입니다. |

`id`는 직접 입력하지 않아도 Supabase/PostgreSQL이 자동으로 만들어 줍니다. `created_at`도 `now()` 기본값 덕분에 자동으로 현재 시간이 들어갑니다.

## 실행 전 확인

먼저 환경 변수가 준비되어 있는지 확인합니다.

```powershell
cd C:\aidev\01_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
python .\06_supabase-db-and-auth\01_supabase-project-and-env\01_check_supabase_env.py
```

그다음 CRUD 예제를 실행합니다.

```powershell
python .\06_supabase-db-and-auth\02_supabase-table-and-crud\01_learning_notes_crud.py
```

이 예제는 다음 순서로 동작합니다.

```text
1. learning_notes 테이블에 실습용 메모 1개를 추가합니다.
2. 최근 메모 5개를 조회합니다.
3. 방금 만든 메모의 제목을 수정합니다.
4. 실습용 메모를 삭제합니다.
```

실행 후 Supabase Table Editor에서 `learning_notes` 테이블을 새로고침하며 데이터가 생겼다가 삭제되는 흐름을 확인합니다.

## CRUD와 SQL 대응 관계

| Supabase Python 코드 | SQL 관점 | 의미 |
| --- | --- | --- |
| `.insert({...})` | `insert into` | 새 데이터를 저장합니다. |
| `.select("*")` | `select` | 저장된 데이터를 조회합니다. |
| `.update({...}).eq("id", note_id)` | `update ... where` | 특정 데이터를 수정합니다. |
| `.delete().eq("id", note_id)` | `delete ... where` | 특정 데이터를 삭제합니다. |

중요한 기준은 조건입니다.

```python
.eq("id", note_id)
```

수정과 삭제를 할 때 조건을 빠뜨리면 의도하지 않은 여러 데이터가 바뀔 수 있습니다. 초보 단계에서는 “update/delete에는 조건이 거의 항상 필요하다”라고 기억하면 좋습니다.

## service role key 주의

이 예제는 Python 백엔드 코드에서 실행하므로 `SUPABASE_SERVICE_ROLE_KEY`를 사용합니다.

```text
service role key는 강한 권한을 가진 서버용 key입니다.
Streamlit 화면, 브라우저 코드, GitHub 저장소에 노출하면 안 됩니다.
```

프론트엔드나 사용자 화면에서 Supabase를 직접 사용할 때는 RLS 정책과 anon key를 함께 사용해야 합니다. 이 내용은 `04_supabase-auth-and-rls`에서 다시 다룹니다.

## 이후 확장

`learning_notes`로 CRUD 흐름을 이해한 뒤, 이후 챕터에서 다음 테이블로 확장합니다.

| 테이블 | 용도 |
| --- | --- |
| `profiles` | 사용자 프로필 |
| `conversations` | 대화 세션 |
| `messages` | 사용자/AI 메시지 |
| `service_logs` | 서비스 실행 로그 |

## 완료 체크리스트

```text
[ ] Supabase SQL Editor에서 learning_notes 테이블을 만들었습니다.
[ ] .env에 SUPABASE_URL과 SUPABASE_SERVICE_ROLE_KEY가 설정되어 있습니다.
[ ] 01_check_supabase_env.py 실행 결과가 정상입니다.
[ ] 01_learning_notes_crud.py를 실행했습니다.
[ ] insert/select/update/delete 흐름을 Supabase 화면에서 확인했습니다.
[ ] update/delete에서 eq("id", note_id)가 왜 필요한지 설명할 수 있습니다.
```
