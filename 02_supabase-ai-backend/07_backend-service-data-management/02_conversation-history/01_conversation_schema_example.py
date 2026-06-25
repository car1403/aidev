"""대화 이력 데이터 구조를 이해하는 예제.

이 파일은 Supabase에 접속하지 않습니다.
먼저 conversation과 message를 왜 나누어 저장하는지 Python dict로 확인합니다.

핵심 아이디어:
- conversation은 하나의 대화방 또는 대화 세션입니다.
- message는 그 대화 안에서 오간 개별 발화입니다.
- 한 conversation에는 여러 message가 연결될 수 있습니다.
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


print("대화 묶음:")
print(conversation)

print("\n메시지 목록:")
for index, message in enumerate(messages, start=1):
    # role을 함께 저장하면 user 질문과 assistant 응답을 구분할 수 있습니다.
    print(f"{index}. [{message['role']}] {message['content']}")

print("\n관계 설명:")
print("messages의 conversation_id가 conversations의 id와 연결됩니다.")
print("이 구조 덕분에 하나의 대화 안에 여러 메시지를 순서대로 저장할 수 있습니다.")
