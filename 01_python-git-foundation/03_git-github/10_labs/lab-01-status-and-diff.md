# Lab 01 - Git Status And Diff

## 목표

이 실습에서는 파일을 수정한 뒤 Git이 변경 내용을 어떻게 보여주는지 확인합니다.

## 1. 작업 위치로 이동

```powershell
cd C:\aidev\01_python-git-foundation
```

## 2. 현재 상태 확인

```powershell
git status
```

처음에는 변경된 파일이 많을 수도 있고 없을 수도 있습니다. 중요한 것은 결과를 읽는 연습입니다.

## 3. 실습 파일 열기

아래 파일을 VS Code에서 엽니다.

```text
03_git-github/10_labs/practice-files/learning-log.md
```

오늘 배운 내용을 한 줄 추가합니다.

## 4. 다시 상태 확인

```powershell
git status
```

방금 수정한 파일이 보이는지 확인합니다.

## 5. 변경 내용 확인

```powershell
git diff -- 03_git-github/10_labs/practice-files/learning-log.md
```

`+`로 시작하는 줄은 새로 추가된 내용입니다.

`-`로 시작하는 줄은 삭제된 내용입니다.

## 정리 질문

1. `git status`는 무엇을 보여주나요?
2. `git diff`는 무엇을 보여주나요?
3. 커밋 전에 `git diff`를 확인해야 하는 이유는 무엇인가요?


