# Lab 03 - 대화와 메시지 데이터 구조

이 실습은 `conversations`와 `messages`를 왜 나누어 저장하는지 확인합니다.

## 목표

- `conversations`는 대화 묶음, `messages`는 개별 메시지라는 것을 설명할 수 있습니다.
- `messages.conversation_id`가 `conversations.id`와 연결된다는 점을 이해합니다.
- `role` 값으로 user/assistant/system 메시지를 구분할 수 있습니다.

## 실행 방법

```powershell
cd C:\aidev\01_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
python .\07_backend-service-data-management\02_conversation-history\01_conversation_schema_example.py
```

## 확인 기준

- 대화 묶음 dict가 출력됩니다.
- 메시지 목록이 user/assistant 역할과 함께 출력됩니다.
- 하나의 대화에 여러 메시지가 연결되는 구조를 설명할 수 있습니다.

## 정리 질문

- 대화 이력을 한 테이블에 모두 저장하지 않는 이유는 무엇인가요?
- 이전 대화 목록 화면을 만들 때 먼저 조회할 테이블은 무엇인가요?
