"""워크플로우 실행 로그를 분석해 개선 포인트를 찾는 예제입니다."""

from collections import Counter
from dataclasses import dataclass
from statistics import mean


@dataclass
class WorkflowLog:
    """워크플로우 실행 로그 한 건입니다."""

    run_id: str
    status: str
    error_type: str | None
    latency_ms: int
    user_feedback: str


def analyze_logs(logs: list[WorkflowLog]) -> dict[str, object]:
    """실행 로그를 운영 지표로 분석합니다."""

    total = len(logs)
    failures = [log for log in logs if log.status != "success"]
    error_counter = Counter(log.error_type for log in failures if log.error_type)
    negative_feedback = [log for log in logs if log.user_feedback == "negative"]

    return {
        "total_runs": total,
        "failure_rate": len(failures) / total,
        "avg_latency_ms": mean(log.latency_ms for log in logs),
        "top_errors": error_counter.most_common(),
        "negative_feedback_count": len(negative_feedback),
    }


def suggest_improvements(analysis: dict[str, object]) -> list[str]:
    """분석 결과를 바탕으로 개선 제안을 만듭니다."""

    suggestions: list[str] = []

    if float(analysis["failure_rate"]) >= 0.3:
        suggestions.append("실패율이 높습니다. Retry와 fallback 조건을 점검하세요.")
    if float(analysis["avg_latency_ms"]) >= 2500:
        suggestions.append("평균 응답 시간이 깁니다. 모델, 프롬프트 길이, Tool 호출 수를 점검하세요.")
    if int(analysis["negative_feedback_count"]) > 0:
        suggestions.append("부정 피드백이 있습니다. 답변 품질 기준과 프롬프트를 개선하세요.")
    if not suggestions:
        suggestions.append("현재 로그 기준으로 큰 문제는 없습니다. 샘플 수를 늘려 계속 관찰하세요.")

    return suggestions


if __name__ == "__main__":
    sample_logs = [
        WorkflowLog("RUN-001", "success", None, 1800, "positive"),
        WorkflowLog("RUN-002", "failed", "timeout", 3100, "negative"),
        WorkflowLog("RUN-003", "success", None, 2400, "neutral"),
        WorkflowLog("RUN-004", "failed", "validation_error", 2600, "negative"),
    ]

    result = analyze_logs(sample_logs)

    print("[Workflow Log Analysis]")
    for key, value in result.items():
        print(f"- {key}: {value}")

    print("\n[Improvement Suggestions]")
    for suggestion in suggest_improvements(result):
        print(f"- {suggestion}")
