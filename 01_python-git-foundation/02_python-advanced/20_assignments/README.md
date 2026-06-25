# 20_assignments

`02_python-advanced` 과정의 종합 과제 모음입니다.

이 과제는 새로운 개념을 많이 추가하기보다, 앞에서 배운 내용을 하나의 작은 프로그램으로 연결하는 데 목적이 있습니다. 이후 FastAPI, Supabase, LLM API 예제를 진행할 때 필요한 기본 구조를 미리 연습합니다.

## 과제 목록

```text
assignment-01_advanced-python-project.md
```

## 진행 기준

```text
1. 01_function-advanced부터 09_project-structure까지의 예제를 먼저 실행합니다.
2. 필요한 코드는 하나의 파일에 모두 넣지 않고 역할별로 나눕니다.
3. 입력 검증, 예외 처리, 데이터 저장, 테스트를 반드시 포함합니다.
4. 별도의 .venv를 만들지 않고 01_python-git-foundation의 공통 .venv를 사용합니다.
5. 실행 방법과 파일 역할을 README에 정리합니다.
```

## 과제에서 확인하는 역량

```text
함수:
  질문 정리, 입력 검증, 응답 생성 같은 처리를 함수로 나눌 수 있는지 확인합니다.

모듈과 패키지:
  main.py, config.py, services.py, storage.py처럼 파일 역할을 나눌 수 있는지 확인합니다.

예외 처리:
  빈 질문, 잘못된 입력, 파일이 없는 상황을 안전하게 처리할 수 있는지 확인합니다.

데이터 처리:
  dict/list 데이터를 JSON 또는 CSV로 저장하고 다시 읽을 수 있는지 확인합니다.

테스트:
  pytest로 핵심 함수가 예상대로 동작하는지 확인할 수 있는지 봅니다.

프로젝트 구조:
  이후 FastAPI와 Supabase 프로젝트로 확장하기 쉬운 구조인지 확인합니다.
```
