# 03. Git GitHub

이 단원은 Python 기초와 고급 문법을 배운 뒤, 코드 변경 이력을 안전하게 관리하고 GitHub에 공유하는 기본 흐름을 익히는 단계입니다.

Git은 내 PC에서 변경 이력을 관리하는 도구이고, GitHub는 인터넷에 있는 원격 저장소 서비스입니다. 이번 단원에서는 AI 코드 작성보다 Git/GitHub 사용법에 집중합니다. AI 기반 코드 리뷰, 디버깅, 리팩토링은 `90_ai-assisted-code-review-and-debugging`에서 본격적으로 다룹니다.

## 학습 목표

- Git과 GitHub의 차이를 설명할 수 있습니다.
- `git status`, `git diff`, `git add`, `git commit`의 역할을 이해합니다.
- 커밋과 브랜치의 기본 개념을 이해합니다.
- VS Code Source Control 화면에서 변경 파일, diff, stage, commit 흐름을 진행할 수 있습니다.
- VS Code에서 GitHub 계정 로그인, 원격 저장소 연결, Push, Pull, Sync Changes 흐름을 이해합니다.
- GitLens 확장을 설치하고 파일 변경 이력, 커밋 이력, 라인별 변경 정보를 확인할 수 있습니다.
- README와 커밋 메시지를 Git 작업 기준에 맞게 작성할 수 있습니다.
- `.env`, `.venv`, API key, Supabase key 같은 민감정보를 GitHub에 올리면 안 되는 이유를 이해합니다.
- 작업 전 상태 확인, 작업 후 변경 내용 확인, 커밋 전 검토 순서를 습관화합니다.

## 폴더 구성

```text
03_git-github
├─ README.md
├─ 00_references
├─ 10_labs
│  └─ practice-files
└─ 20_assignments
```

## 학습 순서

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
12. 개인 과제 제출
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
git commit -m "docs: update learning note"
git log --oneline
```

## 기본 작업 습관

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

같은 Git 작업을 터미널과 VS Code 화면에서 함께 확인합니다.

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

## VS Code에서 GitHub 연동 흐름

```text
1. VS Code에서 C:\aidev\01_supabase-ai-backend 폴더를 엽니다.
2. 왼쪽 Source Control 아이콘을 클릭합니다.
3. Git 저장소가 없으면 Initialize Repository를 누릅니다.
4. GitHub 계정 로그인이 필요하면 Sign in to GitHub를 누릅니다.
5. 브라우저가 열리면 GitHub 계정으로 로그인하고 VS Code 접근을 허용합니다.
6. 변경 파일을 확인합니다.
7. 커밋 메시지를 작성하고 Commit을 누릅니다.
8. GitHub 원격 저장소가 아직 없으면 Publish Branch를 누릅니다.
9. 이후에는 Sync Changes 또는 Push/Pull로 GitHub와 동기화합니다.
```

이미 `C:\aidev` 전체가 Git 저장소로 관리되고 있을 수 있습니다. 이 경우 `01_supabase-ai-backend` 안에서 새 저장소를 다시 만들지 않고, 현재 열려 있는 폴더가 Git으로 추적되는지 Source Control에서 먼저 확인합니다.

가장 조심해야 할 점은 `.env`, `.venv`, 실제 API key, Supabase service role key, Upstash Redis token을 GitHub에 올리지 않는 것입니다.

## VS Code Git 권장 확장

| 확장 | 설치 이름 | 도움이 되는 이유 |
| --- | --- | --- |
| GitLens | `GitLens - Git supercharged` | 파일별 변경 이력, 커밋 이력, 특정 줄을 누가 언제 수정했는지 확인할 수 있습니다. |
| GitHub Pull Requests | `GitHub Pull Requests and Issues` | VS Code 안에서 GitHub Pull Request와 Issue를 확인할 수 있습니다. 팀 프로젝트 단계에서 유용합니다. |
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

GitLens의 유료 기능이나 계정 로그인 기능은 필수가 아닙니다. 처음에는 무료로 제공되는 파일 이력, 커밋 이력, 변경 정보 확인 기능만 사용합니다.

## 참고 문서

| 문서 | 용도 |
| --- | --- |
| `00_references/git-command-cheatsheet.md` | 자주 쓰는 Git 명령 요약 |
| `00_references/git-github-workflow-guide.md` | 로컬 Git과 GitHub 흐름 설명 |
| `00_references/vscode-source-control-guide.md` | VS Code 안에서 Git을 진행하는 방법 |
| `00_references/commit-message-guide.md` | 좋은 커밋 메시지 작성법 |
| `00_references/gitignore-and-secret-guide.md` | `.env`, API key, 개인정보 보호 기준 |
| `00_references/git-review-checklist.md` | 커밋 전 diff, 보안, 문서 점검 기준 |
| `00_references/readme-writing-template.md` | README 작성 템플릿 |

## 실습

| 실습 | 내용 |
| --- | --- |
| `10_labs/lab-01-status-and-diff.md` | `git status`, `git diff` 확인 |
| `10_labs/lab-01b-vscode-source-control.md` | VS Code Source Control에서 변경 확인, stage, commit, GitHub 연동 흐름 확인 |
| `10_labs/lab-02-gitignore-and-env-safety.md` | `.env`와 `.gitignore` 보안 실습 |
| `10_labs/lab-03-branch-and-commit-message.md` | 브랜치와 커밋 메시지 작성 |
| `10_labs/lab-04-diff-review-checklist.md` | 커밋 전 변경 내용과 보안 기준 점검 |

## 이 단원에서 하지 않는 것

이 단원은 Git/GitHub 기본 사용에 집중합니다.

| 다루지 않는 내용 | 다루는 위치 |
| --- | --- |
| AI 기반 코드 리뷰와 디버깅 | `90_ai-assisted-code-review-and-debugging` |
| AI 기반 코드 개선 흐름 | `90_ai-assisted-code-review-and-debugging` |
| GitHub Actions 기반 CI/CD | `06_multi-agent-service-ops` |
| Docker/AWS 배포 자동화 | `06_multi-agent-service-ops` |

## 단원 완료 기준

이 단원이 끝났을 때 아래 내용을 설명할 수 있어야 합니다.

```text
Git은 내 PC의 변경 이력을 관리한다.
GitHub는 원격 저장소에서 코드를 공유한다.
git status는 현재 상태를 확인한다.
git diff는 실제 변경 내용을 확인한다.
VS Code Source Control에서도 같은 변경 내용을 확인하고 커밋할 수 있다.
.env와 API key는 GitHub에 올리면 안 된다.
커밋 메시지는 무엇을 왜 바꾸었는지 짧게 설명해야 한다.
```

