"""워크플로우 노드 간 입력/출력 계약과 상호작용을 보여주는 예제입니다."""

from dataclasses import dataclass


@dataclass
class NodeContract:
    """노드의 입력과 출력 계약을 표현합니다."""

    node_name: str
    required_inputs: list[str]
    outputs: list[str]
    next_nodes: list[str]


def build_node_contracts() -> list[NodeContract]:
    """기술 지원 워크플로우의 노드 연결 계약을 만듭니다."""

    return [
        NodeContract("Trigger", ["event"], ["ticket_id", "message"], ["PrepareData"]),
        NodeContract("PrepareData", ["ticket_id", "message"], ["clean_message", "keywords"], ["Branch"]),
        NodeContract("Branch", ["keywords"], ["route"], ["RAGSearch", "DirectAnswer"]),
        NodeContract("RAGSearch", ["keywords"], ["documents"], ["GenerateAnswer"]),
        NodeContract("DirectAnswer", ["clean_message"], ["draft_answer"], ["Merge"]),
        NodeContract("GenerateAnswer", ["clean_message", "documents"], ["draft_answer"], ["Merge"]),
        NodeContract("Merge", ["draft_answer"], ["final_answer"], ["OutputValidation"]),
        NodeContract("OutputValidation", ["final_answer"], ["validated_answer", "status"], ["Output"]),
    ]


def print_contracts(contracts: list[NodeContract]) -> None:
    """노드 계약을 사람이 읽기 쉬운 형태로 출력합니다."""

    for contract in contracts:
        print(f"\n[{contract.node_name}]")
        print(f"required_inputs: {', '.join(contract.required_inputs)}")
        print(f"outputs: {', '.join(contract.outputs)}")
        print(f"next_nodes: {', '.join(contract.next_nodes)}")


if __name__ == "__main__":
    print_contracts(build_node_contracts())
