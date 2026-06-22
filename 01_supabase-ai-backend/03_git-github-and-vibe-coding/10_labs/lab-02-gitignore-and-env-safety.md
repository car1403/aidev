# Lab 02 - Gitignore And Env Safety

## 목표

이 실습에서는 GitHub에 올리면 안 되는 파일과 `.env.example`의 역할을 이해합니다.

## 1. `.gitignore` 확인

과정 최상위의 `.gitignore` 파일을 확인합니다.

```powershell
cd C:\aidev\01_supabase-ai-backend
Get-Content.gitignore
```

아래 항목이 있는지 확인합니다.

```text
.env
.venv
__pycache__
```

## 2. 예시 환경변수 파일 확인

아래 파일을 엽니다.

```text
03_git-github-and-vibe-coding/10_labs/practice-files/sample.env.example
```

이 파일은 실제 key가 아니라 예시 값만 담고 있습니다.

## 3. 민감정보가 들어가면 안 되는 이유

아래 값을 실제 key처럼 생각해 봅니다.

```text
SUPABASE_SERVICE_ROLE_KEY
UPSTASH_REDIS_REST_TOKEN
GEMINI_API_KEY
OPENAI_API_KEY
```

이 값들이 GitHub에 올라가면 다른 사람이 내 계정 권한이나 비용을 사용할 수 있습니다.

## 4. Codex에게 점검 요청하기

아래 문장으로 Codex에게 점검을 요청해 봅니다.

```text
이 파일에 GitHub에 올리면 안 되는 민감정보가 있는지 확인해 주세요.
.env와.env.example 기준도 함께 설명해 주세요.
```

## 정리 질문

1. `.env`와 `.env.example`은 어떻게 다른가요?
2. `service_role key`는 왜 서버에서만 사용해야 하나요?
3. key가 노출되면 가장 먼저 무엇을 해야 하나요?
