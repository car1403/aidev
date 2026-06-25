# 03 Key And Env Safety

이 문서는 Supabase key와 `.env` 파일을 안전하게 다루는 방법을 설명합니다.

03 과정에서는 Supabase, Gemini API, 선택적으로 OpenAI API와 Upstash Redis를 사용합니다. 이 값들은 코드에 직접 쓰지 않고 `.env` 파일에 보관합니다.

## 1. anon key

`anon key`는 Supabase에서 공개 클라이언트가 사용할 수 있도록 제공하는 key입니다.

Streamlit 같은 프론트엔드에서도 사용할 수 있지만, 안전하게 사용하려면 RLS 정책이 필요합니다.

초보자 기준으로는 이렇게 기억하면 됩니다.

```text
anon key
-> 공개될 수 있는 key
-> 그래도 아무 테이블이나 마음대로 접근하면 안 됨
-> RLS 정책과 함께 사용해야 안전함
```

## 2. service role key

`service role key`는 매우 강한 권한을 가진 서버용 key입니다.

절대 아래 위치에 넣지 않습니다.

```text
Streamlit app.py
README.md
GitHub 저장소
발표 자료
브라우저에서 실행되는 코드
화면 캡처 이미지
```

필요한 경우 FastAPI 백엔드에서만 사용합니다.

```text
FastAPI backend
-> Supabase에 서버 권한으로 접근할 때 제한적으로 사용
```

## 3. .env

실제 key는 `.env` 파일에 넣습니다.

03 과정의 `.env` 위치는 다음 하나입니다.

```text
C:\aidev\04_supabase-ai-mini-project\.env
```

팀 프로젝트 하위 폴더마다 별도의 `.env`를 만들지 않습니다. 최상위 `.env` 하나를 기준으로 사용합니다.

예시:

```env
SUPABASE_URL=https://your-project-ref.supabase.co
SUPABASE_ANON_KEY=your-supabase-anon-key
SUPABASE_SERVICE_ROLE_KEY=your-supabase-service-role-key

GEMINI_API_KEY=your-gemini-api-key
GEMINI_MODEL=gemini-2.5-flash-lite

OPENAI_API_KEY=your-openai-api-key
OPENAI_MODEL=gpt-4.1-mini

API_BASE_URL=http://127.0.0.1:8000

UPSTASH_REDIS_REST_URL=
UPSTASH_REDIS_REST_TOKEN=
```

## 4. .env.example

`.env.example`은 공유용 예시 파일입니다.

실제 key를 넣지 않고, 어떤 환경변수가 필요한지만 보여줍니다.

예시:

```env
SUPABASE_URL=https://your-project-ref.supabase.co
SUPABASE_ANON_KEY=your-supabase-anon-key
SUPABASE_SERVICE_ROLE_KEY=your-supabase-service-role-key

GEMINI_API_KEY=your-gemini-api-key
GEMINI_MODEL=gemini-2.5-flash-lite

OPENAI_API_KEY=your-openai-api-key
OPENAI_MODEL=gpt-4.1-mini

API_BASE_URL=http://127.0.0.1:8000
```

## 5. 제출 전 확인

프로젝트를 제출하거나 GitHub에 올리기 전에 아래를 확인합니다.

```text
.env 파일이 GitHub에 올라가지 않았는가?
.env.example에는 실제 key가 없는가?
README.md에 실제 key가 적혀 있지 않은가?
발표 자료나 캡처 이미지에 key가 보이지 않는가?
service role key가 Streamlit 코드에 들어가지 않았는가?
```

## 6. key가 노출되었을 때

실수로 key가 GitHub나 화면에 노출되면 아래 순서로 처리합니다.

```text
1. Supabase 또는 해당 서비스에서 key를 재발급합니다.
2. 기존 key를 더 이상 사용하지 않도록 합니다.
3. GitHub에서 노출된 파일을 제거합니다.
4. .gitignore에 .env가 포함되어 있는지 확인합니다.
5. 이후에는 .env.example만 공유합니다.
```

key 노출은 누구나 실수할 수 있습니다. 중요한 것은 숨기려 하지 않고 즉시 재발급하고 기록하는 것입니다.
