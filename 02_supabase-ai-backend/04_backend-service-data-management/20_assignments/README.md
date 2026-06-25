# 20_assignments

이 폴더는 `04_backend-service-data-management` 과정의 과제를 정리하는 공간입니다.

`10_labs`가 예제를 실행하며 따라 하는 실습이라면, `20_assignments`는 사용자 프로필, 대화 이력, 서비스 로그, FastAPI endpoint를 직접 설계하고 설명하는 제출 과제입니다.

## 과제 목록

| 순서 | 폴더 | 주제 | 핵심 제출물 |
|---|---|---|---|
| 1 | `assignment-01_service-data-classification` | 서비스 데이터 저장 위치 분류 | Supabase/Redis 분류표 |
| 2 | `assignment-02_user-profile-design` | 사용자 프로필 데이터 설계 | `profiles` 설계 문서 |
| 3 | `assignment-03_conversation-history-design` | 대화 이력 테이블 설계 | `conversations`, `messages` 설계 문서 |
| 4 | `assignment-04_service-log-design` | 서비스 로그 설계 | `service_logs`와 event_type 설계 |
| 5 | `assignment-05_fastapi-endpoint-design` | FastAPI endpoint 설계 | API 요청/응답 설계서 |
| 99 | `assignment-99_service-data-management-mini-design` | 서비스 데이터 통합 설계 | 미니 서비스 데이터 설계서 |

## 공통 제출 형식

Markdown 문서로 작성합니다.

```text
# 과제 제목

## 1. 과제 목표
## 2. 설계 내용
## 3. 테이블 또는 API 구조
## 4. 저장 위치 선택 이유
## 5. 오류 또는 예외 상황
## 6. 최종 정리
```

## 공통 평가 기준

- Supabase에 저장할 데이터와 Upstash Redis에 저장할 데이터를 구분했는가?
- 사용자 프로필, 대화 이력, 서비스 로그의 역할을 혼동하지 않았는가?
- 테이블 컬럼의 의미를 서비스 기능과 연결해서 설명했는가?
- FastAPI endpoint의 Method, URL, Request Body, Response Body가 명확한가?
- 민감한 정보를 로그나 문서에 그대로 남기지 않는 기준을 설명했는가?

## 제출 전 점검

- 실제 API key, token, service role key를 문서에 적지 않았습니다.
- 각 테이블에 저장할 데이터 예시를 최소 1개 이상 작성했습니다.
- API 설계에는 정상 응답과 오류 상황을 모두 포함했습니다.
- Supabase와 Upstash Redis의 역할을 구분했습니다.
