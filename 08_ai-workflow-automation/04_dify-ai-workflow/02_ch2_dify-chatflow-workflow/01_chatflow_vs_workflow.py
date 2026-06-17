"""Dify Chatflow와 Workflow의 차이를 비교하는 예제입니다."""

from dataclasses import dataclass


@dataclass
class FlowType:
    """Dify 앱 유형의 특징을 표현합니다."""

    name: str
    best_for: str
    trigger: str
    output_style: str
    example: str


def build_flow_comparison() -> list[FlowType]:
    """Chatflow와 Workflow의 차이를 비교할 데이터를 만듭니다."""

    return [
        FlowType(
            name="Chatflow",
            best_for="대화형 상담, 지식 검색 챗봇, 연속 질문 응답",
            trigger="사용자 메시지",
            output_style="자연어 답변",
            example="사내 문서 검색 챗봇",
        ),
        FlowType(
            name="Workflow",
            best_for="정해진 입력을 받아 한 번에 처리하는 자동화 작업",
            trigger="API 호출 또는 사용자 실행",
            output_style="구조화된 결과 또는 최종 텍스트",
            example="고객 문의 분류 및 답변 초안 생성",
        ),
    ]


def recommend_flow(use_case: str) -> str:
    """간단한 규칙으로 어떤 Dify 앱 유형이 적합한지 추천합니다."""

    chat_keywords = ["대화", "챗봇", "질문", "상담"]
    if any(keyword in use_case for keyword in chat_keywords):
        return "Chatflow"
    return "Workflow"


if __name__ == "__main__":
    print("[Dify Chatflow vs Workflow]")
    for flow in build_flow_comparison():
        print(f"\n- {flow.name}")
        print(f"  적합한 경우: {flow.best_for}")
        print(f"  시작 방식: {flow.trigger}")
        print(f"  출력 형태: {flow.output_style}")
        print(f"  예시: {flow.example}")

    sample_use_case = "기술 지원 문의를 분류하고 답변 초안을 생성"
    print("\n[Recommendation]")
    print(f"업무: {sample_use_case}")
    print(f"추천 앱 유형: {recommend_flow(sample_use_case)}")
