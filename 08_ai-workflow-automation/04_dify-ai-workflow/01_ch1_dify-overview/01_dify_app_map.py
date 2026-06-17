"""Dify 앱의 주요 구성 요소를 출력하는 예제입니다.

실제 Dify 서버를 호출하지 않고, Dify 화면에서 만나게 될 개념을
Python 데이터 구조로 먼저 정리합니다.
"""

from dataclasses import dataclass


@dataclass
class DifyComponent:
    """Dify 앱을 구성하는 요소를 표현합니다."""

    name: str
    role: str
    beginner_note: str


def build_dify_component_map() -> list[DifyComponent]:
    """Dify 앱을 설계할 때 확인해야 할 구성 요소 목록을 만듭니다."""

    return [
        DifyComponent("App", "사용자가 실행하는 AI 서비스 단위", "챗봇이나 워크플로우 하나를 앱으로 봅니다."),
        DifyComponent("Prompt", "AI에게 역할과 지시를 전달", "답변 스타일, 제한 조건, 출력 형식을 정합니다."),
        DifyComponent("Model", "응답을 생성하는 LLM", "OpenAI, 로컬 모델, 기타 LLM 제공자를 연결할 수 있습니다."),
        DifyComponent("Knowledge", "문서 기반 검색 자료", "FAQ, 매뉴얼, 사내 문서를 연결해 RAG를 구성합니다."),
        DifyComponent("Tool", "외부 기능 호출", "API 조회, 검색, 계산 같은 실제 작업을 담당합니다."),
        DifyComponent("Workflow", "노드 기반 실행 흐름", "입력, 분기, 검색, 생성, 출력 단계를 연결합니다."),
        DifyComponent("API", "외부 서비스에서 앱 호출", "n8n, 백엔드, 프론트엔드에서 Dify 앱을 호출할 수 있습니다."),
        DifyComponent("Logs", "실행 결과 기록", "품질 개선과 오류 분석에 사용합니다."),
    ]


def print_components(components: list[DifyComponent]) -> None:
    """Dify 구성 요소를 읽기 쉬운 형태로 출력합니다."""

    print("[Dify Component Map]")
    for index, component in enumerate(components, start=1):
        print(f"\n{index}. {component.name}")
        print(f"   역할: {component.role}")
        print(f"   초보자 메모: {component.beginner_note}")


if __name__ == "__main__":
    print_components(build_dify_component_map())
