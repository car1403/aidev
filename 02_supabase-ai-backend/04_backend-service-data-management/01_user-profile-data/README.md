# 01_user-profile-data

이 챕터는 AI 서비스에서 사용자 프로필 데이터를 어떻게 설계하고 저장할지 학습합니다.

`03_supabase-db-and-auth`에서는 Supabase 프로젝트, 테이블 생성, CRUD, Auth/RLS, Upstash Redis의 기본 흐름을 배웠습니다. 이번 챕터부터는 그 내용을 실제 백엔드 서비스 데이터 구조로 연결합니다.

## 왜 사용자 프로필이 필요한가요?

Supabase Auth는 사용자가 누구인지 확인해 줍니다. 하지만 실제 서비스에서는 로그인 정보만으로 부족한 경우가 많습니다.

예를 들어 AI 학습 서비스에서는 아래 정보가 필요할 수 있습니다.

```text
display_name
preferred_language
course_level
created_at
```

이런 정보는 Auth 자체 정보에만 의존하기보다 별도의 `profiles` 테이블에 저장하는 것이 좋습니다.

## Supabase Auth와 profiles 테이블의 관계

```text
Supabase Auth
-> 로그인과 사용자 식별 담당
-> auth.users.id 생성

profiles table
-> 서비스에서 필요한 사용자 표시 정보 저장
-> profiles.id가 auth.users.id와 연결됨
```

핵심은 `profiles.id`가 로그인한 사용자의 `auth.users.id`와 같은 값을 사용한다는 점입니다.

## 기본 테이블 구조

`03_supabase-db-and-auth/00_references/supabase-schema.sql`에는 아래 기본 구조가 포함되어 있습니다.

```sql
create table if not exists profiles (
  id uuid primary key,
  display_name text not null,
  created_at timestamptz not null default now()
);
```

## 선택 확장 컬럼

이번 챕터에서 언어와 학습 수준까지 저장하려면 Supabase SQL Editor에서 아래 SQL을 추가로 실행할 수 있습니다.

```sql
alter table profiles
add column if not exists preferred_language text not null default 'ko';

alter table profiles
add column if not exists course_level text not null default 'beginner';
```

이 두 컬럼은 필수는 아니지만, 개인화 AI 서비스에서는 유용합니다.

| 컬럼 | 의미 | 예시 |
|---|---|---|
| `display_name` | 화면에 보여 줄 이름 | `수강생 A` |
| `preferred_language` | 기본 응답 언어 | `ko` |
| `course_level` | 학습 난이도 또는 수준 | `beginner` |

## 실습 파일

| 파일 | 내용 |
|---|---|
| `01_profile_schema_example.py` | Supabase에 접속하지 않고 Python dict로 프로필 구조를 이해합니다. |
| `02_profile_crud_supabase.py` | Supabase `profiles` 테이블에 프로필을 저장하고 조회합니다. |

## 실행 순서

먼저 구조 예제를 실행합니다. 이 파일은 Supabase에 접속하지 않으므로 `.env`가 없어도 실행할 수 있습니다.

```powershell
cd C:\aidev\02_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
python .\04_backend-service-data-management\01_user-profile-data\01_profile_schema_example.py
```

Supabase에 실제 저장하는 예제는 `.env`와 `profiles` 테이블이 준비된 뒤 실행합니다.

```powershell
python .\04_backend-service-data-management\01_user-profile-data\02_profile_crud_supabase.py
```

## 확인 기준

- 사용자 프로필 정보와 Auth 정보의 역할을 구분할 수 있습니다.
- `profiles.id`가 사용자 ID와 연결된다는 점을 설명할 수 있습니다.
- Supabase Table Editor에서 저장된 프로필 데이터를 확인할 수 있습니다.
- service role key를 프론트엔드에 넣으면 안 되는 이유를 설명할 수 있습니다.

## 정리 질문

- 이메일은 Auth 정보에 있는데, `display_name`을 별도로 저장하는 이유는 무엇인가요?
- `preferred_language`는 AI 응답 개인화에 어떻게 활용할 수 있나요?
- `course_level`은 프롬프트 작성이나 응답 난이도 조절에 어떻게 연결될 수 있나요?
- 사용자별 데이터 접근 제어를 하려면 RLS에서 어떤 기준이 필요할까요?
