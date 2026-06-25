# 01. Supabase 프로젝트 만들기

## 1. Supabase 접속

1. 브라우저에서 Supabase 사이트에 접속합니다.
2. GitHub 계정 또는 이메일 계정으로 로그인합니다.
3. `New project`를 선택합니다.
4. 프로젝트 이름을 입력합니다.
5. Region은 가까운 지역을 선택합니다.
6. Database Password는 안전하게 보관합니다.

## 2. 프로젝트 정보 확인

프로젝트가 만들어진 뒤 왼쪽 메뉴에서 다음 화면으로 이동합니다.

```text
Project Settings
-> Data API 또는 API
```

확인할 값은 다음과 같습니다.

```text
Project URL
anon public key
service_role key
```

## 3. .env 파일에 정리

03 과정에서는 아래 파일을 사용합니다.

```text
C:\aidev\03_supabase-ai-mini-project\.env
```

예시:

```env
SUPABASE_URL=https://your-project-id.supabase.co
SUPABASE_ANON_KEY=your-anon-key
SUPABASE_SERVICE_ROLE_KEY=your-service-role-key
GEMINI_API_KEY=your-gemini-api-key
```

## 4. 확인 기준

- `SUPABASE_URL`은 프로젝트마다 다릅니다.
- `SUPABASE_ANON_KEY`는 프론트엔드에서도 사용할 수 있지만, RLS 정책이 필요합니다.
- `SUPABASE_SERVICE_ROLE_KEY`는 백엔드에서만 사용합니다.
- `.env`는 GitHub에 올리지 않습니다.
- `.env.example`에는 실제 key 대신 예시 이름만 작성합니다.
