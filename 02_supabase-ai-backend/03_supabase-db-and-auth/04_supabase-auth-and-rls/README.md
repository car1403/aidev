# 04. Supabase Auth와 RLS

이 챕터에서는 Supabase Auth와 RLS(Row Level Security)를 이해합니다.

앞 챕터까지는 FastAPI 서버가 `SUPABASE_SERVICE_ROLE_KEY`로 Supabase에 접근했습니다. 이번 챕터에서는 사용자가 로그인했을 때 “누가 어떤 데이터에 접근할 수 있는지”를 어떻게 제한하는지 배웁니다.

## 학습 목표

- Supabase Auth가 어떤 역할을 하는지 이해합니다.
- 로그인 결과로 발급되는 JWT의 의미를 이해합니다.
- anon key와 service role key의 차이를 설명할 수 있습니다.
- RLS가 왜 필요한지 이해합니다.
- 사용자별 데이터 접근 정책을 SQL로 설계하는 기본 흐름을 익힙니다.
- Supabase Auth API를 Python에서 호출해 가입/로그인 흐름을 확인합니다.
- FastAPI와 Swagger에서 Bearer token 기반 보호 API 흐름을 확인합니다.

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

## JWT를 조금 더 자세히 보기

JWT는 JSON Web Token의 줄임말입니다. Supabase Auth에서 이메일/비밀번호 로그인이 성공하면 Supabase는 사용자를 식별할 수 있는 토큰을 발급합니다.

로그인 결과에서 중요하게 보는 값은 보통 아래와 같습니다.

| 값 | 의미 |
| --- | --- |
| `user.id` | Supabase Auth가 발급한 사용자 고유 id입니다. |
| `user.email` | 로그인한 사용자의 이메일입니다. |
| `session.access_token` | API 요청에 사용할 JWT입니다. |
| `session.refresh_token` | access token을 다시 발급받을 때 사용하는 토큰입니다. |

JWT는 보통 아래처럼 API 요청 헤더에 들어갑니다.

```text
Authorization: Bearer <access_token>
```

여기서 `Bearer`는 “이 토큰을 가진 사용자로 요청한다”는 의미로 이해하면 됩니다. FastAPI나 Supabase는 이 access token을 확인해서 현재 요청한 사용자가 누구인지 판단합니다.

RLS 정책에서 자주 보는 `auth.uid()`는 로그인한 사용자의 id를 의미합니다.

```sql
using (auth.uid() = id)
```

이 조건은 다음처럼 읽을 수 있습니다.

```text
현재 JWT로 확인된 사용자 id가
이 행의 id와 같을 때만
조회 또는 수정을 허용한다
```

주의할 점:

```text
1. access token은 비밀번호처럼 다룹니다.
2. token 전체 값을 터미널, README, GitHub, 화면 공유에 노출하지 않습니다.
3. access token은 만료될 수 있습니다.
4. refresh token도 노출되면 안 됩니다.
5. RLS는 JWT의 사용자 정보를 기준으로 동작하므로 로그인하지 않은 요청에서는 auth.uid()가 null처럼 동작할 수 있습니다.
```

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

### 1. FastAPI/Swagger로 Auth 흐름 확인

이 챕터의 Python 예제는 실제 Supabase Auth API를 FastAPI endpoint에서 호출합니다.

실행 전 `.env`에 아래 값을 준비합니다.

```env
SUPABASE_URL=https://your-project-ref.supabase.co
SUPABASE_ANON_KEY=your-supabase-anon-key
```

이 예제는 사용자를 대신해 Auth API를 호출하는 흐름이므로 `SUPABASE_SERVICE_ROLE_KEY`가 아니라 `SUPABASE_ANON_KEY`를 사용합니다.

```powershell
cd C:\aidev\02_supabase-ai-backend\03_supabase-db-and-auth\04_supabase-auth-and-rls
..\..\.venv\Scripts\Activate.ps1
uvicorn 01_fastapi_supabase_auth:app --reload --host 127.0.0.1 --port 8002
```

Swagger 주소:

```text
http://127.0.0.1:8002/docs
```

Swagger에서 확인할 endpoint:

| Endpoint | Method | 역할 |
| --- | --- | --- |
| `/health` | GET | FastAPI 서버 실행 확인 |
| `/auth/signup` | POST | Supabase Auth 회원가입 요청 |
| `/auth/signin` | POST | 로그인 후 access token 발급 확인 |
| `/me` | GET | `Authorization: Bearer <access_token>`으로 현재 사용자 확인 |

Swagger 실습 순서:

```text
1. /health를 실행해 서버가 켜져 있는지 확인합니다.
2. /auth/signup에서 테스트 이메일과 비밀번호로 가입합니다.
3. /auth/signin에서 같은 이메일과 비밀번호로 로그인합니다.
4. 응답의 access_token 값을 복사합니다.
5. Swagger 오른쪽 위 Authorize 버튼을 누릅니다.
6. Value에 access_token을 붙여 넣습니다.
   Swagger UI가 Bearer 형식으로 전송합니다.
7. /me를 실행해 현재 로그인한 user id와 email이 나오는지 확인합니다.
```

`/me`는 FastAPI가 직접 비밀번호를 확인하는 예제가 아닙니다. 클라이언트가 보낸 Bearer token을 Supabase Auth에 확인시키고, Supabase가 알려 준 현재 사용자 정보를 반환하는 예제입니다.

주의할 점:

```text
1. /auth/signin 응답에는 실제 access_token이 포함됩니다.
2. 이 값은 수업 중 화면 공유, README, GitHub에 노출하지 않습니다.
3. access_token이 있어야 /me 같은 보호 API를 호출할 수 있습니다.
4. 실제 서비스에서는 token 만료, refresh token, 로그아웃, 권한 정책을 더 엄격하게 다룹니다.
```

Supabase 프로젝트의 이메일 인증 설정에 따라 `sign_up` 후 바로 로그인되지 않을 수 있습니다. 이 경우 Supabase에서 보낸 이메일 인증을 완료한 뒤 다시 `/auth/signin`을 실행합니다.

### 2. /me 결과와 auth.uid() 연결하기

`/me`에서 확인한 `user.id`는 “현재 access token이 가리키는 사용자 id”입니다. Supabase RLS 정책 안에서는 이 값을 `auth.uid()`로 읽습니다.

```text
Swagger /me 결과:
  user.id = 현재 로그인한 사용자 id

Supabase RLS SQL:
  auth.uid() = 현재 로그인한 사용자 id
```

따라서 RLS 정책의 핵심 조건은 보통 아래처럼 읽습니다.

```sql
auth.uid() = user_id
```

```text
현재 로그인한 사용자 id와
이 행(row)의 user_id가 같을 때만
조회, 생성, 수정, 삭제를 허용한다
```

### 3. RLS SQL 의미 예제

아래 SQL은 사용자별 메모 테이블을 만들고, 로그인한 사용자가 자기 메모만 다룰 수 있도록 제한하는 예시입니다. Python 파일로 실행하는 예제가 아니라 Supabase Dashboard의 SQL Editor에서 읽고 실행하는 SQL입니다.

```sql
create table if not exists user_memos (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references auth.users(id) on delete cascade,
  title text not null,
  content text,
  created_at timestamptz not null default now()
);

alter table user_memos enable row level security;

create policy "users can read own memos"
on user_memos
for select
using (auth.uid() = user_id);

create policy "users can create own memos"
on user_memos
for insert
with check (auth.uid() = user_id);

create policy "users can update own memos"
on user_memos
for update
using (auth.uid() = user_id)
with check (auth.uid() = user_id);

create policy "users can delete own memos"
on user_memos
for delete
using (auth.uid() = user_id);
```

SQL 의미:

| 구문 | 의미 |
| --- | --- |
| `user_id uuid references auth.users(id)` | 메모 행을 Supabase Auth 사용자와 연결합니다. |
| `enable row level security` | 테이블에 행 단위 보안 규칙을 켭니다. |
| `auth.uid()` | 현재 JWT로 확인된 사용자 id입니다. |
| `using (...)` | 기존 행을 읽거나 수정/삭제할 수 있는지 검사합니다. |
| `with check (...)` | 새로 만들거나 수정한 행이 허용된 값인지 검사합니다. |
| `auth.uid() = user_id` | 현재 로그인 사용자와 행의 소유자가 같을 때만 허용합니다. |

이 예제에서 가장 중요한 문장은 `auth.uid() = user_id`입니다. `/me`에서 본 사용자 id와 테이블의 `user_id`가 같을 때만 데이터 접근을 허용한다는 뜻입니다.

## 수업 진행 순서

1. Auth와 RLS의 차이를 먼저 설명합니다.
2. Supabase Dashboard에서 Authentication 메뉴를 확인합니다.
3. anon key와 service role key의 차이를 다시 확인합니다.
4. FastAPI/Swagger 예제로 sign up/sign in 흐름을 확인합니다.
5. access token을 `/me` 같은 보호 API에 전달하는 흐름을 확인합니다.
6. `/me` 결과의 user id와 RLS의 `auth.uid()`를 연결해서 설명합니다.
7. `user_memos` RLS SQL을 읽으며 `auth.uid() = user_id` 조건을 설명합니다.
8. RLS를 켰는데 정책이 없으면 데이터가 보이지 않을 수 있다는 점을 설명합니다.

## 자주 만나는 문제

### RLS를 켰더니 데이터가 안 보이는 경우

RLS는 기본적으로 “정책으로 허용한 작업만 가능”하게 만듭니다. RLS를 켰는데 select 정책이 없으면 조회가 막힐 수 있습니다.

### service role key로는 다 보이는 경우

service role key는 RLS를 우회할 수 있습니다. 그래서 FastAPI 서버에서만 사용해야 합니다. 사용자 화면에서 service role key를 사용하면 보안상 매우 위험합니다.

### auth.uid()가 null처럼 동작하는 경우

사용자가 로그인하지 않았거나, 요청에 JWT가 전달되지 않은 경우입니다. 실제 로그인 기반 API에서는 Authorization 헤더에 토큰을 보내야 합니다.

### sign_up 후 sign_in이 바로 실패하는 경우

Supabase Auth의 이메일 인증 설정이 켜져 있으면 가입 직후 바로 로그인되지 않을 수 있습니다. Supabase가 보낸 인증 메일을 확인하거나, 수업용 프로젝트에서 이메일 인증 설정을 어떻게 운영할지 먼저 정합니다.

### access token을 그대로 출력한 경우

토큰은 사용자를 대신해 API를 호출할 수 있는 값입니다. 실습 중 실수로 전체 토큰을 화면에 노출했다면 해당 사용자를 로그아웃시키거나 테스트 계정을 다시 만드는 것이 좋습니다.

## 완료 체크리스트

```text
[ ] Auth와 RLS의 차이를 설명할 수 있습니다.
[ ] anon key와 service role key의 차이를 설명할 수 있습니다.
[ ] service role key를 프론트엔드에 노출하면 안 되는 이유를 설명할 수 있습니다.
[ ] FastAPI/Swagger에서 /auth/signup, /auth/signin, /me 흐름을 확인했습니다.
[ ] access token과 refresh token을 전체 출력하면 안 되는 이유를 이해했습니다.
[ ] Authorization: Bearer <access_token> 헤더의 의미를 설명할 수 있습니다.
[ ] auth.uid() = user_id 조건의 의미를 이해했습니다.
[ ] RLS를 켠 뒤 정책이 없으면 데이터가 막힐 수 있음을 이해했습니다.
```
