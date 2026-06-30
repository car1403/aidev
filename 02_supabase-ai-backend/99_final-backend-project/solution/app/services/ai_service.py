def build_mock_ai_description(product: dict) -> str:
    return (
        f"{product['name']}은(는) {product['target_audience']}에게 적합한 상품입니다. "
        f"{product['description']} 이 특징을 바탕으로 쉽고 신뢰감 있게 소개할 수 있습니다."
    )
