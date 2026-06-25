# 04. Supabase Auth와 RLS

이 챕터에서는 Supabase Auth와 RLS(Row Level Security)를 이해합니다.

앞 챕터까지는 FastAPI 서버가 `SUPABASE_SERVICE_ROLE_KEY`로 Supabase에 접근했습니다. 이번 챕터에서는 사용자가 로그인했을 때 “누가 어떤 데이터에 접근할 수 있는지”를 어떻게 제한하는지 배웁니다.

## 학습 목표

- Supabase Auth가 어떤 역할을 하는지 이해합니다.
- 로그인 결과로 발급되는 JWT의 의미를 이해합니다.
- anon key와 service role key의 차이를 설명할 수 있습니다.
- RLS가 왜 필요한지 이해합니다.
- 사용자별 데이터 접근 정책을 SQL로 설계하는 기본 흐름을 익힙니다.
- Python 코드로 RLS 조건을 단순화해서 확인합니다.

## 핵심 개념

| 개념 | 의미 |
| --- | --- |
| Auth | 사용자가 누구인지 확인하는 기능입니다. |
| JWT | 로그인 성공 후 발급되는 토큰입니다. API 요청에서 사용자 정보를 전달합니다. |
| RLS | 테이블의 행(row) 단위로 읽기/쓰기 권한을 제한하는 기능입니다. |
| anon key | 클라이언트에서 사용할 수 있는 공개용 key입니다. RLS 정책과 함께 사용해야 안전합니다. |
| service role key | RLS를 우회할 수 있는 서버 전용 key입니다. 프론트엔드에 노출하면 안 됩니다. |

## Auth와 RLS의 차이

```text
Auth:
  이 사용자가 누구인지 확인합니다.

RLS:
  이 사용자가 어떤 행을 읽거나 쓸 수 있는지 결정합니다.
```

로그인만 했다고 모든 데이터를 볼 수 있는 것은 아닙니다. 로그인은 “누구인지 확인”이고, RLS는 “어떤 데이터에 접근할 수 있는지 제한”하는 규칙입니다.

## 쉬운 예시

사용자별 프로필 테이블이 있다고 가정합니다.

```text
사용자 A -> 사용자 A의 프로필만 볼 수 있음
사용자 B -> 사용자 B의 프로필만 볼 수 있음
사용자 A -> 사용자 B의 프로필은 볼 수 없음
```

RLS 정책은 이 조건을 데이터베이스에서 강제로 지키게 만듭니다.

## Supabase Dashboard에서 확인할 위치

### Auth 설정

```text
Supabase Dashboard
-> Authentication
-> Providers
```

이곳에서 이메일 로그인, 소셜 로그인 같은 인증 방식을 설정합니다.

### RLS 설정

```text
Supabase Dashboard
-> Table Editor
-> 테이블 선택
-> RLS 설정 확인
```

또는 SQL Editor에서 직접 RLS를 켤 수 있습니다.

## 기본 SQL 예시

아래 SQL은 사용자 프로필 테이블을 만들고, 로그인한 사용자가 자기 프로필만 읽고 수정할 수 있도록 하는 예시입니다.

```sql
create table if not exists profiles (
  id uuid primary key references auth.users(id) on delete cascade,
  display_name text not null,
  created_at timestamptz not null default now()
);

alter table profiles enable row level security;

create policy "users can read own profile"
on profiles
for select
using (auth.uid() = id);

create policy "users can update own profile"
on profiles
for update
using (auth.uid() = id)
with check (auth.uid() = id);
```

### SQL 의미

| SQL | 의미 |
| --- | --- |
| `references auth.users(id)` | Supabase Auth 사용자와 프로필을 연결합니다. |
| `enable row level security` | 테이블에 RLS를 켭니다. |
| `auth.uid()` | 현재 로그인한 사용자의 id를 의미합니다. |
| `using (auth.uid() = id)` | 자기 id와 같은 행만 읽을 수 있습니다. |
| `with check (auth.uid() = id)` | 자기 id와 같은 행만 쓰거나 수정할 수 있습니다. |

## 서버 코드에서 key 선택 기준

| 위치 | 사용할 key | 기준 |
| --- | --- | --- |
| 브라우저/Streamlit 화면 | `SUPABASE_ANON_KEY` | 공개 가능한 key입니다. 반드시 RLS 정책과 함께 사용합니다. |
| FastAPI 서버 | `SUPABASE_SERVICE_ROLE_KEY` | 서버에서만 사용하는 강한 권한의 key입니다. |
| GitHub 저장소 | key 저장 금지 | `.env`는 올리지 않고 `.env.example`만 공유합니다. |

## 예제 실행

이 챕터의 Python 예제는 실제 Supabase Auth API를 호출하지 않습니다. RLS 조건을 Python 함수로 단순화해 “자기 데이터만 접근 가능하다”는 개념을 확인합니다.

```powershell
cd C:\aidev\02_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
python .\06_supabase-db-and-auth\04_supabase-auth-and-rls\01_auth_rls_concept_check.py
```

## 수업 진행 순서

1. Auth와 RLS의 차이를 먼저 설명합니다.
2. Supabase Dashboard에서 Authentication 메뉴를 확인합니다.
3. anon key와 service role key의 차이를 다시 확인합니다.
4. `profiles` 테이블 SQL을 읽으며 `auth.uid() = id` 조건을 설명합니다.
5. Python 예제를 실행해 본인 데이터와 다른 사용자 데이터 접근 결과를 비교합니다.
6. RLS를 켰는데 정책이 없으면 데이터가 보이지 않을 수 있다는 점을 설명합니다.

## 자주 만나는 문제

### RLS를 켰더니 데이터가 안 보이는 경우

RLS는 기본적으로 “정책으로 허용한 작업만 가능”하게 만듭니다. RLS를 켰는데 select 정책이 없으면 조회가 막힐 수 있습니다.

### service role key로는 다 보이는 경우

service role key는 RLS를 우회할 수 있습니다. 그래서 FastAPI 서버에서만 사용해야 합니다. 사용자 화면에서 service role key를 사용하면 보안상 매우 위험합니다.

### auth.uid()가 null처럼 동작하는 경우

사용자가 로그인하지 않았거나, 요청에 JWT가 전달되지 않은 경우입니다. 실제 로그인 기반 API에서는 Authorization 헤더에 토큰을 보내야 합니다.

## 완료 체크리스트

```text
[ ] Auth와 RLS의 차이를 설명할 수 있습니다.
[ ] anon key와 service role key의 차이를 설명할 수 있습니다.
[ ] service role key를 프론트엔드에 노출하면 안 되는 이유를 설명할 수 있습니다.
[ ] auth.uid() = id 조건의 의미를 이해했습니다.
[ ] RLS를 켠 뒤 정책이 없으면 데이터가 막힐 수 있음을 이해했습니다.
[ ] 01_auth_rls_concept_check.py를 실행했습니다.
```
