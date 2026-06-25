"""Supabase Auth와 RLS 개념을 Python 코드로 확인하는 예제입니다.

이 파일은 실제 Supabase Auth API를 호출하지 않습니다.
초보자가 Auth, JWT, RLS, anon key, service role key의 역할을 먼저 이해할 수 있도록
작은 딕셔너리와 함수로 접근 제어 흐름을 흉내 냅니다.
"""

from __future__ import annotations

from pprint import pprint


def can_access_own_row(auth_user_id: str | None, row_user_id: str) -> bool:
    """로그인한 사용자가 특정 행에 접근할 수 있는지 확인합니다.

    Supabase RLS 정책의 `auth.uid() = user_id` 조건을 Python 함수로 단순화한 예제입니다.

    - auth_user_id: 현재 로그인한 사용자 id입니다.
    - row_user_id: 테이블 행을 소유한 사용자 id입니다.

    두 값이 같으면 본인 데이터이므로 접근을 허용합니다.
    두 값이 다르거나 로그인하지 않았다면 접근을 막습니다.
    """

    if auth_user_id is None:
        return False

    return auth_user_id == row_user_id


def can_admin_access_with_service_role(using_service_role_key: bool) -> bool:
    """service role key 사용 여부를 확인합니다.

    service role key는 서버에서만 사용하는 강한 권한의 key입니다.
    실제 Supabase에서는 service role key가 RLS를 우회할 수 있으므로
    브라우저, Streamlit 화면, GitHub 저장소에 노출하면 안 됩니다.
    """

    return using_service_role_key


def build_policy_result(current_user: dict | None, row: dict) -> dict:
    """현재 사용자와 데이터 행을 비교해 RLS 판단 결과를 보기 좋게 정리합니다."""

    auth_user_id = current_user["id"] if current_user else None
    allowed = can_access_own_row(auth_user_id, row["user_id"])

    return {
        "current_user_id": auth_user_id,
        "row_id": row["id"],
        "row_owner_id": row["user_id"],
        "display_name": row["display_name"],
        "allowed_by_rls_policy": allowed,
        "reason": "own row" if allowed else "not logged in or not owner",
    }


def main() -> None:
    """본인 데이터와 다른 사용자 데이터 접근 결과를 비교합니다."""

    # Auth가 성공하면 현재 사용자 정보를 알 수 있다고 가정합니다.
    current_user = {
        "id": "user-001",
        "email": "student@example.com",
    }

    # profiles 테이블의 행을 흉내 낸 데이터입니다.
    own_profile_row = {
        "id": "profile-001",
        "user_id": "user-001",
        "display_name": "사용자 A",
    }

    other_profile_row = {
        "id": "profile-002",
        "user_id": "user-999",
        "display_name": "다른 사용자",
    }

    anonymous_user = None

    print("[RLS policy check: logged-in user]")
    pprint(build_policy_result(current_user, own_profile_row), width=100)
    pprint(build_policy_result(current_user, other_profile_row), width=100)

    print("\n[RLS policy check: anonymous user]")
    pprint(build_policy_result(anonymous_user, own_profile_row), width=100)

    print("\n[service role key check]")
    print("FastAPI server using service role key:", can_admin_access_with_service_role(True))
    print("Browser should use service role key:", can_admin_access_with_service_role(False))

    print("\n핵심 정리")
    print("- Auth는 사용자가 누구인지 확인합니다.")
    print("- RLS는 확인된 사용자가 어떤 행에 접근할 수 있는지 제한합니다.")
    print("- anon key는 RLS 정책과 함께 사용해야 안전합니다.")
    print("- service role key는 FastAPI 서버에서만 사용하고 화면 코드에 노출하지 않습니다.")


if __name__ == "__main__":
    main()
