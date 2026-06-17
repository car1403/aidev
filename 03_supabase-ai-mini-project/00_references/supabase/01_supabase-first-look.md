# 01 Supabase First Look

Supabase는 PostgreSQL 기반 클라우드 백엔드 플랫폼입니다.

웹 서비스를 만들 때 필요한 기능을 빠르게 사용할 수 있게 해줍니다.

```text
Database
Authentication
Storage
API
Dashboard
```

이 과정에서는 주로 다음 기능을 사용합니다.

```text
Supabase Database
Supabase Auth
API Key
RLS Policy
```

## 쉽게 말하면

`03_supabase-ai-mini-project`에서는 PostgreSQL을 내 PC의 Docker 컨테이너로 실행하지 않습니다.

대신 Supabase 클라우드 프로젝트 안의 데이터베이스를 사용합니다. 학생은 Supabase 화면에서 테이블을 만들고, FastAPI는 Supabase API를 통해 데이터를 저장하고 조회합니다.

## 장점

- DB 준비가 빠릅니다.
- 관리 화면이 있습니다.
- Auth 기능을 빠르게 붙일 수 있습니다.
- RLS로 사용자별 데이터 접근을 제어할 수 있습니다.
- 프로토타입을 빠르게 만들 수 있습니다.

## 주의점

- 계정과 프로젝트가 필요합니다.
- API key를 안전하게 관리해야 합니다.
- service role key는 백엔드에서만 사용해야 합니다.
- RLS 정책을 이해해야 합니다.
- 외부 서비스이므로 네트워크 연결이 필요합니다.
