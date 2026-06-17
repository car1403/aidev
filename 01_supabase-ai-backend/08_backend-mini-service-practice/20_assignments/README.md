# Assignments

백엔드 미니 서비스 설계와 구현 결과를 제출합니다.

## Assignment 01 - 요구사항 정리

제출 내용:

- 서비스 이름
- 사용자 시나리오
- 필수 기능 5개 이상
- 제외 범위
- 수업 예제에서 mock을 먼저 사용하는 이유

## Assignment 02 - API 설계

다음 endpoint를 설계합니다.

```text
GET /health
POST /qa
GET /qa
GET /qa/{item_id}
GET /service-logs
```

각 endpoint마다 작성할 것:

```text
HTTP Method
URL
Request Body
Response Body
오류 상황
저장 테이블
```

## Assignment 03 - Supabase 테이블 설계

제출 내용:

- `mini_qa_items` 테이블 컬럼 설명
- `mini_service_logs` 테이블 컬럼 설명
- index가 필요한 이유
- RLS를 나중에 적용한다면 어떤 기준으로 정책을 만들지

## Assignment 04 - 구현 결과 보고서

제출 내용:

- mock 서버 실행 결과
- `POST /qa` 요청/응답 예시
- `GET /service-logs` 결과
- Supabase 저장 버전 실행 여부
- 오류가 발생했다면 원인과 해결 과정

## Assignment 05 - Codex 코드 리뷰 기록

제출 내용:

- Codex에게 리뷰를 요청한 코드 파일
- Codex가 지적한 개선점
- 실제 반영한 수정 사항
- 아직 반영하지 않은 이유
