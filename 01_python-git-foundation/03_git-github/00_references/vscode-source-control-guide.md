# VS Code Source Control Guide

이 문서는 VS Code 안에서 Git을 진행하는 방법을 설명합니다.

터미널 명령을 외우기 어렵더라도 VS Code의 Source Control 화면을 사용하면 변경 파일, 변경 내용, 커밋 준비 상태를 눈으로 확인할 수 있습니다.

이 문서에서는 아래 흐름을 순서대로 다룹니다.

```text
VS Code에서 폴더 열기
-> Source Control 확인
-> 변경 파일 확인
-> Stage
-> Commit
-> GitHub 로그인
-> Publish Branch 또는 Push
-> Pull / Sync Changes
```

## 1. VS Code에서 폴더 열기

PowerShell에서 다음 명령을 실행합니다.

```powershell
code C:\aidev\01_python-git-foundation
```

`code` 명령이 동작하지 않으면 VS Code를 직접 실행한 뒤 아래 메뉴를 사용합니다.

```text
File
-> Open Folder
-> C:\aidev\01_python-git-foundation 선택
```

중요한 점은 파일 하나만 여는 것이 아니라 과정 폴더 전체를 열어야 한다는 것입니다.

잘못 연 예시:

```text
C:\aidev\01_python-git-foundation\README.md 파일 하나만 열기
```

올바르게 연 예시:

```text
C:\aidev\01_python-git-foundation 폴더 전체 열기
```

폴더 전체를 열어야 VS Code가 `.gitignore`, `requirements.txt`, 하위 실습 폴더, Git 변경 상태를 함께 이해할 수 있습니다.

## 2. Source Control 화면 열기

VS Code 왼쪽 메뉴에서 가지 모양 아이콘을 클릭합니다.

```text
Source Control
```

단축키:

```text
Ctrl + Shift + G
```

이 화면에서 Git이 추적하는 변경 파일 목록을 볼 수 있습니다.

Source Control 화면에 보일 수 있는 대표 문구는 다음과 같습니다.

| 화면 문구 | 의미 | 초보자 행동 |
| --- | --- | --- |
| No changes | 아직 수정된 파일이 없거나 모두 커밋된 상태입니다. | 실습 파일을 수정한 뒤 다시 확인합니다. |
| Changes | 수정되었지만 아직 stage하지 않은 파일 목록입니다. | 파일을 클릭해 diff를 봅니다. |
| Staged Changes | 다음 커밋에 포함하기로 선택한 파일 목록입니다. | 커밋 메시지를 작성합니다. |
| Initialize Repository | 현재 폴더가 Git 저장소가 아닙니다. | 진행 안내 후 누릅니다. |
| Publish Branch | 현재 브랜치를 GitHub에 처음 올릴 수 있습니다. | 커밋 후 원격 저장소를 만들 때 사용합니다. |
| Sync Changes | GitHub와 내 PC의 변경 내용을 동기화합니다. | Pull/Push가 필요한지 확인 후 사용합니다. |

## 3. 변경 파일 확인

파일을 수정하면 Source Control 화면에 파일 이름이 나타납니다.

파일 이름을 클릭하면 왼쪽에는 이전 내용, 오른쪽에는 현재 내용이 보입니다.

```text
왼쪽: 이전 파일 내용
오른쪽: 수정한 파일 내용
초록색: 추가된 줄
빨간색: 삭제된 줄
```

터미널의 `git diff`를 화면으로 보는 것과 비슷합니다.

## 4. Stage Changes

커밋에 포함할 파일을 선택하는 과정을 stage라고 합니다.

VS Code에서는 파일 이름 오른쪽의 `+` 버튼을 누르면 stage 됩니다.

```text
Changes
-> 파일 오른쪽 + 클릭
-> Staged Changes로 이동
```

터미널 명령으로는 아래와 같은 의미입니다.

```powershell
git add 파일명
```

## 5. Commit Message 작성

Source Control 상단의 메시지 입력 칸에 커밋 메시지를 작성합니다.

예시:

```text
docs: add Git learning notes
```

그 다음 Commit 버튼을 누릅니다.

터미널 명령으로는 아래와 같은 의미입니다.

```powershell
git commit -m "docs: add Git learning notes"
```

## 6. VS Code에서 GitHub 로그인

GitHub에 코드를 올리려면 VS Code가 GitHub 계정에 접근할 수 있어야 합니다.

VS Code에서 GitHub 로그인이 필요한 순간은 보통 아래 상황입니다.

```text
Publish Branch를 누를 때
GitHub 저장소를 clone할 때
GitHub Pull Request 확장을 사용할 때
원격 저장소로 push할 때 인증이 필요한 경우
```

로그인 순서:

```text
1. VS Code 왼쪽 아래 Accounts 아이콘을 클릭합니다.
2. Sign in to Sync Settings 또는 Sign in with GitHub가 보이면 클릭합니다.
3. 브라우저가 열리면 GitHub 계정으로 로그인합니다.
4. Visual Studio Code 권한 요청 화면에서 Authorize를 누릅니다.
5. 브라우저에서 VS Code로 돌아가라는 메시지가 나오면 허용합니다.
6. VS Code 왼쪽 아래 Accounts 아이콘에 GitHub 계정이 보이는지 확인합니다.
```

초보자가 알아야 할 점:

```text
VS Code 로그인은 GitHub에 push하기 위한 인증입니다.
Git 커밋은 내 PC에서도 만들 수 있습니다.
GitHub 로그인 전에도 git status, diff, commit은 가능합니다.
GitHub에 올리는 push는 로그인 또는 인증이 필요합니다.
```

## 7. VS Code에서 원격 저장소 연결

원격 저장소는 GitHub에 있는 저장소 주소입니다.
보통 `origin`이라는 이름으로 연결됩니다.

### 경우 1. 이미 GitHub 저장소가 연결되어 있는 경우

Source Control 화면에 `Sync Changes`, `Push`, `Pull` 같은 버튼이 보일 수 있습니다.
이 경우 이미 원격 저장소와 연결되어 있을 가능성이 큽니다.

터미널에서 확인하려면 아래 명령을 사용합니다.

```powershell
git remote -v
```

출력 예시:

```text
origin https://github.com/사용자명/저장소명.git (fetch)
origin https://github.com/사용자명/저장소명.git (push)
```

### 경우 2. 아직 GitHub 저장소가 없는 경우

커밋을 만든 뒤 VS Code에서 `Publish Branch` 버튼을 누를 수 있습니다.

```text
Source Control
-> Commit 작성
-> Publish Branch
-> Public 또는 Private 선택
-> GitHub 저장소 생성
```

초보자 이 과정에서는 보통 `Private` 저장소를 권장합니다.
API key나 개인 실습 기록이 실수로 올라갈 위험을 줄이기 위해서입니다.

### 경우 3. GitHub에서 만든 저장소를 현재 폴더와 연결하는 경우

GitHub에서 저장소를 먼저 만들었다면 터미널에서 원격 주소를 연결할 수 있습니다.

```powershell
git remote add origin https://github.com/사용자명/저장소명.git
git push -u origin main
```

VS Code에서는 이후부터 `Sync Changes`로 동기화할 수 있습니다.

## 8. VS Code에서 Push, Pull, Sync 이해

| 버튼 | 의미 | 언제 사용하나요? |
| --- | --- | --- |
| Push | 내 PC의 커밋을 GitHub에 올립니다. | 내가 커밋한 내용을 원격 저장소에 공유할 때 |
| Pull | GitHub의 최신 커밋을 내 PC로 가져옵니다. | 다른 사람이 올린 변경 내용을 받을 때 |
| Sync Changes | Pull과 Push를 함께 처리합니다. | 혼자 실습할 때 간단히 동기화할 때 |
| Publish Branch | 현재 브랜치를 GitHub에 처음 올립니다. | 새 브랜치나 새 저장소를 처음 공유할 때 |

실습 중에는 아래 순서를 권장합니다.

```text
1. 커밋 전 diff 확인
2. 커밋 생성
3. Pull 또는 Sync로 원격 변경 확인
4. Push 또는 Sync로 내 커밋 업로드
```

팀 프로젝트에서는 무작정 Sync를 누르기보다, 먼저 현재 변경 내용과 브랜치를 확인합니다.

## 9. VS Code에서 브랜치 확인

VS Code 왼쪽 아래에 현재 브랜치 이름이 표시됩니다.

예시:

```text
main
practice/git-notes
```

브랜치 이름을 클릭하면 브랜치를 바꾸거나 새 브랜치를 만들 수 있습니다.

초보자는 실습 중 진행 안내 없이 브랜치를 무리하게 바꾸지 않습니다.

새 브랜치를 만들 때는 작업 내용을 짧게 표현합니다.

예시:

```text
docs/git-vscode-guide
feature/supabase-log-api
fix/env-example
```

VS Code에서 브랜치를 만드는 흐름:

```text
왼쪽 아래 브랜치 이름 클릭
-> Create new branch
-> 브랜치 이름 입력
-> Enter
```

## 10. 터미널과 VS Code 비교

| 작업 | 터미널 | VS Code |
| --- | --- | --- |
| 상태 확인 | `git status` | Source Control 파일 목록 |
| 변경 내용 확인 | `git diff` | 변경 파일 클릭 |
| stage | `git add 파일명` | 파일 옆 `+` 버튼 |
| commit | `git commit -m "메시지"` | 메시지 입력 후 Commit |
| branch 확인 | `git branch` | 왼쪽 아래 브랜치 이름 |
| remote 확인 | `git remote -v` | Publish/Sync 버튼 상태 확인 |
| push | `git push` | Push 또는 Sync Changes |
| pull | `git pull` | Pull 또는 Sync Changes |

## 11. 커밋 전 체크리스트

커밋 버튼을 누르기 전에 아래를 확인합니다.

```text
.env 파일이 포함되어 있지 않은가?
.venv 폴더가 포함되어 있지 않은가?
실제 API key나 token이 문서에 들어가지 않았는가?
Supabase service role key가 들어가지 않았는가?
Gemini API key, OpenAI API key, Upstash Redis token이 들어가지 않았는가?
변경 파일을 클릭해서 diff를 확인했는가?
커밋 메시지가 무엇을 바꿨는지 설명하는가?
```

## 12. GitLens 설치와 활용

GitLens는 VS Code에서 Git 변경 이력을 더 쉽게 볼 수 있게 해 주는 확장 프로그램입니다.

VS Code의 기본 Source Control만으로도 stage, commit, push, pull을 할 수 있습니다. GitLens는 여기에 파일별 변경 이력, 커밋 상세 정보, 특정 줄을 누가 언제 수정했는지 확인하는 기능을 추가해 줍니다.

### 설치 방법

VS Code 화면에서 설치합니다.

```text
1. 왼쪽 Extensions 아이콘을 클릭합니다.
2. 검색창에 GitLens를 입력합니다.
3. GitLens - Git supercharged를 선택합니다.
4. Install을 클릭합니다.
```

터미널에서 설치할 수도 있습니다.

```powershell
code --install-extension eamodio.gitlens
```

설치 후 VS Code가 다시 로드되면 왼쪽 메뉴나 Source Control 주변에 GitLens 관련 메뉴가 보일 수 있습니다.

### 과정에서 사용할 GitLens 기능

처음에는 아래 기능만 사용합니다.

| 기능 | 초보자용 설명 | 언제 사용하나요? |
| --- | --- | --- |
| Current Line Blame | 현재 커서가 있는 줄을 마지막으로 수정한 커밋 정보를 보여줍니다. | 특정 줄이 언제 바뀌었는지 확인할 때 |
| File History | 현재 파일의 변경 이력을 보여줍니다. | README나 Python 파일이 어떻게 바뀌었는지 확인할 때 |
| Commit Details | 커밋 하나에 포함된 변경 파일과 메시지를 보여줍니다. | 커밋 내용을 복습하거나 코드 리뷰할 때 |
| Compare with Previous | 이전 버전과 현재 파일을 비교합니다. | 내가 무엇을 바꿨는지 다시 확인할 때 |

### 파일 변경 이력 확인 흐름

예를 들어 `learning-log.md` 파일의 변경 이력을 확인하려면 아래 순서로 진행합니다.

```text
1. learning-log.md 파일을 엽니다.
2. 파일 편집 화면에서 마우스 오른쪽 버튼을 클릭합니다.
3. GitLens 메뉴를 찾습니다.
4. Open File History 또는 Show File History를 선택합니다.
5. 커밋 목록을 클릭해 어떤 변경이 있었는지 확인합니다.
```

명령 팔레트에서도 실행할 수 있습니다.

```text
Ctrl + Shift + P
-> GitLens: Open File History
```

### 라인별 변경 정보 확인

파일 안의 특정 줄을 클릭하면 GitLens가 해당 줄의 마지막 변경 정보를 보여줄 수 있습니다.

확인할 내용:

```text
어떤 커밋에서 바뀌었는가?
커밋 메시지는 무엇인가?
언제 바뀌었는가?
어떤 파일 변경과 함께 커밋되었는가?
```

이 기능은 "왜 이 코드가 이렇게 되어 있지?"라는 질문이 생겼을 때 유용합니다.

### GitLens 사용 시 주의할 점

GitLens는 Git 이력을 보기 쉽게 해 주는 도구입니다. 코드를 자동으로 저장하거나 GitHub에 올리는 도구가 아닙니다.

```text
GitLens로 이력을 본다.
Source Control로 변경 파일을 확인한다.
직접 커밋 메시지를 작성한다.
민감정보가 없는지 확인한 뒤 push한다.
```

또한 GitLens가 보여주는 이력 안에 `.env`, API key, token이 보인다면 이미 과거 커밋에 민감정보가 들어갔을 가능성이 있습니다. 이 경우 혼자 push하지 말고 진행 중인 상황을 바로 공유해야 합니다.

## 13. 자주 만나는 상황

### Source Control에 파일이 너무 많이 보이는 경우

`.venv`, `__pycache__`, 임시 파일이 보인다면 `.gitignore` 설정을 확인합니다.

### Commit 버튼이 비활성화된 경우

커밋 메시지를 입력했는지 확인합니다. VS Code 설정에 따라 stage된 파일이 필요할 수도 있습니다.

### Git 저장소가 아니라고 나오는 경우

VS Code에서 잘못된 폴더를 열었을 수 있습니다. `C:\aidev\01_python-git-foundation` 폴더를 열었는지 확인합니다.

### Publish Branch가 보이지 않는 경우

이미 원격 저장소가 연결되어 있거나, 아직 커밋이 없을 수 있습니다.

확인 순서:

```powershell
git status
git log --oneline -3
git remote -v
```

### GitHub 로그인이 계속 실패하는 경우

브라우저에 다른 GitHub 계정이 로그인되어 있을 수 있습니다.

확인할 것:

```text
브라우저에서 GitHub 계정이 맞는가?
VS Code Accounts에 로그인된 계정이 맞는가?
회사/학교 네트워크에서 GitHub 접근이 막혀 있지 않은가?
```

### Push가 거절되는 경우

GitHub에 내 PC에 없는 최신 커밋이 있을 수 있습니다.

초보자는 바로 강제로 push하지 않습니다.

먼저 아래 순서로 확인합니다.

```text
1. Source Control에서 변경 파일 확인
2. 터미널에서 git status 확인
3. Pull 또는 Sync Changes로 원격 변경을 가져올 수 있는지 확인
4. 충돌이 나면 진행 중인 화면을 함께 확인하고 해결
```

## 14. 과정 권장 방식

처음에는 아래 순서로 진행합니다.

```text
1. VS Code Source Control에서 변경 파일 확인
2. 변경 파일 클릭해서 diff 확인
3. 터미널에서 git status 실행
4. 터미널에서 git diff 실행
5. 두 결과가 같은 내용을 보여준다는 점 이해
6. 커밋 메시지 작성
7. Commit 실행
8. GitHub 연결 상태 확인
9. Push 또는 Sync Changes 실행
```

## 15. 실습용 전체 실습 흐름

아래 흐름은 VS Code 화면 중심으로 진행하는 전체 GitHub 연동 실습입니다.

```text
1. C:\aidev\01_python-git-foundation 폴더를 VS Code로 연다.
2. Source Control을 연다.
3. practice-files/learning-log.md를 수정한다.
4. Source Control에서 변경 파일을 클릭해 diff를 본다.
5. GitLens가 설치되어 있다면 Open File History로 파일 변경 이력을 확인한다.
6. 파일 옆 + 버튼으로 stage한다.
7. 메시지 입력 칸에 docs: update Git learning log를 작성한다.
8. Commit을 누른다.
9. 왼쪽 아래 브랜치 이름을 확인한다.
10. Publish Branch 또는 Sync Changes 버튼이 보이는지 확인한다.
11. GitHub 로그인이 필요하면 로그인한다.
12. Push 또는 Sync Changes로 GitHub에 올린다.
13. GitHub 웹사이트에서 커밋이 올라갔는지 확인한다.
```

