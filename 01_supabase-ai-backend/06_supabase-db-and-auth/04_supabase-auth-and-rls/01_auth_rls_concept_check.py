"""Supabase Auth와 RLS 개념을 코드로 확인하는 예제.

이 파일은 실제 Supabase Auth API를 호출하지 않습니다.
초보자가 로그인, JWT, RLS, key 역할을 먼저 말로 설명할 수 있게
작은 딕셔너리와 함수로 흐름을 흉내 냅니다.
"""


def can_access_row(auth_user_id: str, row_user_id: str) -> bool:
    """사용자 id와 행의 owner id가 같으면 접근을 허용합니다.

    Supabase RLS 정책의 `auth.uid() = user_id` 조건을 Python 함수로
    단순하게 표현한 예제입니다.
    """

    return auth_user_id == row_user_id


current_user = {
    "id": "user-001",
    "email": "student@example.com",
}

own_profile_row = {
    "id": "profile-001",
    "user_id": "user-001",
    "display_name": "수강생 A",
}

other_profile_row = {
    "id": "profile-002",
    "user_id": "user-999",
    "display_name": "다른 사용자",
}

print("본인 데이터 접근:", can_access_row(current_user["id"], own_profile_row["user_id"]))
print("다른 사용자 데이터 접근:", can_access_row(current_user["id"], other_profile_row["user_id"]))

print("\n핵심:")
print("Auth는 사용자가 누구인지 확인합니다.")
print("RLS는 확인된 사용자가 어떤 행에 접근할 수 있는지 제한합니다.")
