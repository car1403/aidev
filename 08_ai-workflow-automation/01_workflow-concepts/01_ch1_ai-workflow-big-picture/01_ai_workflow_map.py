"""AI 워크플로우의 전체 단계를 구조화해서 출력하는 예제입니다.

이 파일은 외부 API를 호출하지 않습니다.
초보자가 워크플로우를 '코드 실행 순서'가 아니라 '업무 처리 단계'로
바라볼 수 있도록 단계 이름, 역할, 입력, 출력을 함께 보여줍니다.
"""

from dataclasses import dataclass


@dataclass
class WorkflowStep:
    """워크플로우의 한 단계를 표현하는 데이터 구조입니다."""

    name: str
    role: str
    input_data: str
    output_data: str


def build_customer_support_workflow() -> list[WorkflowStep]:
    """고객 문의 자동화 시나리오를 단계별 워크플로우로 만듭니다."""

    return [
        WorkflowStep(
            name="Trigger",
            role="새 고객 문의가 들어오면 워크플로우를 시작합니다.",
            input_data="고객 문의 이벤트",
            output_data="처리할 문의 데이터",
        ),
        WorkflowStep(
            name="Classify",
            role="문의 내용을 읽고 유형과 긴급도를 분류합니다.",
            input_data="문의 제목, 본문",
            output_data="문의 유형, 긴급도",
        ),
        WorkflowStep(
            name="Retrieve",
            role="관련 FAQ나 내부 문서를 검색합니다.",
            input_data="문의 유형, 핵심 키워드",
            output_data="참고 문서 목록",
        ),
        WorkflowStep(
            name="Generate",
            role="LLM을 사용해 답변 초안을 생성합니다.",
            input_data="문의 내용, 참고 문서",
            output_data="답변 초안",
        ),
        WorkflowStep(
            name="Validate",
            role="답변이 정책과 품질 기준을 만족하는지 확인합니다.",
            input_data="답변 초안",
            output_data="검증 결과",
        ),
        WorkflowStep(
            name="Action",
            role="답변을 저장하거나 담당자에게 전달합니다.",
            input_data="검증된 답변",
            output_data="전송 또는 저장 결과",
        ),
        WorkflowStep(
            name="Log",
            role="실행 결과와 오류를 기록합니다.",
            input_data="전체 실행 상태",
            output_data="운영 로그",
        ),
    ]


def print_workflow(steps: list[WorkflowStep]) -> None:
    """워크플로우 단계를 사람이 읽기 쉬운 형태로 출력합니다."""

    print("[AI Workflow Map]")
    for index, step in enumerate(steps, start=1):
        print(f"\n{index}. {step.name}")
        print(f"   역할: {step.role}")
        print(f"   입력: {step.input_data}")
        print(f"   출력: {step.output_data}")


if __name__ == "__main__":
    workflow_steps = build_customer_support_workflow()
    print_workflow(workflow_steps)
