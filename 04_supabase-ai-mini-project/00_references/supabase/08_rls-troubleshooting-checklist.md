# 08 RLS Troubleshooting Checklist

이 문서는 Supabase RLS 때문에 데이터가 보이지 않거나 저장되지 않을 때 확인하는 체크리스트입니다.

RLS는 Row Level Security의 줄임말입니다. 테이블 전체 권한이 아니라 “어떤 행(row)을 누가 볼 수 있는가”를 정하는 Supabase/PostgreSQL 보안 기능입니다.

## 1. 먼저 테이블 이름을 확인합니다

04 과정에서는 실습 위치에 따라 사용하는 테이블이 다릅니다.

```text
01_local-dev-basic, 02_instructor-sample-project
-> learning_logs

03_supabase-and-sse-practice, 99_team-projects/team-template
-> service_logs, messages, feedbacks
```

현재 실행 중인 코드가 어떤 테이블을 조회하는지 먼저 확인합니다. 테이블 이름이 다르면 RLS 문제가 아니라 테이블 이름 문제일 수 있습니다.

## 2. 증상 확인

다음과 같은 상황이면 RLS 또는 권한 문제일 가능성이 있습니다.

```text
Supabase Table Editor에는 데이터가 있는데 Python/Streamlit에서는 보이지 않습니다.
insert 요청이 실패합니다.
로그인한 사용자 데이터만 조회되어야 하는데 결과가 비어 있습니다.
anon key로 select가 되지 않습니다.
service role key로는 되는데 anon key로는 되지 않습니다.
```

## 3. 테이블 존재 확인

SQL Editor에서 먼저 테이블이 실제로 있는지 확인합니다.

입문 샘플:

```sql
select * from public.learning_logs;
```

팀 프로젝트:

```sql
select * from public.service_logs;
select * from public.messages;
select * from public.feedbacks;
```

이 SQL부터 실패한다면 RLS보다 테이블 생성 또는 SQL 실행 순서를 먼저 확인해야 합니다.

## 4. RLS 켜짐 여부 확인

Supabase Table Editor에서 대상 테이블의 RLS 상태를 확인합니다.

```text
RLS off
-> 권한 제한이 거의 없는 상태입니다.

RLS on
-> policy가 있어야 select/insert/update/delete가 가능합니다.
```

수업에서는 RLS를 처음부터 완벽하게 외우는 것이 목표가 아닙니다. 먼저 “RLS가 켜져 있으면 policy가 필요하다”는 기준을 이해하면 됩니다.

## 5. anon key 사용 예제인지 확인

로그인 없이 실행하는 예제는 보통 `anon key`를 사용합니다.

이 경우 실습용 select 정책이 필요할 수 있습니다.

예시:

```sql
create policy "practice select service logs"
on public.service_logs
for select
to anon
using (true);
```

입문 샘플에서 `learning_logs`를 사용할 경우에는 테이블 이름만 바꾸면 됩니다.

```sql
create policy "practice select learning logs"
on public.learning_logs
for select
to anon
using (true);
```

## 6. insert가 안 되는 경우

insert 정책에서는 `with check` 조건이 중요합니다.

실습용으로 모든 anon insert를 허용하는 예:

```sql
create policy "practice insert service logs"
on public.service_logs
for insert
to anon
with check (true);
```

로그인 사용자별로 제한하는 예:

```sql
with check (user_id = auth.uid())
```

즉, 저장하려는 데이터의 `user_id`가 현재 로그인한 사용자 id와 같아야 합니다.

## 7. update/delete가 안 되는 경우

update/delete는 `using` 조건을 확인합니다.

예시:

```sql
using (user_id = auth.uid())
```

즉, 수정하거나 삭제하려는 데이터가 현재 사용자에게 허용된 데이터여야 합니다.

## 8. service role key와 anon key를 구분합니다

`service role key`는 RLS를 우회할 수 있습니다.

그래서 service role key로 성공했다고 해서 일반 사용자의 권한 정책이 정상이라는 뜻은 아닙니다.

수업에서는 다음 3가지를 구분해서 확인합니다.

```text
anon key 테스트
authenticated user 테스트
service role key 테스트
```

초보자 기준으로는 다음 원칙을 기억하면 됩니다.

```text
프론트엔드 화면에는 service role key를 넣지 않습니다.
FastAPI 백엔드에서만 service role key를 제한적으로 사용합니다.
사용자별 접근 제어는 RLS policy로 확인합니다.
```

## 9. 해결 기록 템플릿

문제가 생겼을 때는 아래 형식으로 기록합니다.

```text
문제 상황:
사용한 key 종류:
로그인 여부:
실행한 SQL:
현재 RLS 상태:
현재 Policy:
수정한 내용:
최종 확인 결과:
```

이 기록은 팀 프로젝트의 `docs/test-checklist.md` 또는 `docs/dashboard-result.md`에 옮겨 적으면 발표 자료로도 활용할 수 있습니다.
