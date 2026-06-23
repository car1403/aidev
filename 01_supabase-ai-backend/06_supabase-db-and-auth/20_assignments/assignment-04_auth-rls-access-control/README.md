# Assignment 04 - Auth/RLS 접근 제어 설계

Supabase Auth와 RLS를 사용해 사용자별 데이터 접근을 제어하는 설계 과제입니다.

## 목표

- 인증과 권한 제어의 차이를 설명할 수 있습니다.
- 사용자별 데이터 접근 제한이 필요한 이유를 설명할 수 있습니다.
- 보호 API와 RLS 정책을 함께 설계할 수 있습니다.

## 제출물

아래 내용을 포함해 작성합니다.

```text
1. 회원가입 API 설계
2. 로그인 API 설계
3. 보호된 로그 생성 API 설계
4. 사용자별 로그 조회 API 설계
5. 다른 사용자의 로그에 접근하지 못하게 하는 방법
6. RLS가 필요한 이유
7. anon key와 service role key의 사용 위치
8. Streamlit 또는 브라우저 코드에 service role key를 넣으면 안 되는 이유
```

## 보호 API 예시

```text
GET /me
Authorization: Bearer <access_token>
```

실습에서는 `Bearer demo-token` 같은 가짜 토큰으로 구조를 먼저 이해할 수 있습니다. 실제 서비스에서는 Supabase Auth JWT를 검증하는 방식으로 확장합니다.

## RLS 정책 설명에 포함할 내용

```text
사용자는 본인의 user_id와 연결된 데이터만 조회할 수 있다.
다른 사용자의 데이터는 조회, 수정, 삭제할 수 없다.
```

## 확인 기준

- 인증이 필요한 API와 공개 API를 구분했습니다.
- `auth.uid() = user_id` 같은 RLS 조건의 의미를 설명했습니다.
- service role key를 서버에서만 사용해야 하는 이유를 설명했습니다.
