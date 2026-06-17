# 08 RLS Troubleshooting Checklist

RLS 때문에 데이터가 안 보일 때 확인하는 체크리스트입니다.

## 증상

다음과 같은 상황이면 RLS 또는 권한 문제일 수 있습니다.

```text
Supabase Table Editor에는 데이터가 있는데 Python/Streamlit에서는 안 보인다.
insert 요청이 실패한다.
로그인한 사용자 데이터만 조회해야 하는데 결과가 비어 있다.
anon key로 select가 되지 않는다.
```

## 1. 테이블 존재 확인

SQL Editor에서 실행합니다.

```sql
select * from public.learning_logs;
```

이 SQL도 실패하면 RLS보다 테이블 생성 문제일 수 있습니다.

## 2. RLS 켜짐 여부 확인

Supabase Table Editor에서 `learning_logs` 테이블의 RLS 상태를 확인합니다.

```text
RLS off -> 권한 제한이 거의 없음
RLS on  -> policy가 있어야 접근 가능
```

## 3. anon key 사용 예제인지 확인

로그인 없이 실행하는 예제는 anon key를 사용합니다.

이 경우 학습용 select policy가 필요할 수 있습니다.

```sql
create policy "practice select learning logs"
on public.learning_logs
for select
to anon
using (true);
```

## 4. 로그인 사용자 예제인지 확인

로그인 사용자별 데이터 예제는 authenticated role과 `auth.uid()` 정책이 필요합니다.

```sql
user_id = auth.uid()
```

확인할 것:

```text
user_id 컬럼이 있는가?
user_id 값이 로그인한 사용자 id와 같은가?
authenticated role 정책이 있는가?
```

## 5. insert가 안 될 때

insert 정책에는 `with check` 조건이 중요합니다.

예시:

```sql
with check (user_id = auth.uid())
```

즉, 저장하려는 데이터의 `user_id`가 현재 로그인한 사용자 ID와 같아야 합니다.

## 6. update/delete가 안 될 때

update/delete는 `using` 조건이 중요합니다.

예시:

```sql
using (user_id = auth.uid())
```

즉, 수정하거나 삭제하려는 데이터가 내 데이터여야 합니다.

## 7. service role key로는 되는데 anon key로는 안 될 때

service role key는 RLS를 우회할 수 있습니다.

그래서 service role key로 성공한다고 해서 일반 사용자 권한이 정상이라는 뜻은 아닙니다.

실습에서는 다음을 구분해야 합니다.

```text
anon key 테스트
authenticated user 테스트
service role key 테스트
```

## 8. 해결 기록 양식

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

