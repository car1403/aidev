# 04 RLS For Beginners

RLS는 Row Level Security의 줄임말입니다.

테이블의 행마다 누가 볼 수 있는지 정하는 기능입니다.

## 왜 필요한가?

예를 들어 사용자별 학습 로그가 있다고 가정합니다.

```text
user A의 로그
user B의 로그
```

사용자 A가 사용자 B의 로그를 보면 안 됩니다.

이때 RLS 정책을 사용합니다.

## 기본 아이디어

```sql
user_id = auth.uid()
```

뜻:

```text
현재 로그인한 사용자의 ID와 데이터의 user_id가 같을 때만 접근한다.
```

## RLS를 켰는데 데이터가 안 보이는 이유

RLS를 켜고 정책을 만들지 않으면 접근이 막힐 수 있습니다.

그래서 다음을 확인해야 합니다.

- RLS가 켜져 있는가?
- select 정책이 있는가?
- insert 정책이 있는가?
- user_id 값이 auth.uid()와 일치하는가?

## 기억할 문장

```text
RLS는 Supabase에서 사용자별 데이터 접근을 안전하게 만드는 핵심 기능입니다.
```

