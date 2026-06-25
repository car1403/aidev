# 03. VS Code Extensions Guide

VS Code Extensions는 VS Code에 기능을 추가하는 도구입니다.

이번 과정에서는 Python 개발, Markdown 문서 확인, Git/GitHub 연동, GitHub Copilot Chat 사용을 위해 아래 확장들을 설치합니다.

## 1. Extensions 화면 열기

VS Code 왼쪽 메뉴에서 Extensions 아이콘을 클릭합니다.

또는 단축키를 사용합니다.

```text
Ctrl + Shift + X
```

## 2. 필수 확장

| 확장 | 검색 이름 | 용도 |
| --- | --- | --- |
| Python | `Python` | Python 파일 실행, 문법 강조, 가상환경 인식 |
| Pylance | `Pylance` | Python 자동완성, 타입 힌트, 오류 표시 |
| GitHub Copilot | `GitHub Copilot` | 코드 제안 |
| GitHub Copilot Chat | `GitHub Copilot Chat` | VS Code 안에서 질문, 코드 설명, 오류 분석 |
| GitLens | `GitLens` | Git 변경 이력과 작성자 확인 |
| GitHub Pull Requests and Issues | `GitHub Pull Requests and Issues` | GitHub PR과 Issue 확인 |
| Markdown Preview Github Styling | `Markdown Preview Github Styling` | README를 GitHub 스타일로 미리보기 |
| Markdown PDF | `Markdown PDF` | Markdown 문서를 PDF로 변환 |
| DotENV | `DotENV` | `.env` 파일 보기 좋게 표시 |
| YAML | `YAML` | Docker Compose, GitHub Actions YAML 작성 |

## 3. GitHub Copilot Chat 확인

Copilot Chat을 사용하려면 VS Code에서 GitHub 계정으로 로그인되어 있어야 합니다.

확인 순서:

```text
1. VS Code 왼쪽 아래 계정 아이콘 확인
2. GitHub 계정 로그인 확인
3. Extensions에서 GitHub Copilot 설치
4. Extensions에서 GitHub Copilot Chat 설치
5. VS Code 재시작
6. Chat 또는 Copilot 아이콘 열기
```

처음 질문 예시:

```text
이 Python 코드가 어떤 순서로 실행되는지 초보자도 이해할 수 있게 설명해줘.
```

오류 질문 예시:

```text
아래 오류 메시지의 원인과 해결 순서를 알려줘.
```

## 4. Markdown Preview

VS Code에는 기본 Markdown Preview 기능이 있습니다.

README.md 파일을 연 뒤 아래 단축키를 누릅니다.

```text
Ctrl + Shift + V
```

옆으로 미리보기를 열려면 아래 단축키를 사용합니다.

```text
Ctrl + K V
```

GitHub 화면과 비슷한 스타일로 보려면 `Markdown Preview Github Styling` 확장을 설치합니다.

## 5. Markdown PDF

Markdown 문서를 PDF로 저장하려면 `Markdown PDF` 확장을 설치합니다.

사용 방법:

```text
1. README.md 파일 열기
2. Ctrl + Shift + P
3. Markdown PDF: Export (pdf) 선택
4. 같은 폴더에 PDF 생성 확인
```

한글이 이상하게 보이면 VS Code를 재시작한 뒤 다시 변환합니다.

## 6. Git 관련 확장

GitHub 프로젝트를 사용할 때는 아래 확장이 유용합니다.

```text
GitLens
GitHub Pull Requests and Issues
```

GitLens로 할 수 있는 일:

- 파일 변경 이력 확인
- 줄 단위 변경 기록 확인
- 누가 언제 수정했는지 확인
- 커밋 메시지 확인

## 7. Docker와 운영 과정 확장

06~07 과정에서는 아래 확장이 있으면 편합니다.

| 확장 | 용도 |
| --- | --- |
| Docker | Dockerfile, Compose 파일 확인 |
| YAML | GitHub Actions, Docker Compose 작성 |
| REST Client | API 요청 테스트 |

## 8. 설치 확인 체크리스트

- [ ] Python 확장을 설치했다.
- [ ] Pylance 확장을 설치했다.
- [ ] GitHub 계정으로 VS Code에 로그인했다.
- [ ] GitHub Copilot 확장을 설치했다.
- [ ] GitHub Copilot Chat을 열 수 있다.
- [ ] Markdown Preview를 열 수 있다.
- [ ] Markdown PDF를 설치했다.
- [ ] GitLens를 설치했다.
- [ ] DotENV와 YAML을 설치했다.
