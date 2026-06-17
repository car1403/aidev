"""비용 없는 싱글턴 LLM 호출 예제.

실제 API를 호출하지 않고, LLM API 호출 흐름을 함수로 흉내 냅니다.
초보자는 먼저 입력, 파라미터, 응답 구조를 이해하는 것이 중요합니다.
"""


def mock_llm_response(prompt: str, temperature: float = 0.3, max_tokens: int = 200) -> dict:
    """가짜 LLM 응답을 생성합니다."""

    # 실제 API 응답에는 보통 모델 이름, 응답 텍스트, 사용량 정보가 함께 들어옵니다.
    # 여기서는 그 구조를 단순화해서 dict로 흉내 냅니다.
    return {
        "provider": "mock",
        "model": "mock-teacher",
        "usage": {
            # input_length는 실제 토큰 수가 아니라 수업용 예시 값입니다.
            # 실제 서비스에서는 provider가 반환하는 token usage를 확인합니다.
            "input_length": len(prompt),
            "max_tokens": max_tokens,
        },
        "answer": (
            f"질문: {prompt}\n"
            f"temperature={temperature} 설정으로 안정적인 수업용 답변을 생성했다고 가정합니다."
        ),
    }


# 싱글턴 호출은 "사용자 질문 1개 -> AI 답변 1개" 흐름입니다.
question = "FastAPI에서 Pydantic을 왜 사용하나요?"
result = mock_llm_response(question, temperature=0.2, max_tokens=150)

print(result["answer"])
print("\n사용량 예시:", result["usage"])
