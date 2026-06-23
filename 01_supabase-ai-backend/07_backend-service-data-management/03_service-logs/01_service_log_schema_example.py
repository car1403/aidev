"""서비스 로그 데이터 구조를 이해하는 예제.

이 파일은 Supabase에 접속하지 않습니다.
운영 로그를 어떤 모양으로 저장하면 좋은지 Python dict로 확인합니다.

핵심 아이디어:
- event_type은 로그의 종류를 구분합니다.
- message는 사람이 읽는 짧은 설명입니다.
- metadata는 endpoint, 처리 시간, provider, 모델명, 실제 호출 여부 같은 추가 정보를 JSON 형태로 담습니다.
"""


service_log = {
    "event_type": "ai.answer.created",
    "message": "AI 응답 생성이 완료되었습니다.",
    "metadata": {
        "endpoint": "/ai/chat",
        "status_code": 200,
        "duration_ms": 320,
        "provider": "gemini",
        "model": "gemini-2.5-flash-lite",
        "actual_api_called": False,
        "llm_call_mode": "mock-first",
    },
}


error_log = {
    "event_type": "practice.error",
    "message": "AI 응답 생성 중 오류가 발생했습니다.",
    "metadata": {
        "endpoint": "/ai/chat",
        "status_code": 500,
        "provider": "gemini",
        "model": "gemini-2.5-flash-lite",
        "actual_api_called": True,
        "llm_call_mode": "gemini-sdk",
        "error_type": "TimeoutError",
        "retryable": True,
    },
}


print("성공 로그 예시:")
print(service_log)

print("\n오류 로그 예시:")
print(error_log)

print("\n핵심:")
print("event_type은 로그의 종류를 구분합니다.")
print("message는 사람이 읽을 수 있는 설명입니다.")
print("metadata는 endpoint, 처리 시간, provider, 모델명, 실제 호출 여부 같은 추가 정보를 담습니다.")
print("API key, token, 비밀번호 같은 민감한 정보는 로그에 저장하지 않습니다.")
