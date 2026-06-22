"""Assignment 03 starter: Single-turn mock LLM 서비스."""

from pprint import pprint


def estimate_tokens(text: str) -> int:
    """공백 기준으로 토큰 수를 단순 추정합니다."""
    # TODO: text를 공백으로 나눈 개수를 반환하세요.
    return 0


def build_prompt(memo_context: str, user_question: str) -> str:
    """메모 컨텍스트와 질문을 하나의 프롬프트로 만듭니다."""
    # TODO: 메모와 질문이 모두 포함된 문자열을 반환하세요.
    return ""


def call_mock_llm(prompt: str) -> dict:
    """실제 API 대신 mock 응답을 반환합니다."""
    # TODO: provider, model, actual_api_called, answer, usage를 포함하세요.
    return {}


memo_context = "오늘 LLM API의 message 구조와 temperature를 공부했다."
user_question = "오늘 내용을 짧게 복습해줘."

prompt = build_prompt(memo_context, user_question)
response = call_mock_llm(prompt)

pprint(response, width=100)
