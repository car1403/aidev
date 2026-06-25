# 02. 환경 변수와 key 보안

환경 변수는 코드에 직접 쓰면 안 되는 값을 따로 보관하는 방식입니다.

API key, 데이터베이스 주소, 서비스 비밀번호처럼 외부에 공개되면 안 되는 값은 `.env` 파일에 저장합니다.

## .env와 .env.example 차이

```text
.env
-> 실제 실행에 사용하는 비밀 값
-> GitHub에 올리지 않습니다.

.env.example
-> 어떤 환경 변수가 필요한지 알려주는 예시 파일
-> 실제 key는 넣지 않습니다.
-> GitHub에 올려도 됩니다.
```

## 좋은 예시

```env
SUPABASE_URL=https://your-project-id.supabase.co
SUPABASE_ANON_KEY=replace-with-your-anon-key
SUPABASE_SERVICE_ROLE_KEY=replace-with-your-service-role-key
GEMINI_API_KEY=replace-with-your-gemini-api-key
```

## 나쁜 예시

```env
SUPABASE_SERVICE_ROLE_KEY=실제-service-role-key-값
```

실제 key가 들어간 `.env.example`을 GitHub에 올리면 key가 노출됩니다.

## 백엔드와 프론트엔드 key 기준

```text
FastAPI backend
-> service role key 사용 가능
-> 서버에서만 실행되기 때문입니다.

Streamlit frontend
-> 가능하면 FastAPI API만 호출
-> service role key를 직접 넣지 않습니다.
```

## 실습 전 확인

PowerShell에서 아래 명령으로 `.env`가 있는지 확인합니다.

```powershell
cd C:\aidev\04_supabase-ai-mini-project
dir .env
```

Git 추적 여부는 아래 명령으로 확인합니다.

```powershell
git status --short
```

`.env`가 보이면 안 됩니다. `.env.example`만 보여야 합니다.
