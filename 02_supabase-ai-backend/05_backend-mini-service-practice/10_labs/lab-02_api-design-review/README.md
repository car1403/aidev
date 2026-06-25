# Lab 02. API Design Review

## 목표

`/questions` 중심의 API 설계를 확인합니다.

## 확인 파일

```text
../02_api-design/api-design.md
```

## 확인할 API

```text
GET /health
POST /questions
GET /questions
GET /questions/{question_id}
POST /service-logs
GET /service-logs
```

## 확인할 내용

- URL이 리소스 중심으로 작성되어 있나요?
- HTTP Method가 기능에 맞게 사용되었나요?
- 요청 JSON 예시가 있나요?
- 응답 JSON 예시가 있나요?
- 오류 응답 형식이 통일되어 있나요?

## 정리할 내용

`POST /questions`의 요청 필드와 응답 필드를 표로 다시 적어 봅니다.
