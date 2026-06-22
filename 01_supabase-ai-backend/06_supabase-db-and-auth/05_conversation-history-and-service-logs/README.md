# 05_conversation-history-and-service-logs

이 단원은 Supabase에 사용자 대화 이력과 서비스 로그를 저장하는 구조를 설계합니다.

## 학습 목표

- 대화 세션과 메시지 테이블을 분리해 설계합니다.
- 서비스 실행 로그를 저장하는 테이블을 설계합니다.
- FastAPI에서 요청 처리 결과를 Supabase에 기록하는 흐름을 이해합니다.
- Upstash Redis에 저장할 임시 데이터와 Supabase에 저장할 영구 데이터를 구분합니다.

## 추천 테이블 구조

```text
conversations
- id
- user_id
- title
- created_at

messages
- id
- conversation_id
- role
- content
- created_at

service_logs
- id
- user_id
- event_type
- message
- metadata
- created_at
```

## Supabase와 Upstash Redis 역할 구분

이 단원에서는 대화 이력과 서비스 로그를 Supabase에 저장합니다. 이 데이터는 나중에 다시 조회하거나 분석해야 하므로 오래 보관할 수 있어야 합니다.

```text
대화 이력/서비스 로그/피드백
-> Supabase 테이블에 저장
-> FastAPI에서 조회
-> Streamlit 또는 API client에서 확인
```

Upstash Redis는 다음 챕터에서 임시 데이터 용도로 사용합니다.

```text
캐시/TTL/요청 횟수 제한/임시 세션 상태
-> Upstash Redis에 저장
-> 일정 시간이 지나면 자동 만료 가능
```

Docker 기반 Redis 운영은 `C:\aidev\06_multi-agent-service-ops`에서 다룹니다.

## 실습 파일

```text
01_insert_conversation_and_log.py
-> 대화 세션, 메시지, 서비스 로그를 Supabase에 저장하는 흐름을 실습합니다.
```

실행:

```powershell
cd C:\aidev\01_supabase-ai-backend
.\.venv\Scripts\Activate.ps1
python.\06_supabase-db-and-auth\05_conversation-history-and-service-logs\01_insert_conversation_and_log.py
```

## 핵심 확인 사항

- 대화방 자체는 `conversations`에 저장합니다.
- 대화방 안의 질문/답변은 `messages`에 여러 행으로 저장합니다.
- 오류, 처리 시간, 호출한 기능 이름 같은 운영 기록은 `service_logs`에 저장합니다.
- Redis에는 "최근 상태"나 "잠깐 필요한 값"을 저장하고, 나중에 다시 봐야 하는 기록은 Supabase에 저장합니다.
