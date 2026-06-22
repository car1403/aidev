# Git Command Cheatsheet

이 문서는 수업 중 자주 사용하는 Git 명령을 초보자 기준으로 정리한 자료입니다.

## 설치 확인

```powershell
git --version
```

Git이 설치되어 있으면 버전이 출력됩니다.

## 현재 상태 확인

```powershell
git status
```

가장 자주 사용하는 명령입니다. 어떤 파일이 수정되었는지, 어떤 파일이 아직 Git에 추적되지 않는지 확인합니다.

## 변경 내용 확인

```powershell
git diff
```

파일 내용이 어떻게 바뀌었는지 확인합니다. 커밋하기 전에 반드시 확인하는 습관을 들입니다.

## 파일을 커밋 준비 상태로 올리기

```powershell
git add 파일명
git add.
```

`git add 파일명`은 특정 파일만 올립니다.

`git add.`은 현재 폴더 아래의 변경 파일을 한 번에 올립니다. 초보자는 `git status`와 `git diff`를 먼저 확인한 뒤 사용합니다.

## 커밋 만들기

```powershell
git commit -m "docs: update setup guide"
```

커밋은 작업 내용을 하나의 저장 지점으로 남기는 것입니다.

## 최근 커밋 확인

```powershell
git log --oneline -5
```

최근 커밋 5개를 한 줄씩 확인합니다.

## 브랜치 확인

```powershell
git branch
```

현재 어떤 브랜치에서 작업 중인지 확인합니다.

## 새 브랜치 만들고 이동

```powershell
git switch -c practice/readme-update
```

새 기능이나 문서 수정은 별도 브랜치에서 작업하는 습관을 들입니다.

## 원격 저장소 확인

```powershell
git remote -v
```

GitHub 저장소와 연결되어 있는지 확인합니다.

## 수업 중 추천 순서

```text
git status
-> 파일 수정
-> git status
-> git diff
-> git add 파일명
-> git status
-> git commit -m "메시지"
```

