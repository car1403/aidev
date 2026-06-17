"""LLM 파라미터 의미를 비용 없이 이해하는 예제.

이 파일은 실제 AI 모델을 호출하지 않습니다.
temperature, max_tokens 같은 값이 어떤 의도로 쓰이는지 출력으로만 확인합니다.
"""


def describe_generation_settings(temperature: float, max_tokens: int) -> dict:
    """파라미터 값을 사람이 이해하기 쉬운 설명으로 바꿉니다."""

    # temperature는 답변의 무작위성에 영향을 주는 값입니다.
    # 낮게 설정하면 수업 자료, 요약, 코드 설명처럼 안정적인 답변에 유리합니다.
    if temperature < 0.3:
        style = "안정적이고 보수적인 응답"
    elif temperature < 0.7:
        style = "균형 잡힌 응답"
    else:
        style = "더 다양하고 창의적인 응답"

    # max_tokens는 모델이 생성할 수 있는 최대 출력 길이입니다.
    # 실제 API에서는 길게 생성할수록 비용이 늘 수 있으므로 처음에는 작게 시작합니다.
    if max_tokens <= 100:
        length = "짧은 답변"
    elif max_tokens <= 500:
        length = "중간 길이 답변"
    else:
        length = "긴 답변"

    return {
        "temperature": temperature,
        "max_tokens": max_tokens,
        "expected_style": style,
        "expected_length": length,
    }


# 수업에서는 같은 질문이라도 설정값을 바꾸면 응답 성격이 달라진다는 점을 보여줍니다.
examples = [
    describe_generation_settings(temperature=0.2, max_tokens=100),
    describe_generation_settings(temperature=0.7, max_tokens=400),
    describe_generation_settings(temperature=1.0, max_tokens=800),
]


for example in examples:
    # 실제 API를 호출하지 않고도 파라미터의 의미를 먼저 확인합니다.
    print(example)
