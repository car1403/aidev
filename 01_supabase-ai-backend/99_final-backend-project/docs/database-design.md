# Database Design

Supabase 테이블, 컬럼, 관계, RLS 정책을 작성합니다.

## 필수 테이블

```text
qa_items
-> 사용자 질문과 AI 답변 저장

service_logs
-> API 처리 로그와 오류 로그 저장
```

## 선택 테이블

```text
profiles
-> 사용자 프로필

feedback
-> AI 답변 평가

conversations/messages
-> 여러 메시지를 대화방 단위로 관리할 때 사용
```

## 작성할 내용

각 테이블마다 아래 항목을 작성합니다.

```text
테이블 목적:
컬럼 목록:
Primary Key:
Foreign Key:
Index:
RLS 적용 여부:
사용 예시:
```

## Supabase와 Upstash Redis 역할 구분

| 데이터 | 저장 위치 | 이유 |
| --- | --- | --- |
| 질문/답변 | Supabase | 나중에 다시 조회해야 합니다. |
| 서비스 로그 | Supabase | 오류 분석과 운영 기록에 필요합니다. |
| 사용자 피드백 | Supabase | 품질 개선에 사용합니다. |
| 30초 캐시 | Upstash Redis | 짧게 재사용하면 됩니다. |
| 요청 횟수 제한 | Upstash Redis | 시간이 지나면 자동 초기화되어도 됩니다. |

Upstash Redis는 선택 사항입니다. 사용하지 않는 경우에도 "왜 사용하지 않았는지"를 설명합니다.
