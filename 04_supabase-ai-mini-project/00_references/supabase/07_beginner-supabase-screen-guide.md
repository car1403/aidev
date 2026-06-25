# 07 Beginner Supabase Screen Guide

이 문서는 Supabase를 처음 사용하는 사람이 화면에서 무엇을 확인해야 하는지 정리한 안내서입니다.

Supabase 화면 이름은 업데이트에 따라 조금씩 달라질 수 있습니다. 그래서 버튼 위치를 외우기보다, 어떤 정보를 어디에서 찾아야 하는지 이해하는 것이 중요합니다.

## 1. 프로젝트 들어가기

```text
Supabase 로그인
-> Projects 목록
-> 사용할 프로젝트 선택
```

프로젝트에 들어가면 왼쪽 메뉴에서 다음 항목을 자주 사용합니다.

```text
Table Editor
SQL Editor
Authentication
Project Settings
```

## 2. Project URL 찾기

보통 아래 위치에서 찾습니다.

```text
Project Settings
-> API
-> Project URL
```

`.env`에는 다음 이름으로 넣습니다.

```env
SUPABASE_URL=https://your-project-ref.supabase.co
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

```env
SUPABASE_ANON_KEY=your-supabase-anon-key
```

`anon key`는 공개 클라이언트에서 사용할 수 있는 키입니다. 다만 RLS 정책이 제대로 설정되어 있어야 안전합니다.

## 4. service role key 찾기

`service role key`도 API 설정 화면에서 볼 수 있습니다.

이 키는 매우 강한 권한을 가집니다. 초보자 실습에서는 다음 기준을 꼭 지킵니다.

```text
service role key는 FastAPI 같은 서버 코드에서만 사용합니다.
Streamlit 화면 코드에 직접 넣지 않습니다.
GitHub에 올리지 않습니다.
발표 화면이나 캡처 이미지에 노출하지 않습니다.
```

`.env`에는 필요한 경우에만 다음 이름으로 넣습니다.

```env
SUPABASE_SERVICE_ROLE_KEY=your-supabase-service-role-key
```

## 5. Table Editor 확인

Table Editor는 테이블과 데이터를 눈으로 확인하는 곳입니다.

04 과정에서는 실습 단계에 따라 사용하는 테이블이 다릅니다.

| 위치 | 주로 확인하는 테이블 | 용도 |
| --- | --- | --- |
| `01_local-dev-basic` | `learning_logs` | Supabase 연결 감각을 익히는 가장 작은 샘플 |
| `02_instructor-sample-project` | `learning_logs` | 완성된 샘플 실행 확인 |
| `03_supabase-and-sse-practice` | `service_logs`, `messages`, `feedbacks` | 팀 프로젝트에 필요한 핵심 기능 실습 |
| `99_team-projects/team-template` | `service_logs`, `messages`, `feedbacks` | 최종 팀 프로젝트 기본 구조 |

확인할 것:

```text
테이블이 생성되어 있는가?
샘플 데이터가 들어 있는가?
컬럼 이름이 SQL 문서와 같은가?
RLS가 켜져 있는가?
RLS policy가 필요한 기능에 맞게 작성되어 있는가?
```

## 6. SQL Editor 확인

SQL Editor는 SQL 문장을 직접 실행하는 곳입니다.

처음 실행할 SQL은 실습 폴더와 템플릿 폴더에 들어 있습니다.

```text
03_supabase-and-sse-practice/01_supabase-project-and-schema/03_team-project-base-schema.sql
03_supabase-and-sse-practice/01_supabase-project-and-schema/04_team-project-base-schema.sql
05_project-templates/sql/supabase-base-schema.sql
99_team-projects/team-template/sql/supabase-base-schema.sql
```

샘플 연결 확인용 SQL:

```sql
select * from public.learning_logs;
```

팀 프로젝트 확인용 SQL:

```sql
select * from public.service_logs;
select * from public.messages;
select * from public.feedbacks;
```

## 7. Authentication 확인

Authentication 메뉴에서는 가입한 사용자와 인증 설정을 확인합니다.

확인할 것:

```text
실습용 사용자가 생성되었는가?
이메일 확인이 필요한 설정인가?
로그인 테스트 계정이 준비되어 있는가?
RLS 정책에서 auth.uid()를 사용하는 경우 사용자 id와 연결되는가?
```

## 8. 처음 막히면 보는 순서

Supabase 연결이 안 되거나 데이터가 보이지 않을 때는 아래 순서로 확인합니다.

```text
1. SUPABASE_URL이 현재 프로젝트 URL과 같은가?
2. SUPABASE_ANON_KEY가 현재 프로젝트의 anon key인가?
3. .env 파일 위치가 C:\aidev\04_supabase-ai-mini-project\.env 인가?
4. 실행한 실습이 learning_logs를 쓰는지 service_logs를 쓰는지 확인했는가?
5. 필요한 테이블이 Supabase에 생성되어 있는가?
6. 샘플 데이터가 들어 있는가?
7. RLS 정책 때문에 조회/저장이 막힌 것은 아닌가?
8. Python 가상환경과 패키지 설치가 완료되어 있는가?
```

## 9. 기억할 기준

04 과정의 최종 팀 프로젝트 기준 테이블은 `service_logs`, `messages`, `feedbacks`입니다.

`learning_logs`는 Supabase 연결을 처음 익히기 위한 입문용 샘플 테이블입니다. 따라서 최종 프로젝트 문서와 코드는 `service_logs` 중심으로 정리하는 것이 좋습니다.
