"""서비스 로그 데이터 구조를 이해하는 예제.

이 파일은 Supabase에 접속하지 않습니다.
운영 로그를 어떤 모양으로 저장하면 좋은지 Python dict로 확인합니다.
"""


service_log = {
    "event_type": "ai.answer.created",
    "message": "AI 답변 생성이 완료되었습니다.",
    "metadata": {
        "endpoint": "/ai/chat",
        "status_code": 200,
        "duration_ms": 320,
        "model": "mock-teacher",
    },
}


print("서비스 로그 예시:")
print(service_log)

print("\n핵심:")
print("event_type은 로그의 종류를 구분합니다.")
print("message는 사람이 읽을 수 있는 설명입니다.")
print("metadata는 endpoint, 처리 시간, 모델명 같은 추가 정보를 담습니다.")
