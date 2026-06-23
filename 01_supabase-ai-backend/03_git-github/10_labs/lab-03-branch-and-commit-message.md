# Lab 03 - Branch And Commit Message

## 목표

이 실습에서는 브랜치 개념과 커밋 메시지 작성법을 익힙니다.

실제 커밋은 진행 안내에 따라 진행합니다. 실습 환경에 따라 저장소 상태가 다를 수 있으므로, 먼저 `git status`를 확인합니다.

## 1. 현재 브랜치 확인

```powershell
cd C:\aidev\01_supabase-ai-backend
git branch
```

`*` 표시가 있는 줄이 현재 브랜치입니다.

## 2. 실습용 브랜치 이름 생각하기

브랜치 이름은 작업 내용을 짧게 표현합니다.

예시:

```text
practice/git-readme-notes
practice/secret-safety-guide
docs/git-lab-update
```

## 3. 변경 내용 확인

```powershell
git status
git diff
```

변경 내용을 확인한 뒤 커밋 메시지를 작성합니다.

## 4. 커밋 메시지 후보 작성

아래 형식으로 3개를 작성합니다.

```text
docs: update Git learning log
docs: add secret safety notes
chore: practice Git status and diff
```

## 5. 커밋 메시지 점검

```text
1. 메시지가 변경 내용을 설명하나요?
2. type이 적절한가요?
3. 나중에 다시 봐도 어떤 작업인지 이해할 수 있나요?
4. 하나의 커밋에 여러 주제가 섞이지 않았나요?
```

## 정리 질문

1. 브랜치는 왜 사용하나요?
2. 좋은 커밋 메시지는 어떤 특징이 있나요?
3. `docs`, `feat`, `fix`는 각각 언제 사용하나요?


