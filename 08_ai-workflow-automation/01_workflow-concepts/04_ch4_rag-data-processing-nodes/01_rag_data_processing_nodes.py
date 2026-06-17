"""RAG 노드와 데이터 처리 노드의 흐름을 보여주는 예제입니다."""

from dataclasses import dataclass


@dataclass
class NodeResult:
    """각 노드 실행 결과를 기록합니다."""

    node_name: str
    input_data: str
    output_data: str


KNOWLEDGE_BASE = {
    "erp login": "ERP 로그인 장애는 비밀번호 만료, 계정 잠금, VPN 상태를 먼저 확인합니다.",
    "slow ai": "AI 응답 지연은 요청량, 모델 상태, 네트워크 지연, 외부 API 상태를 점검합니다.",
}


def preprocess(user_input: str) -> str:
    """사용자 입력을 검색과 LLM 처리에 적합하도록 정리합니다."""

    return " ".join(user_input.strip().split())


def transform_query(cleaned_input: str) -> str:
    """입력 문장을 간단한 검색 키워드로 변환합니다."""

    lowered = cleaned_input.lower()
    if "erp" in lowered or "로그인" in cleaned_input:
        return "erp login"
    if "느림" in cleaned_input or "지연" in cleaned_input:
        return "slow ai"
    return "general"


def retrieve_document(query: str) -> str:
    """RAG Retrieval 노드처럼 관련 문서를 검색합니다."""

    return KNOWLEDGE_BASE.get(query, "관련 문서를 찾지 못했습니다.")


def generate_answer(user_input: str, document: str) -> str:
    """검색 결과를 참고해 답변 초안을 생성합니다."""

    if "찾지 못했습니다" in document:
        return "관련 문서를 찾지 못했습니다. 담당자 검토가 필요합니다."
    return f"문의 내용: {user_input}\n참고 문서: {document}\n답변: 위 항목을 순서대로 확인해 주세요."


def postprocess(answer: str) -> str:
    """출력 메시지를 사용자가 읽기 쉬운 형태로 정리합니다."""

    return answer.replace("\n", " / ")


def run_rag_data_workflow(user_input: str) -> list[NodeResult]:
    """RAG와 데이터 처리 노드 흐름을 순서대로 실행합니다."""

    results: list[NodeResult] = []

    cleaned = preprocess(user_input)
    results.append(NodeResult("Preprocess", user_input, cleaned))

    query = transform_query(cleaned)
    results.append(NodeResult("Query Transform", cleaned, query))

    document = retrieve_document(query)
    results.append(NodeResult("RAG Retrieval", query, document))

    draft = generate_answer(cleaned, document)
    results.append(NodeResult("LLM Generation", document, draft))

    final = postprocess(draft)
    results.append(NodeResult("Postprocess", draft, final))

    return results


def main() -> None:
    """샘플 입력으로 RAG 데이터 처리 흐름을 출력합니다."""

    results = run_rag_data_workflow(" ERP 로그인이 되지 않습니다. 어떻게 해야 하나요? ")
    for result in results:
        print(f"\n[{result.node_name}]")
        print(f"input: {result.input_data}")
        print(f"output: {result.output_data}")


if __name__ == "__main__":
    main()
