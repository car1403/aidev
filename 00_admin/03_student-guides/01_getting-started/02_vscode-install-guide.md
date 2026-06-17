# 02. VS Code Install Guide

VS Code는 이 수업에서 코드를 보고, 문서를 읽고, 터미널을 실행하는 기본 도구입니다.

## 1. VS Code 설치

VS Code 공식 사이트에서 설치합니다.

```text
https://code.visualstudio.com
```

설치 후 Windows 시작 메뉴에서 `Visual Studio Code`를 실행합니다.

## 2. C:\aidev 폴더 열기

VS Code를 실행한 뒤 아래 순서로 폴더를 엽니다.

```text
File
-> Open Folder
-> C:\aidev 선택
-> Select Folder
```

왼쪽 Explorer에 아래 폴더들이 보이면 정상입니다.

```text
00_admin
01_supabase-ai-backend
02_supabase-ai-frontend
03_supabase-ai-mini-project
04_llm-agent-orchestration
05_llm-agent-mini-project
06_multi-agent-service-ops
07_multi-agent-service-mini-project
08_ai-workflow-automation
09_ai-workflow-mini-project
```

## 3. VS Code 기본 화면

초보자가 자주 쓰는 영역은 아래 4개입니다.

```text
Explorer:
파일과 폴더를 보는 곳

Editor:
README.md, Python 파일을 여는 곳

Terminal:
PowerShell 명령어를 실행하는 곳

Extensions:
Python, Markdown 확장 기능을 설치하는 곳
```

## 4. 터미널 열기

VS Code 상단 메뉴에서 터미널을 엽니다.

```text
Terminal
-> New Terminal
```

또는 단축키:

```text
Ctrl + `
```

터미널에 아래처럼 보이면 PowerShell이 열린 것입니다.

```text
PS C:\aidev>
```

## 5. 폴더를 잘못 열었을 때

Explorer에 `00_admin`, `01_supabase-ai-backend` 같은 폴더가 보이지 않으면 잘못된 폴더를 연 것입니다.

다시 아래를 실행합니다.

```text
File -> Open Folder -> C:\aidev
```

## 6. 수업 중 VS Code 사용 원칙

```text
1. 항상 C:\aidev 폴더를 열고 시작합니다.
2. README.md는 Preview로 읽습니다.
3. Python 파일은 그냥 읽기만 하지 말고 터미널에서 실행해 봅니다.
4. 오류가 나면 파일 경로와 터미널 위치를 먼저 확인합니다.
```
