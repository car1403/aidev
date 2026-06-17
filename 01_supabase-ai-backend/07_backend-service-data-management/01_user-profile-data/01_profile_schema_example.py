"""사용자 프로필 데이터 구조를 이해하는 예제.

이 파일은 Supabase에 접속하지 않습니다.
초보자가 먼저 "서비스에서 사용자 정보를 어떤 모양으로 관리하는지"를
Python dict로 확인하는 예제입니다.
"""


# Auth에서 확인한 사용자 id라고 가정합니다.
# 실제 Supabase Auth의 user id는 uuid 형태입니다.
auth_user_id = "00000000-0000-0000-0000-000000000001"


# profiles 테이블에 저장할 사용자 프로필 예시입니다.
# id는 auth.users.id와 연결하는 기준으로 사용할 수 있습니다.
profile = {
    "id": auth_user_id,
    "display_name": "수강생 A",
    "preferred_language": "ko",
    "course_level": "beginner",
}


def describe_profile(profile_data: dict) -> str:
    """프로필 데이터를 사람이 읽기 쉬운 문장으로 바꿉니다."""

    return (
        f"{profile_data['display_name']}님은 "
        f"{profile_data['course_level']} 단계 수강생이며, "
        f"기본 언어는 {profile_data['preferred_language']}입니다."
    )


print("프로필 데이터:")
print(profile)
print("\n설명:")
print(describe_profile(profile))
