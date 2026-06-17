"""Dify Knowledge/RAG 흐름을 단순 Python 코드로 시뮬레이션합니다."""

from dataclasses import dataclass


@dataclass
class KnowledgeDocument:
    """Dify Knowledge에 들어갈 문서 조각을 표현합니다."""

    doc_id: str
    title: str
    content: str


def build_knowledge_base() -> list[KnowledgeDocument]:
    """실습용 지식 문서를 만듭니다."""

    return [
        KnowledgeDocument(
            doc_id="DOC-001",
            title="서비스 접속 장애 대응",
            content="서비스 접속이 되지 않을 때는 상태 페이지 확인, 브라우저 캐시 삭제, 재로그인을 순서대로 시도합니다.",
        ),
        KnowledgeDocument(
            doc_id="DOC-002",
            title="결제 오류 대응",
            content="결제 오류가 발생하면 결제 수단, 청구 주소, 카드 승인 상태를 확인합니다.",
        ),
        KnowledgeDocument(
            doc_id="DOC-003",
            title="AI 응답 지연 대응",
            content="AI 응답이 느릴 때는 모델 상태, 요청량, 네트워크 지연, 재시도 정책을 확인합니다.",
        ),
    ]


def retrieve_documents(query: str, documents: list[KnowledgeDocument]) -> list[KnowledgeDocument]:
    """질문에 포함된 키워드와 문서 내용을 비교해 관련 문서를 찾습니다."""

    # 너무 흔한 단어는 검색 점수에 크게 도움이 되지 않습니다.
    # 실제 RAG에서는 embedding 유사도를 쓰지만, 여기서는 초보자 이해를 위해
    # 핵심 키워드가 제목에 있으면 더 높은 점수를 주는 방식으로 단순화합니다.
    stopwords = {"무엇을", "확인해야", "하나요?", "발생하면"}
    keywords = [keyword for keyword in query.replace("?", "").split() if keyword not in stopwords]
    scored_documents: list[tuple[int, KnowledgeDocument]] = []

    for document in documents:
        score = 0
        for keyword in keywords:
            if keyword in document.title:
                score += 3
            if keyword in document.content:
                score += 1
        if score > 0:
            scored_documents.append((score, document))

    scored_documents.sort(key=lambda item: item[0], reverse=True)
    return [document for _, document in scored_documents[:2]]


def generate_answer(query: str, matched_documents: list[KnowledgeDocument]) -> str:
    """검색된 문서를 바탕으로 답변 초안을 생성합니다."""

    if not matched_documents:
        return "관련 문서를 찾지 못했습니다. 담당자 확인이 필요합니다."

    evidence = " / ".join(document.title for document in matched_documents)
    first_document = matched_documents[0]
    return (
        f"질문: {query}\n"
        f"참고 문서: {evidence}\n"
        f"답변 초안: {first_document.content}"
    )


if __name__ == "__main__":
    question = "AI 응답 지연이 발생하면 무엇을 확인해야 하나요?"
    knowledge_base = build_knowledge_base()
    results = retrieve_documents(question, knowledge_base)
    answer = generate_answer(question, results)

    print("[Dify RAG Flow Simulation]")
    print(answer)
