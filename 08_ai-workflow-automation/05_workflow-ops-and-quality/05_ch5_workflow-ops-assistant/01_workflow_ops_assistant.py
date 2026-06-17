"""운영 지표를 바탕으로 개선안을 제안하는 간단한 Ops Assistant 예제입니다."""

from dataclasses import dataclass


@dataclass
class OpsMetrics:
    """워크플로우 운영 지표입니다."""

    failure_rate: float
    avg_latency_ms: int
    daily_cost_usd: float
    validation_error_count: int
    negative_feedback_count: int


def recommend_actions(metrics: OpsMetrics) -> list[str]:
    """운영 지표를 보고 다음 조치 목록을 제안합니다."""

    actions: list[str] = []

    if metrics.failure_rate >= 0.2:
        actions.append("실패율이 높습니다. 오류 유형별 retry/fallback 흐름을 추가하세요.")
    if metrics.avg_latency_ms >= 2500:
        actions.append("응답 시간이 깁니다. 프롬프트 길이와 Tool 호출 횟수를 줄여보세요.")
    if metrics.daily_cost_usd >= 10:
        actions.append("일일 비용이 높습니다. 저비용 모델 또는 캐싱 전략을 검토하세요.")
    if metrics.validation_error_count > 0:
        actions.append("출력 검증 오류가 있습니다. Structured Output과 필수 필드를 강화하세요.")
    if metrics.negative_feedback_count > 0:
        actions.append("부정 피드백이 있습니다. 답변 품질 기준과 예시 프롬프트를 개선하세요.")

    if not actions:
        actions.append("현재 운영 지표는 안정적입니다. 모니터링을 유지하세요.")

    return actions


if __name__ == "__main__":
    current_metrics = OpsMetrics(
        failure_rate=0.25,
        avg_latency_ms=2800,
        daily_cost_usd=12.5,
        validation_error_count=3,
        negative_feedback_count=2,
    )

    print("[Workflow Ops Assistant]")
    print(current_metrics)

    print("\n[Recommended Actions]")
    for action in recommend_actions(current_metrics):
        print(f"- {action}")
