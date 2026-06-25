# 99_advanced-mini-project

`02_python-advanced` 과정의 마무리 미니 프로젝트입니다.

이번 프로젝트에서는 실제 AI API를 호출하지 않습니다. 대신 이후 FastAPI, Supabase, LLM API 단원에서 그대로 이어질 수 있는 **챗봇 요청/응답 관리 흐름**을 Python만으로 먼저 연습합니다.

## 프로젝트 주제

```text
AI 챗봇 요청/응답 관리 CLI
```

사용자가 질문을 입력하면 프로그램이 질문을 정리하고, 빈 질문인지 검증한 뒤, 연습용 답변을 생성하고 JSON 파일에 저장합니다.

```text
질문 입력
-> 질문 정리
-> 질문 검증
-> 임시 답변 생성
-> 응답 기록 생성
-> JSON 저장
-> pytest 테스트
```

## 파일 구성

```text
99_advanced-mini-project
├─ README.md
├─ chat_response_manager.py
└─ test_chat_response_manager.py
```

| 파일 | 역할 |
| --- | --- |
| `chat_response_manager.py` | CLI 실행, 질문 검증, 임시 답변 생성, JSON 저장 |
| `test_chat_response_manager.py` | 핵심 함수가 예상대로 동작하는지 pytest로 검증 |

## 실행 전 준비

이 폴더에서는 별도의 `.venv`를 만들지 않습니다. `02_supabase-ai-backend` 최상위에서 만든 공통 가상환경을 사용합니다.

```powershell
cd C:\aidev\01_python-git-foundation
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## 프로그램 실행

```powershell
python .\02_python-advanced\99_advanced-mini-project\chat_response_manager.py
```

실행 후 메뉴에서 원하는 기능을 선택합니다.

```text
1. 질문 추가
2. 저장된 질문 목록 보기
3. 키워드 검색
4. 답변 스트리밍 흉내 보기
5. 종료
```

## 테스트 실행

```powershell
python -m pytest .\02_python-advanced\99_advanced-mini-project
```

## 사용하는 문법

```text
함수:
  질문 정리, 질문 검증, 답변 생성, 저장 기능을 함수로 나눕니다.

dataclass:
  하나의 질문/답변 기록을 객체로 표현합니다.

예외 처리:
  빈 질문이 들어오면 ValueError를 발생시키고 안전하게 처리합니다.

JSON 저장:
  응답 기록을 data/chat_records.json 파일에 저장합니다.

list comprehension:
  키워드 검색 결과를 목록에서 추출합니다.

yield:
  답변을 단어 단위로 하나씩 출력하며 이후 스트리밍 개념으로 연결합니다.

pytest:
  핵심 함수가 예상대로 동작하는지 자동으로 확인합니다.
```

## 이후 과정과의 연결

```text
이 프로젝트의 질문 입력 흐름은 이후 FastAPI 요청 처리로 연결됩니다.
이 프로젝트의 응답 dict 구조는 이후 Pydantic Response Model로 연결됩니다.
이 프로젝트의 JSON 저장은 이후 Supabase 테이블 저장으로 연결됩니다.
이 프로젝트의 yield 예제는 이후 SSE 기반 실시간 응답 스트리밍 이해로 연결됩니다.
이 프로젝트의 pytest 테스트는 이후 API 테스트와 코드 리팩토링 검증으로 연결됩니다.
```

## 완료 기준

```text
1. 질문을 추가할 수 있어야 합니다.
2. 빈 질문을 입력하면 오류 메시지를 보여주고 계속 실행되어야 합니다.
3. 저장된 질문/답변 목록을 볼 수 있어야 합니다.
4. 키워드로 저장된 질문을 검색할 수 있어야 합니다.
5. JSON 파일에 한글이 깨지지 않고 저장되어야 합니다.
6. pytest 테스트가 모두 통과해야 합니다.
```
