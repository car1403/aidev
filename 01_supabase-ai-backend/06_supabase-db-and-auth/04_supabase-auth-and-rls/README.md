# 04_supabase-auth-and-rls

이 단원은 Supabase Auth와 RLS(Row Level Security)를 이해하는 단계입니다.

## 학습 목표

- Supabase Auth의 회원가입/로그인 흐름을 이해합니다.
- anon key와 service role key의 차이를 이해합니다.
- RLS가 왜 필요한지 설명할 수 있습니다.
- 사용자별 데이터 접근 정책을 설계합니다.

## 핵심 개념

```text
Auth : 사용자가 누구인지 확인
JWT : 로그인 결과로 발급되는 토큰
RLS : 테이블 행 단위 접근 제어
anon key : 클라이언트에서 사용할 수 있는 공개용 key
service role key : 서버에서만 사용해야 하는 강한 권한의 key
```

## 권장 실습 흐름

1. Supabase Dashboard에서 Auth 설정을 확인합니다.
2. `profiles` 테이블을 만듭니다.
3. `user_id uuid` 컬럼을 추가합니다.
4. RLS를 켭니다.
5. 본인 데이터만 조회/수정할 수 있는 정책을 작성합니다.

## 강의 주의사항

- service role key는 Streamlit 화면이나 브라우저 코드에 넣지 않습니다.
- service role key는 FastAPI 같은 서버 코드에서만 사용합니다.
- RLS를 켜면 정책이 없을 때 데이터가 보이지 않을 수 있습니다.

## RLS를 이해하는 쉬운 비유

Supabase 테이블은 교실의 사물함과 비슷합니다.

```text
Auth
-> 이 직접 누구인지 확인합니다.

RLS
-> 이 직접 어떤 사물함을 열 수 있는지 정합니다.
```

로그인만 했다고 모든 데이터를 볼 수 있는 것은 아닙니다. 로그인은 "누구인지 확인"이고, RLS는 "어떤 행을 읽고 쓸 수 있는지 결정"하는 규칙입니다.

## 기본 SQL 예시

아래 SQL은 `profiles` 테이블을 만들고 사용자 본인의 프로필만 조회/수정할 수 있게 하는 예시입니다. 수업에서는 Supabase SQL Editor에 직접 붙여 넣으며 설명합니다.

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

## 서버 코드에서의 key 선택 기준

| 위치 | 사용할 key | 이유 |
| --- | --- | --- |
| Streamlit/브라우저 | `SUPABASE_ANON_KEY` | 공개되어도 되는 제한된 key입니다. RLS 정책과 함께 사용합니다. |
| FastAPI 서버 | `SUPABASE_SERVICE_ROLE_KEY` | 서버에서 관리 작업을 할 때 사용합니다. 절대 프론트엔드에 노출하지 않습니다. |
| GitHub 저장소 | key 저장 금지 | `.env`는 올리지 않고 `.env.example`만 올립니다. |

## 실습 질문

다음 질문을 함께 확인합니다.

1. 로그인한 사용자가 다른 사용자의 프로필을 볼 수 있으면 어떤 문제가 생기나요?
2. RLS를 켰는데 정책을 만들지 않으면 왜 데이터가 보이지 않을까요?
3. service role key가 프론트엔드에 노출되면 어떤 위험이 생기나요?
4. FastAPI 서버가 사용자 대신 Supabase에 접근할 때 어떤 로그를 남겨야 할까요?
