# 08_testing-code-quality

이 단원에서는 테스트와 코드 품질을 본 과정에서 필요한 만큼만 다룹니다.

목표는 pytest를 깊게 배우는 것이 아니라, 함수가 예상대로 동작하는지 자동으로 확인하고, 리팩토링 후 기존 기능이 깨지지 않았는지 점검하는 것입니다.

## 이 단원에서 배우는 것

| 파일 | 핵심 내용 | 과정 연결 |
| --- | --- | --- |
| 01_assert_basic.py | `assert` 기본 사용 | 함수 결과를 직접 검증 |
| service_logic.py | 테스트 대상 서비스 함수 | 질문 검증, 응답 dict 생성 |
| test_service_logic.py | pytest 테스트 | 정상/오류/응답 구조 테스트 |

## 실행 전 준비

이 폴더에서는 별도의 `.venv`를 만들지 않습니다. `01_supabase-ai-backend` 최상위에서 만든 공통 가상환경을 사용합니다.

```powershell
cd C:\aidev\01_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
```

pytest는 최상위 `requirements.txt`에 포함되어 있습니다.

```powershell
pip install -r requirements.txt
```

## 실행 방법

```powershell
python .\02_python-advanced\08_testing-code-quality\01_assert_basic.py
python -m pytest .\02_python-advanced\08_testing-code-quality
```

## 핵심 확인

```text
assert:
  예상한 값과 실제 값이 같은지 확인합니다.

pytest:
  test_*.py 파일을 찾아 테스트 함수를 실행합니다.

pytest.raises:
  특정 오류가 발생해야 정상인 경우를 테스트합니다.

리팩토링:
  코드 내부 구조를 바꿔도 테스트가 통과하면 기존 기능이 유지되는지 확인할 수 있습니다.
```

## 본 과정에서 테스트가 필요한 이유

```text
FastAPI 요청 검증 함수가 잘 동작하는지 확인합니다.
LLM 질문이 비어 있을 때 오류 처리되는지 확인합니다.
API 응답 dict에 필요한 key가 있는지 확인합니다.
Supabase 저장 전 데이터 형태가 맞는지 확인합니다.
미니 프로젝트 수정 후 기존 기능이 깨지지 않았는지 확인합니다.
```
