# Lab 04 - Supabase 대화 이력 저장과 조회

이 실습은 Supabase에 대화 묶음과 메시지를 저장하고, 저장된 메시지를 다시 조회합니다.

## 목표

- `conversations` 테이블에 대화 묶음을 저장할 수 있습니다.
- `messages` 테이블에 user/assistant 메시지를 저장할 수 있습니다.
- `conversation_id`를 사용해 특정 대화의 메시지만 조회할 수 있습니다.

## 실행 방법

먼저 대화와 메시지를 저장합니다.

```powershell
cd C:\aidev\01_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
python .\07_backend-service-data-management\02_conversation-history\02_save_conversation_message.py
```

터미널에 출력되는 `conversation_id`를 복사한 뒤 조회 예제를 실행합니다.

```powershell
python .\07_backend-service-data-management\02_conversation-history\03_list_conversation_messages.py
```

## 확인 기준

- Supabase `conversations` 테이블에 새 대화가 저장됩니다.
- Supabase `messages` 테이블에 user/assistant 메시지가 저장됩니다.
- 조회 예제에서 같은 대화의 메시지가 순서대로 출력됩니다.

## 오류 확인

테이블이 없다는 오류가 나오면 아래 SQL 파일을 Supabase SQL Editor에서 실행합니다.

```text
C:\aidev\01_supabase-ai-backend\06_supabase-db-and-auth\00_references\supabase-schema.sql
```
