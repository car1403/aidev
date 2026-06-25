r"""LLM message 구조 이해 예제입니다.

이 파일은 role/content 기반 메시지 구조를 나누어 읽기 위한 학습용 파일입니다.
실제 API를 호출하지 않으므로 API key와 비용이 필요하지 않습니다.

실행:
    cd C:\aidev\02_supabase-ai-backend
    .\.venv\Scripts\Activate.ps1
    python .\02_llm-api-integration\01_llm-api-concepts\01_message_structure.py
"""


# system 메시지는 모델의 역할과 규칙을 정합니다.
# 예를 들어 "학습 도우미처럼 설명해라", "한국어로 답해라",
# "초보자가 이해할 수 있게 단계별로 설명해라" 같은 기준을 넣을 수 있습니다.
system_message = {
    "role": "system",
    "content": "당신은 Python과 FastAPI를 쉽게 설명하는 학습 도우미입니다.",
}


# context_message는 앞 단원에서 만든 메모 API와 연결되는 예시입니다.
# 실제 서비스에서는 Supabase에 저장된 메모, 대화 이력, 로그 데이터가 이 위치에 들어갈 수 있습니다.
context_message = {
    "role": "user",
    "content": "참고 메모: FastAPI에서는 GET으로 조회하고 POST로 생성한다.",
}


# user 메시지는 사용자가 실제로 입력한 질문입니다.
# Streamlit 화면이나 다른 프론트엔드 입력창에서 받은 값이 여기에 들어갑니다.
question_message = {
    "role": "user",
    "content": "참고 메모를 바탕으로 GET과 POST의 차이를 설명해 주세요.",
}


# LLM API는 보통 메시지 1개가 아니라 메시지 목록을 받습니다.
# 목록의 순서가 대화 순서이므로, 오래된 메시지부터 최신 메시지 순서로 넣습니다.
messages = [system_message, context_message, question_message]


print("LLM API에 전달할 messages 예시")
print("-" * 50)

for index, message in enumerate(messages, start=1):
    # enumerate(..., start=1)은 사람이 읽기 쉬운 번호를 붙이기 위해 사용합니다.
    print(f"{index}. role: {message['role']}")
    print(f"   content: {message['content']}")
    print()


print("핵심 정리")
print("-" * 50)
print("LLM API는 role/content 구조의 메시지 목록을 받는 경우가 많습니다.")
print("싱글턴 호출은 현재 질문 중심이고, 멀티턴 호출은 이전 대화까지 함께 보냅니다.")
print("메모, 로그, 대화 이력 같은 참고 자료는 context로 함께 전달할 수 있습니다.")
