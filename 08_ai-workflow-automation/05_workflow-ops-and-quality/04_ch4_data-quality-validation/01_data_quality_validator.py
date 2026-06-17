"""입력/출력 데이터 품질을 검증하는 예제입니다."""

from dataclasses import dataclass


@dataclass
class ValidationResult:
    """검증 결과를 표현합니다."""

    is_valid: bool
    errors: list[str]


def validate_input(payload: dict[str, str]) -> ValidationResult:
    """워크플로우 입력 데이터의 필수 필드와 내용을 검증합니다."""

    errors: list[str] = []
    required_fields = ["ticket_id", "title", "message"]

    for field in required_fields:
        if not payload.get(field):
            errors.append(f"필수 필드 누락: {field}")

    if len(payload.get("message", "")) < 10:
        errors.append("message가 너무 짧습니다.")

    return ValidationResult(is_valid=not errors, errors=errors)


def validate_output(output: dict[str, str]) -> ValidationResult:
    """AI 응답 결과의 구조와 정책 위반 가능성을 검증합니다."""

    errors: list[str] = []
    required_fields = ["category", "urgency", "draft_answer"]
    blocked_words = ["무조건 보장", "100% 해결", "비밀 키"]

    for field in required_fields:
        if not output.get(field):
            errors.append(f"출력 필드 누락: {field}")

    draft_answer = output.get("draft_answer", "")
    for word in blocked_words:
        if word in draft_answer:
            errors.append(f"금지 표현 포함: {word}")

    if output.get("urgency") not in {"low", "normal", "high"}:
        errors.append("urgency 값은 low, normal, high 중 하나여야 합니다.")

    return ValidationResult(is_valid=not errors, errors=errors)


if __name__ == "__main__":
    input_payload = {
        "ticket_id": "DQ-6001",
        "title": "AI 응답 지연",
        "message": "AI 응답이 느립니다. 원인을 확인해 주세요.",
    }

    ai_output = {
        "category": "technical_issue",
        "urgency": "high",
        "draft_answer": "모델 상태, 요청량, 네트워크 지연을 확인해 주세요.",
    }

    print("[Input Validation]")
    print(validate_input(input_payload))

    print("\n[Output Validation]")
    print(validate_output(ai_output))
