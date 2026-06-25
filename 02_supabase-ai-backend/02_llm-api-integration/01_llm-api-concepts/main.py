r"""LLM API 개념을 비용 없이 확인하는 통합 예제입니다.

이 파일은 실제 Gemini 또는 OpenAI API를 호출하지 않습니다.
앞 단원에서 만든 메모 API와 연결될 수 있도록, 사용자의 질문과 메모 컨텍스트를
LLM API에 전달할 messages 형태로 정리하는 과정을 보여줍니다.

실행:
    cd C:\aidev\02_supabase-ai-backend
    .\.venv\Scripts\Activate.ps1
    python .\02_llm-api-integration\01_llm-api-concepts\main.py
"""

from dataclasses import dataclass


@dataclass
class GenerationSettings:
    """LLM 응답 생성 방식을 조절하는 기본 설정입니다.

    실제 API에서는 모델 공급자마다 이름이나 지원 범위가 조금씩 다를 수 있습니다.
    이 과정에서는 01~03 구간에서 Gemini를 기본으로 보고, OpenAI는 선택/비교용으로 둡니다.
    """

    model: str = "gemini-2.5-flash-lite"
    temperature: float = 0.3
    top_p: float = 0.9
    max_tokens: int = 300


def build_messages(user_question: str, memo_context: str) -> list[dict[str, str]]:
    """LLM API에 전달할 메시지 목록을 만듭니다.

    messages는 대화의 순서를 담는 목록입니다.
    role은 메시지의 역할이고, content는 실제 문장 내용입니다.
    """

    system_message = {
        "role": "system",
        "content": "당신은 Python과 FastAPI를 쉽게 설명하는 학습 도우미입니다.",
    }

    context_message = {
        "role": "user",
        "content": f"참고할 메모 내용:\n{memo_context}",
    }

    question_message = {
        "role": "user",
        "content": user_question,
    }

    return [system_message, context_message, question_message]


def estimate_prompt_size(messages: list[dict[str, str]]) -> dict[str, int]:
    """토큰 계산 전 단계로 입력 문장의 대략적인 크기를 확인합니다.

    실제 토큰 수는 모델의 tokenizer가 계산합니다.
    여기서는 초보자가 입력이 길어질수록 비용과 처리량이 커진다는 점을 이해하도록
    글자 수와 단어 수만 간단히 계산합니다.
    """

    combined_text = "\n".join(message["content"] for message in messages)

    return {
        "message_count": len(messages),
        "character_count": len(combined_text),
        "rough_word_count": len(combined_text.split()),
    }


def describe_settings(settings: GenerationSettings) -> dict[str, str | float | int]:
    """파라미터 값이 응답에 어떤 영향을 줄 수 있는지 설명합니다."""

    if settings.temperature < 0.3:
        style = "정확성과 일관성을 우선하는 보수적인 응답"
    elif settings.temperature < 0.8:
        style = "설명과 다양성의 균형을 잡은 응답"
    else:
        style = "표현이 더 다양해질 수 있는 창의적인 응답"

    if settings.max_tokens <= 200:
        length = "짧은 응답"
    elif settings.max_tokens <= 800:
        length = "중간 길이 응답"
    else:
        length = "긴 응답"

    return {
        "model": settings.model,
        "temperature": settings.temperature,
        "top_p": settings.top_p,
        "max_tokens": settings.max_tokens,
        "expected_style": style,
        "expected_length": length,
    }


def print_messages(messages: list[dict[str, str]]) -> None:
    """messages 목록을 사람이 읽기 좋게 출력합니다."""

    print("1. LLM API에 전달할 messages 구조")
    print("-" * 50)

    for index, message in enumerate(messages, start=1):
        print(f"{index}) role: {message['role']}")
        print(f"   content: {message['content']}")
        print()


def main() -> None:
    """LLM API 호출 전 알아야 할 핵심 구조를 순서대로 출력합니다."""

    memo_context = "FastAPI에서는 GET으로 조회하고 POST로 생성한다. Pydantic은 요청 데이터를 검증한다."
    user_question = "이 메모를 바탕으로 FastAPI 요청 처리 흐름을 초보자에게 설명해 주세요."
    settings = GenerationSettings()

    messages = build_messages(user_question=user_question, memo_context=memo_context)

    print_messages(messages)

    print("2. 입력 크기 확인")
    print("-" * 50)
    print(estimate_prompt_size(messages))
    print()

    print("3. 생성 파라미터 의미 확인")
    print("-" * 50)
    print(describe_settings(settings))
    print()

    print("핵심 정리")
    print("-" * 50)
    print("이 파일은 실제 LLM API를 호출하지 않으므로 비용이 발생하지 않습니다.")
    print("다음 단계에서는 .env에 Gemini API key를 설정하고 실제 싱글턴 호출을 연결합니다.")
    print("OpenAI 예제는 선택/비교 실습으로 유지합니다.")


if __name__ == "__main__":
    main()
