# Lab 04 - Codex Diff Review

## 목표

이 실습에서는 Git 변경 내용을 Codex와 함께 읽고, 문서 개선과 보안 점검을 요청합니다.

## 1. 변경 내용 확인

```powershell
cd C:\aidev\01_supabase-ai-backend
git diff
```

변경 내용이 길면 특정 파일만 확인할 수 있습니다.

```powershell
git diff -- 03_git-github-and-vibe-coding/10_labs/practice-files/learning-log.md
```

## 2. Codex에게 변경 내용 설명 요청

아래처럼 요청합니다.

```text
이 git diff를 초보자에게 설명하듯이 정리해 주세요.
추가된 내용, 삭제된 내용, 주의할 점을 나누어 설명해 주세요.
```

## 3. Codex에게 보안 점검 요청

```text
이 변경 내용에 API key, token, password 같은 민감정보가 포함되어 있는지 확인해 주세요.
.env, .env.example, service role key 기준도 함께 점검해 주세요.
```

## 4. Codex에게 README 개선 요청

```text
이 README가 학생들이 수업 중 따라 보기 충분한지 검토해 주세요.
부족한 실행 순서, 주의사항, 초보자 설명을 보강해 주세요.
```

## 정리 질문

1. Codex가 잘 답하게 하려면 어떤 정보를 함께 줘야 하나요?
2. AI가 제안한 내용을 그대로 반영하면 안 되는 이유는 무엇인가요?
3. 문서 개선 요청과 코드 디버깅 요청은 어떻게 다르게 작성해야 하나요?

