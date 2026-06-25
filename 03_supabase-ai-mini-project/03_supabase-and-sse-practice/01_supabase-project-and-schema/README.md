# 01_supabase-project-and-schema

이 단계에서는 팀 프로젝트에서 사용할 Supabase 프로젝트와 기본 테이블 구조를 준비합니다.

03 과정의 앞부분인 `01_local-dev-basic`, `02_instructor-sample-project`에서는 Supabase 연결을 쉽게 익히기 위해 `learning_logs` 샘플 테이블을 사용했습니다. 이 단계부터는 팀 프로젝트 기준인 `profiles`, `conversations`, `messages`, `service_logs`, `feedbacks` 테이블로 넘어갑니다.

## 학습 목표

- Supabase 프로젝트에서 URL과 key를 확인할 수 있습니다.
- `anon key`와 `service role key`의 차이를 설명할 수 있습니다.
- `.env`와 `.env.example`의 차이를 구분할 수 있습니다.
- 팀 프로젝트 기본 테이블 구조를 이해할 수 있습니다.
- Supabase SQL Editor에서 테이블 생성 SQL을 실행할 수 있습니다.

## 진행 순서

1. Supabase에 로그인합니다.
2. 새 프로젝트를 만들거나 수업용 프로젝트를 선택합니다.
3. Project Settings에서 Project URL, anon key, service role key를 확인합니다.
4. `C:\aidev\03_supabase-ai-mini-project\.env` 파일에 값을 정리합니다.
5. 팀 프로젝트 기본 테이블 구조를 확인합니다.
6. SQL Editor에서 `03_team-project-base-schema.sql`을 실행합니다.
7. Table Editor에서 테이블이 생성되었는지 확인합니다.

## 권장 테이블

처음부터 테이블을 너무 많이 만들면 프로젝트가 복잡해집니다. 아래 테이블을 기본으로 시작하고, 필요한 경우에만 추가합니다.

```text
profiles
-> 사용자 기본 정보

conversations
-> 사용자별 대화 묶음

messages
-> 사용자 메시지와 AI 응답

service_logs
-> API 호출, 오류, 실행 상태 기록

feedbacks
-> 사용자가 남긴 응답 평가
```

## key 사용 기준

```text
SUPABASE_URL
-> FastAPI와 Streamlit에서 모두 사용할 수 있는 프로젝트 주소

SUPABASE_ANON_KEY
-> 공개 클라이언트에서 사용할 수 있는 제한된 key
-> RLS 정책과 함께 사용해야 안전함

SUPABASE_SERVICE_ROLE_KEY
-> 모든 데이터에 접근할 수 있는 강한 key
-> FastAPI 같은 백엔드에서만 제한적으로 사용
-> Streamlit 코드나 GitHub에 올리면 안 됨
```

## 실습 파일

- [01_supabase-project-setup.md](./01_supabase-project-setup.md)
- [02_env-and-key-safety.md](./02_env-and-key-safety.md)
- [03_team-project-base-schema.sql](./03_team-project-base-schema.sql)

## 체크리스트

- [ ] Supabase 프로젝트를 생성했다.
- [ ] Project URL, anon key, service role key를 확인했다.
- [ ] `.env` 파일을 만들었다.
- [ ] `.env`를 GitHub에 올리지 않는다는 점을 확인했다.
- [ ] SQL Editor에서 기본 테이블 생성 SQL을 실행했다.
- [ ] Table Editor에서 `service_logs`, `messages`, `feedbacks` 테이블을 확인했다.
