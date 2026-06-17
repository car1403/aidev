# 02. Conversation History

사용자 질문, AI 응답, 생성 시간, 모델 정보를 대화 이력으로 저장하는 구조를 설계합니다.

## 대화 이력을 나누어 저장하는 이유

AI 서비스에서는 보통 대화방과 메시지를 분리합니다.

```text
conversations
-> 대화방 자체의 정보
-> 제목, 사용자 id, 생성 시간

messages
-> 대화방 안의 개별 메시지
-> role, content, model, 생성 시간
```

이렇게 나누면 한 사용자가 여러 대화방을 가질 수 있고, 각 대화방 안에 여러 메시지를 순서대로 저장할 수 있습니다.

## 실습 파일

```text
01_conversation_schema_example.py
-> 대화방과 메시지 데이터 구조를 Python dict로 이해합니다.

02_save_conversation_message.py
-> Supabase에 대화방과 메시지를 저장합니다.

03_list_conversation_messages.py
-> Supabase에서 특정 대화방의 메시지를 조회합니다.
```
