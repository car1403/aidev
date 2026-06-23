# Assignment 99 - 서비스 데이터 관리 미니 설계

`07_backend-service-data-management`에서 배운 내용을 바탕으로 작은 AI 서비스의 데이터 관리 구조를 설계하는 최종 과제입니다.

## 목표

- 사용자 프로필, 대화 이력, 서비스 로그를 하나의 서비스 흐름으로 연결할 수 있습니다.
- Supabase와 Upstash Redis의 역할을 구분한 통합 설계서를 작성할 수 있습니다.
- mock 응답과 Gemini SDK 응답을 같은 데이터 구조로 저장할 수 있도록 설계합니다.
- 이후 `08_backend-mini-service-practice` 또는 `03_supabase-ai-mini-project`로 확장할 수 있는 설계를 만듭니다.

## 프로젝트 주제 예시

```text
개인 학습 AI 챗봇
고객 문의 기록 챗봇
문서 요약 이력 관리 서비스
AI 답변 품질 피드백 서비스
서비스 로그 대시보드 API
```

## 제출물

아래 내용을 포함해 작성합니다.

```text
1. 서비스 주제
2. 사용자 시나리오
3. profiles 테이블 설계
4. conversations/messages 테이블 설계
5. service_logs 테이블 설계
6. FastAPI endpoint 목록
7. Supabase에 저장할 데이터
8. Upstash Redis에 저장할 데이터
9. LLM 응답 저장 metadata 설계
10. 오류 상황과 로그 저장 전략
11. 다음 미니 프로젝트로 확장할 기능
```

## 제출 문서 권장 구조

```text
# 프로젝트명

## 1. 서비스 개요
## 2. 사용자 흐름
## 3. 데이터 저장 구조
## 4. API 설계
## 5. 로그와 오류 처리
## 6. LLM 응답 저장 metadata
## 7. Supabase와 Redis 역할 분리
## 8. 확장 계획
```

## 확인 기준

- 서비스 주제가 명확합니다.
- 데이터 저장 위치가 Supabase와 Redis로 구분되어 있습니다.
- endpoint 목록이 실제 구현 가능한 수준입니다.
- 로그 설계에 성공/오류 상황이 모두 포함되어 있습니다.
- `provider`, `model`, `actual_api_called`, `llm_call_mode` 기준이 포함되어 있습니다.
