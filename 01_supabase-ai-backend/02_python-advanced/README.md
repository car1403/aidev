# 02_python-advanced

`01_python-basic`을 마친 뒤, 파이썬 코드를 더 구조적으로 작성하는 방법을 배우는 과정입니다.

이 과정의 목표는 단순 문법을 넘어서 **함수, 모듈, 예외 처리, 클래스, API, 테스트, 프로젝트 구조**를 익히고 작은 실무형 프로그램을 만들 수 있게 되는 것입니다.

## 이 과정에서 배우는 것

```text
함수 심화
모듈과 패키지
requirements.txt와.venv
예외 처리와 디버깅
클래스와 객체지향 프로그래밍
컴프리헨션과 이터레이터
CSV/JSON/날짜/경로 처리
HTTP API와 외부 데이터
비동기 처리(async/await)와 외부 API 동시 호출
테스트와 코드 품질
파이썬 프로젝트 구조
고급 미니 프로젝트
```

## 전체 구조

```text
02_python-advanced
├─ README.md
├─ SETUP.md
├─ requirements.txt
├─.gitignore
├─ 00_references
├─ 01_function-advanced
├─ 02_module-package-venv
├─ 03_exception-debugging
├─ 04_oop-basic
├─ 05_comprehension-iterator
├─ 06_data-processing-advanced
├─ 07_api-external-data
├─ 08_testing-code-quality
├─ 09_project-structure
├─ 10_labs
├─ 20_assignments
└─ 99_advanced-mini-project
```

## 권장 학습 순서

```text
00_references
-> 01_function-advanced
-> 02_module-package-venv
-> 03_exception-debugging
-> 04_oop-basic
-> 05_comprehension-iterator
-> 06_data-processing-advanced
-> 07_api-external-data
-> 08_testing-code-quality
-> 09_project-structure
-> 10_labs
-> 20_assignments
-> 99_advanced-mini-project
```

## 단원별 핵심 내용

| 단원 | 내용 |
| --- | --- |
| 00_references | 고급 과정 로드맵, 프로젝트 사고방식, 오류/디버깅 가이드 |
| 01_function-advanced | 가변 매개변수, 키워드 인자, 람다, `map`, `filter`, 재귀 기초 |
| 02_module-package-venv | `import`, 표준 라이브러리, 직접 만든 모듈, 패키지 구조, `.venv` |
| 03_exception-debugging | `try/except`, `else/finally`, `raise`, 안전한 입력 처리 |
| 04_oop-basic | 클래스, 객체, 생성자, 인스턴스 변수, 메서드, 상속 |
| 05_comprehension-iterator | list/dict comprehension, generator, iterable/iterator |
| 06_data-processing-advanced | CSV, JSON, 날짜/시간, `pathlib` |
| 07_api-external-data | HTTP GET/POST, JSON 응답 처리, Open-Meteo 날씨 API 호출, `async/await` 기반 동시 요청 |
| 08_testing-code-quality | `assert`, pytest 기초, 타입 힌트, 리팩토링 |
| 09_project-structure | `main.py`, package, config, README, Git 관리 |
| 99_advanced-mini-project | JSON 기반 CLI 주소록 미니 프로젝트 |

## 처음 시작하는 방법

```powershell
cd C:\aidev\02_python-advanced
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python --version
pip install -r requirements.txt
```

## 01_python-basic과의 차이

```text
01_python-basic:
 문법을 배우고 작은 프로그램을 만들기

02_python-advanced:
 코드를 함수, 모듈, 클래스, 테스트, 프로젝트 구조로 정리하기
```

## 초보자에서 다음 단계로 넘어갈 때 중요한 생각

### 1. 코드를 나누는 이유를 이해합니다

작은 예제는 한 파일에 써도 됩니다. 하지만 프로그램이 커지면 역할별로 나누어야 합니다.

```text
입력 처리
데이터 처리
파일 저장
화면 출력
테스트
```

### 2. 오류를 미리 예상합니다

사용자가 잘못 입력할 수 있고, 파일이 없을 수 있고, API가 실패할 수 있습니다. 고급 과정에서는 이런 상황을 코드에 반영합니다.

### 3. 재사용 가능한 코드를 만듭니다

함수, 클래스, 모듈은 코드를 다시 쓰기 쉽게 만드는 도구입니다.

### 4. 실행뿐 아니라 검증까지 생각합니다

프로그램이 한 번 실행되는 것보다 중요한 것은, 여러 입력에서도 안정적으로 동작하는지 확인하는 것입니다.

## 추천 학습 방식

1. 각 단원 README를 읽습니다.
2. 예제 코드를 실행합니다.
3. 예제 값을 바꿔봅니다.
4. `10_labs` 실습을 풉니다.
5. `99_advanced-mini-project`에서 JSON 기반 CLI 앱을 완성합니다.
