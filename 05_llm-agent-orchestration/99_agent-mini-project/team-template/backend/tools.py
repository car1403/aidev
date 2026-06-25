"""팀 프로젝트에서 사용할 도구 함수를 작성하는 파일입니다."""


def example_lookup_tool(keyword: str) -> str:
    """키워드로 Mock 데이터를 조회하는 예시 도구입니다."""
    return f"'{keyword}'에 대한 예시 조회 결과입니다."


def example_calculation_tool(values: list[int]) -> int:
    """숫자 목록의 합계를 계산하는 예시 도구입니다."""
    return sum(values)
