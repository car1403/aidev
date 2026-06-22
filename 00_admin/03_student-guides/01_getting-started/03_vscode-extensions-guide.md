# 03. VS Code Extensions Guide

VS Code Extensions는 VS Code에 기능을 추가하는 도구입니다.

이 수업에서는 Python 코드 작성, Markdown 문서 읽기, API 테스트, Docker 실습, Codex 사용을 위해 몇 가지 확장을 설치합니다. 처음부터 모든 확장을 설치할 필요는 없습니다. 수업 단계에 맞춰 필요한 확장부터 설치하면 됩니다.

## 1. 확장 설치 방법

VS Code 왼쪽 메뉴에서 Extensions 아이콘을 클릭합니다.

```text
왼쪽 사이드바
-> Extensions
-> 검색창에 확장 이름 입력
-> Install 클릭
```

단축키로 열 수도 있습니다.

```text
Ctrl + Shift + X
```

## 2. 처음에 바로 설치할 필수 확장

### Python

검색 이름:

```text
Python
```

제공자:

```text
Microsoft
```

역할:

```text
Python 파일 실행
Python 인터프리터 선택
가상환경(.venv) 인식
디버깅 지원
```

이 확장은 Python 수업의 기본입니다. 설치하지 않으면 VS Code가 Python 파일을 제대로 인식하지 못할 수 있습니다.

### Pylance

검색 이름:

```text
Pylance
```

제공자:

```text
Microsoft
```

역할:

```text
Python 코드 자동완성
타입 힌트 표시
오류 표시
함수와 클래스 설명 표시
```

Pylance는 Python 코드를 더 쉽게 읽고 작성하게 도와줍니다. 초보자는 자동완성과 오류 표시만으로도 큰 도움을 받을 수 있습니다.

### Markdown All in One

검색 이름:

```text
Markdown All in One
```

역할:

```text
README.md 작성 보조
목차 생성
Markdown 단축키 지원
목록, 표, 코드블록 작성 보조
```

수업 자료는 대부분 `README.md` 같은 Markdown 문서로 되어 있습니다. Markdown All in One을 설치하면 문서 작성과 수정이 편해집니다.

## 3. Markdown Preview 확장 선택

VS Code에는 기본 Markdown Preview 기능이 있습니다. 따라서 아무 확장을 설치하지 않아도 `README.md` 파일을 미리보기로 볼 수 있습니다.

기본 Preview 열기:

```text
Ctrl + Shift + V
```

옆에 Preview 열기:

```text
Ctrl + K, V
```

하지만 수업 자료를 더 보기 좋게 읽고 싶다면 아래 두 확장 중 하나를 선택해서 설치하면 됩니다.

## 4. Markdown Preview Github Styling 또는 Markdown Preview Enhanced 선택

둘 다 설치할 필요는 없습니다. 처음 수업에서는 둘 중 하나만 선택해서 설치합니다.

### 선택 1: Markdown Preview Github Styling

검색 이름:

```text
Markdown Preview Github Styling
```

추천 대상:

```text
README.md를 GitHub 화면처럼 깔끔하게 보고 싶은 수업 참여자
복잡한 설정 없이 문서를 편하게 읽고 싶은 수업 참여자
```

장점:

```text
설정이 단순합니다.
GitHub README와 비슷한 스타일로 보입니다.
수업 자료를 읽기 좋습니다.
```

초보자에게는 이 확장을 먼저 추천합니다.

### 선택 2: Markdown Preview Enhanced

검색 이름:

```text
Markdown Preview Enhanced
```

추천 대상:

```text
Markdown 문서 안에서 다이어그램, 수식, 고급 Preview 기능을 사용하고 싶은 수업 참여자
문서 작성 기능을 더 강하게 사용하고 싶은 수업 참여자
```

장점:

```text
Preview 기능이 강력합니다.
다이어그램이나 고급 문서 표현에 유리합니다.
문서 작성과 검토 기능이 다양합니다.
```

단점:

```text
초보자에게는 기능이 많아서 조금 복잡하게 느껴질 수 있습니다.
```

### 강의 권장 선택

처음 수업에서는 아래 기준으로 선택합니다.

| 상황 | 추천 확장 |
| --- | --- |
| README를 보기 좋게 읽는 것이 목적 | Markdown Preview Github Styling |
| 다이어그램, 수식, 고급 문서 기능까지 쓰고 싶음 | Markdown Preview Enhanced |
| 잘 모르겠음 | Markdown Preview Github Styling |

정리하면, 초보자는 `Markdown Preview Github Styling`을 설치하고, 나중에 더 많은 기능이 필요해지면 `Markdown Preview Enhanced`로 바꾸어도 됩니다.

## 5. Markdown PDF 설치

Markdown 문서를 PDF로 저장하려면 `Markdown PDF` 확장을 설치합니다.

검색 이름:

```text
Markdown PDF
```

설치 방법:

```text
Ctrl + Shift + X
-> Markdown PDF 검색
-> Markdown PDF 선택
-> Install 클릭
```

역할:

```text
README.md 파일을 PDF로 변환
Markdown 문서를 HTML, PNG, JPEG로 변환
과제 제출용 PDF 생성
강의 자료 배포용 PDF 생성
```

## 6. Markdown PDF 사용 방법

PDF로 변환할 `.md` 파일을 먼저 엽니다.

예시:

```text
README.md
project-plan.md
final-presentation.md
```

### 방법 1: 마우스 오른쪽 클릭

```text
Markdown 파일 열기
-> 문서 편집 화면에서 마우스 오른쪽 클릭
-> Markdown PDF: Export (pdf) 클릭
```

### 방법 2: Command Palette 사용

단축키:

```text
Ctrl + Shift + P
```

검색:

```text
Markdown PDF: Export (pdf)
```

실행하면 현재 열려 있는 Markdown 문서가 PDF 파일로 저장됩니다.

## 7. Markdown PDF 저장 위치

일반적으로 PDF 파일은 원본 Markdown 파일과 같은 폴더에 생성됩니다.

예시:

```text
README.md
README.pdf
```

과제 제출 전에는 PDF가 제대로 열리는지 반드시 확인합니다.

## 8. Markdown PDF 사용 시 주의사항

### 한글이 깨져 보일 때

PDF에서 한글이 이상하게 보이면 VS Code를 재시작한 뒤 다시 변환해 봅니다. 그래도 문제가 있으면 문서에 한글을 지원하는 글꼴을 지정해야 할 수 있습니다.

강의에서는 우선 아래 순서로 확인합니다.

```text
1. Markdown Preview에서는 한글이 정상인지 확인
2. PDF로 변환
3. PDF에서 한글이 정상인지 확인
4. 깨지면 진행자에게 알리기
```

### 이미지가 보이지 않을 때

Markdown 문서 안의 이미지 경로가 잘못되면 PDF에서도 이미지가 보이지 않습니다.

이미지 파일은 가능하면 Markdown 파일과 가까운 폴더에 두고, 상대 경로를 사용합니다.

예시:

```text
images/screen-01.png
```

### PDF가 생성되지 않을 때

아래를 확인합니다.

```text
Markdown PDF 확장이 설치되어 있는가?
현재 열려 있는 파일이 .md 파일인가?
파일이 저장되어 있는가?
VS Code를 재시작해 보았는가?
```

## 9. Codex 확장

Codex는 OpenAI의 코딩 보조 도구입니다. VS Code 안에서 Codex를 사용하려면 Codex 확장을 설치할 수 있습니다.

검색 이름:

```text
Codex
```

역할:

```text
VS Code 안에서 코드 설명 요청
오류 원인 분석
README 문서 보강
작은 코드 수정 요청
```

처음 수업에서는 Codex App을 먼저 사용하고, 수업에서 안내하는 시점에 VS Code Codex 확장을 설치해도 됩니다.

Codex 설치와 로그인은 아래 문서를 참고합니다.

```text
03_student-guides/01_getting-started/08_codex-install-and-login-guide.md
```

## 10. API 실습에서 사용할 확장

### REST Client

역할:

```text
VS Code 안에서 API 요청 테스트
FastAPI 엔드포인트 테스트
HTTP 요청 파일 작성
```

선택 사항입니다. Swagger UI나 Postman을 사용해도 됩니다.

### Thunder Client

역할:

```text
Postman처럼 API 요청 테스트
GET, POST 요청을 화면에서 쉽게 실행
```

초보자에게는 화면이 친숙해서 사용하기 좋습니다.

## 11. Docker와 배포 수업에서 사용할 확장

06 과정부터는 Docker, Docker Compose, AWS, GitHub Actions를 다룹니다.

그때 설치하면 좋은 확장은 아래와 같습니다.

```text
Docker
Dev Containers
YAML
GitHub Actions
```

처음 수업에서 Docker 확장을 반드시 설치할 필요는 없습니다. Docker는 04 과정부터 천천히 다루고, Docker Compose와 배포 자동화는 06 과정에서 본격적으로 다룹니다.

## 12. 선택 확장

아래 확장은 필수는 아니지만 수업을 따라갈 때 도움이 되는 편의 기능입니다. 처음에는 필수 확장부터 설치하고, 해당 단원에 들어갈 때 필요한 확장을 추가로 설치합니다.

### Git 실습에서 유용한 확장

| 확장 | 검색 이름 | 역할 |
| --- | --- | --- |
| GitLens | `GitLens - Git supercharged` | Git 변경 이력, 파일 이력, 커밋 정보, 라인별 수정 정보를 확인합니다. |
| GitHub Pull Requests | `GitHub Pull Requests and Issues` | VS Code 안에서 Pull Request와 Issue를 확인합니다. 팀 프로젝트와 코드 리뷰 실습에서 유용합니다. |

GitLens 설치 명령:

```powershell
code --install-extension eamodio.gitlens
```

GitLens는 처음부터 모든 기능을 사용할 필요가 없습니다. 수업에서는 아래 기능만 먼저 사용합니다.

```text
파일 변경 이력 보기
커밋 상세 정보 보기
특정 줄이 언제 바뀌었는지 확인하기
이전 버전과 현재 버전 비교하기
```

### 코드 작성에서 유용한 확장

| 확장 | 검색 이름 | 역할 |
| --- | --- | --- |
| Error Lens | `Error Lens` | 오류 메시지를 코드 줄 옆에 바로 표시합니다. |
| Material Icon Theme | `Material Icon Theme` | 파일 아이콘을 보기 좋게 표시해 폴더 구조를 파악하기 쉽게 합니다. |
| indent-rainbow | `indent-rainbow` | 들여쓰기 깊이를 색상으로 구분해 Python 블록 구조를 보기 쉽게 합니다. |
| Todo Tree | `Todo Tree` | `TODO`, `FIXME` 같은 주석을 모아서 보여줍니다. |

### 환경 파일과 설정 파일을 볼 때 유용한 확장

| 확장 | 검색 이름 | 역할 |
| --- | --- | --- |
| DotENV | `DotENV` | `.env` 파일을 보기 좋게 표시합니다. 단, 실제 API key는 GitHub에 올리면 안 됩니다. |
| YAML | `YAML` | Docker Compose, GitHub Actions 같은 YAML 파일을 작성할 때 문법 도움을 줍니다. |

처음에는 너무 많은 확장을 설치하기보다 필수 확장부터 설치합니다. Git 단원에 들어가면 GitLens를 추가하고, API 실습에 들어가면 REST Client 또는 Thunder Client를 추가하는 방식이 좋습니다.

## 13. 설치 확인

Python 파일을 열었을 때 오른쪽 아래 또는 명령 팔레트에서 Python 인터프리터를 선택할 수 있으면 정상입니다.

명령 팔레트 열기:

```text
Ctrl + Shift + P
```

검색:

```text
Python: Select Interpreter
```

`.venv`를 만든 뒤에는 해당 `.venv`의 Python을 선택합니다.

## 14. 수업 첫날 권장 설치 목록

수업 첫날에는 아래 확장만 먼저 설치해도 충분합니다.

```text
Python
Pylance
Markdown All in One
Markdown Preview Github Styling
Markdown PDF
```

Git/GitHub 단원에 들어갈 때는 아래 확장을 추가로 설치하는 것을 권장합니다.

```text
GitLens
GitHub Pull Requests and Issues
```

추가로 API 실습을 바로 진행한다면 아래 중 하나를 설치합니다.

```text
REST Client
Thunder Client
```

## 15. 최종 체크리스트

아래 항목을 확인합니다.

```text
[ ] Python 확장을 설치했다.
[ ] Pylance 확장을 설치했다.
[ ] Markdown All in One을 설치했다.
[ ] Markdown Preview Github Styling 또는 Markdown Preview Enhanced 중 하나를 설치했다.
[ ] README.md를 Ctrl + Shift + V로 Preview로 열 수 있다.
[ ] Markdown PDF를 설치했다.
[ ] README.md를 PDF로 내보내는 방법을 알고 있다.
[ ] Git/GitHub 단원에서 GitLens를 설치하고 파일 변경 이력을 확인할 수 있다.
```
