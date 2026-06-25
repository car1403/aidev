# 02. VS Code Install Guide

VS Code는 이 과정에서 코드를 보고, 문서를 읽고, 터미널을 실행하는 기본 도구입니다.

이번 과정에서는 VS Code 안의 AI Chat 기능으로 GitHub Copilot Chat을 사용할 예정입니다. 그래서 VS Code를 설치하기 전에 GitHub 계정을 먼저 준비합니다.

## 1. GitHub 계정 만들기

GitHub는 코드 저장소, 협업, 제출, VS Code 로그인, GitHub Copilot Chat 사용에 필요한 계정입니다.

아래 사이트에서 계정을 만듭니다.

```text
https://github.com
```

계정 생성 시 확인할 것:

```text
1. 사용할 이메일 주소를 준비합니다.
2. GitHub 사용자 이름(username)을 정합니다.
3. 이메일 인증을 완료합니다.
4. 로그인할 수 있는지 확인합니다.
```

GitHub 계정은 이후 아래 작업에 사용됩니다.

```text
VS Code 로그인
GitHub Copilot Chat 사용
Git 저장소 연결
팀 프로젝트 제출
GitHub Actions 결과 확인
```

## 2. VS Code 설치

VS Code 공식 사이트에서 설치합니다.

```text
https://code.visualstudio.com
```

설치 후 Windows 시작 메뉴에서 `Visual Studio Code`를 실행합니다.

## 3. VS Code에서 GitHub 로그인

VS Code를 실행한 뒤 GitHub 계정으로 로그인합니다.

방법 1:

```text
VS Code 왼쪽 아래 사람 모양 아이콘
-> Sign in to Sync Settings
-> Sign in with GitHub
-> 브라우저에서 GitHub 로그인
-> VS Code 권한 승인
```

방법 2:

```text
Ctrl + Shift + P
-> GitHub: Sign in
-> 브라우저에서 GitHub 로그인
-> VS Code 권한 승인
```

로그인이 완료되면 VS Code 왼쪽 아래 계정 아이콘에 GitHub 계정이 표시됩니다.

## 4. GitHub Copilot Chat 준비

이번 과정에서는 VS Code의 Chat 기능을 GitHub Copilot Chat으로 사용할 예정입니다.

확인할 것:

```text
1. VS Code에서 GitHub 계정으로 로그인되어 있는가?
2. GitHub Copilot 확장이 설치되어 있는가?
3. GitHub Copilot Chat 확장이 설치되어 있는가?
4. VS Code 왼쪽 사이드바 또는 상단 Chat 영역에서 Copilot Chat을 열 수 있는가?
```

Copilot 사용 가능 여부와 결제/라이선스는 GitHub 계정 상태에 따라 달라질 수 있습니다. Copilot이 바로 동작하지 않으면 계정 권한, 무료 체험, 조직/교육용 라이선스, 결제 상태를 확인합니다.

## 5. C:\aidev 폴더 열기

VS Code에서 아래 순서로 폴더를 엽니다.

```text
File
-> Open Folder
-> C:\aidev 선택
-> Select Folder
```

Explorer에 아래 폴더들이 보이면 정상입니다.

```text
00_course-guide
02_supabase-ai-backend
03_supabase-ai-frontend
04_supabase-ai-mini-project
05_llm-agent-orchestration
06_llm-agent-mini-project
07_multi-agent-service-ops
08_multi-agent-service-mini-project
```

## 6. VS Code 기본 화면

| 영역 | 역할 |
| --- | --- |
| Explorer | 파일과 폴더를 봅니다. |
| Editor | README.md, Python 파일을 엽니다. |
| Terminal | PowerShell 명령을 실행합니다. |
| Extensions | Python, Markdown, Copilot 같은 확장을 설치합니다. |
| Chat | GitHub Copilot Chat으로 질문하고 코드 설명을 받습니다. |

## 7. 터미널 열기

VS Code 상단 메뉴에서 터미널을 엽니다.

```text
Terminal
-> New Terminal
```

또는 단축키를 사용합니다.

```text
Ctrl + `
```

터미널에 아래처럼 보이면 정상입니다.

```text
PS C:\aidev>
```

## 8. 폴더를 잘못 열었을 때

Explorer에 `00_course-guide`, `02_supabase-ai-backend` 같은 폴더가 보이지 않으면 다른 폴더를 연 것입니다.

다시 아래 순서로 엽니다.

```text
File -> Open Folder -> C:\aidev
```

## 9. VS Code 사용 원칙

```text
1. 항상 C:\aidev 폴더를 열고 시작합니다.
2. README.md는 Preview로 읽습니다.
3. Python 파일은 터미널에서 실행해 봅니다.
4. 오류가 나면 파일 경로와 현재 터미널 위치를 먼저 확인합니다.
5. Copilot Chat에는 오류 메시지와 현재 파일명을 함께 알려 줍니다.
```
