# 07 Beginner Supabase Screen Guide

Supabase를 처음 사용하는 입문자를 위한 화면 확인 가이드입니다.

Supabase 화면 이름은 업데이트에 따라 조금씩 달라질 수 있습니다. 그래서 버튼 위치를 외우기보다, 아래 정보를 어디에서 찾는지 이해하는 것이 중요합니다.

## 1. 프로젝트에 들어가기

```text
Supabase 로그인
-> Projects 목록
-> 사용할 프로젝트 선택
```

프로젝트에 들어가면 왼쪽 메뉴에서 Database, Authentication, SQL Editor, Project Settings 같은 항목을 볼 수 있습니다.

## 2. Project URL 찾기

보통 다음 위치에서 찾습니다.

```text
Project Settings
-> API
-> Project URL
```

`.env`에는 다음 이름으로 넣습니다.

```text
SUPABASE_URL=Project URL
```

## 3. anon public key 찾기

보통 Project URL과 같은 API 설정 화면에 있습니다.

```text
Project Settings
-> API
-> Project API keys
-> anon public key
```

`.env`에는 다음 이름으로 넣습니다.

```text
SUPABASE_ANON_KEY=anon public key
```

## 4. service role key 찾기

service role key도 API 설정 화면에서 볼 수 있습니다.

하지만 이 key는 매우 강한 권한을 가집니다.

```text
service role key는 서버에서만 사용합니다.
Streamlit 화면 코드에는 넣지 않습니다.
GitHub에 올리지 않습니다.
발표 화면에 노출하지 않습니다.
```

## 5. Table Editor 확인

Table Editor는 데이터를 눈으로 확인하는 곳입니다.

확인할 것:

```text
learning_logs 테이블이 있는가?
샘플 데이터가 들어 있는가?
컬럼 이름이 SQL과 같은가?
RLS가 켜져 있는가?
```

## 6. SQL Editor 확인

SQL Editor는 SQL 문장을 직접 실행하는 곳입니다.

처음 실행할 SQL은 샘플 프로젝트의 `docs/setup-supabase.md`에 포함되어 있습니다.

```text
05_supabase-sample-assets/sample-learning-log-dashboard/docs/setup-supabase.md
```

확인 SQL:

```sql
select * from public.learning_logs;
```

## 7. Authentication 확인

Authentication 메뉴에서는 가입한 사용자를 확인합니다.

확인할 것:

```text
실습용 사용자가 생성되었는가?
이메일 확인이 필요한 설정인가?
로그인 테스트 계정이 준비되었는가?
```

## 8. 처음 막히면 보는 순서

```text
1. Project URL이 맞는가?
2. anon key가 맞는가?
3..env 파일 위치가 맞는가?
4. learning_logs 테이블이 있는가?
5. 샘플 데이터가 있는가?
6. RLS 정책 때문에 막힌 것은 아닌가?
7. Python 패키지가 설치되어 있는가?
```
