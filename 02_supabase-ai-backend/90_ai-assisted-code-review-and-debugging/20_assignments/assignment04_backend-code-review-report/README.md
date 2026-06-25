# Assignment 04 - Backend Code Review Report

이 과제에서는 FastAPI, Supabase, LLM API, Upstash Redis 관련 코드를 Codex와 함께 리뷰하고, 결과를 보고서로 정리합니다.

코드 리뷰 보고서는 단순히 "문제가 있다"라고 적는 문서가 아닙니다. 어떤 파일을 어떤 기준으로 보았고, 어떤 문제를 실제로 수정할지 판단한 내용을 남기는 문서입니다.

## 목표

- 백엔드 코드 리뷰 기준을 직접 적용할 수 있다.
- FastAPI endpoint와 Pydantic 모델을 점검할 수 있다.
- Supabase 테이블명, 컬럼명, update/delete 조건을 확인할 수 있다.
- LLM API 호출과 mock-first 호출을 구분할 수 있다.
- Upstash Redis 활용 여부와 TTL 필요성을 판단할 수 있다.
- Codex 리뷰 결과를 우선순위별로 정리할 수 있다.

## 리뷰 대상 예시

```text
C:\aidev\02_supabase-ai-backend\08_backend-mini-service-practice\04_implementation-guide\main_mock.py
C:\aidev\02_supabase-ai-backend\08_backend-mini-service-practice\04_implementation-guide\main_supabase.py
C:\aidev\02_supabase-ai-backend\08_backend-mini-service-practice\04_implementation-guide\schemas.py
C:\aidev\02_supabase-ai-backend\07_backend-service-data-management\04_fastapi-service-endpoints
```

## 제출 파일

```text
backend-code-review-report.md
```

## Codex 요청 예시

```text
다음 백엔드 코드를 리뷰해주세요.

리뷰 대상:
여기에 파일 경로를 적습니다.

코드 목적:
사용자 질문을 저장하고, AI 응답과 서비스 로그를 관리하는 FastAPI 백엔드 예제입니다.

리뷰 관점:
1. 실행 오류 가능성
2. endpoint URL과 HTTP Method 적절성
3. Pydantic 요청/응답 모델 검증
4. Supabase 테이블명과 컬럼명 일치 여부
5. update/delete 조건 누락 위험
6. LLM API 호출과 mock-first 호출 구분
7. Upstash Redis TTL 또는 key 설계 필요성
8. 서비스 로그의 정보 충분성

출력 형식:
- 치명적인 문제
- 수정이 필요한 문제
- 개선하면 좋은 문제
- 확인 질문
- 실행 또는 테스트 방법

아직 코드를 수정하지 말고 리뷰 결과만 정리해주세요.
```

## 보고서 템플릿

```md
# Backend Code Review Report

## 1. 리뷰 대상

- 파일 또는 폴더:
- 코드 목적:

## 2. 사용한 Codex 요청문

```text
여기에 사용한 요청문을 작성합니다.
```

## 3. Codex가 찾은 문제

### 치명적인 문제

- 

### 수정이 필요한 문제

- 

### 개선하면 좋은 문제

- 

## 4. 직접 판단한 내용

- 동의한 문제:
- 보류한 문제:
- 추가로 확인한 문제:

## 5. 직접 수정한 내용

- 수정한 파일:
- 수정한 이유:
- 수정 후 달라진 점:

## 6. 실행 또는 확인 결과

- 실행 명령:
- 확인 결과:

## 7. 남은 질문

- 
```

## 평가 체크리스트

- [ ] 리뷰 대상 파일을 명확히 적었다.
- [ ] Codex 요청문이 구체적이다.
- [ ] 문제를 치명도별로 분류했다.
- [ ] Codex 의견 중 동의한 내용과 보류한 내용을 구분했다.
- [ ] 직접 확인한 실행 또는 테스트 결과가 있다.
- [ ] 보안이나 비용 관련 확인 항목을 포함했다.
