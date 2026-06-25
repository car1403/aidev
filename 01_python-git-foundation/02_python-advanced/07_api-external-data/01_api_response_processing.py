"""API 응답 처리 구조 예제입니다.

실제 외부 API를 호출하기 전에, API 응답이 보통 어떤 형태인지 먼저 연습합니다.
대부분의 API 응답은 JSON 형태로 오며, Python에서는 dict/list 구조로 다룹니다.
"""


def mock_get_user(user_id: int) -> dict[str, object]:
    """외부 API 응답처럼 보이는 데이터를 반환합니다."""

    # 실제 API라면 서버에서 JSON 응답을 받아오지만,
    # 여기서는 학습을 위해 직접 dict를 만들어 API 응답처럼 사용합니다.
    # dict[str, object]는 "key는 문자열이고 value는 여러 타입이 올 수 있다"는 뜻입니다.
    return {
        "id": user_id,  # 사용자 고유 번호입니다. 함수 인자로 받은 값을 그대로 넣습니다.
        "name": "Jean",  # 사용자 이름입니다.
        "active": True,  # 사용자가 활성 상태인지 나타내는 bool 값입니다.
        "roles": ["student", "python"],  # 사용자의 역할 목록입니다. list[str] 형태입니다.
    }


def format_user_summary(user: dict[str, object]) -> str:
    """API 응답 딕셔너리를 화면 출력 문자열로 변환합니다."""

    # user["roles"]에는 ["student", "python"] 같은 list가 들어 있습니다.
    # ", ".join(...)은 리스트의 문자열들을 쉼표와 공백으로 연결합니다.
    # 결과 예: "student, python"
    roles = ", ".join(user["roles"])

    # f-string을 사용하면 dict에서 꺼낸 값을 문장 안에 쉽게 넣을 수 있습니다.
    # user["name"], user["id"]처럼 key 이름으로 원하는 값을 가져옵니다.
    return f"{user['name']}({user['id']}) - roles: {roles}"


# mock_get_user(1)을 호출하면 사용자 id가 1인 가짜 API 응답 dict가 만들어집니다.
api_user = mock_get_user(1)

# format_user_summary가 dict를 사람이 읽기 좋은 문자열로 바꾸고,
# print가 그 결과를 터미널에 출력합니다.
print(format_user_summary(api_user))
