# 05. 대화 이력과 서비스 로그 저장

이 챕터에서는 AI 서비스에서 생성되는 **대화 이력**과 **서비스 로그**를 Supabase에 저장하는 구조를 배웁니다.

앞 단원에서 `learning_notes` 테이블로 기본 CRUD를 익혔다면, 이번에는 실제 AI 챗봇 서비스에 더 가까운 데이터 구조를 다룹니다. 사용자의 질문, AI의 답변, 서비스 실행 기록을 각각 어떤 테이블에 저장하면 좋은지 확인합니다.

## 학습 목표

- 대화 세션과 메시지를 분리해서 저장하는 이유를 이해합니다.
- `conversations`, `messages`, `service_logs` 테이블의 역할을 구분합니다.
- FastAPI에서 요청 처리 결과를 Supabase에 기록하는 흐름을 이해합니다.
- AI 서비스 운영에서 서비스 로그가 왜 필요한지 이해합니다.
- Supabase에 저장할 영구 데이터와 Upstash Redis에 저장할 임시 데이터를 구분합니다.

## 전체 흐름

```text
사용자 질문
-> FastAPI endpoint
-> mock 응답 생성 또는 Gemini SDK 응답 생성
-> conversations 테이블에 대화방 정보 저장
-> messages 테이블에 사용자/AI 메시지 저장
-> service_logs 테이블에 실행 기록 저장
-> 이후 화면에서 대화 이력 조회
```

이 챕터는 Supabase에 오래 보관할 데이터를 다룹니다. 캐시, TTL, 요청 횟수 제한 같은 임시 데이터는 다음 챕터의 Upstash Redis에서 다룹니다.

## 02_llm-api-integration 변경 사항과의 연결

앞 단원인 `02_llm-api-integration`에서는 LLM 호출 흐름을 아래 기준으로 정리했습니다.

```text
1. mock으로 요청/응답 구조를 먼저 확인합니다.
2. 실제 프로젝트 기본 구현은 Gemini SDK 방식을 사용합니다.
3. Gemini SDK 안내형 예제에서는 key 확인과 오류 안내를 함께 다룹니다.
4. OpenAI 방식은 선택 비교 예제로 둡니다.
```

따라서 이 챕터에서 Supabase에 저장하는 `messages`와 `service_logs`는 특정 호출 방식에만 묶이지 않도록 설계합니다. 예제 코드는 비용 없이 확인할 수 있도록 `actual_api_called=false`인 mock 응답을 저장하지만, 같은 구조는 `02_llm-api-integration/05_fastapi-llm-endpoint/03_gemini_sdk_endpoint.py`에서 생성한 Gemini SDK 응답에도 그대로 사용할 수 있습니다.

## 테이블 역할

| 테이블 | 역할 | 예시 |
| --- | --- | --- |
| `conversations` | 대화방 또는 대화 세션 | “FastAPI 질문 대화”, “오늘 학습 상담” |
| `messages` | 대화방 안의 사용자/AI 메시지 | user 질문, assistant 답변, system 지시 |
| `service_logs` | 서비스 실행 기록 | 대화 생성, API 호출, 오류, 처리 시간 |

## 추천 테이블 구조

Supabase SQL Editor에서 아래 구조가 준비되어 있어야 합니다.

```sql
create table if not exists conversations (
  id uuid primary key default gen_random_uuid(),
  user_id uuid,
  title text not null,
  created_at timestamptz not null default now()
);

create table if not exists messages (
  id uuid primary key default gen_random_uuid(),
  conversation_id uuid references conversations(id) on delete cascade,
  role text not null check (role in ('user', 'assistant', 'system')),
  content text not null,
  created_at timestamptz not null default now()
);

create table if not exists service_logs (
  id uuid primary key default gen_random_uuid(),
  user_id uuid,
  event_type text not null,
  message text not null,
  metadata jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now()
);
```

전체 스키마는 아래 파일에서도 확인할 수 있습니다.

```text
03_supabase-db-and-auth/00_references/supabase-schema.sql
```

## 왜 conversations와 messages를 나누나요?

대화방 1개에는 여러 메시지가 들어갑니다.

```text
conversations 1개
-> messages 여러 개
```

예를 들어 하나의 대화방 안에 다음 메시지가 쌓일 수 있습니다.

```text
user: Supabase에는 어떤 데이터를 저장하면 좋나요?
assistant: 대화 이력, 서비스 로그, 사용자 피드백처럼 나중에 다시 볼 데이터가 좋습니다.
user: Redis와는 어떻게 다르죠?
assistant: Redis는 짧게 보관하는 캐시나 임시 상태에 적합합니다.
```

대화방 정보와 메시지를 한 테이블에 모두 넣으면 나중에 조회와 관리가 어려워집니다. 그래서 대화방 자체는 `conversations`, 실제 메시지는 `messages`에 저장합니다.

## service_logs에는 무엇을 저장하나요?

서비스 로그는 사용자에게 직접 보여주기 위한 대화 내용이 아니라, 서비스를 운영하고 개선하기 위해 남기는 기록입니다.

예시:

```text
conversation.created
message.saved
llm.mock_called
llm.api_called
llm.gemini_sdk_called
error.supabase_insert_failed
```

`metadata` 컬럼은 `jsonb` 타입이므로 구조가 조금씩 다른 부가 정보를 담기 좋습니다.

```json
{
  "conversation_id": "uuid",
  "message_count": 2,
  "provider": "gemini",
  "model": "gemini-2.5-flash-lite",
  "actual_api_called": false
}
```

## Supabase와 Upstash Redis 역할 구분

| 데이터 | 저장 위치 | 이유 |
| --- | --- | --- |
| 대화방 목록 | Supabase | 나중에 다시 조회해야 합니다. |
| 사용자 질문과 AI 답변 | Supabase | 대화 이력으로 오래 보관합니다. |
| 서비스 실행 로그 | Supabase | 오류 분석, 품질 개선, 운영 점검에 사용합니다. |
| 짧은 캐시 | Upstash Redis | 빠르게 조회하고 일정 시간이 지나면 만료되어도 됩니다. |
| 요청 횟수 제한 | Upstash Redis | 1분/1시간 단위 카운터처럼 임시 값에 적합합니다. |
| 임시 세션 상태 | Upstash Redis | 오래 보관할 필요 없는 상태에 적합합니다. |

기준은 다음처럼 기억하면 쉽습니다.

```text
나중에 다시 조회하고 분석해야 한다 -> Supabase
잠깐만 빠르게 보관하고 만료되어도 된다 -> Upstash Redis
```

Docker 기반 Redis 운영은 `C:\aidev\07_multi-agent-service-ops`에서 다룹니다.

## 실행 전 준비

Supabase 환경 변수를 확인합니다.

```powershell
cd C:\aidev\02_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
python .\03_supabase-db-and-auth\01_supabase-project-and-env\01_check_supabase_env.py
```

Supabase SQL Editor에서 `conversations`, `messages`, `service_logs` 테이블이 있는지 확인합니다.

## 예제 실행

```powershell
cd C:\aidev\02_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
python .\03_supabase-db-and-auth\05_conversation-history-and-service-logs\01_insert_conversation_and_log.py
```

이 예제는 다음 순서로 동작합니다.

```text
1. conversations 테이블에 대화방을 1개 만듭니다.
2. messages 테이블에 사용자 메시지를 저장합니다.
3. messages 테이블에 AI 응답 메시지를 저장합니다.
4. service_logs 테이블에 실행 로그를 저장합니다.
5. 방금 저장한 메시지와 로그를 다시 조회합니다.
```

## Supabase 화면에서 확인할 것

실행 후 Supabase Table Editor에서 다음을 확인합니다.

```text
conversations:
  새 대화방이 생성되었는가?

messages:
  같은 conversation_id를 가진 user/assistant 메시지가 저장되었는가?

service_logs:
  event_type과 metadata가 저장되었는가?
```

## 자주 만나는 문제

### Could not find the table 'public.conversations'

Supabase에 `conversations` 테이블이 아직 만들어지지 않은 상태입니다.

해결 방법:

1. Supabase Dashboard의 SQL Editor를 엽니다.
2. `03_supabase-db-and-auth/00_references/supabase-schema.sql` 파일 내용을 복사합니다.
3. SQL Editor에서 실행합니다.
4. Table Editor에서 `conversations`, `messages`, `service_logs` 테이블이 보이는지 확인합니다.
5. 예제 파일을 다시 실행합니다.

### messages 저장이 실패하는 경우

`messages.conversation_id`는 `conversations.id`를 참조합니다. 먼저 `conversations`에 대화방이 만들어져야 메시지를 저장할 수 있습니다.

### role 값 오류가 나는 경우

`messages.role`은 아래 세 값 중 하나여야 합니다.

```text
user
assistant
system
```

### metadata 저장이 헷갈리는 경우

`service_logs.metadata`는 `jsonb` 컬럼입니다. Python 딕셔너리를 그대로 전달하면 Supabase가 JSON 형태로 저장합니다.

## 다음 단계와 연결

이 챕터에서 만든 구조는 다음 과정으로 이어집니다.

| 다음 단계 | 연결 내용 |
| --- | --- |
| `06_upstash-redis-cache-and-session` | 임시 캐시, TTL, 요청 횟수 제한 |
| `03_supabase-ai-frontend` | Streamlit 화면에서 대화 이력 조회 |
| `04_supabase-ai-mini-project` | 실시간 로그 대시보드와 최종 프로젝트 |

## 완료 체크리스트

```text
[ ] conversations 테이블의 역할을 설명할 수 있습니다.
[ ] messages 테이블의 역할을 설명할 수 있습니다.
[ ] service_logs 테이블의 역할을 설명할 수 있습니다.
[ ] Supabase와 Upstash Redis에 저장할 데이터를 구분할 수 있습니다.
[ ] 예제 파일을 실행했습니다.
[ ] Supabase Table Editor에서 대화방, 메시지, 로그를 확인했습니다.
```
