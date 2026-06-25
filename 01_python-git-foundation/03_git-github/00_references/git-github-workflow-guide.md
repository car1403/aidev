# Git And GitHub Workflow Guide

Git과 GitHub는 이름이 비슷하지만 역할이 다릅니다.

## Git

Git은 내 컴퓨터에서 코드 변경 이력을 관리하는 도구입니다.

예를 들어 README를 수정했을 때 Git은 아래 내용을 추적할 수 있습니다.

```text
어떤 파일이 바뀌었는가?
어떤 줄이 추가되었는가?
어떤 줄이 삭제되었는가?
누가 언제 커밋했는가?
```

## GitHub

GitHub는 인터넷에 있는 원격 저장소 서비스입니다. 내 컴퓨터의 Git 저장소를 GitHub에 올리면 다른 사람과 공유하거나 협업할 수 있습니다.

## 기본 흐름

```text
내 컴퓨터에서 파일 수정
-> git status로 상태 확인
-> git diff로 변경 내용 확인
-> git add로 커밋 준비
-> git commit으로 변경 이력 저장
-> GitHub에 push
-> 필요하면 Pull Request 생성
```

## VS Code로 보는 같은 흐름

터미널 명령을 아직 외우기 어렵다면 VS Code 화면에서 같은 흐름을 볼 수 있습니다.

```text
파일 수정
-> Source Control에서 변경 파일 확인
-> 변경 파일 클릭해서 diff 확인
-> 파일 옆 + 버튼으로 stage
-> 메시지 입력 칸에 커밋 메시지 작성
-> Commit 버튼 클릭
-> Push 또는 Sync Changes로 GitHub에 올리기
```

터미널 명령과 VS Code 화면은 서로 다른 도구처럼 보이지만, 실제로는 같은 Git 저장소를 다룹니다.

| 개념 | 터미널 | VS Code |
| --- | --- | --- |
| 상태 확인 | `git status` | Source Control 파일 목록 |
| 변경 내용 확인 | `git diff` | 변경 파일 클릭 |
| 커밋 준비 | `git add` | 파일 옆 `+` 버튼 |
| 커밋 | `git commit` | Commit 버튼 |
| GitHub로 올리기 | `git push` | Push / Sync Changes |
| GitHub에서 받기 | `git pull` | Pull / Sync Changes |

## 초보자가 자주 헷갈리는 점

### 저장과 커밋은 다릅니다

파일을 저장했다고 해서 Git 이력이 남는 것은 아닙니다. Git 이력으로 남기려면 `git commit`을 해야 합니다.

### GitHub에 올리기 전에도 Git은 사용할 수 있습니다

Git은 내 PC에서 먼저 동작합니다. GitHub 연결은 나중에 해도 됩니다.

초보자는 이 순서를 기억하면 됩니다.

```text
Git commit은 내 PC에 저장하는 것
GitHub push는 인터넷 저장소에 올리는 것
```

즉, 커밋했다고 해서 자동으로 GitHub에 올라가는 것은 아닙니다.
GitHub에 올리려면 push 또는 VS Code의 Sync Changes가 필요합니다.

### 모든 파일을 Git에 올리면 안 됩니다

아래 파일은 보통 GitHub에 올리지 않습니다.

```text
.env
.venv
__pycache__
개인 메모
실제 API key가 들어간 파일
```

## 과정 기준

이 과정에서는 GitHub Actions, 자동 배포, CI/CD는 다루지 않습니다. 해당 내용은 `07_multi-agent-service-ops`에서 학습합니다.

이 과정에서 다루는 GitHub 연동 범위는 다음과 같습니다.

```text
GitHub 계정 로그인
원격 저장소 연결 여부 확인
커밋을 GitHub에 push
GitHub의 변경 내용을 pull
민감정보가 올라가지 않았는지 확인
```

