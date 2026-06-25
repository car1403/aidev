# Lab 02 - Supabase profiles 저장과 조회

이 실습은 `profiles` 테이블에 사용자 프로필을 저장하고 다시 조회합니다.

## 목표

- Python 코드에서 Supabase `profiles` 테이블에 데이터를 저장할 수 있습니다.
- `upsert`가 insert와 update를 합친 개념이라는 것을 이해합니다.
- Supabase Table Editor에서 저장 결과를 확인할 수 있습니다.

## 실행 전 확인

`.env`에 Supabase 값이 있어야 합니다.

```text
SUPABASE_URL
SUPABASE_SERVICE_ROLE_KEY
```

기본 스키마를 Supabase SQL Editor에서 실행합니다.

```text
C:\aidev\02_supabase-ai-backend\06_supabase-db-and-auth\00_references\supabase-schema.sql
```

`preferred_language`, `course_level` 컬럼을 사용하려면 `01_user-profile-data/README.md`의 alter table SQL도 실행합니다.

## 실행 방법

```powershell
cd C:\aidev\02_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
python .\07_backend-service-data-management\01_user-profile-data\02_profile_crud_supabase.py
```

## 확인 기준

- 저장된 프로필이 터미널에 출력됩니다.
- 조회한 프로필이 터미널에 출력됩니다.
- Supabase Table Editor의 `profiles` 테이블에서 데이터가 보입니다.

## 오류 확인

컬럼이 없다는 오류가 나오면 `preferred_language`, `course_level` 컬럼 추가 SQL을 실행합니다.
