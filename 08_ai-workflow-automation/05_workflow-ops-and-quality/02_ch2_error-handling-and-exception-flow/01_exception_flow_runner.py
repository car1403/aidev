"""워크플로우 오류 처리와 대체 경로를 시뮬레이션하는 예제입니다."""

from dataclasses import dataclass, field


@dataclass
class WorkflowState:
    """워크플로우 실행 중 상태와 로그를 저장합니다."""

    request_id: str
    retry_count: int = 0
    max_retry: int = 2
    logs: list[str] = field(default_factory=list)
    final_status: str = "running"

    def log(self, message: str) -> None:
        """운영 로그를 추가합니다."""

        self.logs.append(message)


def unstable_ai_step(state: WorkflowState) -> str:
    """실패할 수 있는 AI 처리 단계를 흉내 냅니다."""

    if state.retry_count < state.max_retry:
        raise RuntimeError("AI API temporary timeout")
    return "AI 답변 초안 생성 완료"


def fallback_template_response() -> str:
    """AI 호출이 실패했을 때 사용할 대체 응답입니다."""

    return "현재 AI 응답이 지연되고 있어 담당자가 직접 확인하겠습니다."


def run_with_exception_flow(state: WorkflowState) -> WorkflowState:
    """Retry 후 실패하면 Fallback으로 전환하는 워크플로우입니다."""

    while state.retry_count <= state.max_retry:
        try:
            state.log(f"AI step 시도: {state.retry_count + 1}")
            result = unstable_ai_step(state)
            state.log(result)
            state.final_status = "success"
            return state
        except RuntimeError as error:
            state.log(f"오류 발생: {error}")
            state.retry_count += 1

    state.log("최대 재시도 초과: fallback 실행")
    state.log(fallback_template_response())
    state.final_status = "fallback"
    return state


if __name__ == "__main__":
    workflow_state = run_with_exception_flow(WorkflowState(request_id="REQ-5001"))

    print("[Exception Flow Result]")
    print(f"final_status: {workflow_state.final_status}")
    print("\n[Logs]")
    for log in workflow_state.logs:
        print(f"- {log}")
