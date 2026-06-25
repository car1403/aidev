# 01 Supabase First Look

Supabase는 PostgreSQL 기반 클라우드 백엔드 플랫폼입니다.

웹 서비스를 만들 때 필요한 여러 기능을 빠르게 사용할 수 있게 도와줍니다.

```text
Database
Authentication
Storage
API
Dashboard
```

04 과정에서는 주로 다음 기능을 사용합니다.

```text
Supabase Database
Supabase Auth
API Key
RLS Policy
```

## 쉽게 말하면

`04_supabase-ai-mini-project`에서는 PostgreSQL을 내 PC의 Docker 컨테이너로 실행하지 않습니다.

대신 Supabase 클라우드 프로젝트 안의 데이터베이스를 사용합니다. Supabase 화면에서 테이블을 만들고, FastAPI가 Supabase API를 통해 데이터를 저장하고 조회합니다.

## 장점

- 데이터베이스 준비가 빠릅니다.
- 관리 화면이 제공됩니다.
- Auth 기능을 빠르게 붙일 수 있습니다.
- RLS로 사용자별 데이터 접근을 제어할 수 있습니다.
- 프로젝트 초기 버전을 빠르게 만들 수 있습니다.

## 주의할 점

- Supabase 계정과 프로젝트가 필요합니다.
- API key를 안전하게 관리해야 합니다.
- service role key는 백엔드에서만 사용해야 합니다.
- RLS 정책을 이해해야 합니다.
- 외부 클라우드 서비스이므로 네트워크 연결이 필요합니다.

## 04 과정에서의 역할

Supabase는 아래 데이터를 저장하는 중심 역할을 합니다.

```text
사용자 정보
대화 정보
메시지
서비스 로그
피드백
```

최종 팀 프로젝트에서는 `service_logs`, `messages`, `feedbacks` 테이블을 중심으로 대시보드와 AI 응답 품질 개선 흐름을 구성합니다.
