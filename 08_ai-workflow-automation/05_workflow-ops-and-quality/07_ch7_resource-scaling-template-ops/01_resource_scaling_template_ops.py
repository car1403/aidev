"""워크플로우 리소스 사용량과 확장 전략을 정리하는 예제입니다."""

from dataclasses import dataclass


@dataclass
class WorkflowRunMetric:
    """워크플로우 실행별 리소스와 비용 지표입니다."""

    workflow_name: str
    api_calls: int
    estimated_cost: float
    memory_mb: int
    duration_ms: int
    status: str


def recommend_scaling(metric: WorkflowRunMetric) -> str:
    """실행 지표를 보고 확장 또는 최적화 전략을 추천합니다."""

    if metric.status == "failed":
        return "오류 원인 분석 후 fallback 또는 retry 정책을 점검합니다."
    if metric.api_calls > 20:
        return "API 호출량이 많습니다. 캐시 또는 RAG 검색 범위 축소를 검토합니다."
    if metric.memory_mb > 2048:
        return "메모리 사용량이 높습니다. 문서 chunk 크기와 Context 길이를 줄입니다."
    if metric.duration_ms > 5000:
        return "응답 시간이 깁니다. 병렬 처리 또는 수평 확장을 검토합니다."
    return "현재 리소스 상태는 안정적입니다."


def build_template_checklist() -> list[str]:
    """재사용 가능한 워크플로우 템플릿 체크리스트를 반환합니다."""

    return [
        "입력 스키마가 명확한가?",
        "공통 오류 처리 노드가 있는가?",
        "로그와 비용 추적 노드가 포함되어 있는가?",
        "보안 필터 노드가 포함되어 있는가?",
        "출력 형식이 재사용 가능하게 정의되어 있는가?",
    ]


def main() -> None:
    """샘플 지표와 템플릿 체크리스트를 출력합니다."""

    metric = WorkflowRunMetric(
        workflow_name="tech-support-rag-workflow",
        api_calls=24,
        estimated_cost=0.42,
        memory_mb=1536,
        duration_ms=4200,
        status="success",
    )

    print(metric)
    print(recommend_scaling(metric))

    print("\n[Template Checklist]")
    for item in build_template_checklist():
        print(f"- {item}")


if __name__ == "__main__":
    main()
