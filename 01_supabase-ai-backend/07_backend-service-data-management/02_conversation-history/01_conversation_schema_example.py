"""대화 이력 데이터 구조를 이해하는 예제.

이 파일은 Supabase에 접속하지 않습니다.
대화방(conversation)과 메시지(message)를 왜 나누어 저장하는지 확인합니다.
"""


conversation = {
    "id": "conversation-001",
    "user_id": "user-001",
    "title": "FastAPI 질문",
}

messages = [
    {
        "conversation_id": "conversation-001",
        "role": "user",
        "content": "FastAPI에서 Pydantic은 왜 사용하나요?",
    },
    {
        "conversation_id": "conversation-001",
        "role": "assistant",
        "content": "요청 데이터 검증과 응답 구조 정의를 쉽게 하기 위해 사용합니다.",
    },
]


print("대화방:")
print(conversation)

print("\n메시지 목록:")
for message in messages:
    # role을 함께 저장해야 user 질문과 assistant 답변을 구분할 수 있습니다.
    print(f"[{message['role']}] {message['content']}")
