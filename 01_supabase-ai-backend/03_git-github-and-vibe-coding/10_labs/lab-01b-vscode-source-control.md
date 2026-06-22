# Lab 01b - VS Code Source Control

## 목표

이 실습에서는 VS Code 안에서 Git 변경 내용을 확인하고, stage, commit, GitHub 연동 흐름을 익힙니다.

터미널 명령으로는 `git status`, `git diff`, `git add`, `git commit`을 사용하지만, VS Code에서는 Source Control 화면으로 같은 작업을 확인할 수 있습니다.

## 1. VS Code에서 과정 폴더 열기

PowerShell에서 실행합니다.

```powershell
code C:\aidev\01_supabase-ai-backend
```

`code` 명령이 되지 않으면 VS Code를 직접 실행합니다.

```text
File
-> Open Folder
-> C:\aidev\01_supabase-ai-backend 선택
```

## 2. Source Control 열기

VS Code 왼쪽의 Source Control 아이콘을 클릭합니다.

단축키:

```text
Ctrl + Shift + G
```

## 3. 실습 파일 수정

아래 파일을 엽니다.

```text
03_git-github-and-vibe-coding/10_labs/practice-files/learning-log.md
```

`## 실습 메모` 아래에 한 줄을 추가합니다.

예시:

```text
- VS Code Source Control에서 변경 파일을 확인했습니다.
```

## 4. 변경 파일 확인

Source Control 화면에 `learning-log.md`가 나타나는지 확인합니다.

파일 이름을 클릭하면 변경 전/후 내용이 나란히 보입니다.

확인할 것:

```text
추가한 줄이 초록색으로 보이는가?
수정한 파일 이름이 Source Control에 보이는가?
터미널의 git diff와 같은 내용을 보여주는가?
```

## 5. Stage 실습

파일 오른쪽의 `+` 버튼을 누릅니다.

그러면 파일이 `Staged Changes` 영역으로 이동합니다.

이 작업은 터미널의 아래 명령과 같은 의미입니다.

```powershell
git add 03_git-github-and-vibe-coding/10_labs/practice-files/learning-log.md
```

## 6. 커밋 메시지 작성 연습

Source Control 상단 메시지 입력 칸에 아래 메시지를 적어 봅니다.

```text
docs: update Git learning log
```

수업 상황에 따라 실제 Commit 버튼은 누르지 않을 수 있습니다. 수업 안내에 따라 진행합니다.

Commit 버튼을 누르면 내 PC의 Git 저장소에 변경 이력이 저장됩니다.
아직 GitHub에 올라간 것은 아닙니다.

## 7. Commit 이후 GitHub 연동 확인

커밋 후 Source Control 화면에 아래 버튼 중 하나가 보일 수 있습니다.

| 버튼 | 의미 |
| --- | --- |
| Publish Branch | 현재 브랜치를 GitHub에 처음 올릴 수 있습니다. |
| Push | 내 PC의 커밋을 GitHub에 올립니다. |
| Sync Changes | GitHub에서 받고, 내 커밋도 올리는 동기화 버튼입니다. |
| Pull | GitHub의 최신 변경 내용을 내 PC로 가져옵니다. |

처음 GitHub에 올리는 실습이라면 `Publish Branch`가 보일 수 있습니다.
이미 원격 저장소가 연결되어 있으면 `Sync Changes` 또는 `Push`가 보일 수 있습니다.

## 8. VS Code에서 GitHub 로그인

GitHub 로그인이 필요하면 VS Code가 브라우저를 열어 로그인 화면을 보여줍니다.

진행 순서:

```text
1. Sign in to GitHub 클릭
2. 브라우저에서 GitHub 로그인
3. Visual Studio Code 권한 허용
4. VS Code로 돌아오기
5. Source Control에서 Push 또는 Sync Changes 다시 확인
```

로그인 후에도 `.env`, `.venv`, API key가 GitHub에 올라가지 않는지 반드시 확인합니다.

## 9. GitHub에 올리기 전 보안 점검

Source Control의 Staged Changes에 아래 파일이 들어가 있으면 안 됩니다.

```text
.env
.venv 폴더
__pycache__ 폴더
실제 API key가 적힌 파일
Supabase service role key가 들어간 문서
Upstash Redis token이 들어간 문서
```

커밋 전에 `.gitignore`가 있는지 확인합니다.

```text
C:\aidev\01_supabase-ai-backend\.gitignore
```

## 10. 터미널로 같은 상태 확인

PowerShell에서 확인합니다.

```powershell
cd C:\aidev\01_supabase-ai-backend
git status
```

VS Code에서 stage한 파일이 터미널에서도 stage 상태로 보이는지 확인합니다.

원격 저장소 연결 여부도 확인합니다.

```powershell
git remote -v
```

출력이 없으면 아직 GitHub 저장소와 연결되지 않은 상태입니다.
출력이 있다면 `origin` 주소가 GitHub 저장소 주소인지 확인합니다.

## 11. GitLens로 변경 이력 확인

이번 단계는 선택 실습입니다. GitLens가 설치되어 있으면 진행하고, 설치되어 있지 않으면 수업 안내에 따라 건너뛰어도 됩니다.

### 11-1. GitLens 설치 확인

VS Code에서 Extensions 화면을 엽니다.

```text
Ctrl + Shift + X
```

검색창에 아래 이름을 입력합니다.

```text
GitLens
```

`GitLens - Git supercharged`가 설치되어 있으면 그대로 진행합니다. 설치되어 있지 않다면 Install을 클릭합니다.

터미널로 설치하려면 아래 명령을 사용할 수도 있습니다.

```powershell
code --install-extension eamodio.gitlens
```

### 11-2. 파일 이력 확인

`learning-log.md` 파일을 열고 아래 순서로 확인합니다.

```text
1. 파일 편집 화면에서 마우스 오른쪽 버튼을 클릭합니다.
2. GitLens 메뉴를 찾습니다.
3. Open File History 또는 Show File History를 클릭합니다.
4. 현재 파일에 어떤 커밋 이력이 있는지 확인합니다.
```

명령 팔레트를 사용할 수도 있습니다.

```text
Ctrl + Shift + P
-> GitLens: Open File History
```

### 11-3. 확인할 내용

GitLens 화면에서 아래 내용을 찾아봅니다.

```text
방금 만든 커밋 메시지가 보이는가?
커밋에 포함된 파일 이름이 보이는가?
파일의 어느 부분이 변경되었는지 확인할 수 있는가?
특정 줄을 클릭했을 때 마지막 변경 정보가 보이는가?
```

GitLens는 Git을 대신 수행하는 도구가 아니라 Git 이력을 보기 쉽게 도와주는 도구입니다. 커밋 전 보안 점검과 push는 여전히 직접 확인해야 합니다.

## 정리 질문

1. VS Code Source Control은 터미널의 어떤 Git 명령과 비슷한가요?
2. 파일 옆 `+` 버튼은 어떤 명령과 같은 의미인가요?
3. 커밋 전 파일을 클릭해서 diff를 확인해야 하는 이유는 무엇인가요?
4. Commit과 Push는 무엇이 다른가요?
5. Publish Branch와 Sync Changes는 언제 보이나요?
6. GitHub에 올리면 안 되는 파일은 무엇인가요?
7. GitLens로 확인할 수 있는 Git 정보는 무엇인가요?
