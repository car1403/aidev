# Lab 99 - 서비스 데이터 관리 점검표

이 실습은 `07_backend-service-data-management` 전체 내용을 마무리하며 데이터 저장 위치와 API 흐름을 점검하는 활동입니다.

## 점검표

| 항목 | 확인 |
|---|---|
| 사용자 프로필은 Supabase `profiles`에 저장한다. |  |
| 대화 묶음은 Supabase `conversations`에 저장한다. |  |
| 개별 메시지는 Supabase `messages`에 저장한다. |  |
| 서비스 로그는 Supabase `service_logs`에 저장한다. |  |
| 짧은 캐시와 요청 제한은 Upstash Redis에 저장한다. |  |
| mock API와 Supabase API의 차이를 설명할 수 있다. |  |
| Swagger UI에서 endpoint를 테스트할 수 있다. |  |
| 민감한 key를 로그나 README에 적지 않는다. |  |

## 최종 정리 질문

- `profiles`, `conversations`, `messages`, `service_logs` 중 가장 먼저 설계해야 하는 테이블은 무엇인가요?
- 사용자 질문과 AI 답변을 저장할 때 어떤 순서로 API가 호출되나요?
- 서비스 로그는 이후 배포와 운영에서 어떤 역할을 하나요?
- 이 단원의 API를 `03_supabase-ai-mini-project`로 연결하려면 어떤 화면과 기능이 필요할까요?
