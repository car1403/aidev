# 02. CRUD API 구성

CRUD는 데이터를 다루는 가장 기본적인 네 가지 작업입니다.

```text
Create: 생성
Read: 조회
Update: 수정
Delete: 삭제
```

04 미니 프로젝트에서는 모든 CRUD를 한 번에 완성하려고 하기보다, 아래 순서로 진행합니다.

## 1단계: 조회 API

```text
GET /api/conversations
GET /api/conversations/{conversation_id}/messages
```

먼저 조회 API를 만들면 화면에서 데이터를 표시하는 흐름을 쉽게 확인할 수 있습니다.

## 2단계: 생성 API

```text
POST /api/conversations
POST /api/conversations/{conversation_id}/messages
```

사용자 입력을 받아 Supabase에 저장하는 흐름을 확인합니다.

## 3단계: 로그 API

```text
POST /api/service-logs
```

API 호출 성공, 실패, 오류 메시지, 실행 시간을 저장합니다.

## 4단계: 피드백 API

```text
POST /api/feedbacks
```

AI 응답에 대한 사용자 평가를 저장합니다.

## 실습 팁

- 처음에는 인증을 붙이지 않고 로컬에서 흐름을 확인합니다.
- 데이터가 저장되는지 Supabase Table Editor에서 직접 확인합니다.
- 그다음 RLS와 인증을 붙입니다.
- `service role key`는 FastAPI에서만 사용합니다.
