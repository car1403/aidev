# Lab 04. Diff Review Checklist

## 목표

커밋하기 전에 `git diff`를 읽고 변경 내용과 보안 기준을 점검합니다.

이 실습은 AI 코드 리뷰가 아니라 Git 커밋 전 기본 점검 연습입니다. AI 기반 코드 리뷰와 디버깅은 `90_ai-assisted-code-review-and-debugging`에서 따로 다룹니다.

## 1. 변경 내용 확인

아래 명령으로 샘플 파일의 변경 내용을 확인합니다.

```powershell
git diff -- 03_git-github/10_labs/practice-files/learning-log.md
```

## 2. 변경 내용 설명하기

diff를 보고 아래 질문에 답합니다.

```text
1. 어떤 줄이 추가되었나요?
2. 어떤 줄이 삭제되었나요?
3. 변경 목적은 무엇인가요?
4. 커밋 메시지로 어떻게 요약할 수 있나요?
```

## 3. 민감정보 점검

변경 내용에 아래 정보가 포함되어 있지 않은지 확인합니다.

```text
API key
비밀번호
Supabase service role key
Upstash Redis token
실제 .env 값
개인정보 원문
```

## 4. 커밋 대상 정리

변경 내용이 의도한 파일에만 있는지 확인합니다.

```powershell
git status
```

커밋할 파일만 stage합니다.

```powershell
git add 03_git-github/10_labs/practice-files/learning-log.md
```

## 5. 정리 질문

1. `git diff`와 `git status`는 각각 무엇을 확인할 때 사용하나요?
2. 커밋 전에 민감정보를 확인해야 하는 이유는 무엇인가요?
3. 좋은 커밋 메시지는 어떤 정보를 포함해야 하나요?

