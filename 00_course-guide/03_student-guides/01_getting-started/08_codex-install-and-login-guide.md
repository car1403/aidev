# 48. Codex Install and Login Guide

이 문서는 수업에서 Codex를 사용할 때 필요한 설치와 로그인 안내입니다.

Codex는 OpenAI의 코딩 에이전트입니다. 코드 설명, 생성, 수정, 리뷰, 디버깅, 문서 작성 같은 개발 작업을 도와줍니다.

중요한 점은 Codex가 모든 것을 대신해 주는 도구가 아니라, 직접 코드를 이해하고 더 잘 실습하도록 돕는 학습 파트너라는 점입니다.

## 1. 수업에서 Codex를 사용하는 이유

Codex는 다음 용도로 사용할 수 있습니다.

```text
코드 설명 요청
오류 메시지 분석
README 문서 보강
Python 주석 추가
FastAPI/Streamlit 코드 개선
프로젝트 구조 점검
테스트 체크리스트 작성
```

예를 들어 수업 중 오류가 발생하면 오류 메시지를 Codex에 보여 주고, “이 오류가 왜 발생했는지 초보자에게 설명해 주세요”라고 질문할 수 있습니다.

## 2. Codex 사용 방식

Codex는 여러 방식으로 사용할 수 있습니다.

| 방식 | 설명 | 수업 추천 |
| --- | --- | --- |
| Codex app | Windows/macOS에서 사용하는 데스크톱 앱 | 권장 |
| VS Code Codex extension | VS Code 안에서 Codex를 사용하는 확장 | 권장 |
| Codex CLI | 터미널에서 `codex` 명령으로 사용하는 방식 | 선택 |

초보자 수업에서는 보통 아래 순서를 추천합니다.

```text
1. Codex app 설치
2. ChatGPT 계정으로 로그인
3. C:\aidev 폴더를 프로젝트로 선택
4. 필요하면 VS Code Codex extension 설치
```

## 3. Codex app 설치

Codex app은 데스크톱에서 프로젝트 폴더를 열고 Codex와 함께 작업할 수 있게 해 줍니다.

설치 흐름:

```text
1. 공식 Codex app 다운로드 페이지로 이동
2. Windows용 설치 파일 다운로드
3. 설치 파일 실행
4. Codex 실행
5. ChatGPT 계정 또는 OpenAI API key로 로그인
6. 작업할 프로젝트 폴더 선택
```

수업에서는 보통 아래 폴더를 프로젝트로 선택합니다.

```text
C:\aidev
```

또는 현재 작업할 과정 폴더를 선택할 수도 있습니다.

```text
C:\aidev\42_supabase-ai-backend
C:\aidev\43_supabase-ai-frontend
C:\aidev\44_supabase-ai-mini-project
```

## 4. VS Code Codex Extension

VS Code에서 Codex를 쓰려면 Codex extension을 설치할 수 있습니다.

설치 흐름:

```text
1. VS Code 실행
2. Extensions 메뉴 열기
3. Codex 검색
4. OpenAI Codex extension 설치
5. VS Code 재시작
6. 사이드바에서 Codex 패널 확인
7. 로그인
```

설치 후 Codex 패널이 보이지 않으면 VS Code를 다시 시작합니다.

## 5. Codex와 함께 설치하면 좋은 개발 도구

Codex는 아래 도구가 설치되어 있으면 더 잘 동작합니다.

```text
Git
Node.js
Python
GitHub CLI
```

초보자 수업에서는 Python과 VS Code를 먼저 준비하고, Git, Node.js, GitHub CLI는 수업에서 필요하다고 안내할 때 설치해도 됩니다.

하지만 각 도구가 어떤 역할을 하는지 미리 이해해 두면 이후 수업을 따라가기가 훨씬 쉬워집니다.

## 6. Git을 설치하면 할 수 있는 것

Git은 코드 변경 이력을 관리하는 도구입니다.

처음 진행할 때는 Git을 설치하면 아래 작업을 할 수 있습니다.

```text
프로젝트 변경 내용 확인
수정한 파일 목록 확인
작업 내용을 저장하는 commit 만들기
이전 상태와 현재 상태 비교
GitHub 저장소와 연결
팀 프로젝트에서 코드 변경 이력 공유
```

Codex와 함께 사용할 때는 특히 아래 작업에 도움이 됩니다.

| 할 수 있는 일 | 설명 |
| --- | --- |
| 변경 파일 확인 | Codex가 어떤 파일을 수정했는지 확인할 수 있습니다. |
| 변경 내용 비교 | 수정 전후 차이를 확인할 수 있습니다. |
| 작업 단위 저장 | 좋은 상태를 commit으로 저장할 수 있습니다. |
| 실수 복구 | 이전 commit과 비교하여 문제를 찾을 수 있습니다. |
| 협업 준비 | GitHub에 올릴 준비를 할 수 있습니다. |

자주 사용하는 명령:

```powershell
git --version
git status
git diff
git add.
git commit -m "수정 내용 설명"
```

설치 확인:

```powershell
git --version
```

정상적으로 설치되어 있으면 아래와 비슷하게 표시됩니다.

```text
git version 2.x.x
```

초보자에게 중요한 점:

```text
Git은 코드를 실행하는 도구가 아닙니다.
Git은 코드의 변경 이력을 관리하는 도구입니다.
```

## 7. Node.js를 설치하면 할 수 있는 것

Node.js는 JavaScript를 브라우저 밖에서도 실행할 수 있게 해 주는 실행 환경입니다.

처음 진행할 때는 Node.js를 설치하면 아래 작업을 할 수 있습니다.

```text
React, Vite 같은 프론트엔드 프로젝트 실행
npm 명령으로 JavaScript 패키지 설치
웹 UI 개발 서버 실행
일부 Codex/개발 도구 실행
Markdown 또는 문서 변환 도구 사용
프론트엔드 빌드 작업 수행
```

수업에서 Node.js가 필요한 대표 상황:

| 상황 | 설명 |
| --- | --- |
| React 실습 | `npm install`, `npm run dev` 명령을 사용합니다. |
| Vite 실행 | 프론트엔드 개발 서버를 실행합니다. |
| 문서/빌드 도구 사용 | 일부 문서 변환이나 빌드 도구가 Node.js를 사용합니다. |
| 문서/빌드 도구 사용 | 일부 문서 변환이나 빌드 도구가 Node.js를 사용합니다. |

자주 사용하는 명령:

```powershell
node --version
npm --version
npm install
npm run dev
npm run build
```

설치 확인:

```powershell
node --version
npm --version
```

정상적으로 설치되어 있으면 아래와 비슷하게 표시됩니다.

```text
v24.x.x
14.x.x
```

초보자에게 중요한 점:

```text
Python 수업만 할 때는 Node.js가 바로 필요하지 않을 수 있습니다.
하지만 React, 프론트엔드, 일부 자동화 도구를 다룰 때는 Node.js가 필요합니다.
```

## 8. Python을 설치하면 할 수 있는 것

Python은 이 수업의 가장 기본이 되는 프로그래밍 언어입니다.

처음 진행할 때는 Python을 설치하면 아래 작업을 할 수 있습니다.

```text
Python 파일 실행
FastAPI 백엔드 서버 실행
Streamlit 화면 실행
AI API 호출 코드 작성
데이터 처리 실습
.venv 가상환경 생성
pip로 Python 패키지 설치
```

수업에서 Python이 필요한 대표 상황:

| 상황 | 설명 |
| --- | --- |
| 41 백엔드 실습 | FastAPI 서버를 실행합니다. |
| 42 프론트엔드 실습 | Streamlit UI를 실행합니다. |
| 43 미니 프로젝트 | 백엔드, DB, UI를 연결합니다. |
| 44 이후 LLM Agent 실습 | LLM API, LangGraph, 도구 호출 코드를 실행합니다. |
| 44~47 Agent/운영 실습 | LLM API, LangGraph, 운영 보조 코드를 실행합니다. |

자주 사용하는 명령:

```powershell
python --version
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

설치 확인:

```powershell
python --version
pip --version
```

정상적으로 설치되어 있으면 아래와 비슷하게 표시됩니다.

```text
Python 3.x.x
pip 24.x
```

초보자에게 중요한 점:

```text
Python은 코드를 실행하는 언어입니다.
pip는 Python 패키지를 설치하는 도구입니다.
.venv는 프로젝트마다 독립된 Python 환경을 만드는 도구입니다.
```

## 9. GitHub CLI를 설치하면 할 수 있는 것

GitHub CLI는 터미널에서 GitHub 기능을 사용할 수 있게 해 주는 도구입니다.

명령어 이름은 `gh`입니다.

처음 진행할 때는 GitHub CLI를 설치하면 아래 작업을 할 수 있습니다.

```text
터미널에서 GitHub 로그인
GitHub 저장소 생성
GitHub 저장소 복제
Pull Request 확인
Issue 확인
브랜치와 PR 작업 흐름 이해
```

Codex와 함께 사용할 때는 특히 아래 작업에 도움이 됩니다.

| 할 수 있는 일 | 설명 |
| --- | --- |
| GitHub 로그인 | 브라우저와 터미널을 연결해 GitHub 인증을 할 수 있습니다. |
| 저장소 확인 | 현재 프로젝트가 어떤 GitHub 저장소와 연결되어 있는지 확인할 수 있습니다. |
| PR 확인 | 팀 프로젝트에서 Pull Request 상태를 확인할 수 있습니다. |
| 협업 흐름 학습 | branch, commit, push, pull request 흐름을 익힐 수 있습니다. |

자주 사용하는 명령:

```powershell
gh --version
gh auth login
gh repo list
gh repo clone 사용자명/저장소명
gh pr list
```

설치 확인:

```powershell
gh --version
```

초보자에게 중요한 점:

```text
Git은 내 PC의 코드 변경 이력을 관리합니다.
GitHub는 인터넷에 있는 코드 저장소 서비스입니다.
GitHub CLI는 터미널에서 GitHub를 조작하는 도구입니다.
```

즉, Git과 GitHub CLI는 같은 도구가 아닙니다.

## 14. 네 가지 도구를 함께 이해하기

아래 표처럼 이해하면 쉽습니다.

| 도구 | 한 줄 설명 | 수업에서 주로 하는 일 |
| --- | --- | --- |
| Git | 변경 이력 관리 도구 | 파일 변경 확인, commit, 협업 준비 |
| Node.js | JavaScript 실행 환경 | React/Vite 프론트엔드 실행, npm 패키지 설치 |
| Python | Python 코드 실행 환경 | FastAPI, Streamlit, AI 코드 실행 |
| GitHub CLI | GitHub 터미널 도구 | GitHub 로그인, 저장소, PR 작업 |

초보자 우선순위:

```text
1. Python
2. VS Code
3. Git
4. Node.js
5. GitHub CLI
```

수업 첫날에는 Python과 VS Code가 가장 중요합니다. Git, Node.js, GitHub CLI는 과정이 진행되면서 필요할 때 설치해도 됩니다.

## 11. 설치 여부 한 번에 확인하기

PowerShell에서 아래 명령을 실행해 설치 여부를 확인할 수 있습니다.

```powershell
python --version
pip --version
git --version
node --version
npm --version
gh --version
```

명령이 정상적으로 실행되면 설치된 상태입니다.

아래와 같은 메시지가 나오면 설치가 안 되었거나 PATH 설정이 되지 않은 상태입니다.

```text
The term 'git' is not recognized
```

이 경우 설치 후 PowerShell 또는 VS Code를 완전히 껐다가 다시 실행합니다.

## 12. 로그인 방식

Codex는 보통 아래 방식 중 하나로 로그인합니다.

```text
ChatGPT 계정으로 로그인
OpenAI API key로 로그인
```

초보자에게는 ChatGPT 계정 로그인이 더 이해하기 쉽습니다.

주의:

```text
OpenAI API key로 로그인하면 일부 기능이 제한될 수 있습니다.
API key는 README, 코드, 화면 공유 자료에 적지 않습니다.
API key, 비밀번호, 개인정보는 Codex 프롬프트에 붙여넣지 않습니다.
```

## 13. Codex 사용을 위한 카드 결제 안내

Codex를 사용하기 전에 결제 방식이 어떤 계정에 연결되는지 이해해야 합니다.

초보자가 가장 헷갈리기 쉬운 부분은 아래 두 가지입니다.

```text
ChatGPT 계정 결제
OpenAI API 결제
```

두 결제는 서로 같은 것처럼 보일 수 있지만, 실제로는 목적이 다릅니다.

특히 아래 내용을 반드시 기억해야 합니다.

```text
Codex app 사용을 위한 ChatGPT 계정 결제와
OpenAI API key 연동을 위한 API 결제는 별개의 결제입니다.
```

즉, Codex app에서 ChatGPT 계정으로 로그인해 사용하는 것과, OpenAI API key를 발급받아 코드나 서비스에 연결하는 것은 결제 관리가 다를 수 있습니다.

| 구분 | 주로 사용하는 곳 | 결제 성격 |
| --- | --- | --- |
| Codex app / VS Code Codex extension | Codex 앱, VS Code 안의 Codex 패널 | ChatGPT 계정 플랜 또는 Codex 포함 사용량과 관련 |
| OpenAI API key | Python 코드, FastAPI 서버, 자동화 스크립트, 외부 앱 연동 | OpenAI API 사용량 또는 크레딧 결제와 관련 |

따라서 ChatGPT 유료 플랜을 결제했다고 해서 OpenAI API 사용량이 자동으로 무료가 되는 것은 아닙니다. 반대로 OpenAI API 결제 수단을 등록했다고 해서 ChatGPT 유료 플랜이 자동으로 구독되는 것도 아닙니다.

## 14. ChatGPT 계정 결제와 Codex

Codex는 ChatGPT Free, Go, Plus, Pro, Business, Edu, Enterprise 같은 플랜에 포함될 수 있습니다. 다만 플랜별 사용량, 제한, 기능 제공 범위는 시점에 따라 달라질 수 있으므로 실제 결제 전에는 반드시 ChatGPT 결제 화면에서 확인해야 합니다.

ChatGPT 계정 결제에서 할 수 있는 일:

```text
ChatGPT 유료 플랜 구독
Codex 포함 사용량 이용
더 높은 사용량 또는 기능이 포함된 플랜 선택
결제 카드 등록
구독 변경 또는 해지
결제 내역 확인
```

일반적인 확인 경로:

```text
ChatGPT 웹사이트 로그인
-> Settings
-> Billing
-> 현재 플랜과 결제 수단 확인
```

수업에서는 아래처럼 안내하면 좋습니다.

```text
Codex를 ChatGPT 계정으로 사용할 경우, 먼저 본인의 ChatGPT 플랜에서 Codex 사용이 가능한지 확인합니다.
유료 플랜이 필요하다면 ChatGPT Billing 화면에서 카드 결제를 진행합니다.
```

주의할 점:

```text
플랜 가격과 포함 사용량은 변경될 수 있습니다.
결제 전에는 반드시 공식 결제 화면의 금액과 조건을 확인합니다.
학교, 회사, 팀 계정은 개인이 결제하지 않고 관리자에게 확인해야 할 수 있습니다.
```

## 15. OpenAI API 결제와 Codex

Codex를 OpenAI API key로 로그인해서 사용하는 경우도 있습니다.

이 경우에는 ChatGPT 플랜에 포함된 Codex 사용량이 아니라, API 사용량 기준 과금이 적용될 수 있습니다.

API 결제에서 할 수 있는 일:

```text
OpenAI API key 생성
API 사용량 결제
결제 카드 등록
사용량 한도 설정
선불 크레딧 또는 사용량 기반 결제 관리
API 사용 내역 확인
```

일반적인 확인 경로:

```text
OpenAI Platform 로그인
-> Billing
-> 결제 수단 확인
-> 사용량 또는 크레딧 확인
```

수업에서는 초보자에게 API key 로그인을 바로 권장하지 않는 편이 좋습니다.

이유:

```text
API key는 유출되면 비용이 발생할 수 있습니다.
API 사용량은 토큰 사용량에 따라 비용이 달라질 수 있습니다.
ChatGPT 플랜 결제와 API 결제는 다르게 관리될 수 있습니다.
```

## 16. 카드 결제 전에 반드시 확인할 것

카드 결제를 진행하기 전에 아래 항목을 확인합니다.

```text
[ ] 내가 결제하려는 것이 ChatGPT 플랜인지 OpenAI API 크레딧인지 확인했다.
[ ] 개인 계정인지 학교/회사/팀 계정인지 확인했다.
[ ] 월 구독인지 사용량 기반 결제인지 확인했다.
[ ] 포함 사용량과 초과 사용 시 과금 방식을 확인했다.
[ ] 결제 통화와 세금 포함 여부를 확인했다.
[ ] 자동 갱신 여부를 확인했다.
[ ] 환불 또는 해지 정책을 확인했다.
[ ] API key를 사용할 경우 사용량 한도를 설정할 수 있는지 확인했다.
```

특히 개인 카드로 결제할 때는 진행자에게 먼저 확인하는 것이 좋습니다.

## 17. 수업에서 권장하는 결제 안내 방식

강의에서는 아래 순서로 안내하는 것이 안전합니다.

```text
1. 무료 또는 기존 계정으로 가능한 범위를 먼저 확인합니다.
2. Codex가 꼭 필요한 실습인지 확인합니다.
3. 유료 결제가 필요하면 ChatGPT 플랜 결제인지 API 결제인지 구분합니다.
4. 개인 결제 전에 금액, 자동 갱신, 사용량 제한을 확인합니다.
5. API key를 사용하는 경우 절대 화면 공유나 GitHub에 노출하지 않습니다.
```

수업 중 권장 표현:

```text
결제는 실습을 위한 선택 사항일 수 있습니다.
무조건 결제부터 하지 말고, 본인 계정에서 어떤 기능이 가능한지 먼저 확인합니다.
결제 화면의 금액과 조건은 OpenAI 공식 화면을 기준으로 확인합니다.
```

## 18. 결제 관련 자주 하는 질문

### ChatGPT Plus를 결제하면 API도 무료인가요?

아닙니다. ChatGPT 플랜과 OpenAI API 사용량 결제는 별도로 관리될 수 있습니다. API를 사용하는 실습에서는 API 결제 설정이 별도로 필요할 수 있습니다.

정리하면 아래와 같습니다.

```text
Codex app 사용:
ChatGPT 계정 로그인과 ChatGPT 플랜 결제 영역

OpenAI API key 연동:
OpenAI Platform의 API 사용량 결제 영역
```

수업에서 Codex app만 사용하는 경우에는 API key 결제가 필요하지 않을 수 있습니다. 하지만 Python 코드에서 OpenAI API를 직접 호출하거나, FastAPI 서버에서 AI 모델 API를 연결하는 경우에는 API key와 API 결제 설정이 필요할 수 있습니다.

### Codex를 쓰려면 반드시 API key가 필요한가요?

항상 그런 것은 아닙니다. Codex app이나 VS Code Codex extension은 ChatGPT 계정 로그인으로 사용할 수 있는 경우가 있습니다. 다만 특정 CLI, 자동화, API 기반 사용에서는 API key가 필요할 수 있습니다.

### 카드 결제를 했는데 Codex가 안 보이면 어떻게 하나요?

아래를 확인합니다.

```text
1. 올바른 계정으로 로그인했는가?
2. 결제한 계정과 Codex에 로그인한 계정이 같은가?
3. VS Code 또는 Codex app을 재시작했는가?
4. 학교/회사 계정이라면 관리자가 Codex 사용을 허용했는가?
5. 결제한 항목이 ChatGPT 플랜인지 API 크레딧인지 확인했는가?
```

### API key를 문서에 적어도 되나요?

절대 적으면 안 됩니다.

API key는 비밀번호처럼 다룹니다. README, 과제 문서, 발표 자료, GitHub 저장소, 화면 캡처에 노출하지 않습니다.

## 19. 수업용 Codex 사용 원칙

```text
1. 먼저 README를 읽고 질문합니다.
2. 오류 메시지는 전체를 복사해서 질문합니다.
3. "다 만들어줘"보다 "이 코드가 왜 필요한지 설명해 주세요"라고 질문합니다.
4. Codex가 만든 코드는 반드시 직접 읽고 실행합니다.
5. API Key, 비밀번호, 개인정보는 Codex 프롬프트에 붙여넣지 않습니다.
6. 이해하지 못한 코드는 제출하지 않습니다.
```

## 24. 공식 참고 링크

```text
Codex app:
https://developers.openai.com/codex/app

Codex Windows setup:
https://developers.openai.com/codex/windows

Codex IDE extension:
https://developers.openai.com/codex/ide

Codex CLI:
https://developers.openai.com/codex/cli

Codex pricing:
https://developers.openai.com/codex/pricing

Codex authentication:
https://developers.openai.com/codex/auth

ChatGPT billing settings:
https://help.openai.com/en/articles/9439756-managing-billing-settings-on-chatgpt-web-and-platform
```

## 21. 최종 체크리스트

아래 항목을 확인합니다.

```text
[ ] Codex app을 설치했다.
[ ] ChatGPT 계정 또는 OpenAI 계정으로 로그인할 수 있다.
[ ] C:\aidev 폴더를 프로젝트로 열 수 있다.
[ ] Python이 어떤 역할을 하는지 이해했다.
[ ] Git이 어떤 역할을 하는지 이해했다.
[ ] Node.js가 어떤 역할을 하는지 이해했다.
[ ] GitHub CLI가 어떤 역할을 하는지 이해했다.
[ ] python --version으로 설치 확인을 할 수 있다.
[ ] git --version으로 설치 확인을 할 수 있다.
[ ] node --version으로 설치 확인을 할 수 있다.
[ ] gh --version으로 설치 확인을 할 수 있다.
[ ] ChatGPT 플랜 결제와 OpenAI API 결제의 차이를 이해했다.
[ ] Codex app 사용 결제와 OpenAI API key 연동 결제가 별개라는 것을 이해했다.
[ ] 카드 결제 전 자동 갱신, 포함 사용량, 초과 과금 여부를 확인해야 한다는 것을 이해했다.
[ ] API key를 문서나 GitHub에 올리면 안 된다는 것을 이해했다.
```
