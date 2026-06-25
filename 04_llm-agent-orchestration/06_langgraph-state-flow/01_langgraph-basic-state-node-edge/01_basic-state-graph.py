"""LangGraph의 가장 기본적인 StateGraph 예제입니다."""

from typing import TypedDict

from langgraph.graph import END, START, StateGraph


class SimpleState(TypedDict):
    """그래프 전체에서 공유할 상태 구조입니다."""

    user_request: str
    answer: str


def generate_answer(state: SimpleState) -> dict:
    """사용자 요청을 읽고 답변 값을 업데이트하는 노드입니다."""
    request = state["user_request"]
    return {"answer": f"'{request}' 요청을 처리했습니다."}


# StateGraph는 상태 구조를 기준으로 그래프를 만듭니다.
graph_builder = StateGraph(SimpleState)

# 노드를 등록합니다.
graph_builder.add_node("generate_answer", generate_answer)

# START에서 generate_answer로 이동하고, 이후 END로 종료합니다.
graph_builder.add_edge(START, "generate_answer")
graph_builder.add_edge("generate_answer", END)

graph = graph_builder.compile()

result = graph.invoke({"user_request": "학습 로그를 요약해줘", "answer": ""})
print(result)
