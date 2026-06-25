# Git Review Checklist

이 문서는 커밋하기 전에 변경 내용을 점검하는 기준을 정리합니다.

Git은 단순히 파일을 저장하는 도구가 아니라 “어떤 변경을 왜 했는지”를 기록하는 도구입니다. 커밋 전에는 변경 파일, 변경 내용, 민감정보 포함 여부, 커밋 메시지를 차례대로 확인합니다.

## 1. 현재 상태 확인

```powershell
git status
```

확인할 내용:

- 어떤 파일이 수정되었나요?
- 새로 추가된 파일이 있나요?
- 삭제된 파일이 있나요?
- 의도하지 않은 파일이 포함되어 있나요?

## 2. 변경 내용 확인

```powershell
git diff
```

특정 파일만 확인할 수도 있습니다.

```powershell
git diff -- 03_git-github/10_labs/practice-files/learning-log.md
```

확인할 내용:

- 실제로 바뀐 문장이 의도한 내용인가요?
- 불필요한 공백이나 임시 메모가 들어갔나요?
- 파일 전체가 예상하지 않게 바뀌지는 않았나요?

## 3. 민감정보 확인

커밋 전에 아래 값이 들어가지 않았는지 확인합니다.

```text
API key
Supabase service role key
Upstash Redis token
OpenAI API key
Gemini API key
비밀번호
개인정보 원문
.env 파일
.venv 폴더
```

## 4. .gitignore 확인

```powershell
git status --ignored
```

확인할 내용:

- `.env`가 Git 추적 대상에서 제외되어 있나요?
- `.venv`가 Git 추적 대상에서 제외되어 있나요?
- `__pycache__`, `.pyc` 파일이 제외되어 있나요?
- VS Code 개인 설정을 공유하지 않을 계획이라면 `.vscode`가 제외되어 있나요?

## 5. 커밋 메시지 작성 기준

좋은 커밋 메시지는 변경 목적을 짧게 설명합니다.

```text
docs: update GitHub workflow guide
fix: correct Supabase setup path
chore: add gitignore safety notes
```

피하는 메시지:

```text
수정
update
작업함
final
```

## 6. 최종 체크리스트

- [ ] `git status`로 변경 파일을 확인했습니다.
- [ ] `git diff`로 실제 변경 내용을 확인했습니다.
- [ ] 민감정보가 포함되지 않았습니다.
- [ ] `.env`, `.venv`, 임시 파일이 커밋 대상에 없습니다.
- [ ] 커밋 메시지가 변경 목적을 설명합니다.
- [ ] 하나의 커밋에 너무 많은 unrelated 변경이 섞이지 않았습니다.

