# 01. User Profile Data

사용자 식별자, 이메일, 이름, 가입일 같은 사용자 기본 정보를 설계합니다.

## 왜 사용자 프로필이 필요한가요?

Supabase Auth는 사용자가 누구인지 식별합니다. 하지만 실제 서비스에서는 Auth 정보만으로 부족한 경우가 많습니다.

예를 들어 다음 정보는 별도의 `profiles` 테이블에 저장하는 것이 좋습니다.

```text
display_name
preferred_language
course_level
created_at
```

## 실습 파일

```text
01_profile_schema_example.py
-> 사용자 프로필 데이터 구조를 Python dict로 이해합니다.

02_profile_crud_supabase.py
-> Supabase profiles 테이블에 프로필을 저장하고 조회하는 흐름을 실습합니다.
```

`02_profile_crud_supabase.py`는 실제 Supabase에 데이터를 저장할 수 있으므로 `.env`와 테이블 준비 후 실행합니다.
