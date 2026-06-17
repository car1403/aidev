"""LLM message 구조 이해 예제.

실제 API를 호출하지 않고, LLM API에 보낼 message 목록의 구조만 확인합니다.
"""


# system 메시지는 모델의 역할과 규칙을 정합니다.
# 예를 들어 "강사처럼 설명해라", "짧게 답해라", "한국어로 답해라" 같은 기준을
# 사용자의 질문과 분리해서 전달할 수 있습니다.
system_message = {
    "role": "system",
    "content": "당신은 Python과 FastAPI를 쉽게 설명하는 강사입니다.",
}


# user 메시지는 사용자가 모델에게 보내는 질문입니다.
# 실제 서비스에서는 사용자가 입력창에 작성한 내용이 이 위치에 들어갑니다.
user_message = {
    "role": "user",
    "content": "FastAPI에서 GET과 POST의 차이를 초보자에게 설명해 주세요.",
}


# LLM API는 보통 메시지 1개가 아니라 "메시지 목록"을 받습니다.
# 목록의 순서가 대화 순서이므로, 오래된 메시지부터 최신 메시지 순서로 넣습니다.
messages = [system_message, user_message]


print("LLM API에 전달할 messages 예시")
print("-" * 40)

for index, message in enumerate(messages, start=1):
    # enumerate(..., start=1)은 사람이 읽기 쉬운 번호를 붙이기 위해 사용합니다.
    print(f"{index}. role: {message['role']}")
    print(f"   content: {message['content']}")


print("\n핵심:")
print("LLM API는 role/content 구조의 메시지를 받는 경우가 많습니다.")
print("멀티턴 대화에서는 이전 user/assistant 메시지를 이 목록에 계속 추가합니다.")
