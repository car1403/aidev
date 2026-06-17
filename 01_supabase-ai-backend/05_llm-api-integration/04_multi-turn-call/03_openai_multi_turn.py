"""OpenAI 멀티턴 호출 예제.

OPENAI_API_KEY가 있을 때만 실제 API를 호출합니다.
"""

from pathlib import Path
import os

from dotenv import load_dotenv


# 실제 수업에서는 .env에 OPENAI_API_KEY를 넣은 뒤 이 예제를 실행합니다.
PROJECT_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(PROJECT_ROOT / ".env")


def main() -> None:
    api_key = os.getenv("OPENAI_API_KEY")
    model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

    if not api_key:
        # key가 없으면 비용이 발생하는 실제 호출을 하지 않습니다.
        print("OPENAI_API_KEY가 없습니다. 먼저 mock 멀티턴 예제로 학습하세요.")
        return

    from openai import OpenAI

    client = OpenAI(api_key=api_key)

    # 멀티턴 호출의 핵심은 이전 assistant 답변까지 함께 전달하는 것입니다.
    # 그래야 모델이 "그 설명을 바탕으로" 같은 후속 질문을 이해할 수 있습니다.
    messages = [
        {"role": "system", "content": "당신은 초보자에게 백엔드를 설명하는 강사입니다."},
        {"role": "user", "content": "FastAPI가 무엇인가요?"},
        {"role": "assistant", "content": "Python으로 API 서버를 쉽게 만들 수 있는 프레임워크입니다."},
        {"role": "user", "content": "그 설명을 바탕으로 Pydantic의 역할을 설명해 주세요."},
    ]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        # 멀티턴에서도 파라미터는 싱글턴과 동일하게 적용됩니다.
        temperature=0.3,
        max_tokens=400,
    )

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
