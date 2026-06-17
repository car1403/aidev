"""HTTPException 예외 처리 예제.

API에서는 문제가 생겼을 때 단순히 Python 오류를 보여주면 안 됩니다.
클라이언트가 이해할 수 있는 HTTP 상태 코드와 메시지를 반환해야 합니다.
"""

from fastapi import FastAPI, HTTPException


app = FastAPI(title="HTTPException Practice")


items = {
    1: {"id": 1, "name": "Python 교재", "price": 18000},
    2: {"id": 2, "name": "FastAPI 실습 노트", "price": 0},
}


@app.get("/items/{item_id}")
def get_item(item_id: int):
    """상품 id로 데이터를 조회합니다."""

    if item_id not in items:
        # 404는 요청한 리소스를 찾을 수 없다는 뜻입니다.
        raise HTTPException(status_code=404, detail="Item not found")

    return {"data": items[item_id]}


@app.get("/items/{item_id}/buy")
def buy_item(item_id: int):
    """구매 가능 여부를 확인하는 예제입니다."""

    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")

    item = items[item_id]

    if item["price"] <= 0:
        # 400은 클라이언트 요청 조건이 잘못되었을 때 사용할 수 있습니다.
        raise HTTPException(status_code=400, detail="Free item cannot be purchased")

    return {"message": "purchase ready", "data": item}
