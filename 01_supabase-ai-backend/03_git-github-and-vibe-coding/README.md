# 03. Git, GitHub And Vibe Coding

이 단원은 Python 기초와 고급 문법을 배운 뒤, 코드를 저장하고 협업하는 기본 흐름을 익히는 단계입니다.

Git/GitHub는 코드 변경 이력을 관리하고, 팀 프로젝트에서 작업 내용을 공유하기 위한 도구입니다. Codex는 Git 명령을 대신 외우게 하는 도구가 아니라, 변경 내용을 이해하고 커밋 메시지나 문서 초안을 정리하는 데 도움을 주는 학습 파트너로 사용합니다.

## 학습 목표

- Git과 GitHub의 차이를 설명할 수 있습니다.
- `git status`, `git diff`, `git add`, `git commit`의 역할을 이해합니다.
- 커밋과 브랜치의 기본 개념을 이해합니다.
- README, 과제 문서, 커밋 메시지를 AI와 함께 작성하고 검토할 수 있습니다.
- API key, `.env`, 개인정보를 GitHub에 올리면 안 되는 이유를 이해합니다.
- 작업 전 상태 확인, 작업 후 변경 내용 확인, 커밋 전 검토 순서를 습관화합니다.
- Codex에게 질문할 때 코드, 오류, 목적, 현재 상태를 함께 제공하는 방법을 익힙니다.
- VS Code의 Source Control 화면에서 변경 파일, diff, stage, commit 흐름을 진행할 수 있습니다.
- VS Code에서 GitHub 계정에 로그인하고 원격 저장소와 연결하는 흐름을 이해합니다.
- VS Code에서 `Publish Branch`, `Sync Changes`, `Push`, `Pull` 버튼의 의미를 구분합니다.
- GitLens 확장을 설치하고 파일 변경 이력, 커밋 이력, 라인별 변경 정보를 확인할 수 있습니다.

## 권장 구성

```text
03_git-github-and-vibe-coding
├─ README.md
├─ 00_references
├─ 10_labs
│  └─ practice-files
└─ 20_assignments
```

## 수업 진행 순서

이 단원은 아래 순서로 진행합니다.

```text
1. Git과 GitHub 역할 이해
2. 현재 저장소 상태 확인
3. 샘플 파일 수정
4. 터미널에서 git status로 변경 파일 확인
5. 터미널에서 git diff로 변경 내용 확인
6. VS Code Source Control에서 같은 변경 내용을 화면으로 확인
7. VS Code에서 stage, commit, branch 확인
8. VS Code에서 GitHub 로그인과 원격 저장소 연결 흐름 이해
9. GitLens로 파일 변경 이력과 커밋 이력 확인
10. .gitignore와 .env 보안 기준 확인
11. 커밋 메시지 작성 원칙 학습
12. Codex로 diff 설명과 README 개선 요청
13. 개인 과제 제출
```

## 핵심 개념

| 개념 | 초보자용 설명 |
| --- | --- |
| Git | 내 PC에서 코드 변경 이력을 관리하는 도구입니다. |
| GitHub | 인터넷에 있는 코드 저장소 서비스입니다. |
| Commit | 현재 작업 내용을 하나의 저장 지점으로 남기는 것입니다. |
| Branch | 기존 코드에서 새로운 작업 흐름을 따로 만드는 것입니다. |
| Pull Request | 내가 바꾼 내용을 팀에 검토 요청하는 방식입니다. |
| Remote | GitHub에 있는 원격 저장소 주소입니다. 보통 `origin`이라는 이름을 사용합니다. |
| Push | 내 PC의 커밋을 GitHub 원격 저장소로 올리는 작업입니다. |
| Pull | GitHub 원격 저장소의 최신 변경 내용을 내 PC로 가져오는 작업입니다. |
| Sync Changes | VS Code에서 Pull과 Push를 한 번에 처리하는 버튼입니다. |
| `.gitignore` | Git이 추적하지 않아야 할 파일 목록입니다. `.env`, `.venv`, 임시 파일을 제외할 때 사용합니다. |
| Diff | 이전 내용과 지금 내용의 차이를 보여주는 결과입니다. |
| Source Control | VS Code 왼쪽 메뉴에서 Git 변경 상태를 화면으로 확인하고 커밋할 수 있는 기능입니다. |
| GitLens | VS Code에서 Git 변경 이력, 커밋 기록, 라인별 수정 정보를 보기 쉽게 보여주는 확장 프로그램입니다. |

## 기본 명령

```powershell
git --version
git status
git diff
git add .
git commit -m "학습 내용 정리"
```

## 초보자용 Git 작업 습관

Git을 사용할 때는 명령을 외우는 것보다 순서를 익히는 것이 중요합니다.

```text
작업 전
-> git status로 현재 상태 확인

작업 중
-> 파일 수정
-> 작은 단위로 자주 저장

작업 후
-> git status로 변경 파일 확인
-> git diff로 실제 변경 내용 확인

커밋 전
-> 민감정보가 들어가지 않았는지 확인
-> 커밋 메시지를 한 문장으로 정리
```

## 터미널 방식과 VS Code 방식

수업에서는 같은 Git 작업을 두 가지 방식으로 확인합니다.

| 작업 | 터미널 명령 | VS Code 위치 |
| --- | --- | --- |
| 현재 상태 확인 | `git status` | 왼쪽 Source Control 아이콘 |
| 변경 내용 확인 | `git diff` | 변경 파일 클릭 |
| 커밋 준비 | `git add 파일명` | 파일 옆 `+` 버튼 |
| 커밋 작성 | `git commit -m "메시지"` | Message 입력 후 Commit 버튼 |
| 브랜치 확인 | `git branch` | 왼쪽 아래 브랜치 이름 |
| 원격 저장소 확인 | `git remote -v` | Source Control의 Publish Branch / Sync Changes 상태 |
| GitHub로 올리기 | `git push` | Push 또는 Sync Changes 버튼 |
| GitHub 내용 받기 | `git pull` | Pull 또는 Sync Changes 버튼 |

초보자는 먼저 VS Code 화면에서 변경 파일을 눈으로 확인하고, 같은 내용을 터미널 명령으로도 확인하면 이해가 더 쉽습니다.

## VS Code에서 GitHub 연동 흐름

처음 GitHub와 연결할 때는 아래 순서를 따릅니다.

```text
1. VS Code에서 C:\aidev\01_supabase-ai-backend 폴더를 연다.
2. 왼쪽 Source Control 아이콘을 클릭한다.
3. Git 저장소가 없으면 Initialize Repository를 누른다.
4. GitHub 계정 로그인이 필요하면 Sign in to GitHub를 누른다.
5. 브라우저가 열리면 GitHub 계정으로 로그인하고 VS Code 접근을 허용한다.
6. 변경 파일을 확인한다.
7. 커밋 메시지를 작성하고 Commit을 누른다.
8. GitHub 원격 저장소가 아직 없으면 Publish Branch를 누른다.
9. 이후에는 Sync Changes 또는 Push/Pull로 GitHub와 동기화한다.
```

수업에서는 이미 `C:\aidev` 전체가 Git 저장소로 관리되고 있을 수 있습니다. 이 경우 `01_supabase-ai-backend` 안에서 새 저장소를 다시 만들지 않고, 현재 열려 있는 폴더가 Git으로 추적되는지 Source Control에서 먼저 확인합니다.

초보자가 가장 조심해야 할 점은 `.env`, `.venv`, 실제 API key, Supabase service role key, Upstash Redis token을 GitHub에 올리지 않는 것입니다.

## VS Code Git 실습 권장 확장

이 단원에서는 VS Code 기본 Source Control 기능만으로도 Git 실습을 진행할 수 있습니다. 다만 변경 이력을 더 쉽게 보고 싶다면 아래 확장을 함께 설치하는 것을 권장합니다.

| 확장 | 설치 이름 | 초보자에게 도움이 되는 이유 |
| --- | --- | --- |
| GitLens | `GitLens - Git supercharged` | 파일별 변경 이력, 커밋 이력, 특정 줄을 누가 언제 수정했는지 확인할 수 있습니다. |
| GitHub Pull Requests | `GitHub Pull Requests and Issues` | VS Code 안에서 GitHub Pull Request와 Issue를 확인할 수 있습니다. 팀 프로젝트 단계에서 유용합니다. |
| Error Lens | `Error Lens` | 코드 오류나 경고를 줄 옆에 바로 보여줍니다. Git 실습보다는 Python 코드 작성 단계에서 도움이 됩니다. |
| Material Icon Theme | `Material Icon Theme` | 파일 종류별 아이콘을 보기 좋게 표시해 폴더 구조를 파악하기 쉽습니다. |

GitLens 설치 방법:

```text
1. VS Code 왼쪽 Extensions 아이콘을 클릭합니다.
2. 검색창에 GitLens를 입력합니다.
3. GitLens - Git supercharged를 선택합니다.
4. Install을 클릭합니다.
5. 설치 후 VS Code를 다시 로드하라는 안내가 나오면 Reload를 누릅니다.
```

터미널로 설치할 수도 있습니다.

```powershell
code --install-extension eamodio.gitlens
```

GitLens의 유료 기능이나 계정 로그인 기능은 이 수업에서 필수가 아닙니다. 처음에는 무료로 제공되는 파일 이력, 커밋 이력, 변경 정보 확인 기능만 사용합니다.

## 수업 중 사용할 참고 문서

| 문서 | 용도 |
| --- | --- |
| `00_references/git-command-cheatsheet.md` | 자주 쓰는 Git 명령 요약 |
| `00_references/git-github-workflow-guide.md` | 로컬 Git과 GitHub 흐름 설명 |
| `00_references/vscode-source-control-guide.md` | VS Code 안에서 Git을 진행하는 방법 |
| `00_references/commit-message-guide.md` | 좋은 커밋 메시지 작성법 |
| `00_references/gitignore-and-secret-guide.md` | `.env`, API key, 개인정보 보호 기준 |
| `00_references/codex-git-prompt-examples.md` | Codex에게 Git/diff/문서 검토를 요청하는 예시 |
| `00_references/readme-writing-template.md` | README 작성 템플릿 |

## 수업 중 실습

| 실습 | 내용 |
| --- | --- |
| `10_labs/lab-01-status-and-diff.md` | `git status`, `git diff` 확인 |
| `10_labs/lab-01b-vscode-source-control.md` | VS Code Source Control에서 변경 확인, stage, commit, GitHub 연동 흐름 확인 |
| `10_labs/lab-02-gitignore-and-env-safety.md` | `.env`와 `.gitignore` 보안 실습 |
| `10_labs/lab-03-branch-and-commit-message.md` | 브랜치와 커밋 메시지 작성 |
| `10_labs/lab-04-codex-diff-review.md` | Codex로 변경 내용 설명과 문서 개선 요청 |

## Codex 활용 예시

```text
방금 수정한 README 내용을 보고 커밋 메시지 후보를 3개 작성해 주세요.
이 git diff를 초보자에게 설명해 주세요.
이 README가 수업용 수업 문서로 충분한지 검토해 주세요.
이 변경 내용에 민감정보가 포함되어 있는지 점검해 주세요.
이 과제 설명을 수업 참여자가 이해하기 쉽게 다시 작성해 주세요.
```

## 이 단원에서 하지 않는 것

GitHub Actions 기반 CI/CD, 자동 배포, AWS 배포는 `06_multi-agent-service-ops`에서 다룹니다.

## 단원 완료 기준

수업 참여자는 이 단원이 끝났을 때 아래 내용을 스스로 설명할 수 있어야 합니다.

```text
Git은 내 PC의 변경 이력을 관리한다.
GitHub는 원격 저장소에서 코드를 공유한다.
git status는 현재 상태를 확인한다.
git diff는 실제 변경 내용을 확인한다.
VS Code Source Control에서도 같은 변경 내용을 확인하고 커밋할 수 있다.
.env와 API key는 GitHub에 올리면 안 된다.
커밋 메시지는 무엇을 왜 바꾸었는지 짧게 설명해야 한다.
Codex는 변경 내용을 이해하고 문서화하는 보조 도구로 사용할 수 있다.
```
