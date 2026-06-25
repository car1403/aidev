# 06. Supabase Errors

Supabase 연동 중 자주 만나는 오류입니다.

## 환경변수 누락

확인:

```text
.env 파일이 있는가?
SUPABASE_URL이 있는가?
SUPABASE_ANON_KEY가 있는가?
SUPABASE_SERVICE_ROLE_KEY가 필요한 코드인가?
```

## RLS 때문에 조회가 안 됩니다

가능한 원인:

```text
RLS가 켜져 있지만 select policy가 없다.
로그인 사용자의 user_id 조건이 맞지 않는다.
anon key와 service role key 사용 위치를 혼동했다.
```

## key 보안

```text
service role key는 서버에서만 사용합니다.
Streamlit 화면 코드에 넣지 않습니다.
.env는 GitHub에 올리지 않습니다.
```
