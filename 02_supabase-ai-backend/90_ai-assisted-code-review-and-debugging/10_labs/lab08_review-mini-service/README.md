# Lab 08 - 미니 서비스 종합 리뷰

이 lab에서는 `05_backend-mini-service-practice`에서 만든 미니 서비스를 Codex와 함께 종합 리뷰합니다.

이전 lab이 파일 하나를 중심으로 진행되었다면, 이번 lab은 요구사항, API 설계, SQL 스키마, mock-first 구현, Supabase 구현, 로그 저장 흐름을 함께 확인합니다.

## 실습 목표

- 미니 서비스의 목적과 요구사항을 정리할 수 있다.
- mock-first 구현과 Supabase 구현의 차이를 설명할 수 있다.
- API 설계와 실제 코드가 일치하는지 확인할 수 있다.
- 서비스 로그가 충분한 정보를 담는지 점검할 수 있다.
- 최종 프로젝트로 확장하기 전 개선 항목을 정리할 수 있다.

## 리뷰 대상

```text
C:\aidev\02_supabase-ai-backend\05_backend-mini-service-practice\01_requirements\README.md
C:\aidev\02_supabase-ai-backend\05_backend-mini-service-practice\02_api-design\README.md
C:\aidev\02_supabase-ai-backend\05_backend-mini-service-practice\03_supabase-schema\mini-service-schema.sql
C:\aidev\02_supabase-ai-backend\05_backend-mini-service-practice\04_implementation-guide\main_mock.py
C:\aidev\02_supabase-ai-backend\05_backend-mini-service-practice\04_implementation-guide\main_supabase.py
C:\aidev\02_supabase-ai-backend\05_backend-mini-service-practice\04_implementation-guide\schemas.py
```

## 실습 절차

1. 요구사항 문서를 읽고 서비스 목적을 한 문장으로 정리합니다.
2. API 설계 문서에서 endpoint 목록을 확인합니다.
3. SQL 스키마와 Python 코드의 테이블명, 컬럼명을 비교합니다.
4. `main_mock.py`와 `main_supabase.py`의 공통 흐름을 찾습니다.
5. Supabase 버전에서 추가로 필요한 오류 처리와 보안 기준을 확인합니다.
6. 서비스 로그가 성공, 실패, 오류 상황을 구분하는지 확인합니다.
7. Codex에게 종합 리뷰를 요청합니다.
8. 최종 프로젝트 전 개선 항목을 정리합니다.

## Codex 요청 예시

```text
05_backend-mini-service-practice의 미니 서비스를 종합 리뷰해주세요.

리뷰 대상:
1. 요구사항 문서
2. API 설계 문서
3. Supabase SQL 스키마
4. main_mock.py
5. main_supabase.py
6. schemas.py

리뷰 관점:
1. 요구사항과 endpoint가 일치하는가?
2. mock-first 구현과 Supabase 구현의 차이가 명확한가?
3. Pydantic 모델이 요청/응답 구조를 충분히 표현하는가?
4. Supabase 테이블명과 컬럼명이 코드와 일치하는가?
5. 서비스 로그가 운영에 필요한 정보를 담는가?
6. 오류 응답이 명확한가?
7. 최종 프로젝트로 확장하기 쉬운 구조인가?

출력 형식:
- 치명적인 문제
- 수정이 필요한 문제
- 개선하면 좋은 문제
- 최종 프로젝트 전 확인 질문
- 실행 또는 테스트 방법

아직 코드를 수정하지 말고 리뷰 결과만 정리해주세요.
```

## 결과 정리

```md
## Lab 08 결과

- 서비스 목적:
- 검토한 파일:
- 요구사항과 일치하지 않는 부분:
- Supabase 구현에서 주의할 부분:
- 서비스 로그 보강이 필요한 부분:
- 최종 프로젝트 전 개선 항목:
- 실행 또는 테스트 방법:
```

## 완료 체크리스트

- [ ] 요구사항과 API 설계를 함께 확인했다.
- [ ] SQL 스키마와 Python 코드의 이름을 비교했다.
- [ ] mock-first 구현과 Supabase 구현을 비교했다.
- [ ] 서비스 로그와 오류 응답을 점검했다.
- [ ] 최종 프로젝트 전 개선 항목을 정리했다.
