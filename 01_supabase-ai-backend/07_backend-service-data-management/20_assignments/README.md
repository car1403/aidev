# Assignments

사용자 정보, 대화 이력, 서비스 로그 설계 과제를 작성합니다.

## Assignment 01 - 서비스 데이터 분류표

다음 데이터를 Supabase에 저장할지, Upstash Redis에 저장할지 분류합니다.

```text
사용자 프로필
대화 이력
AI 응답 피드백
최근 1분 요청 횟수
30초 검색 결과 캐시
서비스 오류 로그
```

각 항목마다 이유를 함께 작성합니다.

## Assignment 02 - 대화 이력 테이블 설계

제출 내용:

- `conversations` 테이블 컬럼 목록
- `messages` 테이블 컬럼 목록
- 두 테이블의 관계
- 메시지 role 값의 종류
- 특정 대화방의 메시지를 시간순으로 조회하는 방법

## Assignment 03 - 서비스 로그 설계

제출 내용:

- `event_type` 예시 5개
- `metadata`에 넣을 수 있는 값 5개
- 오류 발생 시 저장할 정보
- 민감 정보를 로그에 남기면 안 되는 이유

## Assignment 04 - FastAPI Endpoint 설계

다음 endpoint의 요청/응답 형태를 설계합니다.

```text
GET /profiles/{user_id}
POST /conversations
POST /conversations/{conversation_id}/messages
GET /conversations/{conversation_id}/messages
POST /service-logs
```

각 endpoint마다 다음을 작성합니다.

```text
HTTP Method
URL
Request Body
Response Body
오류 상황
Supabase 테이블
```
