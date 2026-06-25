# 05 Streamlit FastAPI Supabase Patterns

Supabase를 사용하는 방법은 크게 두 가지입니다.

## Pattern 1: Streamlit -> Supabase

```text
Streamlit 화면에서 Supabase를 직접 호출
```

장점:

- 구조가 단순합니다.
- 빠르게 대시보드를 만들 수 있습니다.

주의점:

- service role key를 절대 쓰면 안 됩니다.
- RLS 정책이 중요합니다.

## Pattern 2: Streamlit -> FastAPI -> Supabase

```text
Streamlit은 FastAPI 호출
FastAPI가 Supabase 호출
```

장점:

- 서버에서 요청 검증을 할 수 있습니다.
- 오류 처리를 통제하기 쉽습니다.
- service role key가 필요할 때 서버에만 둘 수 있습니다.

주의점:

- 구조가 조금 더 복잡합니다.
- FastAPI 서버도 실행해야 합니다.

## 선택 기준

```text
간단한 대시보드 -> Streamlit 직접 호출
권한/검증/서버 로직 필요 -> FastAPI 경유 호출
```

