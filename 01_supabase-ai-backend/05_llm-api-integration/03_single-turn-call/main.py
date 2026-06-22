r"""싱글턴 LLM 호출 흐름을 비용 없이 확인하는 통합 예제입니다.

이 파일은 실제 Gemini 또는 OpenAI API를 호출하지 않습니다.
사용자 질문 1개를 받아 LLM 요청 구조를 만들고, mock 응답으로 결과 형식을 확인합니다.

실행:
    cd C:\aidev\01_supabase-ai-backend
    .\.venv\Scripts\Activate.ps1
    python .\05_llm-api-integration\03_single-turn-call\main.py
"""

from dataclasses import dataclass


@dataclass
class SingleTurnRequest:
    """싱글턴 호출에 필요한 최소 입력값입니다."""

    question: str
    memo_context: str
    temperature: float = 0.2
    max_tokens: int = 300


@dataclass
class SingleTurnResponse:
    """LLM API 응답에서 서비스가 주로 확인하는 값입니다."""

    provider: str
    model: str
    answer: str
    input_length: int
    max_tokens: int


def build_single_turn_prompt(request: SingleTurnRequest) -> str:
    """메모 컨텍스트와 사용자 질문을 하나의 프롬프트로 정리합니다."""

    return (
        "당신은 Python과 FastAPI를 쉽게 설명하는 학습 도우미입니다.\n\n"
        f"참고 메모:\n{request.memo_context}\n\n"
        f"사용자 질문:\n{request.question}\n\n"
        "답변은 초보자가 이해할 수 있도록 단계별로 작성해 주세요."
    )


def mock_llm_call(prompt: str, temperature: float, max_tokens: int) -> SingleTurnResponse:
    """실제 API 호출 대신 mock 응답을 반환합니다."""

    answer = (
        "싱글턴 호출은 이전 대화 이력을 포함하지 않고 현재 질문 하나만 처리하는 방식입니다. "
        "FastAPI에서는 사용자의 질문을 Request Body로 받고, 필요한 컨텍스트를 붙인 뒤 "
        "LLM API에 전달하는 구조로 확장할 수 있습니다."
    )

    return SingleTurnResponse(
        provider="mock",
        model="mock-single-turn-teacher",
        answer=answer,
        input_length=len(prompt),
        max_tokens=max_tokens,
    )


def main() -> None:
    """싱글턴 호출의 입력, 프롬프트, 응답 구조를 순서대로 출력합니다."""

    request = SingleTurnRequest(
        question="FastAPI에서 Pydantic을 왜 사용하나요?",
        memo_context="Pydantic은 요청 데이터의 타입과 길이 조건을 검사하고, 잘못된 요청은 422 오류로 처리한다.",
        temperature=0.2,
        max_tokens=300,
    )

    prompt = build_single_turn_prompt(request)
    response = mock_llm_call(
        prompt=prompt,
        temperature=request.temperature,
        max_tokens=request.max_tokens,
    )

    print("1. 싱글턴 요청")
    print("-" * 50)
    print(request)
    print()

    print("2. LLM에 전달할 프롬프트")
    print("-" * 50)
    print(prompt)
    print()

    print("3. mock 응답")
    print("-" * 50)
    print(response)
    print()

    print("핵심 정리")
    print("-" * 50)
    print("이 파일은 실제 API를 호출하지 않으므로 비용이 발생하지 않습니다.")
    print("실제 Gemini 호출은 03_gemini_rest_single_turn.py에서 key가 있을 때만 실행합니다.")
    print("OpenAI 호출은 선택/비교 실습용으로 유지합니다.")


if __name__ == "__main__":
    main()
