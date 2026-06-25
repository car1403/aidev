r"""LLM 파라미터 의미를 비용 없이 이해하는 예제입니다.

이 파일은 실제 AI 모델을 호출하지 않습니다.
temperature, top_p, max_tokens 같은 값이 어떤 의도로 쓰이는지 출력으로만 확인합니다.

실행:
    cd C:\aidev\02_supabase-ai-backend
    .\.venv\Scripts\Activate.ps1
    python .\05_llm-api-integration\01_llm-api-concepts\02_parameter_simulator.py
"""

from dataclasses import dataclass


@dataclass
class GenerationSettings:
    """LLM 응답 생성 설정입니다."""

    model: str
    temperature: float
    top_p: float
    max_tokens: int


def describe_generation_settings(settings: GenerationSettings) -> dict:
    """파라미터 값을 사람이 이해하기 쉬운 설명으로 바꿉니다."""

    # temperature는 답변의 무작위성에 영향을 주는 값입니다.
    # 낮게 설정하면 수업 자료, 요약, 코드 설명처럼 안정적인 답변에 유리합니다.
    if settings.temperature < 0.3:
        style = "안정적이고 보수적인 응답"
    elif settings.temperature < 0.8:
        style = "균형 잡힌 응답"
    else:
        style = "더 다양하고 창의적인 응답"

    # top_p는 모델이 다음 단어를 고를 때 고려하는 후보 범위와 관련이 있습니다.
    # 초보 단계에서는 temperature와 함께 응답 다양성을 조절하는 값으로 이해하면 충분합니다.
    if settings.top_p < 0.5:
        diversity = "후보 범위를 좁게 보는 설정"
    elif settings.top_p < 0.95:
        diversity = "후보 범위를 적당히 보는 설정"
    else:
        diversity = "후보 범위를 넓게 보는 설정"

    # max_tokens는 모델이 생성할 수 있는 최대 출력 길이입니다.
    # 실제 API에서는 길게 생성할수록 비용이 늘 수 있으므로 처음에는 작게 시작합니다.
    if settings.max_tokens <= 200:
        length = "짧은 답변"
    elif settings.max_tokens <= 800:
        length = "중간 길이 답변"
    else:
        length = "긴 답변"

    return {
        "model": settings.model,
        "temperature": settings.temperature,
        "top_p": settings.top_p,
        "max_tokens": settings.max_tokens,
        "expected_style": style,
        "expected_diversity": diversity,
        "expected_length": length,
    }


# 이 과정에서는 01~03 구간에서 Gemini를 기본 실습 모델로 사용합니다.
# OpenAI 모델은 선택/비교 실습에서 사용할 수 있습니다.
examples = [
    GenerationSettings(model="gemini-2.5-flash-lite", temperature=0.2, top_p=0.8, max_tokens=200),
    GenerationSettings(model="gemini-2.5-flash-lite", temperature=0.5, top_p=0.9, max_tokens=500),
    GenerationSettings(model="gemini-2.5-flash-lite", temperature=0.9, top_p=0.95, max_tokens=1000),
]


print("LLM 생성 파라미터 시뮬레이션")
print("-" * 50)

for example in examples:
    # 실제 API를 호출하지 않고도 파라미터의 의미를 먼저 확인합니다.
    print(describe_generation_settings(example))


print("\n핵심 정리")
print("-" * 50)
print("temperature와 top_p는 응답의 다양성에 영향을 줄 수 있습니다.")
print("max_tokens는 출력 길이와 비용에 영향을 줄 수 있습니다.")
print("처음에는 낮은 temperature와 적당한 max_tokens로 안정적인 응답부터 확인합니다.")
