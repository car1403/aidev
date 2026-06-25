# 02_conversation-history

이 챕터는 AI 서비스에서 사용자 질문과 AI 응답을 대화 이력으로 저장하는 방법을 학습합니다.

AI 챗봇 서비스는 단순히 “현재 질문에 답변”만 하면 끝나지 않습니다. 사용자가 이전 대화를 다시 확인하거나, 이어서 질문하거나, 서비스 품질을 분석하려면 대화 이력을 저장해야 합니다.

## 왜 conversations와 messages를 나누나요?

대화 이력은 보통 `대화 묶음`과 `개별 메시지`를 나누어 저장합니다.

```text
conversations
-> 대화방 또는 대화 세션 자체의 정보
-> 제목, 사용자 id, 생성 시간

messages
-> 대화방 안에서 오간 개별 메시지
-> user 질문, assistant 응답, system 메시지, 생성 시간
```

이렇게 나누면 한 사용자가 여러 대화를 가질 수 있고, 각 대화 안에 여러 메시지를 순서대로 저장할 수 있습니다.

## 테이블 관계

```text
conversations.id
        |
        | messages.conversation_id
        v
messages
```

`messages.conversation_id`는 어떤 메시지가 어떤 대화에 속하는지 알려 주는 연결값입니다.

## Supabase 테이블 준비

아래 SQL 파일에 `conversations`와 `messages` 테이블 생성 구문이 포함되어 있습니다.

```text
C:\aidev\02_supabase-ai-backend\03_supabase-db-and-auth\00_references\supabase-schema.sql
```

Supabase Dashboard의 SQL Editor에서 먼저 실행한 뒤 실습을 진행합니다.

## 실습 파일

| 파일 | 내용 |
|---|---|
| `01_conversation_schema_example.py` | Supabase에 접속하지 않고 대화/메시지 구조를 Python dict로 이해합니다. |
| `02_save_conversation_message.py` | Supabase에 대화 묶음과 user/assistant 메시지를 저장합니다. |
| `03_list_conversation_messages.py` | 특정 대화의 메시지 목록을 생성 시간 순서로 조회합니다. |

## 실행 순서

먼저 구조 예제를 실행합니다. 이 파일은 Supabase에 접속하지 않습니다.

```powershell
cd C:\aidev\02_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
python .\04_backend-service-data-management\02_conversation-history\01_conversation_schema_example.py
```

Supabase에 실제 저장하는 예제는 `.env`와 테이블이 준비된 뒤 실행합니다.

```powershell
python .\04_backend-service-data-management\02_conversation-history\02_save_conversation_message.py
```

저장 예제 실행 후 터미널에 출력된 `conversation_id`를 복사해서 조회 예제에 입력합니다.

```powershell
python .\04_backend-service-data-management\02_conversation-history\03_list_conversation_messages.py
```

## 확인 기준

- `conversations` 테이블에 대화 묶음이 저장됩니다.
- `messages` 테이블에 user 메시지와 assistant 메시지가 저장됩니다.
- `messages.conversation_id`가 `conversations.id`와 연결됩니다.
- 조회 예제에서 같은 대화에 속한 메시지가 순서대로 출력됩니다.

## Supabase와 Redis 저장 기준

대화 이력은 나중에 다시 조회해야 하므로 Supabase에 저장합니다.

Redis는 짧게 유지할 임시 상태나 캐시에 적합합니다. 예를 들어 “최근 30초 동안 같은 질문에 대한 답변 캐시”는 Redis에 둘 수 있지만, 사용자의 전체 대화 기록은 Supabase에 저장하는 것이 좋습니다.

## 정리 질문

- `conversations`와 `messages`를 한 테이블에 합치지 않는 이유는 무엇인가요?
- `role` 값으로 `user`, `assistant`, `system`을 구분하는 이유는 무엇인가요?
- 대화 이력을 Supabase에 저장하고 Redis에 저장하지 않는 이유는 무엇인가요?
- 이후 화면에서 “이전 대화 목록”을 만들려면 어떤 테이블을 먼저 조회해야 할까요?
