"""Multi-Agent Workflow 운영 구조를 시뮬레이션하는 예제입니다."""

from dataclasses import dataclass


@dataclass
class AgentRun:
    """Agent 실행 결과입니다."""

    agent_name: str
    status: str
    result: str


def classifier_agent(message: str) -> AgentRun:
    """문의 유형을 분류합니다."""

    category = "account" if "로그인" in message else "general"
    return AgentRun("classifier_agent", "success", category)


def rag_agent(category: str) -> AgentRun:
    """분류 결과에 따라 참고 문서를 찾습니다."""

    if category == "account":
        return AgentRun("rag_agent", "success", "계정 잠금, 비밀번호 만료, VPN 상태 확인")
    return AgentRun("rag_agent", "success", "일반 FAQ 확인")


def answer_agent(message: str, document: str) -> AgentRun:
    """참고 문서를 바탕으로 답변 초안을 만듭니다."""

    return AgentRun("answer_agent", "success", f"{message} / 참고: {document}")


def review_agent(answer: str) -> AgentRun:
    """답변 품질을 검토합니다."""

    if "참고" in answer:
        return AgentRun("review_agent", "success", "approved")
    return AgentRun("review_agent", "failed", "needs_revision")


def run_multi_agent_workflow(message: str) -> list[AgentRun]:
    """여러 Agent가 협업하는 워크플로우를 실행합니다."""

    runs: list[AgentRun] = []
    category = classifier_agent(message)
    runs.append(category)

    document = rag_agent(category.result)
    runs.append(document)

    answer = answer_agent(message, document.result)
    runs.append(answer)

    review = review_agent(answer.result)
    runs.append(review)

    return runs


def main() -> None:
    """Agent별 실행 상태를 출력합니다."""

    for run in run_multi_agent_workflow("ERP 로그인이 되지 않습니다."):
        print(run)


if __name__ == "__main__":
    main()
