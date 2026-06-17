# Table Design

## mini_qa_items

사용자의 질문과 AI 답변을 저장합니다.

| 컬럼 | 설명 |
| --- | --- |
| `id` | 질문/답변 기록의 고유 id |
| `user_id` | 사용자를 구분하기 위한 값 |
| `question` | 사용자가 보낸 질문 |
| `answer` | AI가 생성한 답변 |
| `model` | 답변 생성에 사용한 모델 이름 |
| `created_at` | 저장 시간 |

## mini_service_logs

서비스 실행 결과를 저장합니다.

| 컬럼 | 설명 |
| --- | --- |
| `id` | 로그 고유 id |
| `event_type` | 로그 종류 |
| `message` | 사람이 읽을 수 있는 로그 메시지 |
| `metadata` | endpoint, item_id, 모델명 등 추가 정보 |
| `created_at` | 저장 시간 |
