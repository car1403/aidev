"""워크플로우 실행 버전과 비용 정보를 기록하는 예제입니다."""

from dataclasses import dataclass
from statistics import mean


@dataclass
class WorkflowRun:
    """워크플로우 한 번의 실행 기록입니다."""

    run_id: str
    workflow_version: str
    prompt_version: str
    model_name: str
    input_tokens: int
    output_tokens: int
    latency_ms: int
    success: bool

    @property
    def total_tokens(self) -> int:
        """입력 토큰과 출력 토큰을 합산합니다."""

        return self.input_tokens + self.output_tokens


def estimate_cost(run: WorkflowRun) -> float:
    """간단한 예시 단가로 실행 비용을 추정합니다.

    실제 비용은 모델 제공자와 시점에 따라 달라집니다.
    여기서는 운영 구조를 이해하기 위해 가상의 단가를 사용합니다.
    """

    cost_per_1k_tokens = 0.002
    return run.total_tokens / 1000 * cost_per_1k_tokens


def summarize_runs(runs: list[WorkflowRun]) -> dict[str, float]:
    """여러 실행 기록을 운영 지표로 요약합니다."""

    total_cost = sum(estimate_cost(run) for run in runs)
    success_rate = sum(1 for run in runs if run.success) / len(runs)
    avg_latency = mean(run.latency_ms for run in runs)
    avg_tokens = mean(run.total_tokens for run in runs)

    return {
        "total_cost": total_cost,
        "success_rate": success_rate,
        "avg_latency_ms": avg_latency,
        "avg_tokens": avg_tokens,
    }


if __name__ == "__main__":
    workflow_runs = [
        WorkflowRun("RUN-001", "wf-1.0.0", "prompt-1.0.0", "gpt-4.1-mini", 900, 300, 1800, True),
        WorkflowRun("RUN-002", "wf-1.0.0", "prompt-1.0.0", "gpt-4.1-mini", 1200, 450, 2200, True),
        WorkflowRun("RUN-003", "wf-1.1.0", "prompt-1.1.0", "gpt-4.1-mini", 800, 250, 1600, False),
    ]

    print("[Workflow Version and Cost Summary]")
    summary = summarize_runs(workflow_runs)
    for key, value in summary.items():
        print(f"- {key}: {value:.4f}")

    print("\n[Run Details]")
    for run in workflow_runs:
        print(
            f"- {run.run_id}: workflow={run.workflow_version}, "
            f"prompt={run.prompt_version}, model={run.model_name}, "
            f"tokens={run.total_tokens}, cost=${estimate_cost(run):.4f}"
        )
