# Assignment 02 - 사용자 프로필 데이터 설계

AI 서비스에서 사용할 사용자 프로필 테이블을 설계하는 과제입니다.

## 목표

- Auth 정보와 서비스 프로필 정보를 구분할 수 있습니다.
- `profiles` 테이블에 필요한 컬럼을 설계할 수 있습니다.
- 개인화 AI 응답에 프로필 데이터를 어떻게 사용할지 설명할 수 있습니다.

## 제출물

아래 내용을 포함해 작성합니다.

```text
1. profiles 테이블의 목적
2. 필요한 컬럼 목록
3. 각 컬럼의 데이터 타입
4. 각 컬럼이 필요한 이유
5. auth.users.id와 profiles.id의 관계
6. 개인화 AI 응답에 활용할 수 있는 프로필 정보
7. 예시 데이터 1개
```

## 권장 컬럼 예시

| 컬럼 | 타입 | 설명 |
|---|---|---|
| `id` | uuid | Auth 사용자 ID와 연결 |
| `display_name` | text | 화면에 보여 줄 이름 |
| `preferred_language` | text | 기본 응답 언어 |
| `course_level` | text | 학습 수준 |
| `created_at` | timestamptz | 생성 시간 |

## 확인 기준

- Auth가 담당하는 정보와 `profiles`가 담당하는 정보를 구분했습니다.
- `profiles.id`가 사용자 식별 기준이라는 점을 설명했습니다.
- 프로필 데이터가 Supabase에 저장되어야 하는 이유를 설명했습니다.
