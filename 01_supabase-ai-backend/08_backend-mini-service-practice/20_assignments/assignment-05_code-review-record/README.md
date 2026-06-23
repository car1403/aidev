# Assignment 05. Code Review Record

## 목표

미니 서비스 구현 코드를 점검하고 개선 기록을 남깁니다.

## 참고 파일

```text
../04_implementation-guide/schemas.py
../04_implementation-guide/main_mock.py
../04_implementation-guide/main_supabase.py
../04_implementation-guide/service_logger.py
```

## 제출 내용

| 항목 | 작성 내용 |
| --- | --- |
| 리뷰한 파일 | 점검한 Python 파일 이름 |
| 확인한 기준 | API 이름, 테이블 이름, 오류 응답, 주석, 보안 기준 등 |
| 발견한 문제 | 수정이 필요한 부분 |
| 수정한 내용 | 실제 반영한 내용 |
| 보류한 내용 | 지금 반영하지 않은 내용과 이유 |

## 점검 기준

- `/questions` API 이름이 일관되게 사용되었나요?
- `mini_questions` 테이블 이름이 일관되게 사용되었나요?
- 오류 응답이 이해하기 쉽게 작성되어 있나요?
- 민감 정보가 로그에 저장되지 않나요?
- 초보자가 읽을 수 있는 주석이 필요한 위치에 있나요?

## 완료 기준

- 최소 2개 이상의 파일을 점검했습니다.
- 개선할 점과 실제 수정한 점이 구분되어 있습니다.
- 보안상 주의할 점이 기록되어 있습니다.
